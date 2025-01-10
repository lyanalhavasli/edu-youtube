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

# Initialize a list to store query timestamps
query_days = []

# Process each conversation
for conversation in conversations:
    if "mapping" in conversation:
        for node in conversation["mapping"].values():
            # Ensure 'message' exists and is from the user
            if node.get("message") and node["message"]["author"]["role"] == "user":
                timestamp = node["message"]["create_time"]
                if timestamp is not None:
                    # Convert timestamp to a weekday (0=Monday, 6=Sunday)
                    day_of_week = datetime.fromtimestamp(timestamp).strftime('%A')  # Full weekday name
                    query_days.append(day_of_week)

# Convert the list to a Pandas DataFrame
df = pd.DataFrame(query_days, columns=["Day of Week"])

# Group by the day of the week and count the number of queries
day_counts = df["Day of Week"].value_counts().reindex(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)  # Ensuring correct order

# Plot the data
plt.figure(figsize=(10, 6))
day_counts.plot(kind="bar", color="skyblue")
plt.xticks(rotation=45)
plt.xlabel("Day of the Week")
plt.ylabel("Number of Queries")
plt.title("Number of Queries by Day of the Week")
plt.tight_layout()

# Show the plot
plt.show()
