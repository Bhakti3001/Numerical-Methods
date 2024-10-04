"""
Author: Bhakti Patel
Class: MATH/CS 425 with Dr.Panza
Date Created: 10/04/2024
Last Edited: 10/04/2024
Purpose: This is a python file for finding roots using the modified secant method.
"""

import numpy as np

def main():
    # Lists to store roots, approximate errors, and true errors for each iteration
    roots = []
    approxE = []
    TrueE = []

    # secant method
    # f: function for which we're finding the root
    # guess 1
    # guess 2
    # sc: stopping criterion
    # trueValue: actual root if known (optional)
    def modified_secant(f, guess1, delta, sc, trueValue=None):
        iteration = 0

        # Print table headers for better visualization
        print('\n')
        print(f"{'Iteration':<12} {'Root':<15} {'Approx. Error (%)':<20} {'True Error (%)':<15}")
        print("-" * 60)

        # First iteration outside the loop to initialize the lists
        roots.append(guess1)

        # Calculate true error for the first iteration if trueValue is provided
        if trueValue is not None:
            true_error = (np.abs(trueValue - roots[-1])) / trueValue * 100
        else:
            true_error = None  # No true error if trueValue is not provided

        TrueE.append(true_error)
        approxE.append(100.0)  # Set the initial approx. error to 100%

        # Print the first iteration
        true_error_str = f"{true_error:<15.8f}" if true_error is not None else "N/A"
        print(f"{iteration:<12} {roots[-1]:<15.8f} {'100.00000000':<20} {true_error_str}")
        iteration += 1


        # Continue iterations until the stopping criterion is met
        while approxE[-1] > sc:
            x_new = guess1 - ((delta*guess1*f(guess1))/(f(guess1+delta*guess1)-f(guess1)))  # modified secant formula
            roots.append(x_new)

            # True error calculation if trueValue is provided
            if trueValue is not None:
                true_error = (np.abs(trueValue - x_new)) / trueValue * 100
            else:
                true_error = None  # No true error if trueValue is not provided
            TrueE.append(true_error)

            # Approximate error (from the second iteration onward)
            approx_error = np.abs((x_new - guess1) / x_new) * 100
            approxE.append(approx_error)

            # Print the current iteration values
            true_error_str = f"{true_error:<15.8f}" if true_error is not None else "N/A"
            print(f"{iteration:<12} {x_new:<15.8f} {approx_error:<20.8f} {true_error_str}")

            guess1 = x_new

            iteration += 1

    # Example function f(x) = your provided function
    def f(x):
        return x**4 - x - 10

    # Call the Newton-Raphson method with the function f, its derivative, stopping criterion (0.01), and initial guess (3)
    modified_secant(f,2,0.00001, 0.5)


if __name__ == "__main__":
    main()
