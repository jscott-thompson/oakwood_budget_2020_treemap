# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 20:03:59 2020

@author: Scott

Data grabbed from https://storage.googleapis.com/proudcity/oakwoodoh/uploads/2020/02/2020-City-of-Oakwood-Budget.pdf
"""
#%%
import matplotlib.pyplot as plt
import pandas as pd
import squarify

#%%
df = pd.read_csv("oakwood_city_budget_2020.csv")
plt.figure(figsize=(10,10))
squarify.plot(sizes=df['Percent'], label=df['Category'],alpha=.8,color=['#7fc97f',
              '#beaed4',
              '#fdc086',
              '#ffff99',
              '#386cb0',
              '#f0027f',
              '#bf5b17'])
plt.axis('off');
plt.title('Oakwood 2020 Budget')
plt.show()
