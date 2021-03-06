import os
import cognitive_face as CF
import numpy as np
import cv2

KEY = os.getenv("KEY_face")  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)
# If you need to, you can change your base API url with:
#CF.BaseUrl.set('https://westcentralus.api.cognitive.microsoft.com/face/v1.0/')

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

array = CF.face.detect("ss/1.jpg")
print("array:", array)

k = CF.face.identify([array[0]['faceId']], "ss")
print(k)