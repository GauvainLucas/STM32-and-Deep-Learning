# Plot mnist instances
from keras.datasets import mnist
from pandas import DataFrame
import matplotlib.pyplot as plt
# load (downloaded if needed) the MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# plot 1 image as gray scale
plt.subplot(111)
plt.imshow(X_train[15], cmap=plt.get_cmap('gray'))
print(DataFrame(X_train[15]))
print("Ce chiffre est:",y_train[15])
# show the plot
plt.show()
