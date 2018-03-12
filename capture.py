import cv2
from PIL import Image, ImageDraw
import numpy as np
from matplotlib import cm
import detect_text

subscription_key_vision = "9c47fc0301fe4e3696b44818e1721da0"
img_url = "http://cse.iitkgp.ac.in/~rahul.kumar/test_image.jpg"
cam = cv2.VideoCapture(0)

while True:
    ret_val, img = cam.read()
    # draw = Image.fromarray(np.uint8(cm.gist_earth(myarray)*255))

    # draw = ImageDraw.Draw(img)
    cv2.imshow("window",img)
    cv2.imwrite ("/run/user/1000/gvfs/sftp:host=cse.iitkgp.ac.in/public_html/test_image.jpg", img)

    cv2.waitKey(5)
    detect_text.localize_text(subscription_key_vision, img_url, "Rahul" )
