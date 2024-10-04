"""
Author: Bhakti Patel
Class: MATH/CS 425 with Dr.Panza
Date Created: 09/28/2024
Last Edited: 10/02/2024
Purpose: This is a python file for finding roots using the bisection method.
"""

import numpy as np

def main():
    # Lists to store lower bounds, upper bounds, midpoints, approximate errors, and true errors for each iteration
    lowerB = []
    upperB = []
    midpoint = []
    approxE = [] 
    TrueE = []

    # Bisection method function
    # f: the function for which we're finding the root
    # sc: stopping criterion
    # lowerBound, upperBound: initial bounds for the root
    # trueValue: the actual root if known (optional)
    def bisection(f, sc, lowerBound, upperBound, trueValue=None):
        iteration = 0

        # Print table headers
        print(f"{'Iteration':<12} {'Lower Bound':<15} {'Upper Bound':<15} {'Midpoint':<15} {'Approx. Error (%)':<20} {'True Error (%)':<15}")
        print("-" * 95)

        # First iteration outside the loop to initialize the lists
        lowerB.append(lowerBound)  # Append the initial lower bound
        upperB.append(upperBound)  # Append the initial upper bound
        mid = (lowerBound + upperBound) / 2  # Calculate the first midpoint
        midpoint.append(mid)  # Store the midpoint for the first iteration

        # Calculate true error if the true root is provided, otherwise skip
        if trueValue is not None:
            true_error = (np.abs(trueValue - mid)) / trueValue * 100  # True error calculation
        else:
            true_error = None  # No true error if trueValue is not provided
        TrueE.append(true_error)  # Store the true error or None

        # For the first iteration, approximate error is set to 100% since it's not yet defined
        approxE.append(100.0)

        # Print the first iteration values
        true_error_str = f"{true_error:<15.8f}" if true_error is not None else "N/A"
        print(f"{iteration:<12} {lowerBound:<15.8f} {upperBound:<15.8f} {mid:<15.8f} {'100.00000000':<20} {true_error_str}")

        iteration += 1  # Increment iteration count

        # Continue iterations until the stopping criterion (approximate error) is met
        while approxE[-1] > sc:
            if f(midpoint[-1]) == 0:  # If the midpoint is the root, stop
                break

            # Determine whether to update the upper or lower bound based on the function's sign
            if f(lowerBound) * f(midpoint[-1]) < 0:
                upperBound = midpoint[-1]  # Update upper bound if the root lies between lowerBound and midpoint
            else:
                lowerBound = midpoint[-1]  # Update lower bound if the root lies between midpoint and upperBound

            # Append new bounds and midpoint
            lowerB.append(lowerBound)
            upperB.append(upperBound)
            mid = (lowerBound + upperBound) / 2  # Recalculate midpoint
            midpoint.append(mid)

            # Recalculate true error if trueValue is provided
            if trueValue is not None:
                true_error = (np.abs(trueValue - mid)) / trueValue * 100
            else:
                true_error = None  # No true error if trueValue is not provided
            TrueE.append(true_error)  # Append the true error or None

            # Approximate error calculation from the difference between two midpoints
            approx_error = np.abs((midpoint[-1] - midpoint[-2]) / midpoint[-1]) * 100
            approxE.append(approx_error)

            # true error string for printing (N/A if true error is not applicable)
            true_error_str = f"{true_error:<15.8f}" if true_error is not None else "N/A"

            # Print the current iteration values
            print(f"{iteration:<12} {lowerBound:<15.8f} {upperBound:<15.8f} {mid:<15.8f} {approx_error:<20.8f} {true_error_str}")

            iteration += 1  # Increment iteration count

    # The function we're finding the root for
    def f(x):
        return 35000 * ((x*(1+x)**7)/((1+x)**7-1)) - 8500

    # Call the bisection method with the function f, a stopping criterion (0.005), and initial bounds (0.1, 0.2)
    bisection(f, 0.005, 0.1, 0.2)

if __name__ == "__main__":
    main()