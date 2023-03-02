import pandas as pd
import re

data1 = {
    "name":['Ravi', 'Arvind', 'Ramesh', 'Akram', 'Jhon'],
    "English":[67,98,78,82,64],
    "Maths":[67,98,78,82,64],
    "Physics":[67,98,78,82,64],
    "Chemistry":[67,98,78,82,64],
    "Physical Education":[67,98,78,82,64],
    "City":['Rameshwaram', 'Kolkata', 'Ajmer', 'Kota', 'kasauli']
 }

df = pd.DataFrame(data1)
df.to_excel('Student.xlsx')
df['Average'] = (df["English"]+df["Maths"] + df["Physics"] + df["Chemistry"]+df["Physical Education"])/5
df['Date of Birth'] = ['12-03-1999', '30-03-1998', '23-09-2000','23-02-1998', '31-05-1997']
#print(df.loc[0])
dob = re.search(r'[0-31]-[0-12]-[0-2022]', str(df.loc[0])).group()
print(dob)
#print(df.loc[:, :])
#print(df.describe())