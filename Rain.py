import scipy.stats as stats

# expected value = 10 obsrving value  6
prob1 = stats.poisson.pmf(6,10)
print("Probabilllity of raining for exactly 6 days:", prob1)

# expected value = 10 probabillity of observing 12-14
prob2 = stats.poisson.pmf(12,10) + stats.poisson.pmf(13,10) + stats.poisson.pmf(14,10)

print("probabillity of raining for 12-14 days:", prob2)