import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pickle
import seaborn as sns

st.set_page_config(page_title="plotting Demo")
st.title('Analytics')

new_df= pd.read_csv('Data/data_vi1.csv')
feature_text= pickle.load(open('Data/feature_text.pkl','rb'))

group_df = new_df.groupby('sector')[['price','price_per_sqft',
         'built_up_area','latitude','longitude']].mean()


#st.dataframe(new_df)
group_df = group_df.reset_index()

#1.
st.header('Sector Price per Sqft Geo_map')
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,
                  hover_name='sector')
st.plotly_chart(fig,use_container_width=True)


plt.rcParams["font.family"] = "Arial"

#2.

st.header('Feature Wordcloud')
wordcloud = WordCloud(width = 800, height = 800, 
                      background_color ='white', 
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text)

fig, ax = plt.subplots(figsize=(8, 8))

ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")

st.pyplot(fig)

# Scatter plot bw area vs Price

#3.

st.header('Area Vs Price')

property_type= st.selectbox('Select Property Type',['flat','house'])
if property_type =='house':
    fig1 = px.scatter(new_df[new_df['property_type']=='house'],x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")
    st.plotly_chart(fig1,use_container_width=True)


else:
    fig1 = px.scatter(new_df[new_df['property_type']=='flat'],x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")

    st.plotly_chart(fig1,use_container_width=True)


#4.

st.header('BHK Pie chart')

sector_options= new_df['sector'].unique().tolist()
sector_options.insert(0,'Overall')

selected_sector= st.selectbox('Select Sector',sector_options)

if selected_sector == 'Overall':
    fig2= px.pie(new_df, names='bedRoom')
    st.plotly_chart(fig2,use_container_width=True)

else:
    fig2= px.pie(new_df[new_df['sector']== selected_sector], names='bedRoom')
    st.plotly_chart(fig2,use_container_width=True)


#5.
st.header(' Side by Side BHK Price Range')
fig3=px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price')
st.plotly_chart(fig3,use_container_width=True)

#6
st.header('Side by Side Distplot for Property Type')



fig4=sns.displot(new_df[new_df['property_type'] == 'house']['price'])
st.pyplot(fig4)
fig5=sns.displot(new_df[new_df['property_type'] == 'flat']['price'])

