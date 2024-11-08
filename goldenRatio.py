"""
Author: Bhakti Patel
Class: MATH/CS 425 with Dr.Panza
Date Created: 11/08/2024
Last Edited: 11/08/2024
Purpose: This is a python file for finding minimum using the golden ratio method.
"""

import numpy as np

# Golden ratio constant
phi = (1 + np.sqrt(5)) / 2  # Approximately 1.61803398875

def main():
    # List to store approximate errors for each iteration
    approxE = []

    # Golden Ratio method to find the minimum of the function
    # f: function for which we're finding the minimum
    # sc: stopping criterion
    # xL, xU: initial interval with a single minimum
    def golden_ratio(f, xL, xU, sc):
        d = (phi - 1) * (xU - xL)
        x1 = xL + d
        x2 = xU - d

        # Print table headers for better visualization
        print('\n')
        print(f"{'xL':<15} {'f(xL)':<15} {'x2':<15} {'f(x2)':<15} {'x1':<15} {'f(x1)':<15} {'xU':<15} {'f(xU)':<15} {'d':<15} {'Error (%)':<15}")
        print("-" * 155)

        # Print the first iteration values with five decimal places
        initial_error = 100.00000
        print(f"{xL:<15.5f} {f(xL):<15.5f} {x2:<15.5f} {f(x2):<15.5f} {x1:<15.5f} {f(x1):<15.5f} {xU:<15.5f} {f(xU):<15.5f} {d:<15.5f} {initial_error:<15.5f}")

        approxE.append(initial_error)

        # Loop until the approximate error meets the stopping criterion
        while approxE[-1] > sc:
            f_x1 = f(x1)
            f_x2 = f(x2)

            # Determine which side of the interval to eliminate
            if f_x1 < f_x2:
                xL = x2
                x2 = x1
                d = (phi - 1) * (xU - xL)
                x1 = xL + d
            else:
                xU = x1
                x1 = x2
                d = (phi - 1) * (xU - xL)
                x2 = xU - d

            # Calculate the minimum estimate and approximate error
            xEST = (x1 + x2) / 2  # Estimated minimum
            approx_error = (2 - phi) * np.abs((xU - xL) / xEST) * 100
            approxE.append(approx_error)

            # Print the current iteration values with five decimal places
            print(f"{xL:<15.5f} {f(xL):<15.5f} {x2:<15.5f} {f(x2):<15.5f} {x1:<15.5f} {f(x1):<15.5f} {xU:<15.5f} {f(xU):<15.5f} {d:<15.5f} {approx_error:<15.5f}")

    # Example function for finding the minimum (replace with your function)
    def f(x):
        return 3 + 6*x + 5*x**2 + 3*x**3 + 4*x**4  # Example function with a minimum

    # Call the Golden Ratio method with the function f, initial interval, and stopping criterion
    golden_ratio(f, -2, 1, 1)

if __name__ == "__main__":
    main()
