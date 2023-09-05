from pysus.online_data.sinasc import download
from pysus.online_data import parquets_to_dataframe
from pysus.online_data import SINAN
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('/Users/walterjr/Downloads/violencia_2009_2021.csv', encoding='latin-1')

# lista1 = SINAN.list_diseases()
# lista2 = SINAN.get_available_years('Violência Domestica')

# df = parquets_to_dataframe(SINAN.download('Violência Domestica', SINAN.get_available_years('Violência Domestica')[0]))

# for ano in SINAN.get_available_years('Violência Domestica')[1:-1]:
#   SINAN.download('Violência Domestica', ano)
#   df_t = parquets_to_dataframe(SINAN.download('Violência Domestica', ano))
#   df = pd.concat([df, df_t], ignore_index=True)

   
# lista1 = SINAN.list_diseases()
# lista2 = SINAN.get_available_years('Violência Domestica')

# df.columns.to_list()

# df = df.loc[(df.CS_SEXO == 'F') & (df.NDUPLIC != "2") &(df.REL_PROPRI != "1")]

# df = df[['TP_NOT', 'DT_NOTIFIC', 'NU_ANO', 'SG_UF_NOT', 'ID_MUNICIP', 'ID_UNIDADE', 'DT_OCOR', 'NU_IDADE_N',
#          'CS_SEXO', 'CS_GESTANT', 'CS_RACA', 'CS_ESCOL_N', 'SG_UF', 'ID_MN_RESI', 'ID_PAIS', 'NDUPLIC',
#          'ID_OCUPA_N', 'SIT_CONJUG', 'DEF_TRANS', 'SG_UF_OCOR', 'ID_MN_OCOR', 'HORA_OCOR', 'LOCAL_OCOR',
#          'OUT_VEZES', 'LES_AUTOP', 'VIOL_FISIC', 'VIOL_PSICO', 'VIOL_TORT', 'VIOL_SEXU', 'VIOL_TRAF',
#          'VIOL_FINAN', 'VIOL_LEGAL', 'VIOL_NEGLI', 'VIOL_INFAN', 'AG_FORCA', 'AG_ENFOR', 'AG_OBJETO',
#          'AG_CORTE', 'AG_QUENTE', 'AG_ENVEN', 'AG_FOGO', 'AG_AMEACA', 'SEX_ASSEDI', 'SEX_ESTUPR', 'SEX_PUDOR',
#          'SEX_EXPLO', 'SEX_PORNO', 'LESAO_NAT', 'LESAO_ESPE', 'LESAO_CORP', 'NUM_ENVOLV', 'REL_SEXUAL',
#          'REL_PAI', 'REL_PAD', 'REL_MAD', 'REL_CONJ', 'REL_EXCON', 'REL_NAMO', 'REL_EXNAM', 'REL_FILHO',
#          'REL_DESCO','REL_IRMAO', 'REL_CUIDA', 'REL_CONHEC', 'REL_PATRAO', 'REL_INST', 'REL_MAE', 'REL_POL',
#          'AUTOR_SEXO', 'AUTOR_ALCO', 'ENC_SAUDE', 'ENC_TUTELA', 'ENC_VARA', 'ENC_ABRIGO', 'ENC_SENTIN',
#          'ENC_DEAM', 'ENC_DPCA', 'ENC_DELEG', 'ENC_MPU', 'ENC_MULHER', 'ENC_CREAS', 'ENC_IML',
#          'REL_TRAB', 'CLASSI_FIN', 'EVOLUCAO',
#          'DT_OBITO', 'ORIENT_SEX', 'IDENT_GEN', 'VIOL_MOTIV', 'CICL_VID', 'REDE_SAU', 'ASSIST_SOC',
#          'REDE_EDUCA', 'ATEND_MULH', 'DIR_HUMAN', 'MPU', 'DELEG_MULH', 'DELEG', 'DEFEN_PUBL', 'DT_ENCERRA']]

# for coluna in df.columns:
#     print(f'{coluna}\n{df[coluna].unique()}\n\n')

df.replace('', np.nan, inplace=True)

# pd.set_option('display.max_rows', None)
# df.isna().mean()*100

df['ASSIST_SOC'].info()

mapeamento = {2.0: 'não', 1.0: 'sim', 9.0: 'ignorado'}
df['ASSIST_SOC'] = df['ASSIST_SOC'].replace(mapeamento)
df['ASSIST_SOC'].tail(20)

# Agrupamento por ano de nas e assist_soc =1

df = df[df['ANO_NASC'] >= 1800]
df1 = df[df['ASSIST_SOC'] == 'sim']
df2 = df[df['ASSIST_SOC'] == 'não']
grouped1 = df1.groupby('ANO_NASC').size().reset_index(name='COUNT')
grouped2 = df2.groupby('ANO_NASC').size().reset_index(name='COUNT')




# gráfico mais elaborado mostrando os valores do eixo y

# Criar o gráfico de barras
plt.figure(figsize=(20, 12))
bars = plt.bar(grouped1['ANO_NASC'], grouped1['COUNT'], color='blue')

# Adicionar rótulos e título
plt.xlabel('Ano de Nascimento')
plt.ylabel('Número de Pessoas')
plt.title('Distribuição de Ano de Nascimento e tiveram assist_soc')

# Adicionar os valores do eixo y acima das barras
for bar in bars:
    yval = bar.get_height()
    plt.annotate(f'{yval:.0f}', xy=(bar.get_x() + bar.get_width() / 2, yval), xytext=(0, 3), 
                 textcoords='offset points', ha='center', va='bottom')

# Mostrar o gráfico
plt.show()


# Criar o gráfico de barras
plt.figure(figsize=(20, 12))
bars = plt.bar(grouped2['ANO_NASC'], grouped2['COUNT'], color='blue')

# Adicionar rótulos e título
plt.xlabel('Ano de Nascimento')
plt.ylabel('Número de Pessoas')
plt.title('Distribuição de Ano de Nascimento e não tiveram assist_soc')

# Adicionar os valores do eixo y acima das barras
for bar in bars:
    yval = bar.get_height()
    plt.annotate(f'{yval:.0f}', xy=(bar.get_x() + bar.get_width() / 2, yval), xytext=(0, 3), 
                 textcoords='offset points', ha='center', va='bottom')

# Mostrar o gráfico
plt.show()



