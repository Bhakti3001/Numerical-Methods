"""
Author: Bhakti Patel
Class: MATH/CS 425 with Dr.Panza
Date Created: 10/04/2024
Last Edited: 10/19/2024
Purpose: This is a python file for finding roots using the secant method.
"""

import numpy as np

def main():
    # Lists to store roots, approximate errors, and true errors for each iteration
    x_prev_table = []  # Previous x values
    x_curr_table = []  # Current x values
    approxE_table = []  # Approximate errors
    TrueE_table = []  # True errors

    def secant(f, x_prev, x_curr, sc, trueValue=None):
        iteration = 0

        # Print table headers for better visualization
        print('\n')
        print(f"{'Iteration':<12} {'fx_(i)':<15} {'fx_(i+1)':<15} {'E_a':<20} {'E_t':<20}")
        print("-" * 80)

        # Initialize the first iteration with the provided guesses
        x_prev_table.append(x_prev)  # x_prev
        x_curr_table.append(x_curr)  # x_curr

        # Set initial approximate error
        approxE_table.append(100.0)

        # Calculate true error for the first guess if trueValue is provided
        true_error = (np.abs(trueValue - x_prev_table[0]) / trueValue * 100) if trueValue is not None else None
        TrueE_table.append(true_error)

        # Print the first iteration
        print(f"{iteration:<12} {x_prev_table[-1]:<15.6f} {x_curr_table[-1]:<15.6f} {approxE_table[-1]:<20.6f} {TrueE_table[-1]:<20.6f}")
        iteration += 1

        # Continue iterations until the stopping criterion is met
        while approxE_table[-1] > sc:
            # Calculate new root using the secant formula
            x_new = x_curr - ((f(x_curr) * (x_prev - x_curr)) / (f(x_prev) - f(x_curr)))
            x_prev_table.append(x_curr)  # Update previous x value
            x_curr_table.append(x_new)  # Update current x value

            # Approximate error (from the second iteration onward)
            approx_error = np.abs((x_new - x_curr) / x_new) * 100
            approxE_table.append(approx_error)

            # Calculate true error if trueValue is provided
            if trueValue is not None:
                true_error = (np.abs(trueValue - x_new) / trueValue) * 100
                TrueE_table.append(true_error)

            # Print the current iteration values
            true_error_str = f"{true_error:<20.6f}" if trueValue is not None else "N/A"
            print(f"{iteration:<12} {x_curr:<15.6f} {x_new:<15.6f} {approxE_table[-1]:<20.6f} {TrueE_table[-1]:<20.6f}")

            x_prev = x_curr  # Update for the next iteration
            x_curr = x_new
            iteration += 1

    def f(x):
        return np.tan(np.pi*x/5)-2

    # Call the secant method with the function f, initial guesses, and stopping criterion
    secant(f, 1, 2, 0.1, 1.762081911747834)

if __name__ == "__main__":
    main()
