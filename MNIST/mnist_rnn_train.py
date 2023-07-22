#Sources : Jason Brownlee et https://colab.research.google.com/github/aamini/introtodeeplearning/blob/master/lab2/Part1_MNIST.ipynb

from keras.datasets import mnist
from keras.models import load_model
from pandas import DataFrame
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils

import numpy
import matplotlib.pyplot as plt

#Recuperation de la base d'image MNIST et affichage de l'une d'elle
# load (downloaded if needed) the MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()


# reshape to be [samples][width][height][channels]
X_train = X_train.reshape(X_train.shape[0], 784).astype('float32')
X_test = X_test.reshape(X_test.shape[0], 784).astype('float32')
# normalize inputs from 0-255 to 0-1
X_train = X_train / 255
X_test = X_test / 255
# one hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)


#Creation du reseau de neurone simple
RNN=Sequential()
RNN.add(Dense(784, input_dim=784, activation="relu", kernel_initializer="normal"))
RNN.add(Dense(10, activation='softmax', kernel_initializer="normal"))
RNN.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print("_"*140+'\n')
print("_"*140+'\n')

RNN.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3, batch_size=200, verbose=1)

RNN.save("model_RNN_handwritting.h5")
Fiabilite=RNN.evaluate(X_test,y_test, verbose=0)
print("\nFiabilite lors de la phase d'évaluation:     " + str(round(100*Fiabilite[1],2)) + "%")
print("\nLe réseau entraîné est enregistré dans :model_RNN_handwritting.h5")
print("_"*140+'\n') 

