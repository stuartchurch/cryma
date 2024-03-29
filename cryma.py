import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import streamlit as st

def load_data():
    data = yf.download(crypto, period=period, interval='1d', progress=False)
    return data

st.title("CryMA : Daily Prices")
st.write("Choose moving averages to explore best buy/sell times")
crypto = st.sidebar.selectbox('Select a Cryptocurrency',['BTC-GBP', 'ETH-GBP', 'XRP-GBP','MATIC-GBP','QNT-GBP','DOT-GBP'])

lowma = st.sidebar.slider("Low Moving Average",1,50,20)
highma = st.sidebar.slider("High Moving Average",10,200,50)
time = st.sidebar.slider("Time period (days)",0,1000,300)
#freq = st.sidebar.radio('Frequency', ['1d','60m'])



#append 'd' to time to define period for yf call
period = '{}{}'.format(time, 'd')
st.header(crypto)
st.write('Low Moving Average =', lowma, ' / High Moving Average =', highma, ' / Period =', period)

#Download the latest data / default interval is one day
#df = yf.download(crypto, period=period, interval='1d', progress=False)

df = load_data()
df.reset_index(inplace = True)



st.write("Latest daily prices")
st.dataframe(df.tail(1))

SMAlow = df['Close'].rolling(window = lowma).mean()
SMAhigh = df['Close'].rolling(window = highma).mean()

matplotlib.rc('font', size='6')

#fig, ax = plt.subplots()
#plt.plot(df['Close'][-time:])
#plt.plot(SMAlow[-time:], label='Low MA')
#plt.plot(SMAhigh[-time:], label='High MA')
#plt.legend(loc='upper left', fontsize='8')
#plt.show()
#st.pyplot(fig)

fig, ax = plt.subplots()
plt.plot(df['Date'],df['Close'])
plt.plot(df['Date'],SMAlow,label='Low MA')
plt.plot(df['Date'],SMAhigh,label='High MA')
plt.legend(loc='upper left', fontsize=15)
plt.show()
st.pyplot(fig)

