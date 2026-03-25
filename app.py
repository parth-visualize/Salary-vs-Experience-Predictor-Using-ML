import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load model 
with open("model.pkl","rb") as f:
    model=pickle.load(f)

st.title("Salary vs Experience Predictor")
st.write("Simple Linear Regression Model")

# input for prediction
exp=st.number_input("Years of Experience",min_value=0.0,max_value=50.0,value=1.0)
prediction=model.predict([[exp]])[0]

st.write(f"Predicted Salary:${prediction:.2f}")

# show dataset and regression line
if st.checkbox("Show Dataset and Regression Line"):
    df=pd.read_csv("salary_data.csv")

    fig,ax=plt.subplots()
    ax.scatter(df["Years Experience"],df["Salary"],alpha=0.7,label="Actual Data")

    # plot Regression line
    line_x=pd.DataFrame({"Years Experience":[df["Years Experience"].min(),df["Years Experience"].max()]})
    line_y=model.predict(line_x)
    ax.plot(line_x, line_y,color="red", label="Regression line")

    ax.set_xlabel("Years of Experience")
    ax.set_ylabel("Salary")
    ax.legend()
    st.pyplot(fig)