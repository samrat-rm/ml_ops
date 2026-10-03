import streamlit as st
import yfinance as yf

st.title('Stock price Analyser')

col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input("Enter a stock ticker",value='MSFT')
with col2:
    start_date = st.date_input('Enter start ticker date')
with col3:
    end_date = st.date_input('Enter the end date')

st.subheader('Stock Price')
st.line_chart(yf.Ticker(name).history(start=start_date, end=end_date)['Close'])
