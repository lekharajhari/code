import streamlit as st
from pages import page1, page2

# Dictionary to map page names to functions
PAGES = {
    "Page 1": page1,
    "Page 2": page2
}

# Streamlit app layout
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Call the selected page's function
page = PAGES[selection]
page.run()