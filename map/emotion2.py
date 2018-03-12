import requests
from io import BytesIO
from PIL import Image, ImageDraw
import os
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from io import BytesIO
from PIL import Image
import mplleaflet
import cv2
import os


subscription_key = os.getenv("KEY_face")
assert subscription_key

emotion_recognition_url = "https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize"
header = {'Ocp-Apim-Subscription-Key': subscription_key }
# requests.post(emotion_recognition_url, headers=headers, json=image_data)

# response = requests.get(img_url)
# img = Image.open(BytesIO(response.content))
# draw = ImageDraw.Draw(img)


# headers  = {'Ocp-Apim-Subscription-Key': subscription_key, "Content-Type": "application/octet-stream" }
# response = requests.post(emotion_recognition_url, headers=headers, data=image_data)
# response.raise_for_status()
# analysis = response.json()
# analysis

def annotate_image():    
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        cv2.imwrite("emo.jpg", img)
        image_path = "emo.jpg"
        image_data = open(image_path, "rb").read()
        headers  = {'Ocp-Apim-Subscription-Key': subscription_key, "Content-Type": "application/octet-stream" }
        response = requests.post(emotion_recognition_url, headers=headers, data=image_data)
        response.raise_for_status()
        analysis = response.json()

        plt.figure()

        image  = Image.open(image_path)
        ax     = plt.imshow(image, alpha=0.6)

        max_ = 0
        min_ = 1
        for face in analysis:
            em = face["scores"]
            if(em["happiness"]>max_):
                max_ = em["happiness"]
            if(em["happiness"]<min_):
                min_ = em["happiness"]  

        for face in analysis:
            fr = face["faceRectangle"]
            em = face["scores"]

            if(max_ == em["happiness"]):
                origin = (fr["left"], fr["top"])
                p = Rectangle(origin, fr["width"], fr["height"], fill=False, linewidth=2, color='b')
                ax.axes.add_patch(p)
                ct = "\n".join(["{0:<10s}{1:>.4f}".format(k,v) for k, v in sorted(list(em.items()),key=lambda r: r[1], reverse=True)][:3])
                # plt.text(origin[0], origin[1], ct, fontsize=20, va="bottom")    
            if(min_ == em["happiness"]):
                origin = (fr["left"], fr["top"])
                p = Rectangle(origin, fr["width"], fr["height"], fill=False, linewidth=2, color='r')
                ax.axes.add_patch(p)
                ct = "\n".join(["{0:<10s}{1:>.4f}".format(k,v) for k, v in sorted(list(em.items()),key=lambda r: r[1], reverse=True)][:3])    
        _ = plt.axis("off")

        plt.savefig("save.jpg")
        save = cv2.imread("save.jpg")
        cv2.imshow("result", save)
        if cv2.waitKey(3000) & 0xFF == ord('q'):
            break

# annotate_image(image_path)    
