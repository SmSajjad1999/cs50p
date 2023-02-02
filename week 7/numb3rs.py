import re
import sys

def main():
        z=input("IP Adress:")
        #print(validate(z))
        match=re.match(r"^(.{1,3})\.(.{1,3})\.(.{1,3})\.(.{1,3})$", z)
        print(match.group(1))
        print(match.group(2))
        print(match.group(3))
        print(match.group(4))
        if int((match.group(1))) <= 255 and int((match.group(2))) <= 255 and int((match.group(3))) <= 255 and int((match.group(4))) <= 255:
            print("Valid")
        else:
            print("Unvalid")



def validate(ip):
    if re.search(r"^(.{1,3})\.(.{1,3})\.(.{1,3})\.(.{1,3})$",ip):
        x="true"
        return x
    

if __name__ == "__main__":
    main()


