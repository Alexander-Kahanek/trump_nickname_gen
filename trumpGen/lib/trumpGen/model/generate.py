import os
from erlport.erlterms import Atom
import numpy
# from sklearn.externals import joblib


def load_model():
    # load model

    path = os.path.abspath('lib/phoenix_ml/model/model.bs30.e500.nL50.output')
    # model = keras.models.load_model(path)
    model = path

    return model


def generate_name(args):
    model = load_model()

    # create actual generate function here
    name = b"test"

    return name
