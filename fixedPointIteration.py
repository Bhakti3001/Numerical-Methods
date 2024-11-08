"""
Author: Bhakti Patel
Class: MATH/CS 425 with Dr.Panza
Date Created: 10/01/2024
Last Edited: 10/02/2024
Purpose: This is a python file for finding roots using the fixed point method.
"""

import numpy as np

def main():
    # List to store roots, approximate errors, and true errors for each iteration
    roots = []
    approxE = []
    TrueE = []

    # Fixed-Point Iteration method
    # g: rearranged equation x = g(x)
    # sc: stopping criterion
    # initial_guess: starting point for iteration
    # trueValue: actual root if known (optional)
    def fixedPointIteration(g, sc, initial_guess, trueValue=None):
        iteration = 0
        x = initial_guess  # Starting point for the iteration

        # Print table headers for better visualization
        print('\n')
        print(f"{'Iteration':<12} {'Root':<15} {'Approx. Error (%)':<20} {'True Error (%)':<15}")
        print("-" * 60)

        # First iteration outside the loop to initialize the lists
        roots.append(x)

        # Calculate true error for the first iteration if trueValue is provided
        if trueValue is not None:
            true_error = (np.abs(trueValue - x)) / trueValue * 100
        else:
            true_error = None  # No true error if trueValue is not provided

        TrueE.append(true_error)
        approxE.append(100.0)  # Set the initial approx. error to 100%

        # Print the first iteration
        true_error_str = f"{true_error:<15.8f}" if true_error is not None else "N/A"
        print(f"{iteration:<12} {x:<15.8f} {'100.00000000':<20} {true_error_str}")
        iteration += 1

        # Continue iterations until the stopping criterion is met
        while approxE[-1] > sc:
            x_new = g(x)  # Apply the iteration formula g(x)
            roots.append(x_new)

            # True error calculation if trueValue is provided
            if trueValue is not None:
                true_error = (np.abs(trueValue - x_new)) / trueValue * 100
            else:
                true_error = None  # No true error if trueValue is not provided
            TrueE.append(true_error)

            # Approximate error (from the second iteration onward)
            approx_error = np.abs((x_new - x) / x_new) * 100
            approxE.append(approx_error)

            # Print the current iteration values
            true_error_str = f"{true_error:<15.8f}" if true_error is not None else "N/A"
            print(f"{iteration:<12} {x_new:<15.8f} {approx_error:<20.8f} {true_error_str}")

            x = x_new  # Update x for the next iteration
            iteration += 1

    # Example g(x) = rearranged equation
    def g(x):
        return (x+10)/(x+1)

    # Call the fixed-point iteration with the function g, stopping criterion (0.01), and initial guess (3)
    fixedPointIteration(g, 0.1, 3)


if __name__ == "__main__":
    main()