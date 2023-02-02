import sys
import random

from pyfiglet import Figlet
figlet=Figlet()

#print(len(sys.argv))
fonts=figlet.getFonts()



if len(sys.argv) == 3 and (sys.argv[1]=="-f" or sys.argv[1]=="--font"):
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Baal")
        sys.exit()
elif len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))
else:
    print("baal")
    sys.exit()




msg=input("Input")


print(figlet.renderText(msg))
