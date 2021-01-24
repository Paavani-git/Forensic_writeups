import requests

img_url = "http://dimik.pub/wp-content/uploads/2020/02/javaWeb.jpg"

r = requests.get(img_url)

with open("appa.jpg","wb") as f:
    f.write(r.content)
