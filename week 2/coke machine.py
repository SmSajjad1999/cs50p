def main():
    due=50
    print("Amount due:",due)
    while due>0:
        coin=int(input("insert coin:"))

        if coin == 25 or coin == 5 or coin == 10:
            due=due-coin
            if due>0:
                print("Amount due:",due)
            elif due<= 0:
                print("Change:",abs(due))
        else:
            print("wrong,Mehraz vai")
            
    
if __name__ == "__main__":
    main()