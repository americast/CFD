import os
import cognitive_face as CF
import numpy as np
import cv2
from PIL import Image, ImageDraw
import matplotlib.cm as cm
import json
import yaml

KEY = os.getenv("KEY_face")  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)
# If you need to, you can change your base API url with:
#CF.BaseUrl.set('https://westcentralus.api.cognitive.microsoft.com/face/v1.0/')

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

def getRectangle(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left + rect['height']
    right = top + rect['width']
    return (left, top, bottom, right)

def getRectangleTuple(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left + rect['height']
    right = top + rect['width']
    return ((left, top), (bottom, right))

f = open('temp.json', 'r')
parsed = json.load(f)

# cam = cv2.VideoCapture(0)
while True:
    # ret_val, img = cam.read()
    img = cv2.imread("img/1.jpg")
    draw = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    drawhere = ImageDraw.Draw(draw)
    cv2.imwrite("temp.jpg", img)
    # draw = ImageDraw.Draw(img)
    array = CF.face.detect("temp.jpg")
    print("array:", array)

    # count = 0
    # for face in array:
    #     count+=1
        # a = draw.crop(getRectangle(face))
        # a.save(count+".jpg")

    flag = False
    for face in array:
        k = CF.face.identify([face['faceId']], "kubs")
        try:
            print("k: ", k)
            print("Found: " + parsed[k[0]['faceId']])
            tuplehere = getRectangleTuple(face)
            drawhere.rectangle(tuplehere, outline='green')
            drawhere.text(tuplehere, parsed[k[0]['faceId']], font=ImageFont.truetype("font_path123"))
        except:
            print("No faces found.")
            flag = True
        if flag:
            for face in array:
                drawhere.rectangle(getRectangleTuple(face), outline='red')


    # draw.show()
    cv2.imshow("result", cv2.cvtColor(np.array(draw), cv2.COLOR_RGB2BGR))
    cv2.waitKey(3000)











