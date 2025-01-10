import numpy as np
from scipy.stats import chisquare

# Observed number of queries for each hour on Friday
observed_queries_friday = [
    7, 28, 4, 4, 3, 4, 12, 11, 10, 16, 7, 2, 4, 3, 1, 5
]

# Total queries and expected distribution assuming uniformity
total_queries_friday = sum(observed_queries_friday)
expected_queries_friday = [total_queries_friday / len(observed_queries_friday)] * len(observed_queries_friday)

# Perform the Chi-Square test
chi2_stat_friday, p_value_friday = chisquare(f_obs=observed_queries_friday, f_exp=expected_queries_friday)

# Significance level
alpha = 0.05

# Print results
print(f"Chi-Square Statistic: {chi2_stat_friday}")
print(f"P-Value: {p_value_friday}")

if p_value_friday < alpha:
    print("Reject the null hypothesis: The queries are not uniformly distributed across the day.")
else:
    print("Fail to reject the null hypothesis: The queries are uniformly distributed across the day.")
