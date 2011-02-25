
import cv

counter = 0

# Save a image consecutively numbered
def saveImage(image):
    global counter
    filename = "tdrImages//tdrImage" + str(counter) + ".png"
    counter = counter + 1
    cv.SaveImage(filename, image)
