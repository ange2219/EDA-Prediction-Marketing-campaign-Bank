import streamlit as st
import pandas as pd
st.logo(image = 'images/banque_logo1.png')
st.sidebar.image('images/banque_logo.jpg', caption = "YOUR BUSINESS PARTNER")
st.markdown("""
## 🗂️ Historique des prédictions

Toutes les prédictions que vous avez effectuées sont conservées ici.  
Vous pouvez consulter les anciennes entrées et leurs résultats associés.

---

### 📒 Détails :
- Données saisies
- Résultat de la prédiction
- Date & heure
- Possibilité de filtrer ou télécharger les résultats

> 📌 Gardez une trace de vos prédictions pour mieux évaluer vos stratégies ou prises de décisions.
""")



# Vérifie si on a des prédictions enregistrées
if "historique" in st.session_state and st.session_state.historique:
    df_historique = pd.DataFrame(st.session_state.historique)
    
    # Afficher le tableau
    st.dataframe(df_historique)

    # Bouton de téléchargement
    csv = df_historique.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Télécharger en CSV", data=csv, file_name="historique_predictions.csv", mime="text/csv")

    # Bouton pour réinitialiser l'historique
    if st.button("🧹 Effacer l'historique"):
        st.session_state.historique = []
        st.success("Historique effacé avec succès.")

else:
    st.info("Aucune prédiction enregistrée pour le moment.")


