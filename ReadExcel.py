import pandas as pd

#load the excel file
df = pd.read_excel("username.xlsx")

#print whole excel file
print(df)


#fro printing the specific values
for index , row in df.iterrows():
    print(f"{row['username']},{row['password']}")


