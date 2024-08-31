import streamlit as st
from pages import home

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", ["Home", "About", "Contact"])

    if page == "Home":
        home.show()
    elif page == "About":
        about.show()
    elif page == "Contact":
        contact.show()

if __name__ == "__main__":
    main()
