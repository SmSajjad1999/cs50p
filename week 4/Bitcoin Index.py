import sys
import requests
import json



if len(sys.argv) == 2:
    try:
        num=float(sys.argv[1])
    except:
        sys.exit("Error")
else:
        sys.exit("Error")

try:
    response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    file=response.json()
    price=float((file["bpi"]["USD"]["rate_float"]))
    price=price * num
    print(f"${price:,.4f}")
except requests.RequestException:
    print("Error")
    sys.exit(1)











