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

# Initialize a list to store query lengths by date
query_lengths = []

# Process each conversation
for conversation in conversations:
    if "mapping" in conversation:
        for node in conversation["mapping"].values():
            # Ensure 'message' exists and is not None
            if node.get("message") and node["message"]["author"]["role"] == "user":
                # Safely extract the query content and timestamp
                query_parts = node["message"]["content"].get("parts", [])
                query_content = ""
                for part in query_parts:
                    if isinstance(part, str):  # Handle case where part is a string
                        query_content += part
                    elif isinstance(part, dict):  # Handle case where part is a dict
                        query_content += part.get("content", "")
                timestamp = node["message"]["create_time"]
                # Calculate the length of the query in words
                query_length = len(query_content.split())
                # Convert timestamp to date
                query_date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
                # Append the data (date, query length) to the list
                query_lengths.append((query_date, query_length))

# Convert the list to a Pandas DataFrame
df = pd.DataFrame(query_lengths, columns=["Date", "Query Length"])

# Group by date to calculate the average query length per day
df_avg_length = df.groupby("Date")["Query Length"].mean().reset_index()

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df_avg_length["Date"], df_avg_length["Query Length"], marker='o', color='skyblue', linestyle='-')
plt.xticks(rotation=45, fontsize=8)
plt.xlabel('Date')
plt.ylabel('Average Query Length (Words)')
plt.title('Average Query Length Over Time')
plt.tight_layout()

# Show the plot
plt.show()
