import json
import matplotlib.pyplot as plt
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

# Initialize a list to store model response lengths
model_data = []

# Process each conversation
for conversation in conversations:
    if "mapping" in conversation:
        for node in conversation["mapping"].values():
            # Ensure 'message' exists and is from the assistant
            if node.get("message") and node["message"]["author"]["role"] == "assistant":
                model_slug = node["message"]["metadata"].get("model_slug", "unknown")
                response_parts = node["message"]["content"].get("parts", [])
                # Combine all parts into a single string
                response_content = " ".join(response_parts) if response_parts else ""
                response_length = len(response_content.split())  # Word count
                model_data.append((model_slug, response_length))

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(model_data, columns=["Model Slug", "Response Length"])

# Group by model and calculate average response length
model_performance = df.groupby("Model Slug")["Response Length"].mean().reset_index()

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(model_performance["Model Slug"], model_performance["Response Length"], color="skyblue")
plt.xlabel("Model Slug")
plt.ylabel("Average Response Length (Words)")
plt.title("Assistant Model Performance: Average Response Length")
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
