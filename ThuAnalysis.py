import numpy as np
from scipy.stats import chisquare

# Observed number of queries for each hour on Thursday
observed_queries_thursday = [
    17, 16, 4, 2, 3, 2, 9, 6, 4, 13, 3, 10, 14
]

# Total queries and expected distribution assuming uniformity
total_queries_thursday = sum(observed_queries_thursday)
expected_queries_thursday = [total_queries_thursday / len(observed_queries_thursday)] * len(observed_queries_thursday)

# Perform the Chi-Square test
chi2_stat_thursday, p_value_thursday = chisquare(f_obs=observed_queries_thursday, f_exp=expected_queries_thursday)

# Significance level
alpha = 0.05

# Print results
print(f"Chi-Square Statistic: {chi2_stat_thursday}")
print(f"P-Value: {p_value_thursday}")

if p_value_thursday < alpha:
    print("Reject the null hypothesis: The queries are not uniformly distributed across the day.")
else:
    print("Fail to reject the null hypothesis: The queries are uniformly distributed across the day.")
