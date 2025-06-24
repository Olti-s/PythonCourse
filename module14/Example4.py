import pandas as pd
import matplotlib.pyplot as plt


#geting data from file
df=pd.read_csv("avgIQpercountry.csv")


nobel_prizes=df.groupby("Continent")["Nobel Prices"].sum()

no_of_continents=nobel_prizes.count()

colors=["gold","lightcoral","yellow","thistle","orange","lightskyblue","aquamarine","burlywood"]
plt.figure(figsize=(10,10))

nobel_prizes.plot(kind="pie", colors=colors, autopct="%1.1f%%")

plt.title("Distribution of Nobel Prizes by Continent")
plt.axis("equal")
plt.ylabel("")
plt.tight_layout()
plt.show()










