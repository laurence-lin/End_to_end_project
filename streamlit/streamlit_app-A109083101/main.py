# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 08:30:14 2021

@author: lawrence123
"""

import streamlit as st
import datetime 
import talib 
import ta
import pandas as pd
import requests
from FinMind.data import DataLoader




st.write("""
# Technical Analysis Web Application
Shown below are the **Moving Average Crossovers**, **Bollinger Bands**, **MACD's**, **Commodity Channel Indexes**, and **Relative Strength Indexes** of any stock!
""")

st.sidebar.header('User Input Parameters')

today = datetime.date.today()
def user_input_features():
    ticker = st.sidebar.text_input("股票代號", '2330')
    start_date = st.sidebar.text_input("Start Date", '2019-01-01')
    end_date = st.sidebar.text_input("End Date", f'{today}')
    return ticker, start_date, end_date

symbol, start, end = user_input_features()

# def get_symbol(symbol):
#     url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)
#     result = requests.get(url).json()
#     for x in result['ResultSet']['Result']:
#         if x['symbol'] == symbol:
#             return x['name']
# company_name = get_symbol(symbol.upper())

start = pd.to_datetime(start)
end = pd.to_datetime(end)


dl = DataLoader()
# 下載台股股價資料
# stock_data = dl.taiwan_stock_daily(
#     stock_id='2330', start_date=start, end_date=end
# )

# API問題解決前，先用假資料應付
stock_data = pd.read_csv('stock.csv')

company_name = '台積電'
# Adjusted Close Price
st.header(f"Adjusted Close Price\n {company_name}")
st.line_chart(stock_data['close'])

# ## SMA and EMA
#Simple Moving Average
stock_data['SMA'] = talib.SMA(stock_data['close'], timeperiod = 20)

# Exponential Moving Average
stock_data['EMA'] = talib.EMA(stock_data['close'], timeperiod = 20)

# Plot
st.header(f"Simple Moving Average vs. Exponential Moving Average\n {company_name}")
st.line_chart(stock_data[['close','SMA','EMA']])

# Bollinger Bands
stock_data['upper_band'], stock_data['middle_band'], stock_data['lower_band'] = \
    talib.BBANDS(stock_data['close'], timeperiod =20)

# Plot
st.header(f"Bollinger Bands\n {company_name}")
st.line_chart(stock_data[['close','upper_band','middle_band','lower_band']])

# ## MACD (Moving Average Convergence Divergence)
# MACD
stock_data['macd'], stock_data['macdsignal'], stock_data['macdhist'] = \
    talib.MACD(stock_data['close'], fastperiod=12, slowperiod=26, signalperiod=9)

# Plot
st.header(f"Moving Average Convergence Divergence\n {company_name}")
st.line_chart(stock_data[['macd','macdsignal']])

## CCI (Commodity Channel Index)
# CCI
cci = ta.trend.cci(stock_data['max'], stock_data['min'], stock_data['close'], n=31, c=0.015)

# Plot
st.header(f"Commodity Channel Index\n {company_name}")
st.line_chart(cci)

# ## RSI (Relative Strength Index)
# RSI
stock_data['RSI'] = talib.RSI(stock_data['close'], timeperiod=14)

# Plot
st.header(f"Relative Strength Index\n {company_name}")
st.line_chart(stock_data['RSI'])

# ## OBV (On Balance Volume)
# OBV
stock_data['OBV'] = talib.OBV(stock_data['close'], stock_data['Trading_Volume'])/10**6

# Plot
st.header(f"On Balance Volume\n {company_name}")
st.line_chart(stock_data['OBV'])


