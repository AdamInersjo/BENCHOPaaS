from oct2py import octave

probs1 = ['P1aI', 'P1bI', 'P1cI']
probs2 = ['P1aII', 'P1bII', 'P1cII']
methods = ['COS', 'RBFFD', 'UniformGrid']

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

for prob in probs1:
    for method in methods:
        time, relerr = octave.singleMethodWithParams(prob, method, params, nout=2)
        print(prob, method, 'withparams')
        print(time, relerr)
        time, relerr = octave.singleMethod(prob, method, nout=2)
        print(prob, method, 'noparams')
        print(time, relerr)

print('*** Problems II ***')
S = [97, 98, 99]
K = 100
T = 0.25
r = 0.1
sig = 0.01
params = [S, K, T, r, sig]

for prob in probs2:
    for method in methods:
        time, relerr = octave.singleMethodWithParams(prob, method, params, nout=2)
        print(prob, method, 'withparams')
        print(time, relerr)
        time, relerr = octave.singleMethod(prob, method, nout=2)
        print(prob, method, 'noparams')
        print(time, relerr)

