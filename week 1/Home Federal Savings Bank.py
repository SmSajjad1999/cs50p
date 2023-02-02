x=input("Greeting:")
x=x.lstrip()
x=x.lower()
print(x)
if x[0:5] == "hello":
    print("0$")
elif x[0] == "h":
    print("20$")
else:
    print("100$")