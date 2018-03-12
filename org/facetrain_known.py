import os
import cognitive_face as CF
import numpy as np
import cv2
import sys
import json

KEY = os.getenv("KEY_face")  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)
# If you need to, you can change your base API url with:
#CF.BaseUrl.set('https://westcentralus.api.cognitive.microsoft.com/face/v1.0/')

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
# img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
person_gp_id = "kubs"
person_name = sys.argv[1]
here = ""
try:
    here = CF.person_group.create(person_gp_id)
except:
    print here
a = CF.person.create(person_gp_id, person_name)
print(a)
backend_person_id = a['personId']

try:
    f = open('temp.json', 'r')
    names = json.load(f)
except:
    names = {}

# img1 = cv2.imread("img/1.jpg")
# img2 = cv2.imread("img/2.jpg")
# img3 = cv2.imread("img/3.jpg")


image_path = sys.argv[2]
face_id1 = CF.person.add_face(image_path, person_gp_id, a['personId'])
# print("face id 1: ", face_id1, "person_name: ", person_name)
names[face_id1['persistedFaceId']] = person_name

image_path = sys.argv[3]
face_id1 = CF.person.add_face(image_path, person_gp_id, a['personId'])
names[face_id1['persistedFaceId']] = person_name

image_path = sys.argv[4]
face_id1 = CF.person.add_face(image_path, person_gp_id, a['personId'])
names[face_id1['persistedFaceId']] = person_name

print(CF.person.get(person_gp_id, a['personId']))
CF.person_group.train(person_gp_id)

print("names: ",names)

with open('temp.json', 'w') as f:
    f.write(json.dumps(str(names)))

