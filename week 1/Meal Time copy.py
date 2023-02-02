def main():
    time=input("What time is it?:")
    convert(time)


def convert(time):
    x , y=time.split(":")
    x=int(x)
    y=int(y)
    if x == 7:
        print("Breakfast time")
    elif x==7 and y==0:
        print("Breakfast time")



if __name__ == "__main__":
    main()