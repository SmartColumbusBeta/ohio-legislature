
# coding: utf-8

# Import statements

# In[1]:


import ipyleaflet as ipyl
from ipyleaflet import *
import ipywidgets as ipyw
import json


# Declare Map and Label widgets, display map

# In[2]:


map = ipyl.Map(center=[39.9612, -82.9988], zoom=7, basemap=basemaps.OpenStreetMap.BlackAndWhite)
label = ipyw.Label(layout=ipyw.Layout(width='100%'))
ipyw.VBox([map, label])


# Add Layer Controller

# In[3]:


map.add_control(LayersControl())


# Add United States Congress Ohio Delegation GeoJSON layer. Check layer controller to verify load.

# In[4]:


with open('data/US_House_of_Representative_Districts_Ohio.geojson') as f:
    data = json.load(f)
for feature in data['features']:
    feature['properties']['style'] = {
        'color': 'grey',
        'weight': 1,
        'fillColor': 'grey',
        'fillOpacity': 0.5
    }
layerUSH = ipyl.GeoJSON(data=data, hover_style={'fillColor': 'purple'}, name='United States House of Representatives')

def hover_handler(event=None, id=None, properties=None):
    label.value = properties['DISTRICT']

layerUSH.on_hover(hover_handler)
map.add_layer(layerUSH)


# Add Ohio Senate GeoJSON layer. Check layer controller to verify load.

# In[5]:


with open('data/Ohio_Senate_Districts.geojson') as f:
    data = json.load(f)
for feature in data['features']:
    feature['properties']['style'] = {
        'color': 'grey',
        'weight': 1,
        'fillColor': 'grey',
        'fillOpacity': 0.5
    }
layerOHS = ipyl.GeoJSON(data=data, hover_style={'fillColor': 'orange'}, name='The Ohio Senate')

def hover_handler(event=None, id=None, properties=None):
    label.value = properties['DISTRICT']

layerOHS.on_hover(hover_handler)
map.add_layer(layerOHS)


# Add Ohio House GeoJSON layer. Check layer controller to verify load.

# In[6]:


with open('data/Ohio_House_Districts.geojson') as f:
    data = json.load(f)
for feature in data['features']:
    feature['properties']['style'] = {
        'color': 'grey',
        'weight': 1,
        'fillColor': 'grey',
        'fillOpacity': 0.5
    }
layerOHH = ipyl.GeoJSON(data=data, hover_style={'fillColor': 'green'}, name='The Ohio House of Representatives')

def hover_handler(event=None, id=None, properties=None):
    label.value = properties['DISTRICT']

layerOHH.on_hover(hover_handler)
map.add_layer(layerOHH)


# **Uncheck all layers when switching between layers to get rid of district outline afterimages.**
