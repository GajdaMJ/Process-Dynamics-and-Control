import numpy as np
from scipy.signal import residue
from sympy import symbols, inverse_laplace_transform, exp

# Define the numerator and denominator coefficients of the transfer function
numerator = [2]  # Coefficient of the numerator
denominator = [1, 5, 9, 7, 2]  # Coefficients of the denominator (expanded form of (s+1)^3 * (s+2))

# Perform partial fraction decomposition
residues, poles, direct_terms = residue(numerator, denominator)

# Define the Laplace variable and time variable
s, t = symbols('s t')

# Calculate the inverse Laplace transform for each term
inverse_laplace_terms = []
for residue, pole in zip(residues, poles):
    term = residue / (s - pole)
    inverse_term = inverse_laplace_transform(term, s, t)
    inverse_laplace_terms.append(inverse_term)

# Sum the inverse Laplace terms
inverse_laplace_result = sum(inverse_laplace_terms)

# Print the results
print("Inverse Laplace Transform:", inverse_laplace_result)