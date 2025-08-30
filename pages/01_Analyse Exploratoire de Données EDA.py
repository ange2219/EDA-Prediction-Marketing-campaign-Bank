import streamlit as st 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px
st.logo(image = 'images/banque_logo1.png')
st.sidebar.image('images/banque_logo.jpg', caption = "YOUR BUSINESS PARTNER")
st.markdown("""
## 🔍 Analyse exploratoire (EDA)

Bienvenue dans la section EDA !  
Ici, vous pouvez explorer les données brutes pour en découvrir la structure, les tendances, les anomalies, et les insights essentiels.

---

### 🧰 Outils utilisés :
- Statistiques descriptives
- Visualisations interactives (matplotlib/seaborn)
- Analyse des distributions, corrélations et valeurs manquantes

> 🎯 L’objectif est de mieux **comprendre** les données avant d’entraîner un modèle prédictif.
---
""")
st.markdown("""### Filtrez le dataset pour plus de lisibilité👇""")

@st.cache_data
def load_data():
    df = pd.read_csv("data/new_bank_dataset.csv")
    return df

df = load_data()


#------------Preprocessing----------------------

df['class'] = df['class'].replace({'engage': 'Engagé',
                                   'non interesse': 'Non interessé',
                                   'potentiel': 'Potentiel'})
df = df.rename({'class':'Classe'})

def imput_outliers(variable, data):
    iqr_variable = data[variable].quantile(0.75) - data[variable].quantile(0.25)
    lower_limit = data[variable].quantile(0.25) - 1.5 * iqr_variable
    upper_limit = data[variable].quantile(0.75) + 1.5 * iqr_variable
    data.loc[data[variable] > upper_limit, variable] = upper_limit
    data.loc[data[variable] < lower_limit, variable] = lower_limit
    return data[(data[variable] < lower_limit) | (data[variable] > upper_limit)]

imput_outliers('duration', df)
imput_outliers('pdays', df)
imput_outliers('campaign', df)
imput_outliers('previous', df)
#-------------------------------Cases à cocher ------------------------------
st.sidebar.markdown("---")

st.sidebar.header('Affichez les graphiques')


show_hist = st.sidebar.checkbox('Histogramme', value = True)

show_cross = st.sidebar.checkbox('Carte de chaleur des classes par metier', value = True)

show_line = st.sidebar.checkbox('Evolution du solde bancaire moyen par metier', value = True)

show_bar = st.sidebar.checkbox('Composition des classes selon le mois', value = True)

def Home():
    with st.expander('Tabulaire'):
        showData = st.multiselect('Filtrez:', df.columns, default=[])
        st.write(df[showData])

Home()

# -------------------- AFFICHAGE DES GRAPHIQUES --------------------
class_color ={'Engagé':"#0026FF", 'Potentiel':"#A5CDEE", 'Non interessé':"#00B8C4"}

if show_hist:  
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    with col1:
        st.subheader("📊 Répartition des classes (Barres)")

        counts = df['class'].value_counts().reset_index()
        counts.columns = ['class', 'count']

        # Barplot avec plotly.express
        fig = px.bar(counts, x='class', y='count',
                    title="Répartition des classes dans la variable cible",
                    color='class', 
                    color_discrete_map=class_color)  

    
        fig.update_layout(template='plotly_dark')  

        # Afficher dans Streamlit
        st.plotly_chart(fig)


    with col2:  
        st.subheader("📊 Durée moyenne par classe")

        # Calcul de la moyenne
        grouped = df.groupby('class')['duration'].mean().reset_index()

        # Barplot avec Plotly
        fig = px.bar(grouped, x='class', y='duration',
                    title="Durée moyenne par classe",
                    color='class',
                    text='duration',  
                    color_discrete_map=class_color)  

        
        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        fig.update_layout(template='plotly_dark', yaxis_title="Durée moyenne", xaxis_title="Classe")

        # Affichage
        st.plotly_chart(fig)


    with col3:
        st.subheader("📊 Nombre d'appel par classe")

        # Calcul de la moyenne
        grouped = df.groupby('class')['pdays'].sum().reset_index()

        # Barplot avec Plotly
        fig = px.bar(grouped, x='class', y='pdays',
                    title="Nombre d'appel moyenne par classe",
                    color='class',
                    text='pdays',  
                    color_discrete_map=class_color)  

        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        fig.update_layout(template='plotly_dark', yaxis_title="Nombre d'appel", xaxis_title="Classe")

        # Affichage
        st.plotly_chart(fig)


    with col4:
        st.subheader("📊 Solde bancaire moyen par classe")

        # Calcul de la moyenne
        grouped = df.groupby('class')['balance'].mean().reset_index()

        # Barplot avec Plotly
        fig = px.bar(grouped, x='class', y='balance',
                    title="Salaire moyen par classe",
                    color='class',
                    text='balance', 
                    color_discrete_map=class_color)  

        
        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        fig.update_layout(template='plotly_dark', yaxis_title="Salaire moyen", xaxis_title="Classe")

        # Affichage
        st.plotly_chart(fig)

    with col5:  
        st.subheader("📊 Nombre de campagne par classe")

        # Calcul de la moyenne
        grouped = df.groupby('class')['campaign'].sum().reset_index()

        # Barplot avec Plotly
        fig = px.bar(grouped, x='class', y='campaign',
                    title="Nombre de campagne par classe",
                    color='class',
                    text='campaign',  
                    color_discrete_map=class_color)  

        
        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        fig.update_layout(template='plotly_dark', yaxis_title="Nombre de campagne", xaxis_title="Classe")

        
        st.plotly_chart(fig)

    with col6:  
        st.subheader("📊 Nombre de jours precedent par classe")

        # Calcul de la moyenne
        grouped = df.groupby('class')['previous'].sum().reset_index()

        # Barplot avec Plotly
        fig = px.bar(grouped, x='class', y='previous',
                    title="Nombre de jours precedent par classe",
                    color='class',
                    text='previous',  
                    color_discrete_map=class_color)  

       
        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        fig.update_layout(template='plotly_dark', yaxis_title="Nombre de jour", xaxis_title="Classe")

        # Affichage
        st.plotly_chart(fig)

