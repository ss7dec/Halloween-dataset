# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:05:37 2023

@author: lenovo
"""

import streamlit as st
import pickle



st.title("Apps for Prediction using Random Regressor Algorithm")
st.write("Kindly enter the required value")

with open('model.pkl', 'rb') as file:
     model = pickle.load(file)


# # stall_no=10
# # mc=2
# # Lc=1
# pc=2
# g=1
# dem=51
# da=0
# c1=240
# c2=11
# mp=5000
# mxp=7000



stall = st.slider("Select the Stall number", 1, 50)
mc = st.number_input("Enter a market category", min_value = 0, max_value = 471)
Lc = st.radio("Kindly verify whether the customer is loyal or not", ("Yes", "No"))


if Lc == "Yes":
    Lc = 1
else:
    Lc = 0
    
    
# Pet_care       679
# Repair         666
# Child_care     655
# Cosmetics      644
# Hospitality    628
# Organic        618
# Technology     617
# Home_decor     611
# Educational    605
# Fashion
# city = st.selectbox("Select your city", ["New York", "London", "Tokyo"])

cat = ["Pet_care", "Repair", 'Child_care', 'Cosmetics' , 'Hospitality', 'Organic', 'Technology', 'Home_decor', 'Educational', 'Fashion']
category = st.selectbox(" Choose the appropriate category", cat)
st.write("Kindly select the box")
# a = st.checkbox("Pet_care")
# b = st.checkbox("Repair")
# c = st.checkbox("Child_care")


with open('model_pc.pkl', 'rb') as file:
     model_pc = pickle.load(file)
     

pc = model_pc.transform([category])

g = st.number_input('Enter Grade', value =  0, min_value = 0, max_value = 3, format = "%d" )
dem = st.number_input("Kindly enter the demand value", value = 50, min_value = 1,max_value = 100, format = "%d" )
da = st.number_input("Kindly enter the discount available", value = 0, min_value = 0, max_value = 90)
c1 = st.number_input("Kindly enter the charge value", value = 1, min_value = 1, step = 1 )
c2 = st.number_input("Kindly enter the charge2 value", value = 1, min_value = 1 )
mp = st.number_input("Kindly enter the Min value", value = 2500, step = 1 )
mxp = st.number_input("Kindly enter the Max value", value = 5000, step = 1 )
if mp>mxp:
    # Pop-up content
    with st.expander("Error"):
        st.write("Maixmum Price is less than Minimum Price.")
        # st.button("Close")
        st.button("Close")

     



a=[[stall,mc,Lc,pc,g,dem,da,c1,c2,mp,mxp]]




button = st.button('Predict')
if button:
    predict = model.predict(a)
    st.write('The prediction of Selling Price is', predict)



