import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Real-Time Stock Dashboard", layout="wide")

st.title("📈 Real-Time Stock Market Dashboard")

# User Input
ticker = st.text_input("Enter Stock Symbol (Example: AAPL, TSLA, MSFT)", "AAPL")

# Fetch Data
stock = yf.Ticker(ticker)
data = stock.history(period="1d", interval="1m")

if not data.empty:

    # Show Metrics
    current_price = data["Close"].iloc[-1]
    open_price = data["Open"].iloc[0]
    high_price = data["High"].max()
    low_price = data["Low"].min()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Current Price", f"${current_price:.2f}")
    col2.metric("Open", f"${open_price:.2f}")
    col3.metric("High", f"${high_price:.2f}")
    col4.metric("Low", f"${low_price:.2f}")

    # Plot Chart
    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close']
    ))

    fig.update_layout(
        title=f"{ticker} Live Price",
        xaxis_title="Time",
        yaxis_title="Price",
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("Invalid stock symbol or no data available.")
