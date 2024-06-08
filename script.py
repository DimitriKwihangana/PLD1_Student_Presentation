import numpy as np

def binomial_probability(n, p):
    probabilities = []
    for k in range(n + 1):
        binom_coeff = np.prod(np.arange(n, n - k, -1)) / np.prod(np.arange(1, k + 1))
        probability = binom_coeff * (p ** k) * ((1 - p) ** (n - k))
        probabilities.append(probability)
    return probabilities

n = 5
p = 0.5

probabilities = binomial_probability(n, p)
print(probabilities)