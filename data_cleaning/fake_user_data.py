import json

import pandas as pd
import names

df = pd.DataFrame.from_csv('uni_numbers.csv', encoding='latin-1', index_col=None, sep=';')
print(df)

seed_array = []
for index, row\
        in df.iterrows():
    user_skeleton =  {
        "username": names.get_full_name(),
        "email": names.get_full_name(),
        "password": 'password',
        "profile": {
            "first_name": 'a',
            "last_name": 'y',
            "allowed_participants":  row['number'],
            "university": row['university'],
            "gender": 'F'
        },
        "create": "true"
    }
    seed_array.append(user_skeleton)
#print(seed_array)

with open('data.json', 'w') as outfile:
    json.dump(seed_array, outfile)
