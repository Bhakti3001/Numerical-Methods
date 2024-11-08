"""
Author: Bhakti Patel
Class: MATH/CS 425 with Dr.Panza
Date Created: 11/08/2024
Last Edited: 11/08/2024
Purpose: This is a python file for finding minimum using the parabolic interpolation method.
"""
import numpy as np

def main():
    # List to store approximate errors for each iteration
    approxE = []

    # Parabolic Interpolation method to find the minimum of the function
    # f: function for which we're finding the minimum
    # sc: stopping criterion
    # x1, x2, x3: initial interval with three points
    def parabolic_interpolation(f, x1, x2, x3, sc):
        iteration = 0

        # Print table headers for better visualization
        print('\n')
        print(f"{'x1':<15} {'f(x1)':<15} {'x2':<15} {'f(x2)':<15} {'x3':<15} {'f(x3)':<15} {'x4':<15} {'f(x4)':<15} {'Error (%)':<15}")
        print("-" * 155)

        # Calculate the first parabolic interpolation estimate
        def parabolic_estimate(x1, x2, x3):
            return x2 - 0.5*( (((x2-x1)**2)*(f(x2)-f(x3))-((x2-x3)**2)*(f(x2)-f(x1)))/(((x2-x1))*(f(x2)-f(x3))-((x2-x3))*(f(x2)-f(x1))))

        # Initial estimate for x4
        x4 = parabolic_estimate(x1, x2, x3)
        
        # Calculate the first approximate error
        approx_error = 100.0  # initial error
        approxE.append(approx_error)

        # Print first iteration values
        print(f"{x1:<15.5f} {f(x1):<15.5f} {x2:<15.5f} {f(x2):<15.5f} {x3:<15.5f} {f(x3):<15.5f} {x4:<15.5f} {f(x4):<15.5f} {approx_error:<15.5f}")
        
        iteration += 1

        # Loop until the approximate error meets the stopping criterion
        while approxE[-1] > sc:
            # Check the condition for updating x1, x2, and x3
            if f(x4) < f(x2) and x4 > x2:
                x1 = x2
                x2 = x4
            elif f(x4) < f(x2) and x4 < x2:
                x3 = x2
                x2 = x4
            else:
                print("Search failed, f(x4) > f(x2)")
                break  # If the search fails, break the loop

            # Recalculate the parabolic estimate for the next x4
            x4 = parabolic_estimate(x1, x2, x3)

            # Calculate the approximate error
            approx_error = np.abs((x4 - x2) / x4) * 100  # Error as a percentage
            approxE.append(approx_error)

            # Print the current iteration values
            print(f"{x1:<15.5f} {f(x1):<15.5f} {x2:<15.5f} {f(x2):<15.5f} {x3:<15.5f} {f(x3):<15.5f} {x4:<15.5f} {f(x4):<15.5f} {approx_error:<15.5f}")

            iteration += 1

    # Example function for finding the minimum (replace with your function)
    def f(x):
        return 3 + 6*x + 5*x**2 + 3*x**3 + 4*x**4  # Example function with a minimum

    # Call the Parabolic Interpolation method with the function f, initial interval, and stopping criterion
    parabolic_interpolation(f, -1, -0.75, 0, 1) 

if __name__ == "__main__":
    main()
