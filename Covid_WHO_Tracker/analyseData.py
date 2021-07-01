'''
A quick and dirty script to plot COVID stats for different countries. The country data
is taken from the WHO website by running the .sh script 

This script is just made for my own quick curiosity and pretty plot formatting is left out
'''

import pandas as pd
import sys
import matplotlib.pyplot as plt

def getCountryData(countryName,data):
    countryData = data[data.Country==countryName]
    return countryData

def plotCountry(country):
    #Open data and rename columns
    data = pd.read_csv("latestData.csv")
    data.rename(columns = {'\ufeffDate_reported':'Date',' Country_code':'Country_code',' Country':'Country',' WHO_region':'WHO_region',' New_cases':'New_cases',' Cumulative_cases':'Cumulative_cases',' New_deaths':'New_deaths',' Cumulative_deaths':'Cumulative_deaths'}, inplace = True)
    data.time = pd.to_datetime(data['Date'],format='%Y-%m-%d')
    
    
    data = getCountryData(str(country),data)
    data['NewDeathsPerCases'] = data['New_deaths'] / data['New_cases']
    data['CumulativeDeathsPerCases'] = data['Cumulative_deaths'] / data['Cumulative_cases']
    
    Columns = list(data.columns)
    
    varList = ['CumulativeDeathsPerCases',
              'NewDeathsPerCases',
              'New_cases',
              'Cumulative_cases',
              'New_deaths',
              'Cumulative_deaths']
    
    for var in Columns:
        if var not in varList and var != 'Date':
            data.drop(var,1)
    
    Columns = list(data.columns)
   
    data.plot(kind='line', subplots=True, grid=True,
            layout=(3, 2), sharex=True, sharey=False, legend=True,
            style=['b', 'b', 'r', 'r', 'g', 'g'],
            x='Date',figsize=(10,10))
    
    plt.tight_layout()
    plt.show()

country = sys.argv[1]
plotCountry(country)
