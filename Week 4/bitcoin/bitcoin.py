import requests
import sys

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        pass

    resposta = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json")
    o = resposta.json()

    bt_value = o["bpi"]["USD"]["rate_float"] * float(sys.argv[1])

    print(f"${bt_value:,.4f}")

except ValueError:
    sys.exit("Command-line argument is not a number")
