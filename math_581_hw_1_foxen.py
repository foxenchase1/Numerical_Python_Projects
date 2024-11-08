# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 16:21:16 2024

@author: foxen
"""

import numpy as np
import matplotlib.pyplot as plt

#%% Problem 1

# Define the function we will be interpolating
def g(x):
    g = 1/(1+25*x**2)
    return g
# Step size
st = 0.25

# Exact function 
x_ex = np.linspace(-1.0075,1.0075,1251)
g_ex = g(x_ex)
# Data points
x_est = np.arange(-1,1+st,st)
g_est = g(x_est)
# Polynomial interpolation
m = len(x_est)
n = m-1
p = np.poly1d(np.polyfit(x_est, g_est, n))

# Plotting data
plt.plot(x_ex, g_ex, color = 'blue', label = 'Exact')
plt.plot(x_est, g_est, 'o', color = 'black', label = 'Data Pts.')
plt.plot(x_ex, p(x_ex), color = 'red', label = 'Interp.')
plt.grid()
plt.axhline(color = 'black')
plt.title('Polynomial Interpolation', loc='center')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

#%% Problem 4

# Define steps
h = [20, 40, 80, 160]
# Define our ODE
def f(t,y):
    f = -y+2*np.exp(-t)*np.cos(2*t)
    return f
# Exact soln
t1 = np.linspace(0,1,num=1000)
def y_ex(t1):
    y_ex = np.exp(-t1)*np.sin(2*t1)
    return y_ex
y_exact = y_ex(t1)
# Euler's Method
for j in range(4):
    # Establish initial condition
    y = [0]
    k = h[j] # Determine how many steps will be taken
    t = np.linspace(0, 1, num=k) # Partition the t axis
    for i in np.arange(0,len(t)-1):
        y.append(y[i])
        y[i+1] = y[i]+(1/k)*f(t[i],y[i])
        error = [np.abs(y[i+1]-y_ex(t[i+1]))]
    global_error = np.linalg.norm(error,np.inf)
    # Plotting data and functions
    title = 'Estimated and Exact Solns. with '+str(k)+' Steps'
    errordisp = 'Global Error of: '+str(round(global_error,4))
    plt.plot(t,y,".", label = 'Numerical')
    plt.plot(t1,y_exact, label = 'Exact')
    plt.grid()
    plt.title(title, loc='center')
    plt.legend()
    plt.xlabel('t Values')
    plt.ylabel('y Values')
    plt.text(0.6, 0.05, errordisp)
    plt.show()
# We see the global error goes down approximately linearly, since the
# global error is halved by doubling the step size

#%% Problem 5
h = np.array([0.1, 0.1, 0.1, 0.1])
t2 = np.linspace(0, 2, 21)

u1_0 = 0
u1 = np.zeros(len(t2))
u1[0] = u1_0

u2_0 = 10 
u2 = np.zeros(len(t2))
u2[0] = u2_0

u3_0 = 0 
u3 = np.zeros(len(t2))
u3[0] = u3_0

u4_0 = 10 
u4 = np.zeros(len(t2))
u4[0] = u4_0

u0 = np.array([u1_0, u2_0, u3_0, u4_0])
u = np.array([u1, u2, u3, u4])
def du(j,uj):
    du = np.array([u[1,j], -0.1*u[1,j]-10, u[3,j], -0.1*u[3,j]-10])
    return du

for j in range(len(t2)-1):
    u[:,j+1] = u[:,j]+h*du(j,u[:,j])

plt.plot(t2,u[0,:], color = 'blue', label = 'u1')
plt.plot(t2,u[1,:], color ='red', label = 'u2')
plt.plot(t2,u[2,:], color = 'green', label ='u3')
plt.plot(t2,u[3,:], color = 'orange', label = 'u4')
plt.grid()
plt.title('System of Coupled Second-Order ODEs vs. Time')
plt.legend()
plt.text(.80,6.25,'u1 = y1 & u3 = y2')
plt.text(.70,-5.0,"u2 = y1\' & u4 = y2\'")
plt.xlabel('t')
plt.ylabel('y')
plt.show()

plt.plot(u[2,:], u[0,:])
plt.grid()
plt.title('Y2 Soln. vs. Y1 Soln')
plt.xlabel('y2')
plt.ylabel('y1')