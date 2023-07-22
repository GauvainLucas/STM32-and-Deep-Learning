from keras.models import load_model
from pandas import DataFrame
from PIL import Image

import numpy 

#Recupération de l'image 28x28 créée précedemment
im = Image.open('image_finale.png')
imgArray = numpy.asarray(im)
print("_"*140+'\n')
print("_"*140+'\n')
print(DataFrame(imgArray))
print("\n\n")

#Transformation de la matrice en une liste
imgArray = imgArray.reshape(1,784)
print(imgArray)
print("\n\n")

#Chargement du reseau de neurone simple
RNN=load_model('model_RNN_handwritting.h5')
resultat= RNN.predict(imgArray,batch_size=None, verbose=1, steps=None, callbacks=None, max_queue_size=10, workers=1, use_multiprocessing=False)

# normalize inputs from 0-255 to 0-1
imgArray = imgArray / 255

#Prediction
prediction=numpy.zeros(10)  #une matrice ligne de 10 zéros
prediction[numpy.argmax(resultat)]=1                    #argmax renvoi l'indice du + grand element du tableau

print(DataFrame(numpy.vstack([resultat, prediction])))   #vstack concatene les lignes

#Affichage du résultat
print("\nPour ce réseau ce chiffre est :",numpy.argmax(resultat))       # indice tableau de la valeur max
print("_"*140+'\n') 

