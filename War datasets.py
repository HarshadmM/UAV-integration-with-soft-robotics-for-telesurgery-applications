# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 17:38:44 2025

@author: Harshad
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy


ukraine_conflict = pd.read_csv("ACLED data Ukraine.csv")


#data conversion for wrangling
ukraine_conflict['disorder_type'] = ukraine_conflict['disorder_type'].astype(str)

#summation of ukraine conflict fatalities per day
date_uc = ukraine_conflict.groupby('event_date')
uc_fatalities = pd.DataFrame(date_uc['fatalities'].sum())
uc_fatalities.reset_index(inplace=True)
print(uc_fatalities)
#date-time conversion
uc_fatalities['event_date'] = pd.to_datetime(uc_fatalities['event_date'])

#noise reduction using monthly data instead of daily 
uc_fatalities = uc_fatalities.groupby(uc_fatalities['event_date'].dt.to_period('M'))



uc_fatalities = pd.DataFrame(uc_fatalities['fatalities'].sum())
uc_fatalities.reset_index(inplace=True)



#change dtype of dates to dt again
uc_fatalities['event_date'] = uc_fatalities['event_date'].dt.to_timestamp()
print(uc_fatalities)


plt.plot('event_date', 'fatalities', data=uc_fatalities, color='red')

plt.scatter('event_date', 'fatalities', data=uc_fatalities, color='red')

plt.xticks(rotation=45, ha='right', fontsize = 8)
plt.xlabel('Timeline')
plt.ylabel('Fatalities')
plt.title('Fatalities in the event of Russo-Ukrainian conflict')
plt.tight_layout()
