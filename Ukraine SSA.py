# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 20:08:42 2025

@author: Harshad
"""

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

#setup SSA Data
ukraine_ssa = pd.read_csv('WHO SSA Ukraine.csv')

print(ukraine_ssa.columns.tolist())

#changing dtypes
ukraine_ssa['ATTACKDATE'] = pd.to_datetime(ukraine_ssa['ATTACKDATE'])

#setting new df
ukraine_new = ukraine_ssa.loc[: , ['ATTACKDATE', 'VICTIMSTOTALDEATH', 'VICTIMSTOTALINJURED']]

#split dataset based off total death and total injured
ukraine_new1 = ukraine_new.groupby(ukraine_new['ATTACKDATE'].dt.to_period('M'))
ukraine_new1 = pd.DataFrame(ukraine_new1['VICTIMSTOTALDEATH'].sum())

ukraine_new2 = ukraine_new.groupby(ukraine_new['ATTACKDATE'].dt.to_period('M'))
ukraine_new2 = pd.DataFrame(ukraine_new2['VICTIMSTOTALINJURED'].sum())

#reset indices 
ukraine_new1.reset_index(inplace=True)
ukraine_new2.reset_index(inplace=True)

#change dtype to dt again
ukraine_new1['ATTACKDATE'] = ukraine_new1['ATTACKDATE'].dt.to_timestamp()
ukraine_new2['ATTACKDATE'] = ukraine_new2['ATTACKDATE'].dt.to_timestamp()

print(ukraine_new1)
print(ukraine_new2)

#plots 
plt.plot(ukraine_new1['ATTACKDATE'], ukraine_new1['VICTIMSTOTALDEATH'], data = ukraine_new1, color = 'red')
plt.plot(ukraine_new2['ATTACKDATE'], ukraine_new2['VICTIMSTOTALINJURED'], data = ukraine_new2, color = 'blue')

plt.xticks(rotation=45, ha='right', fontsize = 8)
plt.xlabel('Timeline')
plt.ylabel('Fatalities')
plt.title('Surveillance system for attacks on healthcare (Ukraine)')
plt.legend(['Fatalities', 'Injuries'], loc='upper right')
plt.tight_layout()