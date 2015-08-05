import os
import image
class imageArray:
    def __init__(self, directory):
            self.directory = directory
            self.mslist = [ name for name in os.listdir(self.directory) if os.path.isdir(os.path.join(self.directory, name)) ]
            self.images = []
            for d in self.mslist:
                self.images.append(image.image(d, directory + d))

    def toString(self):
        imageString = ''
        for image in self.images:
            imagesString += (" " + image + " ")
        return imagesString

 
