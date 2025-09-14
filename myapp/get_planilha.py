import pandas as pd
from cadastros.models import Cliente

df = pd.read_excel("Planilha.xlsx", skiprows=1)




def create_clients(df: pd.DataFrame):
    for index, item in df.iterrows():
        Cliente(nome= item['Empresa'], cnpj= item['CNPJ']).save()



