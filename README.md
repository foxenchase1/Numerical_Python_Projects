This is a collection of problems in numerical analysis which I have solved using Python. Some of these are from school, some of them are just personal projects.
The libraries numpy, pandas, and matplotlib are used. The following files are included with brief descriptions:
  1) kepler_eqn_num_analysis.py
     This script solves Kepler's equation from orbital mechanics, M = E - sin(E).
     It asks for three parameters, two are properties of an eccentric orbit and the other is the number of iterations.
     The method is fixed-point iteration, but there is code which is commented out that is for Newton's method. I decided to put this in another script though.
  2) kepler_eqn_newton_method.py
     This script solves Kepler's equation using the Newton-Raphson method. It also asks for the same parameters as kepler_eqn_num_analysis.py
  
