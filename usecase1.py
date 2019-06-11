import pandas as pd
import matplotlib.pyplot as plt

link = "https://datatank.stad.gent/4/mobiliteit/fietstellingencoupure.csv?limit=100000"
df = pd.read_csv(link, sep=';')
print(df.head())
print(len(df))
combined = df['datum'] + ' ' + df['tijd']
print(combined.head)
print(type(combined))
