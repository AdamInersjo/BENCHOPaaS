from oct2py import octave

problems = ['P1aI', 'P1bI', 'P1cI', 'P1aII', 'P1bII', 'P1cII']
methods = ['COS', 'RBFFD', 'UniformGrid']

# RBFFD returns NaN for all problems.

# Add the singleMethod function to Octave
octave.addpath('./BENCHOP/BENCHOP')

# Execute singleMethod function, nout=2 specifies the number of return values and is required
time, relerr = octave.singleMethod('P1aI', 'COS', nout=2)

print(time)
print(relerr)
