def main():
    time=input("What time is it?:")
    v=convert(time)
    if 7 <= v<= 8:
        print("Breakfast Time")
    elif 12 <= v <= 13:
        print("Lunch Time")
    elif 18 <= v<= 19:
        print("Dinner Time")
    else:
        print("Hello Goribs,Kam kor")


def convert(time):
    x , y=time.split(":")
    x=float(x)
    y=float(y)/60
    z=x+y
    v=z
    return v
    


if __name__ == "__main__":
    main()