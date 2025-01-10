import numpy as np
from scipy.stats import chisquare

# Observed number of queries for each hour on Tuesday
observed_queries_tuesday = [
    7, 13, 4, 16, 4, 13, 7, 6, 12, 23, 4, 5, 9, 7, 3, 14, 10
]

# Total queries and expected distribution assuming uniformity
total_queries_tuesday = sum(observed_queries_tuesday)
expected_queries_tuesday = [total_queries_tuesday / len(observed_queries_tuesday)] * len(observed_queries_tuesday)

# Perform the Chi-Square test
chi2_stat_tuesday, p_value_tuesday = chisquare(f_obs=observed_queries_tuesday, f_exp=expected_queries_tuesday)

# Significance level
alpha = 0.05

# Print results
print(f"Chi-Square Statistic: {chi2_stat_tuesday}")
print(f"P-Value: {p_value_tuesday}")

if p_value_tuesday < alpha:
    print("Reject the null hypothesis: The queries are not uniformly distributed across the day.")
else:
    print("Fail to reject the null hypothesis: The queries are uniformly distributed across the day.")
