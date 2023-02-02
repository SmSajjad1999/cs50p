import sys

def main():
    check()
    try:
        file=open(sys.argv[1],'r')
        x=file.readlines()

    except:
        sys.exit('file not found')

    p=check_line(x)



    print(p)
    print("heda")





def check():
    if len(sys.argv) > 2:
        sys.exit("Too many argument")
    elif len(sys.argv) <2:
        sys.exit("too few argv")


def check_line(x):

    count = 0
    for line in x:
        if line.isspace():
            pass
        elif line.lstrip().startswith("#"):
            pass
        else:
            count+=1
    return count
if __name__ == "__main__":
    main()