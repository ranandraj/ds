import pandas as pd
import matplotlib.pyplot as plt

link = "https://datatank.stad.gent/4/mobiliteit/fietstellingencoupure.csv?limit=100000"
df = pd.read_csv(link, sep=';')
#print(df.head())
#print(len(df))
#combined = df['datum'] + ' ' + df['tijd']
df.index=pd.to_datetime(df['datum'] + ' ' + df['tijd'])
df=df.drop(['datum','tijd'],axis=1)
df=df.rename(columns={'ri Centrum': 'direction_center','ri Mariakerke':'direction_mariakerke'})
#print(df.head)
print(pd.Series(df.index).diff().value_counts())
print(df.describe())
df_both=df.sum(axis=1)
df_quiet=df_both[df_both<5]
print(df_quiet.head())
print(df[(df['direction_center'] < 3) | (df['direction_mariakerke'] < 3)].head())
print(df.resample('H').sum().mean())
df_monthly=df.resample('M').sum()
df_monthly.plot()
plt.savefig('output.pdf',format='pdf')
