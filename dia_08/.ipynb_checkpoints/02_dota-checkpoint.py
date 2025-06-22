import requests
import pandas as pd

url = "https://api.opendota.com/api/heroes"

resp = requests.get(url)
df = pd.DataFrame(resp.json())
df.to_csv("heroes.csv", index=False, encoding="utf-8-sig")
#print(df.head())