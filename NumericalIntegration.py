""" This is a script to compute the LEFT (Riemann) sum
and Simpson's Rule approximations of the area under a curve y = f(x) """

import numpy as np
import math

# define the bounding function
def f(x):
    y = math.exp(x)
    return y

def compute_LeftSum(a,b,n):
    # This function computes the left sum approximation
    # of the area bounded by f(x) and the interval [a,b]

    # width of rectangle over each subinterval
    delta_x = (b - a) / n

    # vector containing the endpoints of each subinterval
    xi_arr = np.linspace(a, b, n + 1, endpoint=True)

    # initialize the area approximation
    area_approx = 0

    # add the area of the rectangle over each subinterval
    for i in range(n):
        left_endpt = xi_arr[i]
        area_i = f(left_endpt) * delta_x
        area_approx = area_approx + area_i

    return area_approx

def compute_Simpsons(a,b,n):
    # This function computes the Simpson's rule approximation
    # of the area bounded by f(x) and the interval [a,b]

    # width of rectangle over each subinterval
    delta_x = (b - a) / n

    # vector containing the endpoints of each subinterval
    xi_arr = np.linspace(a, b, n + 1, endpoint=True)

    # vector containing the multipliers for each y_i
    # this gives an array of length n+1 called coeff_arr such that
    # coeff_arr = [1 4 2 4 2 ... 2 4 1]
    coeff_arr = np.empty((n - 1))
    coeff_arr[::2] = 4
    coeff_arr[1::2] = 2
    coeff_arr = np.append([1], coeff_arr)
    coeff_arr = np.append(coeff_arr, 1)

    # create a version of the function f that takes in vector inputs
    vectorized_f = np.vectorize(f)

    # evaluate f at the xi's
    fxi = vectorized_f(xi_arr)

    # calculate the Simpson's Rule approximation to the area under the curve
    area_approx = 0
    for i in range(len(fxi)):
        area_approx = area_approx + coeff_arr[i] * fxi[i]

    # could also compute the area approximation as a dot product of the coefficient array and the f(xi)'s, i.e.,
    # area_approx = print(np.dot(coeff_arr,fxi))

    area_approx = (delta_x / 3) * area_approx

    return area_approx


# limits of integration (a and b)
a = -2
b = 2

# number n of subintervals
n = 10

# compute the area approximations given a, b, and n
left_approx = compute_LeftSum(a,b,n)
Simpsons_approx = compute_Simpsons(a,b,n)
print('Approximations of the signed area of the region bounded by y = exp(x) over [' + str(a) + ',' + str(b) + '] with n='+str(n))
print('A) Left sum rule: ' + str(left_approx))
print('B) Simpson\'s rule: ' + str(Simpsons_approx))

