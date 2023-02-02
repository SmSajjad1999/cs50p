import re
import sys


def main():
    l=(count(input("Text: ")))
    print(len(l))


def count(s):
    match=re.findall(r"\b(um)\b",s)
    return match


...


if __name__ == "__main__":
    main()