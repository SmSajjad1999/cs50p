def main():
    name=input("name:")
    x=camelcase(name)


def camelcase(name):
    print (name[0].lower(),end="")
    for i in name[1:]:
        if i.isupper():
            print("_",i.lower(),end="")
        else:
            print(i,end="")



if __name__ == "__main__":
    main()
