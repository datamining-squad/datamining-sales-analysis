import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import os
import seaborn as sns

data = pd.read_csv("D:/PLU/Fall19/data_mining/project/sales_data.csv")

print(data.shape)

data.head()

data.describe()

fig1, ax1 = plt.subplots()

ax1.set_title('House Value Distribution')
ax1.boxplot(data["house_val"])
plt.show()

fig2, ax2 = plt.subplots()
ax2.set_title('Probability Buy New Car')
ax2.boxplot(data["car_prob"])
plt.show()

sns.boxplot(data=data, palette='coolwarm',orient='v')
