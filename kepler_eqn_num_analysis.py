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
n = int(input("Provide the number of iterations: "))+1

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


# Newton's Method for Kepler's Equation

#def kepler_eqn_newton(ecc, M, n):
#    E_N = np.empty(n)
#    E_N[0] = M
#    errs_N = np.empty(n-1)
#    for k in range(0, n-1):
#        E_N[k+1] = E_N[k]-(E_N[k]-ecc*np.sin(E_N[k])-M)/(1-ecc*np.cos(E_N[k]))
#        errs_N[k] = abs(E_N[k+1]-E_N[k])
#    return E_N, errs_N

# Run function and assign variables to tuple from function
#E_Newton = kepler_eqn_newton(ecc, M, n)
#E_N1 = E_Newton[0]
#errs_N1 = E_Newton[1]

# Display E_N values
#print("Newton's Method for Kepler's Equation Results:")
#print(E_N1)
#print(errs_N1)

# Compare methods
#rel_err = abs(errs-errs_N1)
#print("Relative error between the two methods: ")
#print(rel_err)