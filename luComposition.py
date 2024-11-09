"""
Author: Bhakti Patel
Class: MATH/CS 425 with Dr. Panza
Date Created: 11/08/2024
Last Edited: 11/08/2024
Purpose: This is a Python file implementing the LU decomposition method for finding roots.
"""


import numpy as np

def lu_decomposition(A):
    """
    Performs LU decomposition of a square matrix A such that A = L * U.
    L is a lower triangular matrix, U is an upper triangular matrix.

    Parameters:
    A (2D array): Coefficient matrix (must be square).

    Returns:
    L, U (2D arrays): Lower and Upper triangular matrices.
    """
    n = len(A)
    L = np.zeros_like(A, dtype=float)
    U = np.zeros_like(A, dtype=float)

    for i in range(n):
        # Upper triangular matrix U
        for j in range(i, n):
            sum_ = 0
            for k in range(i):
                sum_ += L[i, k] * U[k, j]
            U[i, j] = A[i, j] - sum_

        # Lower triangular matrix L
        for j in range(i + 1, n):
            sum_ = 0
            for k in range(i):
                sum_ += L[j, k] * U[k, i]
            L[j, i] = (A[j, i] - sum_) / U[i, i]

        # Set diagonal elements of L to 1
        L[i, i] = 1

    return L, U

def forward_substitution(L, b):
    """
    Solves Ld = b using forward substitution.

    Parameters:
    L (2D array): Lower triangular matrix.
    b (1D array): Constants vector.

    Returns:
    d (1D array): Solution vector.
    """
    n = len(b)
    d = np.zeros_like(b, dtype=float)

    for i in range(n):
        sum_ = 0
        for j in range(i):
            sum_ += L[i, j] * d[j]
        d[i] = b[i] - sum_

    return d

def backward_substitution(U, d):
    """
    Solves Ux = d using backward substitution.

    Parameters:
    U (2D array): Upper triangular matrix.
    d (1D array): Solution vector from forward substitution.

    Returns:
    x (1D array): Solution vector.
    """
    n = len(d)
    x = np.zeros_like(d, dtype=float)

    for i in range(n - 1, -1, -1):
        sum_ = 0
        for j in range(i + 1, n):
            sum_ += U[i, j] * x[j]
        x[i] = (d[i] - sum_) / U[i, i]

    return x

def main():
    # Example usage for a 3x3 system
    A = np.array([[2, -6, -1], [-3, -1, 7], [-8, 1, -2]], dtype=float)
    b = np.array([-38, -34, -20], dtype=float)

    # Perform LU decomposition
    L, U = lu_decomposition(A)

    # Print L and U matrices
    print("Lower triangular matrix L:")
    print(np.round(L, 5))
    print("\nUpper triangular matrix U:")
    print(np.round(U, 5))

    # Solve Ld = b for d using forward substitution
    d = forward_substitution(L, b)

    # Solve Ux = d for x using backward substitution
    x = backward_substitution(U, d)

    # Print the solution
    print("\nSolution for the variables:")
    print(np.round(x, 5))

if __name__ == "__main__":
    main()
