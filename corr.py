from matplotlib.pyplot import savefig
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib as plt

uploaded_file = st.file_uploader("Choose an excel (xlsx) file")

if uploaded_file is not None:
  df = pd.read_excel(uploaded_file).astype(str)
  combined = pd.read_excel(uploaded_file)
  combined_str = pd.read_excel(uploaded_file).astype(str)
  features_list = []
  for i in combined.columns:
    features_list.append(i)

  #Title
  st.title("Correlation Matrix App")
  st.write('The following selected features will drop from the matrix.')
  #List of ticker lists that are going to drop from the correlation matrix.
  options =st.multiselect('Select the features.',features_list)
  st.write('You selected:', options)

  

  
  #It takes an excel file and then write into the streamlit.
  st.write('Downloaded Excel File')
  #Drop option for the options list.
  dropped_combine = combined.drop(options,axis=1)
  
  st.write(combined_str)
  cormat = dropped_combine.corr()
  fig = sns.set(rc={'figure.figsize':(40,35)})

  #Represented Seaborn figure.
  sns.set(font_scale = 0.9)
  sns.heatmap(cormat)
  sns.heatmap(cormat, annot=True, fmt='.2f')
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.pyplot()


