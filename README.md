# PLD 1 Machine Learning: Binomial Distribution

## Overview

This task involves understanding and calculating the binomial distribution using only NumPy in Python. The binomial distribution is a discrete probability distribution that describes the number of successes in a fixed number of independent trials of a binary experiment.

## Binomial Distribution

The binomial distribution is used to model the number of successes in a fixed number of trials, each with the same probability of success. The formula for the binomial probability mass function is:

\[ P(X = k) = \binom{n}{k} \cdot p^k \cdot (1 - p)^{n - k} \]

Where:
- \( P(X = k) \) is the probability of getting exactly \( k \) successes in \( n \) trials.
- \( n \) is the total number of trials.
- \( k \) is the number of successes.
- \( p \) is the probability of success on a single trial.
- \( \binom{n}{k} \) is the binomial coefficient, calculated as \( \frac{n!}{k!(n - k)!} \).

## Task Description

In this task, we will:
1. Calculate the binomial probabilities for a given number of trials (`n`) and probability of success (`p`) using only NumPy.

## Code Explanation

### Import Library

We use `numpy` for numerical computations.

```python
import numpy as np

Define Parameters

Set the parameters for the binomial distribution:

n: Total number of trials.
p: Probability of success in each trial.
n = 5
p = 0.5

Calculate Binomial Probabilities
Define a function to calculate probabilities for each number of successes from 0 to n:
def binomial_probability(n, p):
    probabilities = []
    for k in range(n + 1):
        binom_coeff = np.prod(np.arange(n, n - k, -1)) / np.prod(np.arange(1, k + 1))
        probability = binom_coeff * (p ** k) * ((1 - p) ** (n - k))
        probabilities.append(probability)
    return probabilities

Compute Probabilities
Compute and print the probabilities:
probabilities = binomial_probability(n, p)
print(probabilities)
```

## Summary

We were able to demonstrate using numpy only how binomial distribution is calculuted in this task. Understanding the binomial distribution helps us model and analyze scenarios with binary outcomes, which is very important in machine learning applications.


