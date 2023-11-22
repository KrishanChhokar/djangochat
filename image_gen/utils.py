import json
import requests
from PIL import Image
import io
import re
from time import time

API_TOKEN = "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"  # token in case you want to use private API
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "X-Wait-For-Model": "true",
    "X-Use-Cache": "false"
}
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

def generate_image(prompt):
    data = json.dumps({"inputs": prompt})
    response = requests.request("POST", API_URL, headers=HEADERS, data=data)
    original_image = Image.open(io.BytesIO(response.content))

    # Resize the image to your desired dimensions (e.g., 300x300)
    resized_image = original_image.resize((500, 500))

    

    filename = f"{slugify(prompt)}-{int(time())}.png"
    image_path = f"media/{filename}" # Assuming you have a 'media' directory in your Django project
    resized_image.save(image_path)

    return image_path



def slugify(text):
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text
