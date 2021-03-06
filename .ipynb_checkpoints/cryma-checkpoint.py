import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


st.title("CryMA : Daily Prices")
st.write("Choose moving averages to explore best buy/sell times")
crypto = st.sidebar.selectbox('Select a Cryptocurrency',['BTC-GBP', 'ETH-GBP', 'XRP-GBP','BCH-GBP','LTC-GBP','XLM-GBP'])
#st.sidebar.write("Choose moving averages to explore best buy/sell times")
lowma = st.sidebar.slider("Low Moving Average",5,50,20)
highma = st.sidebar.slider("High Moving Average",20,200,50)
time = st.sidebar.slider("Time period (days)",100,1000,300)

#append 'd' to time to define period for yf call
period = '{}{}'.format(time, 'd')
st.header(crypto)
st.write('Low Moving Average =', lowma, ' / High Moving Average =', highma, ' / Period =', period)

#Download the latest data / default interval is one day
df = yf.download(crypto, period=period, interval='1d', progress=False)

#st.dataframe(df.tail(30))


SMAlow = df['Close'].rolling(window = lowma).mean()
SMAhigh = df['Close'].rolling(window = highma).mean()


#plt.figure(figsize=(20, 8))
fig, ax = plt.subplots()
plt.plot(df['Close'][-time:])
plt.plot(SMAlow[-time:], label='SMAlow')
plt.plot(SMAhigh[-time:], label='SMAhigh')
plt.legend(loc='upper left', fontsize=10)
plt.show()
st.pyplot(fig)
