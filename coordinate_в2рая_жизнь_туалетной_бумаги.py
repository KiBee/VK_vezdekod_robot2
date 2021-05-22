import osmnx as ox
import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
name_file = 'result.png'
print('Creating', name_file,'...')
nyc = pd.read_csv('nyc_robots.csv', delimiter=';')
nyc = nyc.drop(columns=['tripduration', 'start station id', 'starttime',
                        'stoptime', 'end station id', 'Robots',
                        'birth year', 'usertype', 'gender']).drop_duplicates()

re_cols = {"start station latitude": "s_lat",
           'start station longitude': 's_lon',
           "end station latitude": "e_lat",
           'end station longitude': 'e_lon',
           'start station name': 's_name',
           'end station name': 'e_name',
           }
nyc = nyc.rename(columns=re_cols)

gdf = nyc[['s_lon','s_lat','s_name','e_lon','e_lat','e_name']]

edges = ['Jersey City, USA',
        'Manhattan, New York City, New York, USA', 'Brooklyn, USA']
edges = ox.geocode_to_gdf(edges)


ax = edges.plot(color='white', edgecolor='black', figsize=(150, 200))

ax.plot(gdf['e_lon'], gdf['e_lat'],
        marker='o', linestyle='', color='red', markersize=8)

ax.plot(gdf['s_lon'], gdf['s_lat'],
        marker='.', linestyle='', color='lime', markersize=5)

gdf.apply(lambda x: ax.annotate(
    x['s_name'], (x['s_lon'] + 0.0005, x['s_lat']),fontsize=14), axis=1)


gdf.apply(lambda x: ax.annotate(
    x['e_name'], (x['e_lon'] + 0.0005, x['e_lat']),fontsize=14), axis=1)


plt.savefig(name_file,)
print('Completed!')