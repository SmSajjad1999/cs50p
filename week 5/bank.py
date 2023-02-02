def main():
    x=input("Greeting:")
    print(value(x))
    


def value(greeting):
    
    x=greeting.lstrip().lower()
    if x[0:5] == "bello":
        return ("0$")
    elif x[0] == "h":
        return ("20$")
    else:
        return ("100$")
    


if __name__ == "__main__":
    main()