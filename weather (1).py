#!/usr/bin/env python
# coding: utf-8

# # WeatherPy
# ----
# 
# #### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
from scipy.stats import linregress

# Import API key
from api_keys import weather_api_key

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)


# ## Generate Cities List

# In[2]:


# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(lat_range[0], lat_range[1], size=1500)
lngs = np.random.uniform(lng_range[0], lng_range[1], size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
len(cities)


# ### Perform API Calls
# * Perform a weather check on each city using a series of successive API calls.
# * Include a print log of each city as it'sbeing processed (with the city number and city name).
# 

# In[13]:





# ### Convert Raw Data to DataFrame
# * Export the city data into a .csv.
# * Display the DataFrame

# In[15]:





# In[16]:





# ## Inspect the data and remove the cities where the humidity > 100%.
# ----
# Skip this step if there are no cities that have humidity > 100%. 

# In[6]:





# In[17]:


#  Get the indices of cities that have humidity over 100%.


# In[19]:


# Make a new DataFrame equal to the city data to drop all humidity outliers by index.
# Passing "inplace=False" will make a copy of the city_data DataFrame, which we call "clean_city_data".


# In[ ]:





# ## Plotting the Data
# * Use proper labeling of the plots using plot titles (including date of analysis) and axes labels.
# * Save the plotted figures as .pngs.

# ## Latitude vs. Temperature Plot

# In[10]:





# ## Latitude vs. Humidity Plot

# In[11]:





# ## Latitude vs. Cloudiness Plot

# In[12]:





# ## Latitude vs. Wind Speed Plot

# In[13]:





# ## Linear Regression

# In[24]:





# ####  Northern Hemisphere - Max Temp vs. Latitude Linear Regression

# In[25]:





# ####  Southern Hemisphere - Max Temp vs. Latitude Linear Regression

# In[26]:





# ####  Northern Hemisphere - Humidity (%) vs. Latitude Linear Regression

# In[27]:





# ####  Southern Hemisphere - Humidity (%) vs. Latitude Linear Regression

# In[28]:





# ####  Northern Hemisphere - Cloudiness (%) vs. Latitude Linear Regression

# In[29]:





# ####  Southern Hemisphere - Cloudiness (%) vs. Latitude Linear Regression

# In[30]:





# ####  Northern Hemisphere - Wind Speed (mph) vs. Latitude Linear Regression

# In[31]:





# ####  Southern Hemisphere - Wind Speed (mph) vs. Latitude Linear Regression

# In[32]:





# In[ ]:




