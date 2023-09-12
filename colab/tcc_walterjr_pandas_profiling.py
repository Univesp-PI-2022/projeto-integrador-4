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


