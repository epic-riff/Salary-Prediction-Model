from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle

df = pd.read_csv('C:\\Users\\Laksh-Games\\OneDrive\\Desktop\\Coding Files\\Py Stuff\\Supervised ML\\linear regression\\Salary_Data.csv')
df.dropna()

y = df['Salary']
X = df['YearsExperience']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

lr = LinearRegression()
lr.fit(X_train.values.reshape(-1,1), y_train)

with open('expredmodel.pickle', 'wb') as f:
    pickle.dump(lr, f)