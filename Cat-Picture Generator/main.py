import requests
import os
from PIL import Image

url = "https://cataas.com/cat"

filename = "randomcat.jpg"


def ask():
    choice = input("Do you wish to delete the image? (y/n) ")
    choice = choice.lower()

    if choice == "n":
        print("\nImage saved to current directory:")
        print(os.getcwd() + "/" + filename)

    elif choice == "y":
        os.remove(filename)
        print("\nImage deleted")

    else:
        ask()


r = requests.get(url)
with open(filename, "wb") as f:
    f.write(r.content)

if os.path.exists(filename):
    img = Image.open(filename)
    img.show()

    ask()