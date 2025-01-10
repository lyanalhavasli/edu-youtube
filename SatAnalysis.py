import numpy as np
from scipy.stats import chisquare

# Observed number of queries for each hour on Saturday
observed_queries_saturday = [
    22, 20, 10, 15, 18, 1, 1, 4, 4, 8, 10, 10, 13, 6, 5, 21, 20
]

# Total queries and expected distribution assuming uniformity
total_queries_saturday = sum(observed_queries_saturday)
expected_queries_saturday = [total_queries_saturday / len(observed_queries_saturday)] * len(observed_queries_saturday)

# Perform the Chi-Square test
chi2_stat_saturday, p_value_saturday = chisquare(f_obs=observed_queries_saturday, f_exp=expected_queries_saturday)

# Significance level
alpha = 0.05

# Print results
print(f"Chi-Square Statistic: {chi2_stat_saturday}")
print(f"P-Value: {p_value_saturday}")

if p_value_saturday < alpha:
    print("Reject the null hypothesis: The queries are not uniformly distributed across the day.")
else:
    print("Fail to reject the null hypothesis: The queries are uniformly distributed across the day.")
