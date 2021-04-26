import os
import pandas as pd
from matplotlib import pyplot as plt

print(*os.listdir("opinions"), sep="\n")
productId=input("Podaj kod produktu: ")

opinions=pd.read_json(f"./opinions/{productId}.json")

opinions.rcmd=opinions.rcmd.apply(lambda x: True if x=="Polecam" else False if x=="Nie polecam" else None)
opinions.stars=opinions.stars.apply(lambda x: float(x.split("/")[0].replace(",", ".")))
opinions.content=opinions.content.apply(lambda x: x.replace("\n", " ").replace("\r", " "))
opinions.purchased=opinions.purchased.apply(lambda x: bool(x))
opinions.useful=opinions.useful.apply(lambda x: int(x))
opinions.useless=opinions.useless.apply(lambda x: int(x))

average_score=opinions.stars.mean()
print(average_score)

recommendations=opinions.rcmd.value_counts(dropna=False).plot.pie(label="", labels=['Recommend', 'Not recommend', 'No data'])
plt.show()
#print(recommendations)

#rcmd=True if rcmd=="Polecam" else False
#stars=float(stars.split("/")[0].replace(",", "."))
#content=content.replace("\n", " ").replace("\r", " ")
#purchased=bool(purchased)
#useful=int(useful)
#useless=int(useless)


print(opinions.head(10))