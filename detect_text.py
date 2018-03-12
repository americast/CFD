import requests
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from io import BytesIO
from PIL import Image, ImageDraw
import urllib


image_url = "https://3.bp.blogspot.com/-lmL864sF8A4/WGph86k0eEI/AAAAAAAAEE4/34SkurmxHXI2bqupRoeGO2makaYFkPQngCLcB/s1600/je2.png"
vision_base_url = 'http://westcentralus.api.cognitive.microsoft.com/vision/v1.0/'
ocr_url = vision_base_url + "ocr"
ocr_url = "http://10.131.40.182:8000/je2.png"
subscription_key = "9c47fc0301fe4e3696b44818e1721da0"
assert subscription_key

def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
    # return the image
    return image

def localize_text(subscription_key, image_url, key_text):
    headers  = {'Ocp-Apim-Subscription-Key': subscription_key}
    params   = {'language': 'unk', 'detectOrientation ': 'true'}
    data     = {'url': image_url}
    response = requests.post(ocr_url, headers=headers, params=params, json=data)
    response.raise_for_status()

    analysis = response.json()
    # print(analysis)

    line_infos = [region["lines"] for region in analysis["regions"]]
    word_infos = []
    for line in line_infos:
        for word_metadata in line:
            for word_info in word_metadata["words"]:
                # print(word_info["text"])
                if(key_text.lower() in word_info["text"].lower()):
                    word_infos.append(word_info)
    word_infos
    # image = url_to_image(image_url)

    # for word in word_infos:
    #     bb = [int(num) for num in word["boundingBox"].split(",")]
    #     tl = (bb[0], bb[1])
    #     br = (bb[0]+bb[2], bb[1]+bb[3])
    #     cv2.rectangle(image,tl,br,(0,255,0),3)
    # print("word_infos = ",word_infos)


    plt.figure(figsize=(12,12))

    image  = Image.open(BytesIO(requests.get(image_url).content))
    ax     = plt.imshow(image, alpha=0.8)
    for word in word_infos:
        bbox = [int(num) for num in word["boundingBox"].split(",")]
        text = word["text"]
        origin = (bbox[0], bbox[1])
        patch  = Rectangle(origin, bbox[2], bbox[3], fill=False, linewidth=2, color='g')
        ax.axes.add_patch(patch)
        # plt.text(origin[0], origin[1], text, fontsize=20, weight="bold", va="top")
    _ = plt.axis("off")

    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle() 
    plt.show()
    # imshow("final",image)
    # cv2.waitKey(5)

# localize_text(subscription_key, "http://10.131.40.182:8000/je2.png", "Rahul")