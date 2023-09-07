import time
import numpy as np
import numpy.linalg as la

def driver():
# main function

    exerciseOne()
    
    exerciseTwo_Three()
    
    return

def exerciseOne():
# code for exercise 1
    
    n = 10
    x = np.linspace(0,10,n)
    
    f = lambda x: x**2 + 4*x + 2*np.exp(x)
    g = lambda x: 0*x

    y = f(x)
    w = g(x)

# evaluate the dot product of y and w     
    dp = dotProduct(y,w,n)

# print the output
    print('the dot product is : ', dp)

    return

def exerciseTwo_Three():
# code for exercises 2 and 3
    
    # Dot Product Test with np.dot()
    print(dotProduct([1,2,3,4,5],[5,4,3,2,1],5) == np.dot([1,2,3,4,5],[5,4,3,2,1]))
    
    sep()
    
    # Two by Two Test with np.matmul()
    twoByTwoTest()
    
    sep()
    
    # Larger Matrix Test with np.matmul()
    largerMatrixTest()
    
    sep()
    
    # Speed Test : 1x1 up to 10x10
    speedTest()
    
    
    
def dotProduct(x,y,n):
# function from testDot.py

    dp = 0.
    for j in range(n):
        dp = dp + x[j]*y[j]
        
    return dp

def matrixMultiply(mat1, mat2, n):
# computes matrix multiplication product 
# only needs length of one dimension (n)
# since can only multiply square matrices
    
    rmat = np.ones([n,n], dtype=int)
    
    for ii in range(n):
        for jj in range(n):
            rmat[ii,jj] = dotProduct(mat1[ii,:],mat2[:,jj],n)
    
    return rmat

def twoByTwoTest():
# tests matrixMultiply() on a two by two matrix
    
    mtrx1 = np.array([[1,2],[3,4]], dtype=int)
    mtrx2 = np.array([[3,4],[1,2]], dtype=int)
    
    rmat = matrixMultiply(mtrx1, mtrx2, 2)    
    
    print(rmat == np.matmul(mtrx1, mtrx2))
        
def largerMatrixTest():
# tests matrixMultiply() on a larger (5x5) matrix
    
    mtrx1 = np.ones([5,5], dtype=int)
    mtrx2 = np.ones([5,5], dtype=int)
    
    for ii in range(5):
        mtrx1[ii,:] = np.arange(5*ii+1,5*(ii+1)+1,1, dtype=int)
        mtrx2[ii,:] = np.arange(5*(ii+1),5*ii,-1, dtype=int)
    
    rmat = matrixMultiply(mtrx1, mtrx2, 5)
     
    print(rmat == np.matmul(mtrx1, mtrx2))
    
def speedTest():
# tests which method is faster on 10x10 matrix

    speedFunc = np.zeros(10)
    speedBuilt = np.zeros(10)

    for n in range(1,11):
        mtrx1 = np.ones([n,n], dtype=int)
        mtrx2 = np.ones([n,n], dtype=int)
        
        # using made functions
        start = time.time()
        rmat = matrixMultiply(mtrx1, mtrx2, n)
        elapse = time.time() - start
        speedFunc[n-1] = elapse
        
        # using built in functions
        start = time.time()
        rmat = np.matmul(mtrx1, mtrx2)
        elapse = time.time() - start
        speedBuilt[n-1] = elapse
   
    print('Made Funcs times (ms)     :')
    print(speedFunc[:])
    print('Built-in Funcs times (ms) :')
    print(speedBuilt[:])
    
    sep()
    
    print('Built in Funcs better, especially for larger matrices')
        
def sep():
# prints dashes to separate output
          
    print('----------------')

driver()