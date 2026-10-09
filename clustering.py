import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv("data/customer.csv")

X = data[["AnnualIncome", "SpendingScore"]]

model = KMeans(n_clusters=4, random_state=42, n_init=10)

data["Cluster"] = model.fit_predict(X)

print(data)

import matplotlib.pyplot as plt

plt.scatter(
    data["AnnualIncome"],
    data["SpendingScore"],
    c=data["Cluster"],
    s=100
)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")

plt.show()

print("\nCluster Summary:")
print(data.groupby("Cluster")[["AnnualIncome", "SpendingScore"]].mean())


