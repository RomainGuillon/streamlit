import streamlit as st
import plotly.express as px

#Configfuration de la page streamlit
st.set_page_config(page_title="DataViz — Démo", page_icon="📊", layout="wide")
st.title("📊 Démo Streamlit + Plotly")
st.write("Bienvenue ! Ceci est votre toute première page d'application.")

#chargement des données iris de plotly
df = px.data.iris()

fig = px.scatter(
    df, x="sepal_width", y="sepal_length", color="species",
    title="Iris — largeur vs longueur des sépales"
)

st.plotly_chart(fig, use_container_width=True)