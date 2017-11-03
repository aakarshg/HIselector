import pandas as pd

df = pd.read_csv('Business_Rules_PUF.csv', usecols=[7,18,19])

df = df[df['DentalOnlyPlan']=='No']

df = df[df['MarketCoverage']=='Individual']

for row in df.iterrows():
    print row

df = df['StandardComponentId']
df.to_csv('Plans_shortlisted.csv')
