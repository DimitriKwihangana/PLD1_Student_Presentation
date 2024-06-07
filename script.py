import numpy as np

# Parameters
n = 10
p = 0.3

# Function to compute binomial probability
def binomial_probability(n, k, p):
    binom_coeff = np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n - k))
    return binom_coeff * (p ** k) * ((1 - p) ** (n - k))

# Compute probabilities for all possible number of successes
probabilities = [binomial_probability(n, k, p) for k in range(n + 1)]

probabilities
