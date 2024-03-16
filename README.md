# Stock-Price-Prediction-with-Sentiment-Analysis

## Summary
Forecasting the highly volatile stock market is a significant computing challenge due to its erratic nature. Investors often face the risk of selling shares at inopportune times due to market unrest. While precise prediction is very difficult to attain, leveraging historical data analysis and machine learning techniques can help minimize losses. This project proposes to bridge the gap between financial market sentiment and stock price movements by combining the sentiment analysis on social media data with historical stock data from Yahoo Finance with an aim to determine if user sentiments have a notable impact on changes in the stock market.

## Data
1. https://www.kaggle.com/datasets/omermetinn/tweets-about-the-top-companies-from-2015-to-2020
2. https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests/data
3. Yahoo Finance Stock Data API
4. Reddit Praw API

## Project Goals
The core objective of our project is to conduct a comprehensive analysis and scrutiny of stock prices. We place a particular emphasis on discerning underlying patterns and implementing time series evaluations on the stock prices data. This involves using time-series models such as ARIMA and LSTM. Our aim is to build a robust model that integrates sentiment scores of social media posts using VADER scores and news headlines using FINBERT with stock prices. The focus is on predicting future stock price movements. Additionally, we aim to conduct a comparative study between the movement of stocks with and without social media sentiments.

## User Interface: 
Upon launching the application, users are prompted to choose an S&P 500 stock from a dropdown list. Real-time data is then scraped from Yahoo Finance to provide fundamental details such as symbol, name, currency, and sector for the chosen stock. The user then has access to five features:
- Top News Headlines: Users can access the latest news related to their selected stock. This feature keeps users informed about recent developments and news that might impact the stock's performance.
- Stock Trend Graph: Users have the ability to specify start and end dates for a selected stock. The application generates interactive graphs, allowing users to visualize and analyze the close price and daily total returns during the specified time frame. The user can also plot two moving averages on the close price line graph for an interactive study. 
- Historical Price Chart: A detailed chart is available, presenting essential stock prices, including high, low, open, close, and adjusted close. This feature provides users with a comprehensive view of the historical performance of the selected stock.
- Future Close Price Prediction: Users can choose from eight prominent stocks (Apple, Google, Amazon, GameStop, Meta, Netflix, Nvidia, or Tesla). The application leverages predictive analytics to display possible future close price values, aiding users in making informed investment decisions.
- Chatbot: The application incorporates a chatbot feature powered by OpenAI's ChatGPT. Users can engage in conversations with the chatbot to learn about the stock market, enhancing their understanding of financial concepts and market dynamics.


Check out the user interface we built: https://stock-analytics.streamlit.app/

(To deploy the app we created another repo: https://github.com/Amey1398/stock-app-deployment/tree/main)
