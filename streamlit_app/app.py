import streamlit as st
import plotly.express as px
import pandas as pd
import datetime as dt
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

# --- Section: Graphiques réutilisables ---
from utils.charts import make_line, make_bar

# Affiche une selectbox pour choisir le type de graphique
choix = st.selectbox("Type de graphique", ["Courbe", "Barres"])

# Selon le choix, génère la figure correspondante avec le style cohérent
if choix == "Courbe":
    fig = make_line(data, x="date", y="ventes", color="categorie",
                    title="Ventes — courbe")
else:
    fig = make_bar(data, x="date", y="ventes", color="categorie",
                   title="Ventes — barres")

# Affiche le graphique dans Streamlit
st.plotly_chart(fig, use_container_width=True)

# --- Section: Filtres (sidebar) ---
with st.sidebar:
    st.header("🎛️ Filtres")  # Titre du panneau latéral
    cats = sorted(list(data["categorie"].cat.categories))  # Liste triée des catégories
    f_cats = st.multiselect("Catégories", options=cats, default=cats)  # Sélection multiple des catégories
    dmin = st.date_input("Date min", value=data["date"].min().date())  # Sélection de la date minimale
    dmax = st.date_input("Date max", value=data["date"].max().date())  # Sélection de la date maximale

# État partagé — on met à jour session_state à chaque exécution
st.session_state["f_cats"] = f_cats  # Sauvegarde des catégories sélectionnées
st.session_state["dmin"] = dmin      # Sauvegarde de la date min sélectionnée
st.session_state["dmax"] = dmax      # Sauvegarde de la date max sélectionnée


# --- Section: Application des filtres ---

# 1. Construire le dictionnaire de filtres depuis les variables des widgets
filtres = dict(
    categorie=f_cats,
    date_min=dmin,
    date_max=dmax
)

# 2. Appliquer les filtres au DataFrame
df_filtered = filter_data(data, **filtres)

# 3. Afficher un message contextuel avec le nombre de lignes restantes
st.toast(f"{len(df_filtered):,} lignes après filtre".replace(",", " "), icon="✅")

# 4. Générer et afficher le graphique filtré
fig_filt = make_line(
    df_filtered, x="date", y="ventes", color="categorie",
    title="Ventes filtrées"
)
st.plotly_chart(fig_filt, use_container_width=True)