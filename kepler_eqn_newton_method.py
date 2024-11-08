import numpy as np
import pandas as pd

# Kepler's Equation:
# M = E - e*sin(E)
# or equivalently,
# E = M + e*sin(E) (implicitly defining for E)

# Establish parameters 
M = float(input("Provide M [deg]: "))
ecc = float(input("Provide eccentricity 'e': "))
n = int(input("Provide number of iterations: "))

# Initial guess for E is M
E0 = M*np.pi/180 # here we convert the input M in degrees to radians

# Define function for solving Kepler's Equation with Newton's Method
def keplers_eqn_newton(E0, ecc, n):
	#Create arrays to store values in
	E_vals = np.empty(n)
	E_vals[0] = E0
	Error_vals = np.empty(n-1) # here is where we will store local error
	# Run Newton's method on the equation
	for k in range(1, n):
		E_vals[k] = E_vals[k-1] - (E_vals[k-1]- ecc*np.sin(E_vals[k-1])-E0)/(1-ecc*np.cos(E_vals[k]))
		Error_vals[k-1] = abs(E_vals[k]-E_vals[k-1])
	return E_vals, Error_vals

soln = keplers_eqn_newton(E0, ecc, n)
E_vals = soln[0]*180/np.pi # Convert back to degrees for display
Error_vals = np.append([0], soln[1])

# Organize data and labels for tabulation
data_out = np.array([E_vals, Error_vals])
index_values = ['E Values','Local Error']
column_values = np.array(list(range(n)))

# Create data frame with Pandas
df = pd.DataFrame(data = data_out, index = index_values, columns = column_values)
print(df)