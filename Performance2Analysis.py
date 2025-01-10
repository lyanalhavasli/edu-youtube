from scipy.stats import chisquare

# Observed number of queries for each model
observed_queries_models = [600, 300, 150, 50, 25]  

# Total queries and expected distribution assuming uniformity
total_queries_models = sum(observed_queries_models)
expected_queries_models = [total_queries_models / len(observed_queries_models)] * len(observed_queries_models)

# Perform the Chi-Square test
chi2_stat, p_value = chisquare(f_obs=observed_queries_models, f_exp=expected_queries_models)

# Significance level
alpha = 0.05

# Print results
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"P-Value: {p_value}")

if p_value < alpha:
    print("Reject the null hypothesis: The queries are not uniformly distributed across the models.")
else:
    print("Fail to reject the null hypothesis: The queries are uniformly distributed across the models.")
