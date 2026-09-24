import streamlit as st
st.title("welcome to my firstapp")
st.write("hello")
name=st.text_input("enter your name")
if st.button("submit"):
    st.write("hello", name)