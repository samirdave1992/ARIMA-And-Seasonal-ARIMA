import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

st.header("SARIMA Model")

df=pd.read_csv('/Users/Samir/Desktop/GITHUB/ML/ARIMA-And-Seasonal-ARIMA/Sales.csv')

st.write("""
st.dataframe(df.head())
st.dataframe(df.tail())
To see how the DF looks
""")

df.columns=["Months","Sales"]
df.drop(105,axis=0, inplace=True)
df.drop(106,axis=0, inplace=True)
st.dataframe(df.tail())

#convert to month

# Convert Month into Datetime
df.set_index("Months",inplace=True)

st.dataframe(df.head())

fig=plt.figure(figsize=(20,8))
EDA_plt=df.plot()

st.pyplot(EDA_plt)
