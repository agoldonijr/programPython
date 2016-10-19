# -*- coding: utf-8 -*-
#
# LU.py - LU decomposition (by Croud method) for solve linear system
#
#
# Autor: Pedro Garcia Freitas <sawp@sawp.com.br>
# License: Creative Commons
#      <http://creativecommons.org/licenses/by-nc-nd/2.5/br/>
#

from math import fabs, sqrt, exp, pi, sin, cos, log
from pprint import pprint
import sys


def LU(A, b):
    """
    Return a list with the solution of linear system.

    LU(A, b)

    INPUT:
    * A: a matrix of coefficients
    * b: a list, relative a vector of independent terms

    return: a list with all unknown variables of system.

    Author: Pedro Garcia <sawp@sawp.com.br>
    see: http://www.sawp.com.br

    License: Creative Commons
             http://creativecommons.org/licenses/by-nc-nd/2.5/br/

    Mar 2010
    """

    def pivot(A, k):
        n = len(b)
        p = k
        bigger = abs(A[k][k])
        for i in xrange(k+1, n):
            sentinel = abs(A[i][k])
            if (sentinel > bigger):
                bigger = sentinel
                p = i
        if p != k:
            for i in xrange(k, n):
                (A[p][i], A[k][i]) = (A[k][i], A[p][i])
        return A

    def crout_decomposition(M):
        """ Perform the Crout-based algorithm for decomposition the matriz
        A in two L and U using the Croud's Method.
        """
        n = len(M)
        L = [[0.0 for i in xrange(n)] for j in xrange(n)]
        U = [[0.0 for i in xrange(n)] for j in xrange(n)]

        for j in xrange(n):
            U[0][j] = M[0][j]
        for i in xrange(n):
            L[i][0] = M[i][0]/U[0][0]

        for i in xrange(n):
            # Calculate L
            for j in xrange(i+1):
                suma = 0.0
                for k in xrange(j):
                    suma += L[i][k] * U[k][j]
                L[i][j] = M[i][j] - suma

            # Calculate U
            for j in xrange(i, n):
                suma = 0.0
                for k in xrange(i):
                    suma += L[i][k] * U[k][j]
                U[i][j] = (M[i][j] - suma)/L[i][i]
        return (L, U)

    def solveLU(A, b):
        n = len(b)
        y = [0.0 for i in xrange(n)]
        x = [0.0 for i in xrange(n)]
        (L, U) = crout_decomposition(A)

        # Step 1: Solve the L system: L * y = b
        y[0] = b[0]/L[0][0]
        for i in xrange(1, n):
            suma = 0.0
            for j in xrange(i):
                suma += L[i][j] * y[j]
            y[i] = (b[i] - suma)/L[i][i]

        # Step 2: Solve the U system: U * x = y (regressive replacement)
        x[n-1] = y[n-1]/U[n-1][n-1]
        for i in xrange(n-1, -1, -1):
            suma = y[i]
            for j in xrange(i+1, n):
                suma = suma - U[i][j] * x[j]
            x[i] = suma/U[i][i]
        return x

    # Function body
    return solveLU(A, b)

if __name__ == "__main__":
    #mat = [[10, 1, 1, 2, 3, -2],
    #        [4, -20, 3, 2, -1, 7],
    #        [5, -3, 15, -1, -4, 1],
    #        [-1, 1, 2, 8, -1, 2],
    #        [1, 2, 1, 3, 9, -1],
    #        [4, 3, 1, 2, -1, 12]]
    #b = [6.570, -68.448, -112.05, -3.968, -2.180, 10.882]
    mat = [	[2,2,1], 
		[1,1,1],
		[3,2,1]]
    b = [-18, -40,-26]

    print ("The soluction of linear system is: ")
    print LU(mat, b)
