import re
import sys


def main():
    print((convert(input("Hours: ").strip())))


def convert(s):

    if match := re.search(r"^0?([1-9]|1[120])(?:\:([0-5][0-9]))? (AM|PM) ?to ([1-9]|1[120])(?:\:([0-5][0-9]))? (AM|PM)$",s) :
        #return True

        one=int(match.group(1))
        four=int(match.group(4))
        if match.group(3) == "PM":
            one=int(match.group(1))+12
        if match.group(6) == "PM":
            four=int(match.group(4))+12

        two= 00
        five= 00
        if match.group(2) != None:
            two+=int(match.group(2))
        if match.group(5) != None:
            five+=int(match.group(5))
    
        return (f"{one:02}:{two:02} to {four:02}:{five:02}")
    else:
        raise ValueError
    
...


if __name__ == "__main__":
    main()