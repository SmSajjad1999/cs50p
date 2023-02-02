import random


def main():
    lvl=get_level()
    
    generate_integer(lvl)


def get_level():
    while True:
        try:
            x=int(input("lvl: "))
            if 1 <= x <=3:
                return x
        except:
            pass
     


def generate_integer(level):
    prlm=0
    score=0
    while prlm<=2:
        if level == 1:
            a=random.randrange(0,9)
            b=random.randrange(0,9)
        elif level == 2:
            a=random.randrange(10,99)
            b=random.randrange(10,99)
        elif level == 3:
            a=random.randrange(100,999)
            b=random.randrange(100,999)
        
        c=a+b
        q=0
        while q<=3:
            a=str(a)
            b=str(b)
            try:
                ans=int(input(a+"+"+b+":"))
                if ans==c:
                    prlm+=1
                    score+=1
                    break
                else:
                    if q<2:
                        print("EEE")
                        q+=1
                    else:
                        prlm+=1
                        print(c)
                        break
            except:
                pass

    print("Score:"+str(score)+"/3")                


                     
    
    


if __name__ == "__main__":
    main()