import cv2
import numpy as np
import imageio
import argparse



# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
args = vars(ap.parse_args())

# load the image
img = cv2.imread(args["image"])


#file="B.jpg"
#filename=file.split(".")[0]
file=args["image"]
filename=file.split(".")[0]

img = cv2.imread(file,0)
img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

titles = ['Original_Image', 'Global_Thresholding (v = 127)',
            'Adaptive_Mean_Thresholding', 'Adaptive_Gaussian Thresholding']
images = [img, th1, th2, th3]

gif_images=[]
for i in range(0,4):
	cv2.namedWindow(titles[i],cv2.WINDOW_NORMAL)
	cv2.imshow(titles[i], images[i])
	cv2.imwrite(filename+"_"+titles[i]+".jpg",images[i])
	gif_images.append(imageio.imread(filename+"_"+titles[i]+".jpg"))
	cv2.waitKey(0)
imageio.mimsave(filename+"_gif.gif",gif_images)