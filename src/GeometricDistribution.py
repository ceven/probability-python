import math


# Probability of success at kth trial given success probability p, following Binomial distribution
def success_at_k_trial(k, p):
    return math.pow(1-p, k-1) * p


print success_at_k_trial(6, 1.0/6)

