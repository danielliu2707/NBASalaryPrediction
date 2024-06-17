import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image

# Creating title and sidebar
st.set_page_config(
    page_title = "NBA Player Salary Prediction",
    page_icon = "🏀"
)

# Loading in ML Model
@st.cache_data
def load_data(model):
    return pickle.load(open(model, 'rb'))   # loading data from binary file

model = load_data('model.sav')

st.markdown("# NBA Player Salary Prediction")
st.sidebar.header('Player Data')

# Defining widget options and storing user input in DataFrame
def user_report():
    rating = st.sidebar.slider('Rating', 50, 100, 1)
    jersey = st.sidebar.slider('Jersey', 0, 100, 1)
    team = st.sidebar.slider('Team', 0, 30, 1)
    position = st.sidebar.slider('Position', 0, 10, 1)
    country = st.sidebar.slider('Country', 0, 3, 1)
    draft_year = st.sidebar.slider('Draft Year', 2000, 2020, 2000)
    draft_round = st.sidebar.slider('Draft Round', 1, 10, 1)
    draft_peak = st.sidebar.slider('Draft Peak', 1, 30, 1)
    
    user_report_data = {
        'rating':rating,
        'jersey':jersey,
        'team':team,
        'position':position,
        'country':country,
        'draft_year':draft_year,
        'draft_round':draft_round,
        'draft_peak':draft_peak
    }
    
    report_data = pd.DataFrame(user_report_data, index = [0])
    return report_data

# Display user data
user_data = user_report()
st.markdown('### Player Data:')
st.write(user_data)

# Make prediction using model and user data
salary = model.predict(user_data)
st.markdown('### Player Salary:')
st.subheader('$' + str(np.round(salary[0], 2)))

st.button("Reload Page Here")