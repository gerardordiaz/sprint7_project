import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

st.header("ABALISIS DE VEHICULOS")
boton_histograma = st.button("construir histograma")

if boton_histograma:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crea un histograma
    fig = px.histogram(df, x="odometer")

    # muestra el grafico
    st.plotly_chart(fig, use_container_width=True)

boton_dispersion = st.button("gráfico de dispersión")

if boton_dispersion:
    st.write(
        "crea un grafico de dispersion para el conjunto de datos de anuncios de venta de coches"
    )
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig)
