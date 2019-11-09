import numpy as np 
import neat
import nltk
import os, sys
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
####################
from keras.models import Model
from keras.layers import Input
from keras.layers import Dropout, GaussianNoise, BatchNormalization, Flatten
from keras.layers import Activation
from keras.optimizers import Adam, RMSprop

####################

class Seq2Seq:
    def __init__(self):
        self.model = None
        ### PARAMETERS FOR SEQUENCE TO SEQUENCE MODEL ###

        ## Input Parameters
        self.inputshape = (1, 1, 1)
        ## Batch Normalization Parameters
        self.batchnormmomentum = 0.8
        self.batchepsilon = 1e-6
        ## Adam Optimizer Parameters
        self.adamlr = 0.0002
        self.adam_b = 0.5
    
    # build. . .
    def __call__(self):
        pass

    def encoder(self):
        pass

    def decoder(self):
        pass


class AdaBoost:
    pass

