# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:36:06 2025

@author: Harshad
"""

import pandas as pd
import matplotlib.pyplot as plt

"""
Data is coded according to access dimensions, indicators and sub-indicators, 
then scored on a 0 to 5 severity scale

Pillars and overall access scores are represented on a scale from 0 to 5, where:

5 - Extreme access constraints
4 - Very high access constraints
3 - High access constraints
2 - Moderate access constraints
1 - Low access constraints
0 - No constraints
"""

#load acaps file
acaps_path = '20220701_acaps_humanitarian_access_dataset.xlsx'

#open pillars sheet from the file 
pillars = pd.read_excel(acaps_path, sheet_name ='pillars')

pillars.info()

scores = [0,1,2,3,4,5]
score_frequency = {s: 0 for s in scores}

'''function to determine frequency of scores to be used in plots
    column (column from the pd.DF)
    dictionary (frequency of values in column)
'''
def frequency_eval (column,dictionary) :
    for value in column : 
        if value in dictionary :
            dictionary[value] += 1

frequency_eval(pillars['Physical, Environmental and Security Constraints'], score_frequency)

humanitarian_frequency = {s: 0 for s in scores}

frequency_eval(pillars['HUMANITARIAN ACCESS'], humanitarian_frequency)



# Create one figure with two axes (side-by-side)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 5), sharey=True)

# Plot 1: Physical, Environmental and Security Constraints
axes[0].bar(score_frequency.keys(), score_frequency.values())
axes[0].set_title('Global Physical, Environmental and Security Constraints (July 2022)')
axes[0].set_xlabel('Access Scores')
axes[0].set_ylabel('Frequency')
axes[0].set_xticks([0, 1, 2, 3, 4, 5])

# Plot 2: Humanitarian Access Constraints
axes[1].bar(humanitarian_frequency.keys(), humanitarian_frequency.values(), color = 'red')
axes[1].set_title('Global Humanitarian Access Constraints (July 2022)')
axes[1].set_xlabel('Access Scores')
axes[1].set_xticks([0, 1, 2, 3, 4, 5])

# Adjust spacing
plt.tight_layout()
plt.show()


