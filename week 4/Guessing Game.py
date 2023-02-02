import random
import pyfiglet
from pyfiglet import Figlet
figlet=Figlet()
font=figlet.getFonts()
figlet.setFont(font="slant")

while True:
    try:
        n=int(input("Number: "))
        if n >= 0:
            break
    except:
        pass

n=random.randrange(0,n)
c=1
while True:
    try:
        c=int(input("Guess: "))
        if c < n:
            print("Too Small!")
        elif c > n:
            print("Too Large")
        elif c == n:
            break
    except:
        pass
print(figlet.renderText("Right Guess"))




