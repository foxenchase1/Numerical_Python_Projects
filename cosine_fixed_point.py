# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:15:06 2024

@author: foxen
"""

import numpy as np
import pandas as pd

x0 = float(input("Specify an initial x: "))
n = int(input("Specify number of iterations: "))+1

def cosine_fixed_point(x0, n):
    cosine_vals = np.empty(n)
    cosine_vals[0] = x0
    errs = np.empty(n)
    errs[0] = 0
    for k in range(n-1):   
        cosine_vals[k+1] = np.cos(cosine_vals[k])
        errs[k+1] = abs(cosine_vals[k+1]-cosine_vals[k])
    return cosine_vals, errs

iteration_array = cosine_fixed_point(x0, n)
data_out = np.array([iteration_array[0],iteration_array[1]])
index_values = ['Cosine Values','Local Error']
column_values = np.array(list(range(n)))
df = pd.DataFrame(data = data_out, index = index_values, columns = column_values, dtype = object)

print(df)