from pysus.online_data.sinasc import download
from pysus.online_data import parquets_to_dataframe
from pysus.online_data import SINAN
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_profiling import ProfileReport

df = pd.read_csv('/Users/walterjr/Downloads/violencia_2009_2021_tratado.csv', encoding='latin-1')
df_visao = df.head(10)


profile = ProfileReport(df)
profile.to_file("relatorio_pandas_profiling.html")



df['DT_OCOR'] = pd.to_datetime(df['DT_OCOR'], format='%d/%m/%Y')
df['DT_OCOR'].info()

df['dia_semana'] = df['DT_OCOR'].dt.dayofweek
nomes_dias_semana = {
    0: 'Segunda-feira',
    1: 'Terça-feira',
    2: 'Quarta-feira',
    3: 'Quinta-feira',
    4: 'Sexta-feira',
    5: 'Sábado',
    6: 'Domingo'
}
agrupado = df.groupby('dia_semana')['DT_OCOR'].count().reset_index()
agrupado['dia_semana'] = agrupado['dia_semana'].map(nomes_dias_semana)


