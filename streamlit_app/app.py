import streamlit as st
import plotly.express as px
import pandas as pd
from utils.data import load_data, filter_data

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

# Affiche un spinner pendant le chargement des données
with st.spinner("Chargement des données…"):
    data = load_data()  # Chargement des données avec cache

# Affiche un aperçu interactif des premières lignes du DataFrame
st.write("Aperçu des données :")
st.dataframe(data.head(), use_container_width=True)

# Crée un graphique de l'évolution des ventes par catégorie
fig_line = px.line(data, x="date", y="ventes", color="categorie",
                   title="Ventes journalières")
# Affiche le graphique dans l'application Streamlit
st.plotly_chart(fig_line, use_container_width=True)