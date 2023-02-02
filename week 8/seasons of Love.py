from datetime import date
import sys
import re


def main():
    birth=input("Birthday:").strip()
    check(birth)





def check(s):
    if match := re.search(r"^[0-9]{4}-([01][0-9])-([1230][0-9])$",s):
        print("valid")
    else:
        sys.exit("invalid")
...


if __name__ == "__main__":
    main()