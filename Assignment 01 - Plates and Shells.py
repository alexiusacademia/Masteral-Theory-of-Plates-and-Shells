#-------------------------#
# Generalized Hooke's Law #
#-------------------------#
import sympy as sm
from sympy import init_printing

# Create variable symbols
v = sm.Symbol('v')              # Poison's ratio
E = sm.Symbol('E')              # Modulus of elasticity
Qx = sm.Symbol('Qx')            # for sigma x
Qy = sm.Symbol('Qy')            # for sigma y
EPx = sm.Symbol('EPx')          # for epsilon x
EPy = sm.Symbol('EPy')          # for epsilon y

""" Create list then convert to array """
# In matrix format, the general equation will be
# M.X=V 
# Applying Qz = 0 and EPz = 0
# M = |1 -v|
#     |-v 1|
# X = |Qx|
#     |Qy|
# V = |E*EPx|
#     |E*EPy|

M = sm.Matrix([[1, -v], 
               [-v, 1]])        # Create the M matrix
V = sm.Matrix([E*EPx, E*EPy])   # Create the V matrix

MInv = M**-1                    # Get the inverse matrix of M

X = MInv * V                    # Solving for the X matrix

print(sm.simplify(X[0]))        # Print the stress at x
print(sm.simplify(X[1]))        # Print the stress at y
