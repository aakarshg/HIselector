import sqlite3
import pandas as pd

df = pd.read_csv('Plans_shortlisted.csv')
plans_list = []

for row in df.iterrows():
    plans_list.append(row[1])


conn = sqlite3.connect('/home/agopi/sample.db')
c = conn.cursor()

df1 = pd.read_csv('Business_Rules_PUF.csv', usecols=[7,18,19]) # open the particular csv file and give indices needed for columns


### Do sample processing needed here as
# df = df[df['MarketCoverage']=='Individual']




for row in df1.iterrows():
    if row[0] in plans_list: # assuming 0 is the plan_id index
        c.execute("insert into table {tn} VALUES({},{},{});".format(row[0],
        row[1],row[2],row[3]) )    #add table name, values and rows accordingly

conn.commit()
conn.close()
