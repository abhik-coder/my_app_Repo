import os
import urllib.requests

day = ["01d", "02d"]
night = ["01n", "02n"]

img_dir = './img/'
if not os.path.exists(img.dir):
    os.makedirs(img_dir)

for name in day:
    file = img_dir + name
    if not os.path.exists(file):
        urllib.requests.urlretrieve(
