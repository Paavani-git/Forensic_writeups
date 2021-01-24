import requests

response = requests.get("https://devnote.in/wp-content/uploads/2020/04/devnote.png")

file = open("appa.png", "wb")
file.write(response.content)
print (response.content)
file.close()
