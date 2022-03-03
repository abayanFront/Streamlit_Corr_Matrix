from matplotlib.pyplot import savefig
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib as plt


#List of ticker lists that are going to drop from the correlation matrix.
drop_list = ['ticker','price_2016','performance_2016', 'price_2017',
'price_2018',
'price_2019',
'price_2020',
'price_2021',     
'price_2022',
'new_price_2016',
'new_price_2017',
'new_price_2018',
'new_price_2019',
'new_price_2020',
'new_price_2021',
       ]

#Title
st.title("Correlation Matrix App")
#It takes an excel file and then write into the streamlit.
uploaded_file = st.file_uploader("Choose an excel (xlsx) file")
if uploaded_file is not None:
  df = pd.read_excel(uploaded_file).astype(str)
  
  st.write(df)


combined = pd.read_excel('stock_features_version_2_regression_2016_Q1_2289_stocks_CLEANED (1).xlsx')
combined.drop(drop_list,axis=1)

cormat = combined.corr()
fig = sns.set(rc={'figure.figsize':(40,35)})

#Represented Seaborn figure.
sns.set(font_scale = 0.9)
sns.heatmap(cormat)
sns.heatmap(cormat, annot=True, fmt='.2f')
st.pyplot(fig)
st.set_option('deprecation.showPyplotGlobalUse', False)

