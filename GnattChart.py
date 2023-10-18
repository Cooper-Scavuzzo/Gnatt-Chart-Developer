# Create a Gnatt Chart from using the Google Sheets API and Importing Data from Basecamp

# Import Libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

# Import Data from Google Sheets
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open("Gnatt Chart").sheet1
data = wks.get_all_values()
headers = data.pop(0)
df = pd.DataFrame(data, columns=headers)

# Convert Data to Datetime
df['Start Date'] = pd.to_datetime(df['Start Date'])
df['End Date'] = pd.to_datetime(df['End Date'])

# Create a list of unique projects
projects = df['Project'].unique()

# Create a list of unique people
people = df['Person'].unique()

# Create a list of unique dates
dates = df['Start Date'].unique()
dates = np.sort(dates)

# Create a list of unique dates
dates = df['Start Date'].unique()
dates = np.sort(dates)

# Create a list of unique dates
dates = df['Start Date'].unique()
dates = np.sort(dates)

# Create a list of unique dates
dates = df['Start Date'].unique()
dates = np.sort(dates)

# Create a list of unique dates
dates = df['Start Date'].unique()
dates = np.sort(dates)

# Create a list of unique dates
dates = df['Start Date'].unique()
dates = np.sort(dates)

# Create a list of unique dates

