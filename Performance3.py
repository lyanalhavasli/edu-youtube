import json
import pandas as pd
import matplotlib.pyplot as plt

# Load the JSON data
with open('conversations.json', 'r') as file:
    data = json.load(file)

# Check if the data is a list or dictionary
if isinstance(data, list):
    conversations = data
elif isinstance(data, dict) and "mapping" in data:
    conversations = [data]
else:
    raise ValueError("Unexpected JSON structure. Please check the file format.")

# Initialize a list to store model information for user queries
model_queries = []

# Process each conversation
for conversation in conversations:
    if "mapping" in conversation:
        for node in conversation["mapping"].values():
            # Ensure 'message' exists and is from the user
            if node.get("message") and node["message"]["author"]["role"] == "user":
                # Retrieve parent node for the assistant's response
                parent_id = node.get("parent")
                if parent_id and parent_id in conversation["mapping"]:
                    parent_node = conversation["mapping"][parent_id]
                    if parent_node.get("message") and parent_node["message"]["author"]["role"] == "assistant":
                        # Retrieve model slug
                        model_slug = parent_node["message"]["metadata"].get("model_slug", None)
                        if not model_slug:
                            model_slug = parent_node["message"]["metadata"].get("default_model_slug", "unknown")
                        # Combine query content into a single string
                        query_parts = node["message"]["content"].get("parts", [])
                        query_content = " ".join(
                            part.get("content", "") if isinstance(part, dict) else part for part in query_parts
                        )
                        query_length = len(query_content.split())  # Word count
                        model_queries.append((model_slug, query_length))

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(model_queries, columns=["Model Slug", "Query Length"])

# Remove rows where "Model Slug" is "unknown"
df = df[df["Model Slug"] != "unknown"]

# Group by model and calculate average query length
average_query_lengths = df.groupby("Model Slug")["Query Length"].mean().reset_index()

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(average_query_lengths["Model Slug"], average_query_lengths["Query Length"], color="skyblue")
plt.xlabel("Model Slug")
plt.ylabel("Average Query Length (Words)")
plt.title("Average Length of User Queries for Each ChatGPT Model")
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
