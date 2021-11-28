
import json
import requests
block = "0000000000000000000bc6f5cfeedbfe0c9fbdd2388cc3f9e99807141bd0f583"
url = "https://blockchain.info/rawblock/"+block

# make get url

f = requests.get(url)
f = f.text
blockJson = json.loads(f)
prevBlock = blockJson["prev_block"]
transactions = blockJson["tx"]

print(transactions[1]["out"])
#for tx in transactions:
#    print(tx)