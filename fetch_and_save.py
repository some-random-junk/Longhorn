import requests
from datetime import datetime

# BOM radar image URL
url = "http://www.bom.gov.au/radar/IDR703.gif"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "http://www.bom.gov.au/"
}

# Download image
r = requests.get(url, headers=headers)
if r.status_code == 200:
    with open("radar/IDR703.gif", "wb") as f:
        f.write(r.content)
    print(f"Downloaded radar image at {datetime.now()}")
else:
    print(f"Failed to download image: {r.status_code}")