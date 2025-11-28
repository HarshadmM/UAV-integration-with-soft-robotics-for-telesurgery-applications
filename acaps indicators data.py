# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 02:31:21 2025

@author: Harshad
"""

"""
Data is coded according to access dimensions, indicators and sub-indicators, 
then scored on a 0 to 5 severity scale

Pillars and overall access scores are represented on a scale from 0 to 5, where:
Indicators are scored on a scale from 0 to 3, with 3 representing the highest level of constraints.

5 - Extreme access constraints
4 - Very high access constraints
3 - High access constraints
2 - Moderate access constraints
1 - Low access constraints
0 - No constraints
"""
import pandas  as pd
import matplotlib.pyplot as plt

#load acaps file
acaps_path = '20220701_acaps_humanitarian_access_dataset.xlsx'

#open indicators sheet from the file 
indicators = pd.read_excel(acaps_path, sheet_name ='indicators')

#get aggregate access scores for all the different types
indicators = indicators.iloc[:, 2:-3]

indicator_means = indicators.mean()

indicator_means.index = (
    indicator_means.index.str.replace(r'^\d+\.?\s*', '', regex=True)
)


#plot

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(indicator_means.index, indicator_means.values)

ax.set_ylabel("Mean score")
ax.set_title("Average Severity of ACAPS Access Constraints")

#Remove x-axis labels
ax.set_xticks([])

#Add labels inside bars
for bar, label in zip(bars, indicator_means.index):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
       0.05,                 # small offset above the base
       label,
       ha='center',
       va='bottom',
       rotation=90,
       color='white',
       fontsize=9,
       clip_on=True 
    )

plt.tight_layout()
plt.show()