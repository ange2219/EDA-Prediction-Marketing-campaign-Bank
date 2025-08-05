import streamlit as st 
import numpy as np
import pandas as pd
import joblib
import time
from datetime import datetime
st.logo(image = 'images/banque_logo1.png')
st.sidebar.image('images/banque_logo.jpg', caption = "YOUR BUSINESS PARTNER")
st.markdown("""
## 🤖 Prédiction automatique

Dans cette section, vous pouvez tester le **modèle prédictif** entraîné sur notre dataset.

---

### ✨ Fonctionnalités :
- Saisissez les caractéristiques d’un individu ou d’un événement
- Obtenez une prédiction instantanée
- Interprétation des résultats fournie

> 📢 Le modèle a été sélectionné pour sa **précision** et sa **robustesse**.
---
### 📝 Renseigez les information svp
""")


@st.cache_resource
def load_model():
    model = joblib.load("model/bank.plk")  
    return model

model = load_model()



# Entrer utilisateur 
col1, col2, col3 = st.columns(3)

col4, col5, col6 = st.columns(3)

col7, col8, col9 = st.columns(3)

col10, col11, col12 = st.columns(3)

with col1:
    age = st.number_input(
        label=('Quelle age a votre client'), min_value=41
        )

with col2:
    job = st.selectbox(
        label="Quelle est la profession de votre client", 
        options=['Employé administratif', 'Technicien', 
                 'Personnel de service', 'Cadre/manager', 
                 'Retraité', 'Ouvrier', 'Chomeur', 
                 'Entrepreneur', 'Femme de ménage', 'Inconnu', 
                 'Travailleur indépendant', 'Etudiant']
                 )
    
    job_mapping = {'Employé administratif': 0,'Technicien': 1, 'Personnel de service': 2, 
                   'Cadre/manager': 3, 'Retraité': 4, 'Ouvrier': 5, 
                   'Chomeur': 6, 'Entrepreneur': 7, 'Femme de ménage': 8, 
                   'Inconnu': 9, 'Etudiant': 10, 'Travailleur indépendant': 11}
    job_num = job_mapping[job]

with col3:
    balance = st.number_input(label=('Quelle est le solde banquaire de votre client?'), min_value=-6847, value=1528)

with col4:
    housing = st.selectbox(label="Le client a t'il un pret immobilier?", options=['Oui', 'Non'])

    housing_mapping = {'Oui':1, 'Non':0}

    housing_num = housing_mapping[housing]

with col5:
    loan = st.selectbox(label="Le client a t'il un pret personnel?", options=['Oui', 'Non'])

    loan_mapping = {'Oui':1, 'Non':0}

    loan_num = loan_mapping[loan]

with col6:
    marital = st.selectbox(label="Quelle est la situation matrimoniale de votre client?", options=['Marié', 'Celibataire', 'Divorcé'])

    marital_mapping = {'Marié':0, 'Celibataire':1, 'Divorcé':2}

    marital_num = marital_mapping[marital]

with col7:
    education = st.selectbox(label="Quelle est le niveau d'etude de votre client? ", options=['Primaire', 'College', 'Université', 'Inconnu'])

    education_mapping = {'Primaire':2, 'College':0, 'Université':1, 'Inconnu':3}

    education_num = education_mapping[education]
with col8:
    contact = st.selectbox(label="Quelle est le canal de communication? ", options=['Téléphone portable', 'Telephone fixe', 'Inconnu'])

    contact_mapping = {'Téléphone portable':1, 'Telephone fixe':2, 'Inconnu':0}

    contact_num = contact_mapping[contact]

with col9:
    duration = st.number_input(label=("Durée de contact(En sec)"), min_value=2, value=371)

with col10:
    campaign = st.number_input(label=("Nombre de contact précédent"), min_value=0, value=2)

with col11:
    pdays = st.number_input(label=('Nombre de jours depuis le dernier contact'), min_value=-1, max_value=8, value=-1)

with col12:
    previous = st.number_input(label=('Nombre de contacts precedents'), min_value=0)

#-----------------Fonction inference--------------
def inference(duration, campaign, balance, age, job_num, 
              pdays, contact_num, housing_num, previous, 
              education_num, marital_num, loan_num):
    new_data = pd.DataFrame([[duration, campaign, balance, 
                         age, job_num, pdays, contact_num, 
                         housing_num, previous, education_num, 
                         marital_num, loan_num]],
                         columns= ["duration", "campaign", "balance", 
                         "age", "job", "pdays", "contact", 
                         "housing", "previous", "education", 
                         "marital", "loan"])
    pred = model.predict(new_data)[0]
    pred_proba = model.predict_proba(new_data)[0]
    return pred, pred_proba[0]

#Boutton 

if st.button('Lancez la prédiction'):
    prediction, prob = inference(duration, campaign, balance, age, job_num,
                            pdays, contact_num, housing_num, previous, 
                            education_num, marital_num, loan_num)
    
    if prediction == 0:
        st.subheader("🔋 Taux d'engagement du client")
        progress_bar = st.progress(0)
        for i in range(int(prob*100) + 1):
            time.sleep(0.01)
            progress_bar.progress(i)
        st.success("✅ Notre modèle prédit que le client sera **engagé** avec une probabilité de : " + f"{round(prob*100, 2)}%")

    elif prediction == 1:
        st.subheader("🔋 Taux d'engagement du client")
        progress_bar = st.progress(0)
        for j in range(int(prob*100) + 1):
            time.sleep(0.01)
            progress_bar.progress(j)
        st.error("❌ Notre modèle prédit que le client **ne sera pas intéressé** avec une probabilité de : " + f"{round(prob*100, 2)}%")

    else:
        st.subheader("🔋 Taux d'engagement du client")
        progress_bar = st.progress(0)
        for k in range(int(prob*100) + 1):
            time.sleep(0.01)
            progress_bar.progress(k)
        st.warning("🤔 Le client est **potentiellement intéressé**, avec une probabilité de : " + f"{round(prob*100, 2)}%")
        



    # Informations à sauvegarder
    prediction_info = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Classe prédite": int(prediction),                      
        "Probabilité (%)": round(float(prob) * 100, 2)
        }

    # Créer la liste 
    if "historique" not in st.session_state:
        st.session_state.historique = []

    # Ajouter cette prédiction à la mémoire
    st.session_state.historique.append(prediction_info)


