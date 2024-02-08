 # streamlit run djia_csv_to_streamlit.py  # Optional: --client.showErrorDetails=False


import streamlit as st
import pandas as pd
import numpy as np
import datetime

DATA_URL = 'upload_DJIA_table.csv'

st.title("Dow Jones Industrial Data")
# st.sidebar.title("Analyse Data by column or row")

# st.markdown("Dow Jones Industrial Data by Date")
st.sidebar.subheader("Dow Jones Industrial Data")


@st.cache_data(persist=True)
def load_data():
    data = pd.read_csv(DATA_URL)
    return data
data = load_data()

df = pd.DataFrame(data)

if st.sidebar.checkbox("Volume By Date", True):
    df = pd.DataFrame(data)
    # df = st.table(data)
    st.subheader("Volume by Day")
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    df = df.set_index(['Date'])
    df = df.sort_values(by="Date",ascending=True)
    df
    

if st.sidebar.checkbox("Volume By Year", False):
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    df_year = df['Date'].dt.strftime('%Y')
    df = df.groupby(df_year)['Volume'].sum()
    chart_data = df
    col1, col2 = st.columns(spec=2, gap='small')
    with col1:
        st.subheader("Volume by Year")
        df
    with col2:
        st.subheader("Charted Volume by Year")
        st.bar_chart(chart_data) # , use_container_width=False)

if st.sidebar.checkbox("Volume By Month", False):
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    df_month = df['Date'].dt.strftime('%Y-%m')
    df = df.groupby(df_month)['Volume'].sum()
    chart_data = df
    col1, col2 = st.columns(spec=2, gap='small')
    with col1:
        st.subheader("Volume by Month")
        df
    with col2:
        st.subheader("Charted Volume by Month")
        st.line_chart(chart_data) # , use_container_width=False)


st.sidebar.subheader("Select a Column")
if st.sidebar.checkbox("By Category, By Day", False):
    st.subheader("By Category, By Day")
    choice = st.sidebar.multiselect('Select column', ('Open','High','Low','Close','Volume','Adj Close'))        
    date_default = ('Date')
    choice.append(date_default)
    if len(choice) > 1:  
        df = data[choice]
        df['Date'] = pd.to_datetime(df['Date'])
        df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
        df = df.rename_axis('ID') # renames DataFrame index
        df = df.set_index(['Date'])
        df = df.sort_values(by="Date",ascending=True)       
        df

