import os
import pandas as pd
import numpy as np
from erlport.erlterms import Atom
from tensorflow import keras
# from sklearn.externals import joblib


def load_model():
    # load model

    path = os.path.abspath('lib/trumpGen/model/model.bs30.e500.nL50.output')
    model = keras.models.load_model(path)

    return model


def generate_name(args):
    model = load_model()

    p_gen_len, token2i, i2token, i2name, max_tokens, token_dimensions = get_variables()
    # create actual generate function here

    # name = b"test"

    print(type(args))
    print(args)
    
    name = predict_name(model, args.decode("utf-8"), p_gen_len, token2i, i2token, i2name, max_tokens, token_dimensions)
    name = str.encode(name)

    return name

def get_variables():
    # reading in probabilities of name size
    raw = pd.read_csv(os.path.abspath('lib/trumpGen/model/cleaned.nicknames.csv'))
    name_matrix = raw.groupby(['len real', 'len fake']).agg({'count':'count'}).reset_index()
    name_matrix = name_matrix[name_matrix['len real'] == 2]
    p_gen_len = name_matrix[['len fake']]
    p_gen_len['p'] = name_matrix['count']/name_matrix['count'].sum()

    # tokenizing data ##################
    def tokenize(realname, nickname):
        '''tokenizes reach real name and nickname to follow the rules defined'''

        # get a dictionary for the real name and corrospoinding token, ie input
        real2token = {word: f'<name{X+1}>' for X, word in enumerate(realname.split(' '))}
        # convert dictionary to word tokenized groups and join into single string
        real_tokenized = ' '.join([f'{word} {real2token[word]}' for word in real2token])

        # change nickname into single string with tokenization and substitution
        # grab names to substitute
        subs = [sub for sub in realname.split(' ') if sub in nickname]

        if len(subs) == 0:
            # then there are no splits, tokens are <nope>
            nick_tokenized = ' '.join([f'{word} <nope>' for word in nickname.split(' ')])
            return (real_tokenized, nick_tokenized)

        substituted = ' '.join([word if word not in subs else f'{real2token[word]}' for word in nickname.split(' ')])

        tokens = ['<prefix>', '<suffix>', '<name>']
        index = 0
        tokenized = []

        for word in substituted.split(' '):
            if 'name' in word:
                index = 2

            tokenized.append(f'{word} {tokens[index]}')
            if index == 2:
                index = 1
        
        nick_tokenized = ' '.join(tokenized)

        return (real_tokenized, nick_tokenized)

    #######################################
    tokenized_names = [tokenize(realname, nickname) for i, nickname, realname in raw[['fake name', 'real name']].itertuples()]

    ##### get probabilities of name length #####
    name_matrix = raw.groupby(['len real', 'len fake']).agg({'count':'count'}).reset_index()
    name_matrix = name_matrix[name_matrix['len real'] == 2]
    p_gen_len = name_matrix[['len fake']]
    p_gen_len['p'] = name_matrix['count']/name_matrix['count'].sum()

    ##### get vocab ######
    # flatten paired list to get all names
    flatten = [name for pair in tokenized_names for name in pair]
    # make sure the created tokens go first in the vocad dictionaries
    flatten[:0] = ['<prefix>', '<suffix>', '<name>', '<nope>', '<name1>', '<name2>', '<name3>', '<name4>', '<name5>', '<name6>']

    ###### get dictionaries #########
    # get dictionary of nicknames to
    nick2real = {nickname:realname for (realname, nickname) in tokenized_names}
    # get dictionaries for vocab
    uni_tokens = {token:0 for name in flatten for token in name.split(' ')}
    # dictionary for token to index
    token2i = {token:i for i, token in enumerate(uni_tokens)}
    # dictionary for index to token
    i2token = {token2i[token]: token for token in token2i}
    # dictionary for index to real name token
    i2name = {token2i[word]:word for pair in tokenized_names for word in pair[0].split(' ') if '<' not in word}

    max_tokens = max([len(name.split(' ')) for name in flatten])
    # find total number of tokens, ie columns in matrix
    token_dimensions = len(i2token)

    return p_gen_len, token2i, i2token, i2name, max_tokens, token_dimensions

def predict_name(model, input, p_gen_len, token2i, i2token, i2name, max_tokens, token_dimensions):
    '''generates a nickname based on length of word and input given'''

    word_vec = np.zeros((1, max_tokens, token_dimensions))

    p_len = p_gen_len['p']
    gen_len = p_gen_len.loc[np.random.choice(range(len(p_len)), p=p_len),'len fake']
    # print(gen_len)
    # get a dictionary for the real name and corrospoinding token, ie input
    token2input = {f'<name{X+1}>': word for X, word in enumerate(input.split(' '))}
    # convert dictionary to word tokenized groups and join into single string
    input_tokenized = ' '.join([f'{token2input[token]} {token}' for token in token2input])
    nName = 0 # tracks the number of name affix given

    affixs = []
    for index in range(gen_len):
        index = (index+1)*2 -1

        # pull probabilities for each affix
        p_affix = list(model.predict(word_vec)[0,index])[0:4]
        # normalize probabilities
        p_affix_norm = p_affix / np.sum(p_affix)
        # guess a affix
        guess = np.random.choice(range(len(p_affix_norm)), p=p_affix_norm)
        affix = i2token[guess]

        # check affix to make sure names are not chosen more than the given user amount
        if 'name' in affix:
            if nName < len(token2input):
                nName += 1
            else:
                while 'name' in affix:
                    guess = np.random.choice(range(len(p_affix_norm)), p=p_affix_norm) # choose an affix
                    affix = i2token[guess]
        # assign value to generated name vector
        word_vec[0, index, guess] = 1
        # print(f'p={p_affix_norm}, g={i2token[guess]}, i={index}')
        affixs.append(affix)

    def predict_token(index, affix):
        '''generates a token based on the given affix''' 
        # print(f'g={guess}, i={index}')
        if 'name' in affix:
            # pull probabilities for all names: index 4 - 4+given amount (max ind 9)
            p_name = list(model.predict(word_vec)[0,index])[4:4+len(token2input)]
            p_name_norm = p_name / np.sum(p_name)
            # generate name token
            guess = np.random.choice(range(4, len(p_name_norm)+4), p=p_name_norm)

            # prevent repeat name tokens
            while word_vec[0,index-2,guess] == 1.0:
                guess = np.random.choice(range(4, len(p_name_norm)+4), p=p_name_norm)
                # print(guess, len(p_name_norm)+4, len(token2input))
                # print(i2token[guess], input)
            token = i2token[guess]
            word = token2input[token]
        
        else:
            # affix is prefix, suffix, or nope
            # grab porbabilities of all non affix or name tokens: 10 - end
            p_tokens = list(model.predict(word_vec)[0,index])[10:]
            p_tokens_norm = p_tokens / np.sum(p_tokens)
            # generate a guess from probabilities
            guess = np.random.choice(range(10, len(p_tokens_norm)+10), p=p_tokens_norm)

            # prevent named vocab from being chosen and repeat tokens
            while guess in i2name or word_vec[0,index-2,guess] == 1.0:
                # print(i2token[guess])
                guess = np.random.choice(range(10, len(p_tokens_norm)+10), p=p_tokens_norm)
            word = i2token[guess]
            
        word_vec[0, index, guess] = 1
        return word

    # print(f'{input}: {affixs}')
    tokens = [predict_token(i*2, affix) for i, affix in enumerate(affixs)]
    return " ".join(tokens)