# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO DETECT AND COUNT NUMBER OF FACES IN AN IMAGE USING OpenCV LIBRARY
#
# OpenCV-Python is a library of Python bindings designed to solve computer vision problems. OpenCV-Python makes use of
# Numpy, which is a highly optimized library for numerical operations with a MATLAB-style syntax. All the OpenCV array
# structures are converted to and from Numpy arrays. This also makes it easier to integrate with other libraries that
# use Numpy such as SciPy and Matplotlib.
#
# The module can be installed using the command - pip install opencv-python

# Importing necessary packages
import os
import cv2
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    root.previewlabel = Label(root, bg="deepskyblue4", fg="white", text="IMAGE PREVIEW", font=('Comic Sans MS',20))
    root.previewlabel.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

    root.imageLabel = Label(root, bg="deepskyblue4", borderwidth=3, relief="groove")
    root.imageLabel.grid(row=2, column=1, padx=10, pady=10, columnspan=3)

    root.openImageEntry = Entry(root, width=40, textvariable=imagePath)
    root.openImageEntry.grid(row=3, column=1, padx=10, pady=10)

    root.openImageButton = Button(root, width=10, text="BROWSE", command=imageBrowse)
    root.openImageButton.grid(row=3, column=2, padx=10, pady=10)

    root.detectCountButton = Button(root, width=15, text="DETECT & COUNT", command=detectCountFaces)
    root.detectCountButton.grid(row=3, column=3, padx=10, pady=10)

    root.faceLabel = Label(root, bg="deepskyblue4", fg="white", borderwidth=3, relief="groove",
                           text="Number Of Faces:", font=('Comic Sans MS',20))
    root.faceLabel.grid(row=4, column=1, padx=10, pady=10, columnspan=3)

    imageView = Image.open("/Users/abhijithwarrier/Pictures/RandomImage.png")
    imageResize = imageView.resize((640, 480), Image.ANTIALIAS)
    imageDisplay = ImageTk.PhotoImage(imageResize)
    root.imageLabel.config(image=imageDisplay)
    root.imageLabel.photo = imageDisplay

def imageBrowse():
    # Presenting user with a pop-up for directory selection. initialdir argument is optional
    # Retrieving the user-input destination directory and storing it in destinationDirectory
    # Setting the initialdir argument is optional. SET IT TO YOUR DIRECTORY PATH
    openDirectory = filedialog.askopenfilename(initialdir="YOUR DIRECTORY PATH")
    # Displaying the directory in the directory textbox
    imagePath.set(openDirectory)
    # Opening saved image using the open() of Image class which takes saved image as argument
    imageView = Image.open(imagePath.get())
    # Resizing the image using Image.resize()
    imageResize = imageView.resize((640, 480), Image.ANTIALIAS)
    # Creating object of PhotoImage() class to display the frame
    imageDisplay = ImageTk.PhotoImage(imageResize)
    # Configuring the label to display the frame
    root.imageLabel.config(image=imageDisplay)
    # Keeping a reference
    root.imageLabel.photo = imageDisplay

def detectCountFaces():
    # Storing the XML file path in the casc_path variable
    casc_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    # Reading the pre-trained ML Models and loading it using the CascadeClassifer Method
    face_cascade = cv2.CascadeClassifier(casc_path)
    # Loading the image from the specified file
    image = cv2.imread(imagePath.get())
    # Converting the original image color to Black & White using the cvtColor() Method
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detecting faces in the image using the detectMultiScale() Method
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    # Printing and displaying the number of faces
    print("\nFOUND {0} FACES!".format(len(faces)))
    root.faceLabel.config(text="Number Of Faces:"+str(len(faces)))
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),3)

    # Fetching and storing the selected image path
    new_image_path = os.path.dirname(os.path.abspath(imagePath.get())) + "/"
    # Fetching only the name of the selected image without extentsion from the complete path and
    # concatenating the name with keyword _facesdetected and .jpeg extension
    new_image_name = os.path.splitext(imagePath.get().split('/')[-1])[0] + "_facesdetected.jpeg"
    # Storing the complete new image name with path
    complete_image_path_name = new_image_path + new_image_name
    # Saving the image with rectangle around the faces as the new image
    cv2.imwrite(complete_image_path_name, image)
    # Opening the new saved image using open() of Image class which takes saved image as argument
    imageView = Image.open(complete_image_path_name)
    # Resizing the image using Image.resize()
    imageResize = imageView.resize((640, 480), Image.ANTIALIAS)
    # Creating object of PhotoImage() class to display the frame
    imageDisplay = ImageTk.PhotoImage(imageResize)
    # Configuring the label to display the frame
    root.imageLabel.config(image=imageDisplay)
    # Keeping a reference
    root.imageLabel.photo = imageDisplay


# Creating object of tk class
root = tk.Tk()

# Setting the title, window size, background color and disabling the resizing property
root.title("Python-FaceDetect&Count")
root.geometry("670x670")
root.resizable(False, False)
root.configure(background = "deepskyblue4")

# Creating tkinter variables
destPath = StringVar()
imagePath = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()
