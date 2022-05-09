# -*- coding: utf-8 -*-


import requests
import pandas as pd

url = "https://qa.bki.dk/api/stats/ncr"

payload={}
headers = {
  'Authorization': 'Basic bm1vOkxhZ2thZ2VwbGFnZTEyMw==',
  'Cookie': 'LtpaToken=AAECAzYyNzhDMTdBNjI3OTMxRkFDTj1OaWNob2xhaiBNhm5zc29uIE9sc2VuL09VPUJydWdlcmUvT1U9SG9qYmplcmcvREM9YmtpL0RDPWRrJWJFFxF7CQtHYevRAfStIiKZQHc=; SessionID=6757E9F11F001C6E9AB9C32545944DAAF94F5146'
}

response = requests.request("GET", url, headers=headers, data=payload)

response_json = response.json()[0]
# response_json = response_json[0]
response_headers = response_json['fields']
response_headers_keys = [k for k,v in response_headers.items()]


response_data = response_json['data']

df_response_data = pd.DataFrame(columns = response_headers_keys)
df_response_data = pd.DataFrame(response_data)

# df_response = pd.DataFrame.from_dict(response_json)

