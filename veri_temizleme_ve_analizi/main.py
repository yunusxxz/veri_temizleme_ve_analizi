import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sb_nuts = pd.read_csv("starbucks.csv")
print(sb_nuts)

print(sb_nuts.columns)

sb_nuts = sb_nuts.drop(["Unnamed: 0"], axis=1) #Bir kere kullandıktan sonra bunu da comment e al.
print(sb_nuts)


print(sb_nuts.describe())

numerics = sb_nuts.drop(["item", "type"], axis=1)
print(numerics)
print(numerics.corr())



sns.boxplot(numerics)
sns.histplot(numerics)
sns.lineplot(numerics)
sns.scatterplot(numerics)
sns.pairplot(sb_nuts.drop(["item"], axis=1), hue="type")
sns.boxplot(sb_nuts.drop(["item"], axis=1), x="type", y="calories", hue=type)
plt.show()


