import streamlit as st
import pandas as pd
import numpy as np

## ttile of the app
st.title("hello streamlit")

#display a simple text
st.write("this is a simple text")

# create a simple df
df=pd.DataFrame({
    'first col':[1,2,3,4],
    'second col':[10,20,30,40]
})

## display the df
st.write("here is the dataframe")
st.write(df)

# create a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)