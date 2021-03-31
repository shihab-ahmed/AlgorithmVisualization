import pandas as pd
import json as js

file = 'MRTK_Content.xlsx'
xl = pd.read_excel(file, sheet_name="Sheet1", header=0)
print(xl)
"""
data = {}
data["locationSet"] = []
for index, row in xl.iterrows():
    loc = row["location"].split(",")
    location = row["location"]
    name = row["Names"]
    data["locationSet"].append(
        {
            'id': location,
            'name': name,
            'lat': loc[0],
            'lot': loc[1]
        }
    )
with open('data.json', 'w') as outfile:
    js.dump(data, outfile)
print(data)
"""
