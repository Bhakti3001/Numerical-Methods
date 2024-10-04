"""
Author: Bhakti Patel
Class: MATH/CS 425 with Dr.Panza
Date Created: 09/28/2024
Last Edited: 10/02/2024
Purpose: This is a python file for finding roots using the false position method.
"""

import numpy as np

def main():
    # Lists to store lower bounds, upper bounds, roots, approximate errors, and true errors for each iteration
    lowerB = []
    upperB = []
    root = []
    approxE = [] 
    TrueE = []

    # False Position method function
    # f: the function for which we're finding the root
    # sc: stopping criterion
    # lowerBound, upperBound: initial bounds for the root
    # trueValue: the actual root if known (optional)
    def falsePosition(f, sc, lowerBound, upperBound, trueValue=None):
        iteration = 0

        # Print table headers
        print('\n')
        print(f"{'Iteration':<12} {'Lower Bound':<15} {'Upper Bound':<15} {'Root':<15} {'Approx. Error (%)':<20} {'True Error (%)':<15}")
        print("-" * 95)

        # First iteration: Initialize the lower bound, upper bound, and calculate the initial root
        lowerB.append(lowerBound)
        upperB.append(upperBound)
        # False Position formula to calculate the first root
        rootB = upperBound - ((f(upperBound)*(lowerBound-upperBound))/(f(lowerBound)-f(upperBound)))
        root.append(rootB)

        # Calculate true error for the first root if trueValue is provided
        if trueValue is not None:
            true_error = (np.abs(trueValue - rootB)) / trueValue * 100  # True error calculation
        else:
            true_error = None  # No true error if trueValue is not provided
        TrueE.append(true_error)

        # For the first iteration, approximate error is set to 100% since it's not yet defined
        approxE.append(100.0)

        # Print the first iteration's values
        true_error_str = f"{true_error:<15.8f}" if true_error is not None else "N/A"
        print(f"{iteration:<12} {lowerBound:<15.8f} {upperBound:<15.8f} {rootB:<15.8f} {'100.00000000':<20} {true_error_str}")
        iteration += 1  # Increment iteration count

        # Continue iterations until the stopping criterion is met
        while approxE[-1] > sc:
            if f(rootB) == 0:  # If the root is found exactly, stop
                break

            # Update the bounds based on the sign of the function at the root
            if f(lowerBound) * f(rootB) < 0:
                upperBound = rootB  # Root lies between lowerBound and rootB, so update upperBound
            else:
                lowerBound = rootB  # Root lies between rootB and upperBound, so update lowerBound

            # Append the updated bounds to the lists
            lowerB.append(lowerBound)
            upperB.append(upperBound)

            # Recalculate the root using the False Position formula
            rootB = upperBound - ((f(upperBound)*(lowerBound-upperBound))/(f(lowerBound)-f(upperBound)))
            root.append(rootB)

            # True error calculation if trueValue is provided
            if trueValue is not None:
                true_error = (np.abs(trueValue - rootB)) / trueValue * 100
            else:
                true_error = None  # No true error if trueValue is not provided
            TrueE.append(true_error)

            # Approximate error calculation based on the difference between roots
            approx_error = np.abs((root[-1] - root[-2]) / root[-1]) * 100
            approxE.append(approx_error)

            # true error string for printing
            true_error_str = f"{true_error:<15.8f}" if true_error is not None else "N/A"

            # Print the current iteration's values
            print(f"{iteration:<12} {lowerBound:<15.8f} {upperBound:<15.8f} {rootB:<15.8f} {approx_error:<20.8f} {true_error_str}")

            iteration += 1  # Increment iteration count

    # The function we're finding the root for
    def f(x):
        return 35000 * ((x*(1+x)**7)/((1+x)**7-1)) - 8500

    # Call the falsePosition method with the function f, stopping criterion (0.005), and initial bounds (0.1, 0.2)
    falsePosition(f, 0.005, 0.1, 0.2)


if __name__ == "__main__":
    main()
