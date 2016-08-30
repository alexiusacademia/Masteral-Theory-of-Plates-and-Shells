#-------------------------#
# Generalized Hooke's Law #
#-------------------------#

# To run this file, you must have sympy installed.
import sympy as sm

# Create variable symbols
v = sm.Symbol('[v]')              # Poison's ratio
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
Qx = sm.simplify(X[0])
Qy = sm.simplify(X[1])
print('\nMatrix M:')
sm.pprint(M)
print('\nMatrix V')
sm.pprint(V)
print('\nM*X = V, hence X = ')
print(X)
print('\nInterpretation of result:\n')
print('\nQx:')
sm.pprint(Qx)        # Print the stress at x
print('\nQy:')
sm.pprint(Qy)        # Print the stress at y
