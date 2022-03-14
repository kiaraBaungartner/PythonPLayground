#import
import pandas as pd
import os
from twilio.rest import Client

client = Client('ACe1d1d00ca38f22f6047adf00536f2ef7', '535af5523d787785ea1d07089bfb257c')

#code
listaMeses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in listaMeses:
    tabelaVendas = pd.read_excel(f'{mes}.xlsx')

    if (tabelaVendas['Vendas'] > 55000).any():
        linha = tabelaVendas['Vendas'] > 55000
        vendedor = tabelaVendas.loc[linha, 'Vendedor'].values[0]
        vendas = tabelaVendas.loc[tabelaVendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'no mes de {mes}, a pessoa {vendedor}, bateu a meta de vendas com {vendas}R$')
        message = client.messages.create(
        from_='+12134604243',
        to='+5511930307349',
        body = f'no mes de {mes}, a pessoa {vendedor}, bateu a meta de vendas com {vendas} R$')
        print(message.sid)


