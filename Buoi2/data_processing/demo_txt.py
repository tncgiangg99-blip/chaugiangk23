#%%
import pandas as pd
#%%
df = pd.read_csv('../dataset/SalesTransactions/SalesTransactions.txt',
                 encoding = 'utf-8', dtype = 'unicode',low_memory=False)
print(df)
#%% CSV
df1 = pd.read_csv('../dataset/SalesTransactions/SalesTransactions.csv',encoding = 'utf-8', dtype = 'unicode',low_memory=False)
print(df1)
#%%
from bs4 import BeautifulSoup
with open ('../dataset/SalesTransactions/SalesTransactions.xml','r') as f:
    data = f.read()
bs_data = BeautifulSoup(data,'lxml')
UelSample = bs_data.find_all('UelSample')
print(UelSample)
#%% excel
import pandas as pd
dataframe = pd.read_excel('../dataset/SalesTransactions/SalesTransactions.xlsx')
print(dataframe)
#%% json
import pandas as pd
df = pd.read_json("../dataset/SalesTransactions/SalesTransactions.json",encoding = 'utf-8',dtype = 'unicode')
print(df)
