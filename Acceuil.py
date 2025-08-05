import streamlit as st
st.logo(image = 'images/Banque_logo1.jpg')
st.sidebar.image('images/Banque_logo.jpg', caption = "YOUR BUSINESS PARTNER")
def main():
    st.markdown("""
    ## 👋 Bienvenue dans l'application d'analyse et de prédiction !

    Cette application a été conçue pour **explorer**, **analyser** et **prédire** à partir de notre dataset, en combinant **Data Science** et **Machine Learning**.

    ---

    ### 📌 À propos du projet :

    - **Auteur** : Ange DAHOU, étudiant en Physique-Chimie et aspirant Data Scientist 🧠
    - **Objectif** : Détecter des tendances et faire des prédictions à partir d’un dataset réel 📊
    - **Technos utilisées** : Python, Pandas, Scikit-learn, Matplotlib, Streamlit 🚀

    ---

    ### 📂 À propos du dataset :

    - **Nom du dataset** : `bank.csv`
    - **Source** : https://archive.ics.uci.edu/static/public/222/bank+marketing.zip
    - **Nombre d'observations** : `11162`
    - **Nombre de variables** : `17`

    > 🔎 Ce projet vous propose une navigation simple :  
    > - Analyse exploratoire (EDA)  
    > - Prédiction par modèle  
    > - Historique des prédictions  

    ### 📌 Contexte et problématique

    Dans un environnement de plus en plus concurrentiel, les institutions financières cherchent à optimiser leurs campagnes marketing en identifiant les clients les plus susceptibles d’adhérer à leurs offres. C’est dans cette optique qu’une banque portugaise a mené plusieurs **campagnes de marketing direct**, principalement via des appels téléphoniques, afin de proposer à ses clients de **souscrire à un dépôt à terme bancaire**.

    Les données collectées au cours de ces campagnes incluent :

    * des informations **sociodémographiques** (âge, profession, situation familiale, etc.),
    * des variables liées à l’**historique bancaire** du client (solde, crédits, défaut de paiement, etc.),
    * des **données comportementales** (canal de contact, durée des appels, nombre de contacts antérieurs, etc.).

    L’objectif de ce projet est de réaliser une **analyse exploratoire de ces données** pour comprendre les facteurs influençant la décision d’un client à **accepter ou refuser l’offre**. À terme, cette compréhension permettra de **développer un outil de prédiction** basé sur des modèles de Machine Learning, afin d’**optimiser les campagnes futures**.

    ### ❓ Problématique

    > **Quels sont les profils de clients les plus susceptibles de souscrire à un dépôt à terme, et quels sont les facteurs déterminants dans leur décision ?**

    Répondre à cette question permettra à la banque :

    * de **mieux cibler ses efforts marketing**,
    * de **réduire les coûts liés aux campagnes inefficaces**,
    * et d’**améliorer la satisfaction client** grâce à des approches plus personnalisées.
    ### Bon passage
    """)

if __name__ == '__main__':
    main()