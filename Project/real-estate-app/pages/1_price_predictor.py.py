import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Viz Demo")
# property_type	sector	bedRoom	bathroom	balcony	agePossession	built_up_area
# servant room	store room	furnishing_type	luxury_category	floor_category

# We will load df.pkl 
with open('df.pkl','rb') as file:
    df= pickle.load(file)

# we will import the pipeline
with open('pipeline.pkl','rb') as file:
    pipeline= pickle.load(file)

#st.dataframe(df)

st.header('Enter your Inputs')

# We will creat a form where we will take the inputs from the user

#1.Property Type
property_type= st.selectbox('Property Type',['flat','house'])

# 2.Sector
sector=st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

# 3.Bedroom
bedroom=float(st.selectbox('Number of Bedroom',sorted(df['bedRoom'].unique().tolist())))

# 4.Bathroom
bathroom= float(st.selectbox('Number of Bathrooms',sorted(df['bathroom'].unique().tolist())))

# 5.Balcony
balcony=(st.selectbox("Balconies",sorted(df['balcony'].unique().tolist())))

# 6. age_possesion

property_age= st.selectbox("Propert Age",sorted(df['agePossession'].unique().tolist()))

#7.built_up_area

built_up_area=float(st.number_input("Builtuparea"))

#8. Servant_room

servant_room=float(st.selectbox("Servant Room",[1,0]))

#8. Store_room

store_room=float(st.selectbox("Store Room",[1,0]))

# 9. furnishing_type

furnishing_type= st.selectbox("Furnishing Type",sorted(df['furnishing_type'].unique().tolist()))

# 10. furnishing_type

luxury_category= st.selectbox("Luxury Category",sorted(df['luxury_category'].unique().tolist()))

# 11.floor_category

floor_category= st.selectbox("Floor Category",sorted(df['floor_category'].unique().tolist()))


if st.button('predict'):

    #form a Data frame:
    data=[[property_type,sector,bedroom,bathroom,balcony,property_age,built_up_area,
           servant_room,store_room,furnishing_type,luxury_category,floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
       'agePossession', 'built_up_area', 'servant room', 'store room',
       'furnishing_type', 'luxury_category', 'floor_category']
    
    one_df=pd.DataFrame(data,columns=columns)
    
    st.dataframe(one_df)

    #Predict
    base_price= np.expm1(pipeline.predict(one_df))[0]
    low= base_price-0.22
    high= base_price +0.22

    #display
    st.text("The price of the flat is in between {}cr and {}cr".format (round(low,2), round(high,2)))
