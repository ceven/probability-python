import math
import CountingUtil


# Probability of observing the kth success on the nth trial
# = probability of succeeding (k-1) times during (n-1) first trials * prob of succeeding nth trial
def negative_binomial(k, n, p):
    return CountingUtil.combinations_count(k-1, n-1) * math.pow(p, k-1) * math.pow(1-p, n-k) * p

