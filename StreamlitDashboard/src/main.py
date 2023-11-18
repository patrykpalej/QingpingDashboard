import streamlit as st
from pymongo import MongoClient

from tabs.tab1 import tab1


st.set_page_config(layout="wide")

client = MongoClient()
collection = client["qingping"]["balkon"]
data_balkon = collection.find()


def main():
    st.sidebar.title("Sensory")
    st.session_state.current_page = st.session_state.get(
        "current_page", "Balkon")

    # Tab 1
    if st.sidebar.button("Balkon"):
        st.session_state.current_page = "Balkon"

    # Tab 2
    # if st.sidebar.button("Tab 2"):
    #     st.session_state.current_page = "Tab 2"

    if st.session_state.current_page == "Balkon":
        tab1(data_balkon)
    # elif st.session_state.current_page == "Tab 2":
    #     tab2()


if __name__ == "__main__":
    main()
