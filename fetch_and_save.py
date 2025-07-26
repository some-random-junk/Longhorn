import requests
from datetime import datetime
from PIL import Image
import os
import struct

# Setup
url = "http://www.bom.gov.au/radar/IDR703.gif"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "http://www.bom.gov.au/"
}
output_dir = "radar"
os.makedirs(output_dir, exist_ok=True)

# Filenames
gif_path = os.path.join(output_dir, "IDR703.gif")
jpg_path = os.path.join(output_dir, "IDR703_320x240.jpg")
raw_path = os.path.join(output_dir, "IDR703_320x240.raw")

# Download the GIF
r = requests.get(url, headers=headers)
if r.status_code == 200:
    with open(gif_path, "wb") as f:
        f.write(r.content)
    print(f"Downloaded GIF at {datetime.now()}")

    # Convert to 320x240 JPEG and RAW RGB565
    img = Image.open(gif_path).convert("RGB").resize((320, 240))
    
    # Save resized JPG (optional)
    img.save(jpg_path, "JPEG")
    print(f"Saved resized JPG: {jpg_path}")

    # Save RAW RGB565
    with open(raw_path, "wb") as raw:
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = img.getpixel((x, y))
                rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
                raw.write(struct.pack(">H", rgb565))  # Big endian
    print(f"Saved RAW RGB565: {raw_path}")

else:
    print(f"Failed to download image: {r.status_code}")
