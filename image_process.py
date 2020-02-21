!pip install numpy
!pip install matplotlib
!pip install opencv-python

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import cv2

# EXTRACT GRAYSCALE VALUES FROM IMAGES TO USE AS TRAINING DATA

path = os.path.join("/Users/anavilcapoma/Desktop/", "Botguy")
# if multiple directories stem from one directory, i.e. botguy/orange ball from Objects, use os.path.join, use nested for loop to go through both

size = 200
training = []
directory = "/Users/anavilcapoma/Desktop/Botguy"

for img in os.listdir(directory):
    # stores grayscale values in temp array 
    temp = cv2.imread(os.path.join(driectory, img), cv2.IMREAD_GRAYSCALE)
    # resizes gray array
    resized_gray_array = cv2.resize(temp, (size, size))
    
    # print images
    plt.imshow(resized_gray_array, cmap = 'gray')
    plt.show()
    print(resized_gray_array)
    
    # adds new values to array
    training.append([resized_gray_array])

# scales resized gray array values to range of 0-1 instead of 0-255
scaled_RG_array = []
    
for i in training:
    for j in i:
        scaled_RG_array.append([j / 255.0])
        
# scaled_RG_array now contains resized grayscale values of all images

# gaussian noise????????
