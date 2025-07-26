from PIL import Image
import requests
from io import BytesIO
from datetime import datetime
import os

# BOM radar image URL
url = "http://www.bom.gov.au/radar/IDR703.gif"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "http://www.bom.gov.au/"
}

# Create output folder if it doesn't exist
os.makedirs("radar", exist_ok=True)

# Download image
r = requests.get(url, headers=headers)
if r.status_code == 200:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save original high-res GIF
    orig_path = "radar/IDR703_orig.gif"
    with open(orig_path, "wb") as f:
        f.write(r.content)
    print(f"[{timestamp}] Saved original GIF to {orig_path}")

    # Open it with PIL and convert to RGB
    img = Image.open(BytesIO(r.content)).convert("RGB")

    # Resize image to 320x240 max, preserving aspect ratio
    img.thumbnail((320, 240))

    # Save resized image as JPEG
    resized_path = "radar/IDR703.jpg"
    img.save(resized_path, "JPEG", quality=85)
    print(f"[{timestamp}] Saved resized JPEG to {resized_path}")

else:
    print(f"Failed to download image: {r.status_code}")
