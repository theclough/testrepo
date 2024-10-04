# Fixed Point Iteration

import numpy as np

def fixedPt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    results = [-1]
    count = 0
    while (count <Nmax):
        count = count +1 
        try:
            x1 = f(x0)
            results += [x1]
            if (abs(x1-x0) <tol):
                xstar = x1
                ier = 0
                return [xstar,ier,results[1::]]
            x0 = x1
        except:
            print('error: ',x0)
            break
    xstar = x1
    ier = 1
    return [xstar, ier,results[1::]]