import numpy as np
import pandas as pd
from sklearn.metrics import r2_score,mean_absolute_error
import pickle


# Load Model and Data
with open("model.pkl","rb") as f:
    model=pickle.load(f)

df=pd.read_csv("salary_data.csv")
x=df[["Years Experience"]]
y=df["Salary"]

# make Predictions
predictions=model.predict(x)

# calculate metrics
r2=r2_score(y,predictions)
mae=mean_absolute_error(y,predictions)

print(f"R Score:{r2:.3f}")
print(f"MAE:${mae:.2f}")
