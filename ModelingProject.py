# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 15:23:56 2021

@author: Hill
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import stats


#bac_data=pd.read_csv(r'C:\Users\Hill\Documents\University of Virginia Class Documents\SP21\BME 6311\ModelData.csv')

#Prof2=pd.DataFrame(bac_data, columns=['P2T1','P2T2', 'P2T3', 'P2T4', 'P2T5', 'P2T6','P2T7', 'P2T8', 'P2T9', 'P2T10'])
#Prof1=pd.DataFrame(bac_data, columns=['P1T1','P1T2', 'P1T3', 'P1T4', 'P1T5', 'P1T6','P1T7', 'P1T8', 'P1T9', 'P1T10'])

#means2=Prof2.mean(axis=1)
#means1=Prof1.mean(axis=1)

t2=[54, 53, 59, 57, 54, 57, 56, 55, 53, 56]
print(sum(t2)/10)
t1=[71, 70, 73, 71, 70, 74, 71, 73, 75, 70]
print(sum(t1)/10)
t4=[49, 47, 55, 49, 51, 52, 46, 50, 50, 51]
print(sum(t4)/10)

plt.hist(t2, label='Prolif-rate=2 hr')
plt.hist(t1, label='Prolif-rate=1 hr')
plt.title('Time Distributions')
plt.xlabel('Time (hr)')
plt.ylabel('Density')
plt.legend()
plt.show()

plt.hist(t2, label='Prolif-rate=2 hr')
plt.hist(t4, label='Prolif-rate=4 hr')
plt.title('Time Distributions')
plt.xlabel('Time (hr)')
plt.ylabel('Density')
plt.legend()



Tfast=stats.ttest_ind(t1, t2)
Tslow=stats.ttest_ind(t2, t4)


