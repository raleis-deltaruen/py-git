from pyfiglet import Figlet

figlet = Figlet()
import sys
import random

x = input("type something: ")

font_name = random.choice(figlet.getFonts())
figlet.setFont(font=font_name)

if len(sys.argv) == 3:
    arg = sys.argv[1]
    font_name = sys.argv[2]
    if arg == "-f" or arg == "--font":
        for font in figlet.getFonts():
            if font_name == font:
                figlet.setFont(font=font_name)
                break
        else: 
            print("Invalid")
            sys.exit()           
    else: 
        print("Invalid")
        sys.exit()        
print(figlet.renderText(x))