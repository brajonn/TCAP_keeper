import requests
import json

url = "https://api.thegraph.com/subgraphs/name/cryptexfinance/tcap-graph"
json = {'query': '{vaults(where: {currentRatio_gt:"0", debt_gt:"0", currentRatio_lt:"175"}) {vaultId owner debt collateral currentRatio address}}'}
#json = {'query': '{vaults(where: {owner:"0xee5a82516dc71ba3cb0cc2056095e41fb894ae2d"}) {vaultId owner debt collateral currentRatio address}}'}
response = requests.post(url=url, json=json)
_data = response.json()
vaults = []
if _data['data'] == []:
    print('No vaults with currentRatio under 225')
else:
    for n  in _data['data']['vaults']:
        vaults.append(int(n.get('vaultId')))

print(_data)
print(vaults)
