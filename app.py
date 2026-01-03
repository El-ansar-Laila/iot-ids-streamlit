import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="IoT IDS – Attack Detection",
    layout="centered"
)

st.title("🚨 IoT Intrusion Detection System")
st.write("Cette application utilise un modèle de Machine Learning pour détecter les attaques IoT.")

# Charger le modèle
model = joblib.load("iot_ids_pipeline.pkl")

# Upload du fichier CSV
uploaded_file = st.file_uploader(
    "📂 Charger un fichier CSV de nouvelles données",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Aperçu des données")
    st.dataframe(df.head())

    try:
        predictions = model.predict(df)

        df["Prediction"] = predictions

        st.subheader("Résultats de la prédiction")
        st.dataframe(df.head(20))

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "📥 Télécharger les résultats",
            csv,
            "predictions.csv",
            "text/csv"
        )

    except Exception as e:
        st.error(f"Erreur lors de la prédiction : {e}")
