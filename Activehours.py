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

# Initialize a dictionary to count queries per hour
queries_per_hour = {hour: 0 for hour in range(24)}

# Process each conversation
for conversation in conversations:
    if "mapping" in conversation:
        for node in conversation["mapping"].values():
            # Ensure 'message' exists and is not None
            if node.get("message") and node["message"]["author"]["role"] == "user":
                # Extract the timestamp of the query
                timestamp = node["message"]["create_time"]
                # Convert timestamp to the hour
                hour = datetime.fromtimestamp(timestamp).hour
                # Increment the query count for the hour
                queries_per_hour[hour] += 1

# Convert the data to a Pandas DataFrame for easier plotting
df = pd.DataFrame({'Hour': list(queries_per_hour.keys()), 'Queries': list(queries_per_hour.values())})

# Sort the DataFrame by Hour for proper visualization
df = df.sort_values(by="Hour")

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(df['Hour'], df['Queries'], color='skyblue')
plt.xticks(ticks=range(24), labels=[f'{hour}:00' for hour in range(24)], rotation=45)
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Queries')
plt.title('Most Active Hours of the Day')
plt.tight_layout()

# Show the plot
plt.show()
