import pandas as pd
import numpy as np
from IPython.display import Image

# 01-1. 파일 입출력

from opendata import dataset

# 데이터셋 다운로드
dataset.download('판다스입출력샘플')


# excel 불러오기
sample = pd.read_excel('data/file_sample.xlsx', sheet_name=None, engine='openpyxl')

print(sample.keys())

sample_202010 = sample['2020년 10월']

print(sample_202010)