import math
import CountingUtil


# Probability of k success in n trials given success probability p, following Binomial distribution
def k_success(k, n, p):
    return CountingUtil.combinations_count(k, n) * math.pow(p, k) * math.pow(1 - p, n - k)


print k_success(2, 3, 0.5)

