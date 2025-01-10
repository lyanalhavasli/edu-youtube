from scipy.stats import chisquare

# Observed average query lengths
observed_averages = [50, 60, 250, 20, 150]  

# Define the expected averages (e.g., uniform distribution)
total_average = sum(observed_averages)
expected_averages = [total_average / len(observed_averages)] * len(observed_averages)

# Perform Chi-Square Goodness-of-Fit Test
chi2_stat, p_value = chisquare(f_obs=observed_averages, f_exp=expected_averages)

print(f"Chi-Square Statistic: {chi2_stat}")
print(f"P-Value: {p_value}")

if p_value < 0.05:
    print("Reject the null hypothesis: The averages do not match the expected distribution.")
else:
    print("Fail to reject the null hypothesis: The averages match the expected distribution.")
