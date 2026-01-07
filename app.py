import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")
boton_histograma = st.button("construir histograma")

if boton_histograma:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crea un histograma
    fig = px.histogram(df, x="odometer")

    # muestra el grafico
    st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
