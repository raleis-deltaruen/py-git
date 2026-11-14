import requests
import sys
try:
    bitcoin_amount = float(sys.argv[1])

except ValueError:
    print("Must be a number")


response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=c21b97f6e6c160d633351c346ef4c891774d7ca2ab9a9497df8af0fa26e8e4fe")
objects = response.json()
print(objects)
print('{:,}'.format(float(objects["data"]["priceUsd"]) * bitcoin_amount))