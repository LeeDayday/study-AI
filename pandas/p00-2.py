import pandas as pd
import numpy as np

# 00-2. pandas 기본 자료구조 - Dataframe

# 00-2)-1
data = {
    'food': ['KFC', 'McDonald', 'SchoolFood'],
    'price': [1000, 2000, 2500],
    'rate': [4.5, 3.9, 4.2]
}
df = pd.DataFrame(data)
print(df)

# 00-2)-2
print(df[['food', 'rate']])

# 00-2)-3
df.rename(columns={'food': 'place'}, inplace=True)
print(df)
