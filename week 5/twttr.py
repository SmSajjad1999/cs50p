def main():
    name=input("Name:")
    short=shorten(name)
    print(short)


def shorten(word):
    name=""
    for i in word:
        if not i.lower() in ["a","e","i","o","u"]:
            name=name + i
    return name


if __name__ == "__main__":
    main()