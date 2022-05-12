#!/usr/bin/env python
# coding: utf-8

# In[1]:


import folium
iran_map = folium.Map(location = [32.4279,53.6880],zoom_start = 5)
iran_map


# In[2]:


import pandas as pd
ubaar = pd.read_csv("C:\\Users\\Lenovo\Desktop\\New folder\\train.csv")
sample_ubaar = ubaar.head(1000)
ubaar.head()


# In[3]:


for lat, lng in zip(sample_ubaar.sourceLatitude,sample_ubaar.sourceLongitude):
    folium.CircleMarker(
        [lat, lng],
        radius=2,
        color='red',
        fill=True,
        fill_color='darkred',
        fill_opacity=0.5 ).add_to(iran_map)
iran_map


# In[4]:


for lat, lng in zip(sample_ubaar.destinationLatitude,sample_ubaar.destinationLongitude):
 folium.CircleMarker(
    [lat, lng],
    radius=2,
    color='blue',
    fill=True,
    fill_color='blue',
    fill_opacity=0.3 ).add_to(iran_map)
iran_map


# In[5]:


iran_map = folium.Map(location = [32.4279,53.6880],zoom_start = 5)


# In[7]:


for row in range(sample_ubaar.shape[0]):
    folium.CircleMarker(
         location=[sample_ubaar.iloc[row,:]['sourceLatitude'],
         sample_ubaar.iloc[row,:]['sourceLongitude']],
         radius=int(sample_ubaar.iloc[row,:]['price']),
         color='red',
         fill=True,
         fill_color='darkred',
         fill_opacity = 0.7
         ).add_to(iran_map)


# In[8]:


iran_map


# In[9]:


iran_map = folium.Map(location = [32.4279,53.6880],zoom_start = 5)


# In[10]:


for row in range(sample_ubaar.shape[0]):
    folium.CircleMarker(
        location=[sample_ubaar.iloc[row,:]['destinationLatitude'],
        sample_ubaar.iloc[row,:]['destinationLongitude']],
        radius=int(sample_ubaar.iloc[row,:]['price']),
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity = 0.1
        ).add_to(iran_map)
iran_map


# In[11]:



iran_map = folium.Map(location = [32.4279,53.6880],zoom_start = 5)
from folium.plugins import HeatMap
iran_map = folium.Map(location = [32.4279,53.6880],zoom_start = 5)
iran_map


# In[12]:


ubaar['price_normalized'] = (ubaar['price'] - ubaar['price'].min())/ ubaar['price'].max()
HeatMap(
 data=list(zip(ubaar.head(20000)['sourceLatitude'],
 ubaar.head(20000)['sourceLongitude'],
 ubaar.head(20000)['price_normalized'])
 ) ,
 radius = 12
).add_to(iran_map)
iran_map


# In[ ]:




