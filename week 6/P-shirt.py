import sys
import os
from PIL import Image,ImageOps





def main():
    
    check_command_line()    
    split_up=os.path.splitext(sys.argv[1])
    #x='C:\Users\Meheraj\.vscode\week 6\shirt.png'
    try:
        pic1=Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not Found")
    
    shirt=Image.open("shirt.png")

    size=shirt.size

    after=ImageOps.fit(pic1,size)

    after.paste(shirt,shirt)

    after.save(sys.argv[2])







    print("hurrah")






def check_command_line():
    
    if len(sys.argv) > 3:
        sys.exit("Too many Argument")
    if len(sys.argv) < 3:
        sys.exit("Too few Argument")
    if not (sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".jpeg") or sys.argv[1].endswith(".png")):
        sys.exit("File1 not found")
    if not (sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".jpeg") or sys.argv[2].endswith(".png")):
        sys.exit("File2 not found")
    split_1st=os.path.splitext(sys.argv[1])
    split_2st=os.path.splitext(sys.argv[2])
    if not split_1st[1] == split_2st[1]:
        sys.exit("Not same extensiton")




















if __name__ == "__main__":
    main()