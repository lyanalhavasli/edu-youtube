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
queries = []

# Process each conversation
for conversation in conversations:
    if "mapping" in conversation:
        for node in conversation["mapping"].values():
            # Ensure 'message' exists and is from the user
            if node.get("message") and node["message"]["author"]["role"] == "user":
                timestamp = node["message"]["create_time"]
                if timestamp is not None:
                    # Convert timestamp to hour and weekday
                    dt = datetime.fromtimestamp(timestamp)
                    queries.append({"Day": dt.strftime('%A'), "Hour": dt.hour})

# Convert the list to a Pandas DataFrame
df = pd.DataFrame(queries)

# Define the order of days
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Plot a separate graph for each day of the week
for day in days_of_week:
    # Filter data for the current day
    day_data = df[df["Day"] == day]
    # Count the number of queries for each hour
    hour_counts = day_data["Hour"].value_counts().reindex(range(24), fill_value=0)
    
    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.bar(hour_counts.index, hour_counts.values, color="skyblue")
    plt.xticks(ticks=range(24), labels=[f"{hour}:00" for hour in range(24)], rotation=45)
    plt.xlabel("Hour of the Day")
    plt.ylabel("Number of Queries")
    plt.title(f"Number of Queries During the Day ({day})")
    plt.tight_layout()
    
    # Show the plot
    plt.show()
