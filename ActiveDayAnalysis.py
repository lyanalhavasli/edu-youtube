import numpy as np
from scipy.stats import chisquare

# Observed number of queries for each day of the week
observed_queries_week = [
    180, 160, 140, 120, 150, 200, 100  # Replace with your actual observed values from the graph
]

# Total queries and expected distribution assuming uniformity
total_queries_week = sum(observed_queries_week)
expected_queries_week = [total_queries_week / len(observed_queries_week)] * len(observed_queries_week)

# Perform the Chi-Square test
chi2_stat_week, p_value_week = chisquare(f_obs=observed_queries_week, f_exp=expected_queries_week)

# Significance level
alpha = 0.05

# Print results
print(f"Chi-Square Statistic: {chi2_stat_week}")
print(f"P-Value: {p_value_week}")

if p_value_week < alpha:
    print("Reject the null hypothesis: The queries are not uniformly distributed across the days of the week.")
else:
    print("Fail to reject the null hypothesis: The queries are uniformly distributed across the days of the week.")
