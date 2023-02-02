import re
import sys


def main():
    parse(input("HTML: "))


def parse(s):
    if match := re.search(r'^<iframe .*src="https?:\/\/(?:www\.)?youtube\.com\/embed\/(.+?)"',s):
        print(f"\nhttps://youtu.be/{match.group(1)}")
    else:
        print(None)



if __name__ == "__main__":
    main()