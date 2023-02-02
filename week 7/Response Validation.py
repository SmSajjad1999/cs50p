from validator_collection import validators


def main():
    print(check(input("Your Email Adress: ")))



def check(s):
    try:
        validators.email(s)
        return "Valid"
    except:
        return "Invalid"


if __name__=="__main__":
    main()