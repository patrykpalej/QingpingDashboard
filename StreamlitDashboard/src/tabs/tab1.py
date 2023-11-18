import streamlit as st
import plotly.express as px
import pandas as pd


def create_plot(df, y_col, title):
    fig = px.line(df, x='timestamp', y=y_col, title=title, height=500, width=1200)
    fig.add_scatter(x=df['timestamp'], y=df[y_col], mode='markers', showlegend=False)
    fig.update_layout(title_x=0.5, title_font=dict(size=24))
    return fig


def tab1(data):
    st.markdown(
        """
        <style>
            h1 {
                margin-top: -80px;
            }
            
            
        </style>
   """, unsafe_allow_html=True)

    st.title("Balkon")

    df = pd.DataFrame(data)

    fig = create_plot(df, "temperature", "Temperatura")
    st.plotly_chart(fig)

    # ---
    for _ in range(3):
        st.markdown("<br>", unsafe_allow_html=True)
    # ---

    fig = create_plot(df, "humidity", "Wilgotność")
    st.plotly_chart(fig)

    # ---
    for _ in range(3):
        st.markdown("<br>", unsafe_allow_html=True)
    # ---

    fig = create_plot(df, "co2", "CO2")
    st.plotly_chart(fig)

    # ---
    for _ in range(3):
        st.markdown("<br>", unsafe_allow_html=True)
    # ---

    fig = create_plot(df, "pm25", "PM 2.5")
    st.plotly_chart(fig)

    # ---
    for _ in range(3):
        st.markdown("<br>", unsafe_allow_html=True)
    # ---

    fig = create_plot(df, "pm10", "PM 10")
    st.plotly_chart(fig)
