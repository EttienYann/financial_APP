#1IMPORTATION DES BIBLIOTHEQUES

import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle as pkl
#crer une nav bar
from streamlit_option_menu import option_menu
#ajouter une image
from PIL import Image
import base64



#DESCRIPTION

st.title('FINANCIAL APP')

st.text("DEVELOPPER PAR ETTIEN KOUASSI YANN") 

# Créer une barre de navigation
with st.sidebar:
    selected = option_menu(
        menu_title=" Menu",
        options=["Home", "Prediction", "About"],
        icons=["house", "graph-up-arrow", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

# Fonction pour convertir une image en base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
img_path = "C:/Users/user/Downloads/streamlit/streamlit/Account.jpeg"
try:
    img_base64 = get_base64_image(img_path)
except FileNotFoundError:
    st.error(f"File not found: {img_path}")
    st.stop()

# Utilisation de l'image de fond via CSS
st.markdown(
    f"""
    <style>
    .main {{
        background-image: url('data:image/jpeg;base64,{img_path}');
        background-size: cover;
    }}
    .stButton>button {{
        background-color: #4CAF50;
        color: white;
    }}
    .stRadio>div>div>label>div>div {{
        color: black;
    }}
    .stNumberInput>div>div>label>div>div {{
        color: black;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

if selected == "Home":
    st.header("Home")
    st.write("Bienvenue sur la page d'accueil de l'application financière.")
    img = Image.open("Acount1.jpeg")
elif selected == "Prediction":
    st.header("Prediction")
    #CHARGEMENT DU MODEL
    file = open("model_rf_end1.pkl","rb")
    model = pkl.load(file)
    file.close()
    ##4 DEFINITION DE LA FONCTION D'INTERFERENCE(PERMET DE FAIRE LA PREDICTION)

    def inference(household_size,age_of_respondent,location_type,cellphone_access,gender_of_respondent,education_level_Primary,education_level_Tertiary,education_level_Vocational,employed_Government,employed_Private):
        data = np.array([household_size,age_of_respondent,location_type,cellphone_access,gender_of_respondent,education_level_Primary,education_level_Tertiary,education_level_Vocational,employed_Government,employed_Private])
        #df = pd.DataFrame(data,columns=['household_size', 'age_of_respondent', 'location_type', 'cellphone_access', 'gender_of_respondent', 'education_level_Primary', 'education_level_Tertiary', 'education_level_Vocational', 'employed_Government', 'employed_Private'])
        banck_account_pred = model.predict(data.reshape(1,-1))
        return banck_account_pred



    #5 SAISIE DES INFORMATIONS

    household_size = st.number_input(label="Taille de l'entreprise")
    age_of_respondent =st.number_input("age")
    location_type = st.radio("Type de location?: ", ('rural', 'urban'))
    if location_type == 'rural':
        location_type =0
    else :
        location_type = 1

    cellphone_access = st.radio("Telephone?: ", ('oui', 'non'))
    if cellphone_access == 'oui':
        cellphone_access =1
    else :
        cellphone_access = 0

    gender_of_respondent = st.radio("Genre: ", ('Male', 'Female'))
    if gender_of_respondent == 'Female':
        gender_of_respondent=0
    else:
        gender_of_respondent=1
    education_level_Primary = st.radio("NIveau d'etude primaire : ", ('oui', 'non'))
    if education_level_Primary == 'oui':
        education_level_Primary= 1
    else : 
        education_level_Primary =0
    education_level_Tertiary = st.radio("NIveau d'etude Tertaire : ", ('oui', 'non'))
    if education_level_Tertiary == 'oui':
        education_level_Tertiary=1
    else :
        education_level_Tertiary =0

    education_level_Vocational = st.radio("Vocation : ", ('oui', 'non'))
    if education_level_Vocational == 'oui' :
        education_level_Vocational=1
    else :
        education_level_Vocational =0

    employed_Government = st.radio("Fonctionnaire?: ", ('oui', 'non'))
    if employed_Government == 'oui' :
        employed_Government = 1
    else :
        employed_Government = 0

    employed_Private = st.radio("Salarie? : ", ('oui', 'non'))
    if employed_Private == 'oui':
        employed_Private=1
    else :
        employed_Private=2
    # st.number_input("Fonctionnaire?")
    #6CREATION DU BOUTON DE PREDICTION

    if st.button('Prédire') :
        result_pred = inference(household_size,age_of_respondent,location_type,cellphone_access,gender_of_respondent,education_level_Primary,education_level_Tertiary,education_level_Vocational,employed_Government,employed_Private)
        
        if result_pred[0]== 0 :
            st.warning("La personne n'est pas succeptible d'avoir un compte")
        elif result_pred[0] ==1:
            st.success("La personne est succeptible de créer un compte")

elif selected == "About":
    st.header("About")
    st.write("Cette application a été développée par ETTIEN KOUASSI YANN.")