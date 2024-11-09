"""
Author: Bhakti Patel
Class: MATH/CS 425 with Dr. Panza
Date Created: 11/08/2024
Last Edited: 11/08/2024
Purpose: This is a Python file for finding roots in a system of equations using Cramer's Rule.
"""

import numpy as np

def cramer_rule(A, b):
    """
    Solve the system of linear equations AX = B using Cramer's Rule.

    Parameters:
    A (2D array): Coefficient matrix (must be square).
    b (1D array): Constants vector.
    """
    # Calculate the determinant of the coefficient matrix
    det_A = np.linalg.det(A)
    if det_A == 0:
        print("The system has no unique solution.")
        return

    n = len(b)
    solution = np.zeros(n)

    # Calculate the determinant for each modified matrix A_i
    for i in range(n):
        # Create a copy of A and replace the i-th column with B
        A_i = np.copy(A)
        A_i[:, i] = b
        det_A_i = np.linalg.det(A_i)

        # Compute the solution for x_i using Cramer's Rule
        solution[i] = det_A_i / det_A

    # Print A, b, and the computed solution with each value rounded to five decimals
    print("\nCoefficient matrix A:\n")
    print(np.round(A, 5))
    print("\nConstant vector b:\n")
    print(np.round(b, 5))
    print("\nSolution for the variables:\n")
    print(np.round(solution, 5))

def main():
    # Example usage for a 3x3 system
    A = np.array([[2, -6, -1], [-3, -1, 7], [-8, 1, -2]])
    b = np.array([-38, -34, -20])

    cramer_rule(A, b)

if __name__ == "__main__":
    main()
