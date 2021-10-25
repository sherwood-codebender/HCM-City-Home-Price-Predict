import pandas as pd
import numpy as np
import os

# Join tất cả data các file excel vào cùng 1 file excel
def process_docs(path_dir):
    df = pd.DataFrame()
    for filename in os.listdir(path_dir):
        data = pd.read_excel(path_dir + '/' + filename)
        df = pd.concat([df, data], ignore_index=True)
    return df

data = process_docs('./data')
data.to_excel('data.xlsx')

data = pd.read_excel('data.xlsx')
