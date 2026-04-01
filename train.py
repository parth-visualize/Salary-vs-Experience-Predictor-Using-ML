import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle


# load Dataset
df=pd.read_csv("salary_data.csv")

# prepare data
x=df[["Years Experience"]]
y=df["Salary"]

# train model
model=LinearRegression()
model.fit(x,y)

# save model
with open("model.pkl","wb") as f:
    pickle.dump(model,f)

print("Model training complete. Model Saved as model.pkl")
print(f"Coefficient:{model.coef_[0]:.2f}, Intercept:{model.intercept_:.2f}")
