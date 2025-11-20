import streamlit as st

pages = [
    st.page(page="pages/page1.py", title="Home", icons"🏠"),
    st.page(page="pages/page2.py", title="visualisasi Data", icons📊"),
    st.page(page="pages/page3.py", title="Settings", icons"⚙️")
]

pg = st.navigation(
    pages,
    position="sidebar",
    expanded=True
)

pg.run()