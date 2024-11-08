This is a collection of problems in numerical analysis which I have solved using Python. Some of these are from school, some of them are just personal projects.
The libraries numpy, pandas, and matplotlib are used. The following files are included with brief descriptions:
  1) kepler_eqn_num_analysis.py ||
     This script solves Kepler's equation from orbital mechanics, M = E - sin(E).
     It asks for three parameters, two are properties of an eccentric orbit and the other is the number of iterations.
     The method is fixed-point iteration, but there is code which is commented out that is for Newton's method.
     I decided to put this in another script though.
  2) kepler_eqn_newton_method.py ||
     This script solves Kepler's equation using the Newton-Raphson method.
     It also asks for the same parameters as kepler_eqn_num_analysis.py
  3) math_581_hw_1.py ||
     This was the first homework for the course Numerical Methods for Differential Equations at Iowa State University.
     I will also include the pdf of the problems in the repo, but the coding only applied to 3 of the 5.
     Problem 5 is incorrect, but I have the solution in Matlab. I will get the Python fixed to actually work and post that
     as a revised version.
  4) cosine_fixed_point.py || A simple demonstration that cosine has a fixed point. It takes an input number and a specified number of iterations.
