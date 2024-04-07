from PIL import Image
import requests
from io import BytesIO

image_url = 'https://example.com/mona_lisa.jpg'
response = requests.get(image_url)
image_data = BytesIO(response.content)

mona_lisa = Image.open(image_data)

width, height = mona_lisa.size
aspect_ratio = height / float(width)
new_width = 100
new_height = int(aspect_ratio * new_width * 0.55)

mona_lisa = mona_lisa.resize((new_width, new_height))
mona_lisa = mona_lisa.convert('L')

ascii_chars = "@%#*+=-:. "

ascii_image = []
pixels = mona_lisa.getdata()
for pixel_value in pixels:
    ascii_image.append(ascii_chars[pixel_value // 32])

ascii_str = ''.join(ascii_image)

for i in range(0, len(ascii_str), new_width):
    print(ascii_str[i:i+new_width]
