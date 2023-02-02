def main():
    x=doller(input("What is your bill?:"))
    y=parcent(input("What is your parcent?:"))
    Tip=x * y
    print(f"Leave ${Tip:.2f}")
def doller(d):
    d=d.strip("$")
    d=float(d)
    return d
def parcent(p):
    p=p.strip("%")
    p=float(p)/100
    return p
        

main()    
   