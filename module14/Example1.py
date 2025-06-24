import pandas as pd
import matplotlib.pyplot as plt


#geting data from file
df=pd.read_csv("avgIQpercountry.csv")
#filering the data based on average iq
filtered_DF=df[df["Average IQ"]>=100]
#sorting data
filtered_DF=filtered_DF.sort_values(by="Average IQ", ascending=False)
#test the data
print(filtered_DF)
#krijimi i figures ku do te shfaqet te dhenat
plt.figure(figsize=(14,8))
#grafikat si shtylla ku definohet qka osht ne x e qka ne y
bars=plt.bar(filtered_DF["Country"],filtered_DF["Average IQ"], color="skyblue")

plt.title("Average IQ by Country (IQ>100)", fontsize=16)
plt.xlabel("Country",fontsize=14)
plt.ylabel("Average IQ",fontsize=14)

plt.bar_label(bars,fmt="%.2f", fontsize=10,color="black")
plt.tight_layout()





plt.show() #shfaq te dhenat