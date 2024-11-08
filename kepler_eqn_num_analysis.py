# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 22:13:16 2024

@author: foxen
"""

import numpy as np
import pandas as pd

# Kepler's Fixed-Point Method

# Establish variables
M = float(input("Provide M [deg]: "))
ecc = float(input("Provide the eccentricity (e) of the orbit: "))
n = int(input("Provide the number of iterations: "))

M = M*np.pi/180 # Convert from degrees to radians

# Define Kepler's equation for fixed-point iteration
def kepler_eqn(ecc, M, n):
    E = np.empty(n)
    E[0] = M
    errs = np.empty(n-1)
    for k in range(0, n-1):
        E[k+1] = M + ecc*np.sin(E[k])
        errs[k] = abs(E[k+1]-E[k])
    return E, errs

# Run iteration and compute error
E_vals = kepler_eqn(ecc, M, n)
E_vals1 = np.round(E_vals[0]*180/np.pi,7)
errs = np.append([0],E_vals[1])

# Organize data for display
data_out = np.array([E_vals1, errs])
index_values = ['E Values','Local Error']
column_values = np.array(list(range(n)))
df = pd.DataFrame(data = data_out, index = index_values, columns= column_values, dtype = object)

# Display E values
print("Kepler's Method Results: ")
print(df)