if show_cross:
    st.subheader("🔍 Répartition de la variable cible 'class' selon les métiers (job)")

    # Création du tableau croisé
    crosstab = pd.crosstab(df['job'], df['class'], normalize='index') * 100

    
    job_order = df['job'].value_counts().index
    crosstab = crosstab.loc[job_order]

    # Affichage de la heatmap
    fig, ax = plt.subplots(figsize=(12, len(crosstab) * 0.5))  
    sns.heatmap(crosstab, annot=True, fmt=".1f", cmap="Blues", linewidths=.5, ax=ax)

    plt.title("Répartition (%) des classes pour chaque job")
    plt.xlabel("Classe cible")
    plt.ylabel("Job")
    st.pyplot(fig)
col7, col8 = st.columns(2)
if show_line:
    with col7:
        st.subheader("📊 Solde bancaire moyen par métier")

        # Calculer la moyenne du solde par métier
        job_balance = df.groupby("job")["balance"].mean().sort_values(ascending=True).reset_index()

        # Tracer la courbe
        fig = px.line(job_balance,
                    x="job",
                    y="balance",
                    title="💼 Solde bancaire moyen par métier",
                    markers=True)

    
        fig.update_layout(
            xaxis_title="Métier",
            yaxis_title="Solde bancaire moyen (€)",
            template="plotly_dark",  
            height=500,
            width=900
        )

        
        st.plotly_chart(fig, use_container_width=True)

    
if show_bar:
    with col8:
        st.subheader("📊 Répartition des classes par mois")

        # Comptage brut par mois
        ct = pd.crosstab(df['month'], df['class'])
        ct = ct.loc[df['month'].value_counts().index[::-1]]  # Tri

        # Remise en forme en long format
        ct_reset = ct.reset_index().melt(id_vars='month', var_name='class', value_name='count')


        # Tracé avec plotly
        fig = px.bar(ct_reset, x='count', y='month', color='class',
                    orientation='h',
                    title="Répartition des classes par mois (barres empilées)",
                    labels={'month': 'Mois', 'count': 'Nombre d’observations'},
                    color_discrete_map=class_color
                    )

        fig.update_layout(template='plotly_dark',
                        barmode='stack',
                        height=500,
                        width=900)
        st.plotly_chart(fig, use_container_width=True)

   

