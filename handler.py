import imagearray
import image
import cv2
import numpy
import os



def setup(directory):

    mslist = [ name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name)) ] #gathers all the ms subdirectories in mlist
    images = []
    for d in mslist:
        images.append(image.image(d, directory +"/" + d)) #formats mlist
    return images
    
    images = imagearray.imageArray(directory)
    return images


def average(images, output): #takes a list of strings pointing to images
    imagesString = ""
    for image in images:
        imagesString += (" " + image + " ")
    averageString = "convert" + imagesString + "-average" + output
    print averageString
    a = os.system(averageString)
    

def subtract(image1, image2, output):
    os.system("convert " +  image1 + " "+ image2+  " -compose Change-mask -composite placeholder.png")
    os.system("convert -background black placeholder.png -flatten " + output)
    os.system("rm placeholder.png")

def getInfo(image, output):
    idstring = "identify -verbose  " + image +" >" + output
    print idstring
    os.system(idstring)

def calcRead(directory):
    images = setup(directory)
    imagelocs = []
    print images
    for image in images:
        imagelocs.append(image.biasLocation)
    print imagelocs
    average(imagelocs, "biasAvg.png")
    
    for image in imagelocs:
        subtract(image, "biasAvg.png", image+"biasSub.png")
        getInfo(image+"biasSub.png", image+"ReadNoiseHistogram.txt")

def calcDark(directory):
    images = setup(directory)
    imagelocs = []
    for image in images:
        imagelocs.append(image.biasLocation)
    average(imagelocs, "biasAvg.png")
    imagelocs = []
    print images
    for image in images:
        imagelocs.append(image.location)
    print imagelocs
    average(imagelocs, "DarkAvg.png")
    for image in imagelocs:
        subtract(image, "average.png", image+"biasSub.png")
        getInfo(image+"biasSub.png", image+"bias_info.txt")
    
    
def squareROI(x,y,size,pic):
    os.system("convert " + pic + "-crop " size[0] + "x" + size[1] +"+" x + "+" y)
    
    
def calcGain(image1, image2):
    subtract(image1, "biasAvg.png", "subtactedimg1.png") 
    subtract(image2, "biasAvg.png", "subtactedimg2.png")
    x = raw_input("Open file subtractedimg1.png and choose a start coordinate x value ")
    y = raw_input("choose a y coordinate")
    size[0] = raw_input("choose x size" )
    size[1] = raw_input("choose y size" )
    squareROI(x,y,size,"subtactedimg1.png")
    squareROI(x,y,size,"subtactedimg2.png")
    cropstring = "identify -verbose  " + image1 +" >" + "image1Info.txt"
    os.system(cropstring)
    cropstring = "identify -verbose  " + image2 +" >" + "image2Info.txt"
    os.system(cropstring)
    
    
    
    
