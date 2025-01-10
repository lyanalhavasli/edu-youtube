import json
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

# Load the JSON data
with open('conversations.json', 'r') as file:
    data = json.load(file)

# Check if the data is a list or dictionary
if isinstance(data, list):
    conversations = data  # If it's a list, directly assign
elif isinstance(data, dict) and "mapping" in data:
    conversations = [data]  # If it's a dictionary with a "mapping" key, wrap it in a list
else:
    raise ValueError("Unexpected JSON structure. Please check the file format.")

# Initialize a dictionary to count queries per day
queries_per_day = {}

# Define the start of November as a timestamp
november_start = datetime(2024, 11, 1).timestamp()

# Process each conversation
for conversation in conversations:
    if "mapping" in conversation:
        for node in conversation["mapping"].values():
            # Ensure 'message' exists and is not None
            if node.get("message") and node["message"]["author"]["role"] == "user":
                # Extract the timestamp of the query
                timestamp = node["message"]["create_time"]
                # Filter queries starting from November
                if timestamp >= november_start:
                    # Convert timestamp to a readable date format
                    date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
                    # Increment the query count for the day
                    queries_per_day[date] = queries_per_day.get(date, 0) + 1

# Sort the dictionary by date
sorted_dates = sorted(queries_per_day.keys())
sorted_counts = [queries_per_day[date] for date in sorted_dates]

# Convert to a Pandas DataFrame for easier plotting
df = pd.DataFrame({'Date': sorted_dates, 'Queries': sorted_counts})

# Plot the data
plt.figure(figsize=(12, 6))
plt.bar(df['Date'], df['Queries'], color='skyblue')
plt.xticks(rotation=45, fontsize=8)
plt.xlabel('Date')
plt.ylabel('Number of Queries')
plt.title('Number of Queries Per Day (Starting November)')
plt.tight_layout()

# Show the plot
plt.show()
