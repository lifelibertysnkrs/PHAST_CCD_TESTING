import cv2
import numpy as np
class image:
    def __init__(self, ms, directory):
        self.ms = ms.replace("-ms", "")
        self.location = directory + "/img-1.png"
        self.biasLocation = directory + "/imgBIAS1-1.png"
        
##        self.img = cv2.imread('location' + '\img-1.png')
##        self.imgVals = []
##        height, width, channels = self.img.shape
##        for h in xrange(height):
##            for w in xrange(width):
##                self.imgVals.append([h, w, self.img[h][w][1]])
                
        

                
        
        
