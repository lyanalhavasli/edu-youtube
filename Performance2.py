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

# Initialize a list to store model information for assistant responses
model_queries = []

# Process each conversation
for conversation in conversations:
    if "mapping" in conversation:  # Ensure 'mapping' exists
        for node in conversation["mapping"].values():
            # Ensure 'message' exists and is from the assistant
            if node.get("message") and node["message"]["author"]["role"] == "assistant":
                # Safely retrieve the model_slug or default_model_slug
                model_slug = node["message"]["metadata"].get("model_slug", None)
                if not model_slug:  # Fall back to default_model_slug if model_slug is None or missing
                    model_slug = node["message"]["metadata"].get("default_model_slug", "unknown")
                model_queries.append(model_slug)

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(model_queries, columns=["Model Slug"])

# Count the number of responses per model
model_counts = df["Model Slug"].value_counts().reset_index()
model_counts.columns = ["Model Slug", "Query Count"]

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(model_counts["Model Slug"], model_counts["Query Count"], color="skyblue")
plt.xlabel("Model Slug")
plt.ylabel("Number of Queries")
plt.title("Number of Queries by ChatGPT Model")
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
