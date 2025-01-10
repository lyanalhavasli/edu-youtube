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

# Initialize lists to store conversation durations and lengths
conversation_data = []

# Process each conversation
for conversation in conversations:
    if "mapping" in conversation:
        # Extract messages and their timestamps
        timestamps = [
            node["message"]["create_time"]
            for node in conversation["mapping"].values()
            if node.get("message") and node["message"]["create_time"] is not None
        ]
        
        # Calculate the time spent on the conversation
        if timestamps:
            start_time = min(timestamps)  # First message
            end_time = max(timestamps)  # Last message
            duration = (end_time - start_time) / 60  # Convert seconds to minutes
            conversation_id = conversation.get("conversation_id", "unknown")
            conversation_length = len(timestamps)
            conversation_data.append((conversation_id, duration, conversation_length))

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(conversation_data, columns=["Conversation ID", "Duration (Minutes)", "Message Count"])

# Plot the data
plt.figure(figsize=(10, 6))
plt.scatter(df["Duration (Minutes)"], df["Message Count"], alpha=0.7, color='skyblue')
plt.xlabel('Time Spent on Conversation (Minutes)')
plt.ylabel('Number of Messages')
plt.title('Time Spent on Each Conversation vs Conversation Length')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
