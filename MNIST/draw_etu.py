from tkinter import *
from PIL import Image, ImageOps                                 #ImageOps for grayscale

#Variables globales
old_x, old_y = 0, 0

#This function displays the mouse coordinates in Label widget
def MouseCoord(event):
    global cadre
    global old_x, old_y                                                #Allows to modify a global variable
    X = event.x
    Y = event.y
    coord.set("x= "+ str(X)+ " ; y= "+ str(Y))

    old_x = event.x
    old_y = event.y


def Dessin(event):
    global old_x, old_y
    x = event.x
    y = event.y
    cadre.create_line(old_x, old_y ,x, y, width= 10)

    old_x = event.x
    old_y = event.y
    
def Save_as_png(event):
    global cadre         #Allows to modify a global variable                                     
    # MGA: bellows are listed the different steps to store your canvas drawing into a 28px x 28 px grayscale png picture
    # 1 - save postscipt image 
    imgps_save = cadre.postscript(file='image.ps')

    # 2 - use PIL to convert to PNG 
    image = Image.open('image.ps')

    # 3 - use ImageOps to invert black and white 
    inverted_image = ImageOps.invert(image)

    # 4 - use PIL to convert in grayscale
    image_grayscale = ImageOps.grayscale(inverted_image)

    # 5 - use PIL to reduce picture to 28px x 28 px
    image_reduce = image_grayscale.resize((28,28), Image.ANTIALIAS)

    # 6 - use PIL to save picture as png
    image_reduce.save('image_finale.png')


fenetre1=Tk()    #Swinen's book p76       

                                     

cadre=Canvas(fenetre1, width=200, height=200, bg='#FFFFFF')     #p89
cadre.bind("<Motion>", MouseCoord)
cadre.bind("<B1-Motion>", Dessin)
cadre.bind("<Button-3>", Save_as_png)                           # call the save function on left click
cadre.pack()


# create here your Label widget
coord = StringVar()
label = Label(fenetre1, textvariable = coord , bd = 20) 
coord.set("x= "+ X+ " ; y= "+ Y)
label.pack()  

fenetre1.mainloop()

