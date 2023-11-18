import streamlit as st


def tab2():
    st.markdown(
        """
        <style>
            h1 {
                margin-top: -80px;
            }
        </style>
   """, unsafe_allow_html=True)

    st.title("Tab 2")

    select_box, start_date, multi_input, slider_input = (
        st.session_state.get("select_box_id", None),
        st.session_state.get("start_date", None),
        st.session_state.get("multi_input", None),
        st.session_state.get("slider_input", None),
    )

    st.write(f"Select box: {select_box}\nStart date: {start_date}"
             f"\nMulti input: {multi_input}\nSlider input: {slider_input}")
