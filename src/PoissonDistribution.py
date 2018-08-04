import math


# Probability of a given number of events occurring in a fixed interval of time or space
#  if these events occur with a known constant rate and independently of the time since the last event
# Poisson of k events in interval, where lambda is the average number of events per interval:
def poisson(k, lambda_):
    return math.exp(-lambda_) * math.pow(lambda_, k) / math.factorial(k)


# E.g. probability of 2 floods in 100 years, where lambda = 1 is the average number of floods in 100 years
print poisson(2, 1)

# Probability of 3 goals in a match, where lambda = 2.5 goals in a match on average
print poisson(3, 2.5)

