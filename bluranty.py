import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type = str, required=True,
    help="path to input image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
img2 = cv2.blur(img,(10,10))
cv2.imshow('original',img)
cv2.imshow("img",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()