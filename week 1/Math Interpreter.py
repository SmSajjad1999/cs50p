e=input("Expression=")
e=e.strip()
x,y,z=e.split(" ")
x=int(x)
y=(y)
z=int(z)
a=x,y,z
if y == "+" :
    ans =x + z
    ans=float(ans)
    print(f"{ans:.2f}")
elif y == "*" : 
    ans =x * z
    ans=float(ans)
    print(f"{ans:.1f}")
elif y == "-" :
    ans =x - z
    ans=float(ans)
    print(f"{ans:.1f}")
elif y == "/" :
    ans =x / z
    ans=float(ans)
    print(f"{ans:.1f}")
