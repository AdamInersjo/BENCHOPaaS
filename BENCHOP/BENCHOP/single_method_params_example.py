'''Essentially the same as the other example, but calling
    singleMethodWithParms.m with parameters defined in python
    instead.'''

from oct2py import octave

problems = ['P1aI', 'P1bI', 'P1cI', 'P1aII', 'P1bII', 'P1cII']
methods = ['COS', 'RBFFD', 'UniformGrid']

# RBFFD returns NaN for all problems.

# Add the singleMethod function to Octave
octave.addpath('./BENCHOP/BENCHOP') #Warns, and works without this anyways? /Patrik

#Define parameters, these are standard for P1*I
#(Look in singleMethod.m under the P1*II problems for their params )
S = [90, 100, 110]
K = 100
T = 1.0
r = 0.03
sig = 0.15
params = [S, K, T, r, sig]


time, relerr = octave.singleMethodWithParams('P1aI', 'COS', params, nout=2)
print('aI with params')
print(time)
print(relerr)
