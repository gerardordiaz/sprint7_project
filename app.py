import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

st.header("ANALISIS DE VEHICULOS")
# PRIMERO QUIERO HACER UNA SESION QUE NO SE INTERRUMPA

if "show_hist" not in st.session_state:
    st.session_state.show_hist = False

if "show_scatter" not in st.session_state:
    st.session_state.show_scatter = False

# creacion de botones

if st.button("construir histograma"):
    st.session_state.show_hist = True

if st.button("grafico de dispersion"):
    st.session_state.show_scatter = True

# histograma

if st.session_state.show_hist:
    st.write("Creación de un histograma para el conjunto de datos")
    fig_hist = px.histogram(df, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# grafico de dispersion

if st.session_state.show_scatter:
    st.write(
        "Creación de gráfico de dispersion para el conjunto de datos de venta de coches")
    fig_scatter = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)
