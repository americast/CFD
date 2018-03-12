import os
import cognitive_face as CF
import numpy as np
import cv2
from PIL import Image, ImageDraw

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

cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        draw = Image.fromarray(np.uint8(cm.gist_earth(myarray)*255))

        draw = ImageDraw.Draw(img)
        image_array = []
        count = 0
        for face in faces:
            count+=1
            a = draw.crop(getRectangle(face))
            a.save(count+".jpg")

            array = CF.face.detect(count+".jpg")
            print("array:", array)

            k = CF.face.identify([array[0]['faceId']], "kubs")
            try:
                print("Found: " + parsed[k[0]['faceId']])
                tuplehere = getRectangleTuple(face)
                draw.rectangle(, outline='red')
                draw.text(tuplehere, parsed[k[0]['faceId']], font=ImageFont.truetype("font_path123"))
            except:
                print("No faces found.")

        draw.show()