st.markdown("""## Rapport d’Analyse Exploratoire : Optimisation des Campagnes Marketing pour Dépôts à Terme

L'analyse s'est concentrée sur la répartition des clients dans trois classes cibles : **Engagé**, **Non intéressé**, et **Potentiel**. Nous avons exploré la distribution de ces classes selon diverses dimensions, telles que la profession, le mois de l'année, le salaire, le nombre d'appels reçus, etc.

### 1. Analyse des Profils des Clients

#### 1.1 Répartition des Classes par Profession

Les professions ont une influence significative sur l'engagement des clients :

* **Retraités** et **étudiants** montrent une forte proportion de clients **engagés**. Cela pourrait être dû à une plus grande disponibilité ou à une capacité à prendre des décisions financières plus rapidement.
* Les **travailleurs indépendants** (self-employed) sont également une cible intéressante, avec un fort taux d’engagement malgré un faible taux de conversion potentiel.
* Les **chômeurs** et **ouvriers** présentent une répartition plus équilibrée entre les classes, avec un léger biais vers les **non intéressés**.

#### 1.2 Répartition des Classes par Mois

* Le mois de **mai** ressort comme celui avec le plus grand nombre de clients **engagés**. Ce mois pourrait correspondre à une période favorable pour les offres bancaires, probablement liée à la gestion des finances personnelles au début de l'année ou après les vacances.
* Les mois **août** et **juillet** présentent des périodes où les clients sont moins réceptifs, avec une forte proportion de clients **non intéressés**. Ces mois peuvent correspondre à une période de distraction estivale où l’attention des clients est ailleurs.

#### 1.3 Nombre de Jours Précédents par Classe

* **Les clients engagés** ont eu un nombre de jours beaucoup plus élevé précédant l’offre, suggérant que ces clients ont un historique plus long avec la banque ou ont été sollicités de manière plus ciblée.
* **Les non intéressés** et **potentiels** montrent un nombre de jours plus faible, indiquant une réactivité plus rapide, mais moins de suivi à long terme.

#### 1.4 Nombre de Campagnes par Classe

* **Les clients engagés** ont été contactés par un plus grand nombre de campagnes. Cette donnée confirme l’idée que ces clients sont plus réceptifs aux campagnes répétées.
* Les **non intéressés** et **potentiels** ont reçu moins d'appels, ce qui peut indiquer qu'une segmentation plus fine est nécessaire pour ces groupes afin de maximiser l'engagement.

### 2. Facteurs Clés Influents

#### 2.1 Solde bancaire Moyen par Classe

* Les clients **engagés** ont un solde moyen nettement plus élevé (1,804.27 euros), ce qui pourrait être un facteur clé pour leur capacité à souscrire à des produits financiers.
* En revanche, les **non intéressés** (1,236.54 euros) et **potentiels** (1,341.78 euros) ont des soldes moyens plus bas, ce qui peut indiquer que ces clients sont moins disposés ou capables de souscrire à des produits comme un dépôt à terme.

#### 2.2 Nombre d’Appels Moyens par Classe

* **Les clients engagés** reçoivent une quantité significative d'appels (en moyenne 96,813), ce qui suggère qu'ils sont plus réceptifs aux efforts marketing.
* **Les non intéressés** (28,518) et **potentiels** (15,068) sont moins sollicités, mais peut-être qu’une augmentation de ces appels pourrait les transformer en clients engagés.

#### 2.3 Durée Moyenne des Appels

* Les **engagés** ont des appels plus longs (500.65 secondes en moyenne' soit 8 mnutes), ce qui suggère qu’ils sont plus ouverts à la discussion et à la réception d'informations détaillées.
* **Les non intéressés** et **potentiels** ont des appels plus courts, ce qui peut indiquer un faible niveau d'intérêt.

#### 2.4 Répartition des Classes dans la Variable Cible

* La majorité des **clients engagés** (plus de 5000) fait partie de la variable cible, ce qui confirme que ce groupe est celui qui réagit le mieux aux offres de dépôt à terme.
* Les **non intéressés** et **potentiels** ont des représentations plus faibles, mais ils restent des segments importants à surveiller pour d'éventuelles stratégies de conversion.

### 3. Recommandations

#### 3.1 Ciblage des Profils Engagés

Les clients dans des professions comme **étudiants**, **retraités**, et **travailleurs indépendants** doivent être priorisés dans les campagnes de marketing. Ces segments montrent une forte propension à accepter des offres de dépôt à terme.

#### 3.2 Optimisation des Efforts Marketing

Augmenter le nombre d’appels et la durée des interactions avec les **non intéressés** et **potentiels**. Leurs soldes moyens plus bas suggèrent qu’ils pourraient bénéficier de campagnes plus personnalisées et de messages adaptés à leurs besoins spécifiques.

#### 3.3 Planification des Campagnes

Concentrer les efforts pendant des mois comme **mai**, où les clients sont plus réceptifs, et éviter des périodes comme **août** et **juillet**, qui montrent une plus grande proportion de clients non intéressés.

#### 3.4 Amélioration de l’Approche Par Canal

Les campagnes téléphoniques doivent être renforcées pour les **engagés**, car ces clients semblent plus réceptifs aux appels et aux informations détaillées. Il pourrait être pertinent d’explorer d’autres canaux (emails, notifications mobiles) pour les **potentiels**.

---

Cette analyse fournit des insights précieux pour améliorer le ciblage des campagnes marketing et maximiser l'efficacité des efforts bancaires. En utilisant ces résultats, la banque pourra affiner ses stratégies et proposer des offres plus personnalisées, augmentant ainsi le taux de conversion des clients et réduisant les coûts liés aux campagnes inefficaces.

---

""")


