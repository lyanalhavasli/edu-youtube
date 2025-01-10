import numpy as np
from scipy.stats import chisquare

# Observed number of queries for each hour (22 hours in this case)
observed_queries = [
    3, 14, 21, 13, 14, 2, 3, 7, 4, 3, 2, 2,
    1, 1, 2, 11, 5, 9, 27, 5, 16, 17
]

# Total queries and expected distribution assuming uniformity
total_queries = sum(observed_queries)
expected_queries = [total_queries / len(observed_queries)] * len(observed_queries)  # Match lengths to 22

# Perform the Chi-Square test
chi2_stat, p_value = chisquare(f_obs=observed_queries, f_exp=expected_queries)

# Significance level
alpha = 0.05

# Print results
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"P-Value: {p_value}")

if p_value < alpha:
    print("Reject the null hypothesis: The queries are not uniformly distributed across the day.")
else:
    print("Fail to reject the null hypothesis: The queries are uniformly distributed across the day.")
