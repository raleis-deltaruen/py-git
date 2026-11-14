import sys
from PIL import Image

if len(sys.argv) > 3:
    print("Too many arguments given")
    sys.exit()
try:   
    photo = Image.open(sys.argv[1])
    shirt = Image.open(sys.argv[2])
    photo = photo.resize((600,800))

    photo.paste(shirt, (0,100), mask = shirt)
    photo.save("newShirt.png")

except FileNotFoundError:
    print("File does not exist")
except IndexError:
    print("File name not given")