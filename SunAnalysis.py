import numpy as np
from scipy.stats import chisquare

# Observed number of queries for each hour on Sunday
observed_queries_sunday = [
    10, 12, 7, 7, 8, 3, 2, 1, 3, 2, 6, 2, 3, 7, 2, 1, 1
]

# Total queries and expected distribution assuming uniformity
total_queries_sunday = sum(observed_queries_sunday)
expected_queries_sunday = [total_queries_sunday / len(observed_queries_sunday)] * len(observed_queries_sunday)

# Perform the Chi-Square test
chi2_stat_sunday, p_value_sunday = chisquare(f_obs=observed_queries_sunday, f_exp=expected_queries_sunday)

# Significance level
alpha = 0.05

# Print results
print(f"Chi-Square Statistic: {chi2_stat_sunday}")
print(f"P-Value: {p_value_sunday}")

if p_value_sunday < alpha:
    print("Reject the null hypothesis: The queries are not uniformly distributed across the day.")
else:
    print("Fail to reject the null hypothesis: The queries are uniformly distributed across the day.")
