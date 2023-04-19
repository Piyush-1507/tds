#%%
import streamlit as st

st.header("TDS Week 8: Largest Among 3")
st.write("#### Enter 3 numbers")
a = st.number_input("Enter 1st number")
b = st.number_input("Enter 2nd number")
c = st.number_input("Enter 3rd number")

calc = st.button("Find Largest")
if calc:
    lg = max(a, b, c)
    st.header(f"Largest number is: {lg}")
# %%
# %%
