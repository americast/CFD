import os
import cognitive_face as CF

KEY = os.getenv("KEY_face")  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)
# If you need to, you can change your base API url with:
#CF.BaseUrl.set('https://westcentralus.api.cognitive.microsoft.com/face/v1.0/')

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
img_url = 'http://www.dailyexcelsior.com/wp-content/uploads/2015/09/Prime-Minister-Narendra-Modi-in-a-group-photograph-with-the-leading-Fortune-500-CEOs-at-a-special-event-in-New-York-on-Thursday.-UNI.jpg'
faces = CF.face.detect(img_url)
# print(faces)

import requests
from io import BytesIO
from PIL import Image, ImageDraw

def getRectangle(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left + rect['height']
    right = top + rect['width']
    return ((left, top), (bottom, right))

#Download the image from the url
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))

print(img)
#For each face returned use the face rectangle and draw a red box.
draw = ImageDraw.Draw(img)
x = []
for face in faces:
    temp = (getRectangle(face))
    draw.rectangle(getRectangle(face), outline='red')
    x.append(img[temp[0][1]:temp[1][1], temp[0][0]:temp[1][0]])

print(x)
imshow(x[1])
#Display the image in the users default image browser.
img.show()