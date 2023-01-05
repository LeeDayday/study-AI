import pandas as pd
import numpy as np

# 00-1. pandas 기본 자료구조 - Series

# 00-1)-1
s1 = pd.Series(np.arange(3.0, 13.0, 2.0), dtype='float32')
print(s1)

# 00-1)-2
s2 = pd.Series(['가', '나', '다', '라', '마'])
print(s2)

# 00-1)-3
sample = pd.Series(np.arange(10, 51, 10), dtype='int64')
sample.index = list('가나다라마')
print(sample)

# 00-1)-4
print(sample[['나', '라']])

np.random.seed(20)
sample2 = pd.Series(np.random.randint(100, 200, size=(15,)), dtype='int64')

# 00-1)-5
print(sample2[sample2 <= 160])

# 🎯 00-1)-6
print(sample2[(130 <= sample2) & (sample2 <= 170)])

# 00-1)-7
s3 = pd.Series(['apple', np.nan, 'banana', 'kiwi', 'gubong'])
s3.index = list('가나다라마')
print(s3)

# 00-1)-8
sample3 = pd.Series(['IT서비스', np.nan, '반도체', np.nan, '바이오', '자율주행'])
print(sample3[sample3.isna()])

# 00-1)-9
print(sample3[sample3.notna()])

np.random.seed(0)
sample4 = pd.Series(np.random.randint(100, 200, size=(10,)))

# 00-1)-10
print(sample4[2:7])

# 00-1)-11
np.random.seed(0)
sample5 = pd.Series(np.random.randint(100, 200, size=(10,)), index=list('가나다라마바사아자차'))
print(sample5['바':'차'])
print(sample5['가':'다'])
print(sample5['나':'바'])
