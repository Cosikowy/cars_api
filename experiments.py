import requests
import pandas as pd
from pprint import pprint
import json


# r = requests.get('https://api.github.com/events')

# r = requests.get('https://vpic.nhtsa.dot.gov/api//vehicles/GetAllMakes?format=json')

# some_dict = json.loads(r.content)

# df = pd.DataFrame(some_dict['Results'])
# pprint(df)


with open('makes.json') as makes:
    makes_dict = json.load(makes)
df = pd.DataFrame(makes_dict['Results'])

make = 'T'
if df['Make_Name'].isin([make]).any():
    print('y')
else:
    print('n')


print(make)
print(df['Make_Name'][1])
