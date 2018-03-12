import os
import cognitive_face as CF

KEY = os.getenv("KEY_face")  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)
# If you need to, you can change your base API url with:
#CF.BaseUrl.set('https://westcentralus.api.cognitive.microsoft.com/face/v1.0/')

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
# img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'

CF.person_group.create("ss")
a = CF.person.create("ss", "namo")
print(a)

# img1 = cv2.imread("img/1.jpg")
# img2 = cv2.imread("img/2.jpg")
# img3 = cv2.imread("img/3.jpg")

face_id1 = CF.person.add_face("ss/1.jpg", "ss", a['personId'])
face_id2 = CF.person.add_face("ss/1.jpg", "ss", a['personId'])
face_id3 = CF.person.add_face("ss/1.jpg", "ss", a['personId'])

print(CF.person.get("ss", a['personId']))
CF.person_group.train("ss")