import matplotlib.pyplot as plt
import cv2
import numpy as np

def cropping_photos(filename,xPosition,yPosition,fiberName="FP",height=200,width=200,save=False):
    imgData = plt.imread(filename)
    imgData = imgData[xPosition:xPosition+width,yPosition:yPosition+height]
    fiberName = r"C:/Users/bmehl/Desktop/Fibers/"+fiberName+".png"
    plt.imshow(imgData)
    if save:
        plt.savefig(fiberName)
    else:
        plt.show()
