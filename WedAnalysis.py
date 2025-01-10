import numpy as np
from scipy.stats import chisquare

# Observed number of queries for each hour on Wednesday
observed_queries_wednesday = [
    3, 5, 4, 3, 4, 7, 11, 3, 1, 13, 7, 4, 6, 4, 8, 7, 11, 7, 19
]

# Total queries and expected distribution assuming uniformity
total_queries_wednesday = sum(observed_queries_wednesday)
expected_queries_wednesday = [total_queries_wednesday / len(observed_queries_wednesday)] * len(observed_queries_wednesday)

# Perform the Chi-Square test
chi2_stat_wednesday, p_value_wednesday = chisquare(f_obs=observed_queries_wednesday, f_exp=expected_queries_wednesday)

# Significance level
alpha = 0.05

# Print results
print(f"Chi-Square Statistic: {chi2_stat_wednesday}")
print(f"P-Value: {p_value_wednesday}")

if p_value_wednesday < alpha:
    print("Reject the null hypothesis: The queries are not uniformly distributed across the day.")
else:
    print("Fail to reject the null hypothesis: The queries are uniformly distributed across the day.")
