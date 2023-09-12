from pysus.online_data.sinasc import download
from pysus.online_data import parquets_to_dataframe
from pysus.online_data import SINAN
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from pandas_profiling import ProfileReport

df = pd.read_csv('/Users/walterjr/Downloads/violencia_2009_2021_tratado_novo.csv', encoding='latin-1')
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

# Gerando gráfico para análise

plt.figure(figsize=(12, 8))
bars = plt.bar(agrupado['dia_semana'], agrupado['DT_OCOR'])
plt.xlabel('Dia da Semana')
plt.ylabel('Número de Ocorrências')
plt.title('Número de Ocorrências por Dia da Semana')
plt.xticks(rotation=45)

for bar in bars:
    height = bar.get_height()
    plt.annotate('{}'.format(height),
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # 3 pontos de deslocamento vertical
                 textcoords="offset points",
                 ha='center', va='bottom')

plt.tight_layout()
plt.show()


# Criar o gráfico de barras com Seaborn

plt.figure(figsize=(10, 6))
ax = sns.barplot(x='dia_semana', y='DT_OCOR', data=agrupado)
plt.xlabel('Dia da Semana')
plt.ylabel('Número de Ocorrências')
plt.title('Número de Ocorrências por Dia da Semana')
plt.xticks(rotation=45)  


for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='baseline')

plt.tight_layout()
plt.show()


# Uso de plotly para gráfico interativo

fig = px.bar(agrupado, x='dia_semana', y='DT_OCOR',
             labels={'dia_semana': 'Dia da Semana', 'data_ocor': 'Número de Ocorrências'},
             title='Número de Ocorrências por Dia da Semana')


fig.update_layout(xaxis_tickangle=-45, xaxis_title=None, yaxis_title=None)


fig.update_traces(texttemplate='%{y}', textposition='outside')

display(fig)

import plotly.io as pio
pio.write_html(fig, file='grafico_interativo.html', auto_open=True)





