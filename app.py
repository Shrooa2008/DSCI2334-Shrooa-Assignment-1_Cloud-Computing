import streamlit as st
import pandas as pd

df = pd.read_csv('cafe_sales.csv')
st.title('Qahwa Corner Sales')
selected_branch = st.selectbox('Select Branch', df['branch'].unique())
filtered_df = df[df['branch'] == selected_branch]
st.metric(label='Total Revenue (SAR)', value=filtered_df['total_sar'].sum())
st.bar_chart(filtered_df.groupby('product')['quantity'].sum())
