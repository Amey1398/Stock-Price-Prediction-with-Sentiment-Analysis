# pip install streamlit fbprophet yfinance plotly
import streamlit as st
from datetime import date

import yfinance as yf
# from prophet import Prophet
# from prophet.plot import plot_plotly
from plotly import graph_objs as go
import pickle
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from functions import *

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Forecasting App')

stocks = ('GOOG', 'MSFT', 'AMZN', 'TSLA')
selected_stock = st.selectbox('Select stock for prediction', stocks)

#n_years = st.slider('Years of prediction:', 1, 4)
#period = n_years * 365

days = ('Days', 'Month', 'Year','Predict')
predict_type = st.selectbox('Select what to predict', days)

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

	
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')


#df, startdate,enddate = load_data(selected_stock)


st.subheader('Stock data')
st.write(data.tail())

# Plot raw data
def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(title_text='Data with Rangeslider', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
	
plot_raw_data()

# path = 'Stock-Price-Prediction-with-Sentiment-Analysis\Saved Models\MSFT_model.pkl'

# Get model path
def get_path(stock):
     path = r"Stock-Price-Prediction-with-Sentiment-Analysis\Saved Models\{}_model.pkl".format(stock)
     return path

# Get saved model weights
def get_pickle(path):
	with open(path, 'rb') as f:
		model = pickle.load(f)
	return model

path = get_path(selected_stock)
stock_model = get_pickle(path)
#print(stock_model.keys())

#new_mod = 'E:\NORTHEASTERN\FALL 2023\CAPSTONE\Stock-Price-Prediction-with-Sentiment-Analysis\app\saachi_trial\GOOG_model'
      
# Prepare the data
features = ['Close', 'High', 'Low', 'Open', 'Volume']
look_back = 5 # No. of Lags to consider
predict_type = 'predict' #predict_type.lower()
train_X, train_Y, train_dates, test_X, test_Y, test_dates, scaler, test_data = prepare_data_multivariate(data, selected_stock, START, TODAY, features=features, look_back=look_back, predict_type=predict_type )



# How to use the saved weights to do same thing as predict function
# How to get dates
# Need to change predict function into multiple functions
input_size = 5  # Number of input features (High, Low, Open, Close, Volume)
output_size = 1  # Number of output features (Close price)
num_epochs = 100
num_layers = 2 
hidden_sizes = [64, 64]


file = open(r"GOOG_params.pkl",'rb')
object_file = pickle.load(file)

model = DynamicLSTM(object_file['input_size'], object_file['hidden_size'], object_file['num_layers'], object_file['output_size'])
model.load_state_dict(torch.load(r"GOOG_model"))
model.eval()

table = get_preds(test_X, test_data, test_dates, scaler, model)


st.subheader('Predicted values')
st.write(table)



