import json
from datetime import datetime
from scipy.stats import pearsonr, spearmanr
import numpy as np

# Load the JSON data
with open('conversations.json', 'r') as file:
    data = json.load(file)

# Initialize lists for time spent and number of messages
time_spent = []
num_messages = []

# Check if the data is a list or dictionary
if isinstance(data, list):
    conversations = data
elif isinstance(data, dict) and "mapping" in data:
    conversations = [data]
else:
    raise ValueError("Unexpected JSON structure. Please check the file format.")

# Process each conversation
for conversation in conversations:
    if "mapping" in conversation:
        timestamps = []
        message_count = 0

        # Extract messages
        for node in conversation["mapping"].values():
            if node.get("message"):
                message = node["message"]
                # Check if it's a user or assistant message
                if "create_time" in message:
                    timestamps.append(message["create_time"])
                if message["author"]["role"] in ["user", "assistant"]:
                    message_count += 1

        # Filter out None values from timestamps
        timestamps = [t for t in timestamps if t is not None]

        if timestamps:  # Only calculate if timestamps is not empty
            start_time = min(timestamps)
            end_time = max(timestamps)
            duration_minutes = (end_time - start_time) / 60  # Convert seconds to minutes
            time_spent.append(duration_minutes)
        else:
            time_spent.append(0)  # Default to 0 if no valid timestamps

        # Add the number of messages
        num_messages.append(message_count)

# Ensure the lists have the same length
if len(time_spent) != len(num_messages):
    raise ValueError("Mismatch in lengths of time_spent and num_messages.")

# Print extracted data
print("Time Spent (minutes):", time_spent)
print("Number of Messages:", num_messages)

# Perform correlation analysis
time_spent_array = np.array(time_spent)
num_messages_array = np.array(num_messages)

# Pearson Correlation
pearson_corr, pearson_p = pearsonr(time_spent_array, num_messages_array)
print(f"Pearson Correlation: {pearson_corr}, P-Value: {pearson_p}")

# Spearman Correlation
spearman_corr, spearman_p = spearmanr(time_spent_array, num_messages_array)
print(f"Spearman Correlation: {spearman_corr}, P-Value: {spearman_p}")

# Interpret results
if pearson_p < 0.05:
    print("Pearson: Reject the null hypothesis. There is a significant linear correlation.")
else:
    print("Pearson: Fail to reject the null hypothesis. No significant linear correlation.")

if spearman_p < 0.05:
    print("Spearman: Reject the null hypothesis. There is a significant monotonic correlation.")
else:
    print("Spearman: Fail to reject the null hypothesis. No significant monotonic correlation.")
