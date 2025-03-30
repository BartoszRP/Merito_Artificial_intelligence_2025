import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


weight_df = pd.read_csv("weight-height.csv")
print(weight_df.head())
print(type(weight_df))

weight_df.Height *= 2.54
weight_df.Weight /= 2.2
print(weight_df.head())

#plt.hist(weight_df.Weight, bins=100)
plt.hist(weight_df.query("Gender=='Male'").Weight, bins=100)
#plt.show()

plt.hist(weight_df.query("Gender=='Female'").Weight, bins=100)
plt.show()


sns.histplot(weight_df.query("Gender=='Male'").Weight, bins=100)
#plt.show()

sns.histplot(weight_df.query("Gender=='Female'").Weight, bins=100)
plt.show()

weight_df=pd.get_dummies(weight_df)
print(weight_df.head())

del (weight_df['Gender_Male'])
weight_df.rename(columns={'Gender_Female': 'Gender'}, inplace=True)
print(weight_df.head())

# Linear Regression #################################################
model = LinearRegression()
model.fit(weight_df[["Height", "Gender"]], weight_df["Weight"])

print(model.coef_, model.intercept_)
print(f'Waga = {model.coef_[0]} * wzrost + {model.coef_[1]} * plec + {model.intercept_}')
print(model.predict([[192, 0], [192, 1], [80, 1]]))