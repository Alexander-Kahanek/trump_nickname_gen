# Trump Nickname AI generator

This repository holds the analysis of data, the process of training a model, and the final model and output decoding produced for generating nicknames based on Trump's unique nickname data from Wikipedia.
: > data: https://en.wikipedia.org/wiki/List_of_nicknames_used_by_Donald_Trump

The data was scraped directly from Wikipedia, then I created the Tableau Dashboard to display the patterns based on the initial exploratory data analysis. The data was then used to create two different approaches to generating nicknames based on a user given input name. Both methods used a LSTM Neural Network for training. The character-based generation method did not have good results; however, the word-based generation method had great results due to the addition of affix's being encoded into the data as embeddings.

![Tabluea Graph](https://github.com/Alexander-Kahanek/trump_nickname_gen/blob/main/graphs/trump_graph.png)

# Python Notebooks

These notebooks were created as a walkthrough of the whole process taken from the inital data analysis, to the end product of a working model.

+ 1_intial_analysis.ipynb
  - This notebook contains the original analysis that was done on the dataset before it was used to train the LSTM Neural Network.

+ 2_character.nn.gen.ipynb
  - This notebook was the first attempt at training the model, using a character based approach.
  - This character based approach did not have goo results, and thus a word based model was created.

+ 3_word.nn.gen.ipynb
  - This notebook is the creation of the word based approach to nickname generation.
  - This model had much better results, especially when utilizing the affix information of the nicknames.


# PROJECT UNDER DEVELOPMENT

Working on displaying the Phoenix / Elixir Web Application that was created to implement the model displayed in the 3_word.nn.gen.ipynb analysis
