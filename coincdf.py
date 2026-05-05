import scipy.stats as stats

# calculate the probabillity
prob = 1 - stats.binom.cdf(6,10,0.5)
print("the probabillity of gettting more than 6 heads in 10 coin flips:", prob)