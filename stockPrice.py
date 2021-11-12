import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('data.csv')
print(df.head())

x = df['Date']
y = df['Price']

plt.xlabel('Date', fontsize=18)
plt.ylabel('Price', fontsize=16)
plt.bar(x, y)

plt.show()

