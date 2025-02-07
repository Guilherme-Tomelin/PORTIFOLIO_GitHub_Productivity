import streamlit as st


with open("styles.css") as style:
    st.markdown(f"<style>{style.read()}</style>", unsafe_allow_html=True)

st.title("My GitHub Productivity")

url = st.text_input("Digite a URL:", placeholder="https://github.com/Joao-Barros")

if st.button("OK"):
    user_input = url
    print(user_input)
