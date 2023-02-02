import inflect

p = inflect.engine()


name=[]
x=1
while x!= "exit":
    try:
        x=input("Name:")
        name.append(x)
    except:
        print()
        break

c=p.join(name)

print("Adieu, adieu, to",c)
