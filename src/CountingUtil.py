import math


# Compute n-choose-k = number of combinations of choosing k amidst n
def combinations_count(k, n):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

