"""
Author: Bhakti Patel
Class: MATH/CS 425 with Dr. Panza
Date Created: 11/08/2024
Last Edited: 11/08/2024
Purpose: This is a Python file implementing the Naive Gauss Elimination method with operation counts for additions/subtractions and multiplications/divisions.
"""

import numpy as np

def naive_gauss_elimination(A, b):
    """
    Solve the system of linear equations AX = B using the Naive Gauss Elimination method.

    Parameters:
    A (2D array): Coefficient matrix (must be square).
    b (1D array): Constants vector.

    Returns:
    x (1D array): Solution vector if the system has a unique solution.
    """
    n = len(b)
    # Initialize counters for operations
    add_sub_count = 0
    mul_div_count = 0

    # Forward elimination to convert A to upper triangular form
    for k in range(n - 1):
        for i in range(k + 1, n):
            if A[k, k] == 0:
                raise ValueError("Zero pivot encountered. This method cannot handle it.")
            factor = A[i, k] / A[k, k]

            # Update row i in matrix A and vector b
            for j in range(k, n):
                A[i, j] -= factor * A[k, j]
                add_sub_count += 1  # Subtraction for row update
                mul_div_count += 1  # Multiplication for factor * A[k, j]

            b[i] -= factor * b[k]
            #add_sub_count += 1  # Subtraction in b update
            mul_div_count += 1  # Multiplication for factor * b[k]

    # Back substitution to solve for the unknowns
    x = np.zeros(n)
    x[-1] = b[-1] / A[-1, -1]
    mul_div_count += 1  # Division for solving the last variable

    for i in range(n - 2, -1, -1):
        # Start with b[i] as the initial value for x[i]
        x[i] = b[i]

        # Accumulate the subtraction of A[i, j] * x[j] directly into x[i]
        for j in range(i + 1, n):
            x[i] -= A[i, j] * x[j]
            mul_div_count += 1  # Multiplication for each A[i, j] * x[j]
            add_sub_count += 1  # Subtraction for x[i] -= A[i, j] * x[j]

        # Divide by A[i, i] to finalize x[i]
        x[i] /= A[i, i]
        mul_div_count += 1  # Division for solving x[i]

    print("\nSolution for the variables:")
    print(np.round(x, 5))
    print("\nNumber of additions/subtractions:", add_sub_count)
    print("Number of multiplications/divisions:", mul_div_count)

def main():
    # Example usage for a 3x3 system
    A = np.array([[2, -6, -1], [-3, -1, 7], [-8, 1, -2]], dtype=float)
    b = np.array([-38, -34, -20], dtype=float)

    naive_gauss_elimination(A, b)

if __name__ == "__main__":
    main()
