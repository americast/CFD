import requests
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from io import BytesIO
from PIL import Image, ImageDraw


image_url = "https://3.bp.blogspot.com/-lmL864sF8A4/WGph86k0eEI/AAAAAAAAEE4/34SkurmxHXI2bqupRoeGO2makaYFkPQngCLcB/s1600/je2.png"
vision_base_url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/'
ocr_url = vision_base_url + "ocr"
subscription_key = "accbc69d955b4c85a1e509825d295f7d"
assert subscription_key

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
    # print("word_infos = ",word_infos)
    plt.figure(figsize=(5,5))

    image  = Image.open(BytesIO(requests.get(image_url).content))
    ax     = plt.imshow(image, alpha=0.5)
    for word in word_infos:
        bbox = [int(num) for num in word["boundingBox"].split(",")]
        text = word["text"]
        origin = (bbox[0], bbox[1])
        patch  = Rectangle(origin, bbox[2], bbox[3], fill=False, linewidth=2, color='y')
        ax.axes.add_patch(patch)
        # plt.text(origin[0], origin[1], text, fontsize=20, weight="bold", va="top")
    _ = plt.axis("off")

    plt.show()

localize_text(subscription_key, image_url, "Rahul")