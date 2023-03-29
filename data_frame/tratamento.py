#%% importando as bibliotecas
#import sys
#import os
import dotenv
import pandas as pd

import numpy as np
import googlemaps


#%% importando os Dados
caminho = 'https://raw.githubusercontent.com/Alisson-Ursulino-git/Statidados/main/Data_frame/data_frame.csv'
Dados   = pd.read_csv(caminho)
df = Dados
df.replace(to_replace='normal',value=np.nan, inplace=True)
c_type1 = df.dtypes.value_counts()


#%% Ajustando os Preços

#Verifica os valores numéricos
n = df.select_dtypes(include='number')

# Substitui o formato financeiro
filter_price = [col for col in df if col.startswith('listing.pricing')]
df_price = df[filter_price].astype(str)
df_price = df_price.apply( lambda x: (x.str.replace(".","").str.replace(",",".")).replace('nan', np.nan) ) 



#df_price.info()
col_price = df_price.columns
for i in range(len(col_price)):
    df_price[col_price[i]] = df_price[col_price[i]].apply(pd.to_numeric, errors='ignore')

# Devolve ao df os preços ajustados
for i in range(len(col_price)):
    df[col_price[i]] = df_price[col_price[i]]
c_type2 = df.dtypes.value_counts()
#%% Cria uma coluna do endereço completo
df.columns[:13]
listaddress = ['listing.address.city','listing.address.neighborhood', 'listing.address.street']
listnumber = ['listing.address.streetNumber']
df['listing.address'] = df['listing.address.state'].str.cat(df[listaddress], sep=', ')
df['listing.address'] = df['listing.address'].str.cat(df[listnumber].astype(str).replace('nan',''), sep = ' ')
df['listing.address'] = df['listing.address'].replace(np.nan,'')
df.reset_index(inplace=True)
#%% Dataframe Reduzido
df1 = df.select_dtypes(include='number')
df2 = df[filter_price].select_dtypes(include=['object', 'category'])
new_df = pd.concat([df1, df2], axis=1 )

#%% Retorna um BD
def created_data():

    return new_df

created_data()


