import pandas as pd
import os

cityofHighestUnemployment = ""
directory = os.fsencode(r'C:\Users\rahul\Projects\covid19hackathon2020\datasets\localAreaUnemployement\Data\California')
maxRate = 0.0
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    data = pd.read_excel(r'C:\Users\rahul\Projects\covid19hackathon2020\datasets\localAreaUnemployement\Data\California\\' + filename,skiprows=11, header=None, names=["Year", "Period", "laborforce", "employment", "unemployment", "unemploymentrate"])
    df = pd.DataFrame(data)
    row = df[['unemploymentrate']].idxmax()
    maxUnemploymentRate = df.iloc[row]['unemploymentrate'].values[0]
    
    
    
    cityData = pd.read_excel(r'C:\Users\rahul\Projects\covid19hackathon2020\datasets\localAreaUnemployement\Data\California\\' + filename, header=None)
    df2 = pd.DataFrame(cityData)
    if(filename.endswith(".xlsx")):
        if(maxRate < maxUnemploymentRate):
            maxRate = maxUnemploymentRate
        else:
            print(maxRate)
            cityName = df2.iloc[5].values[1]
            cityofHighestUnemployment = "" + cityName
            print(cityofHighestUnemployment)


