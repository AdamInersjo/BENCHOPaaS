from oct2py import octave

problems = ['P1aI', 'P1bI', 'P1cI', 'P1aII', 'P1bII', 'P1cII']
methods = ['COS', 'RBFFD', 'UniformGrid']

# RBFFD returns NaN for all problems.

# Add the singleMethod function to Octave
octave.addpath('./BENCHOP/BENCHOP')
S = [90, 100, 110]
K = 100
T = 1.0
r = 0.03
sig = 0.15
params = [S, K, T, r, sig]
# Execute singleMethod function, nout=2 specifies the number of return values and is required
time, relerr = octave.singleMethodWithParameters('P1aI', 'COS', params, nout=2)

print(time)
print(relerr)
