import json
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 1: Load JSON data from the file
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Step 2: Extract user queries
def extract_user_queries(chatgpt_json):
    queries = []
    if "mapping" in chatgpt_json:  # Check if "mapping" exists
        for node_id, node_data in chatgpt_json["mapping"].items():
            # Ensure "message" exists and is from the user
            message = node_data.get("message")
            if message and message.get("author", {}).get("role") == "user":
                # Extract the query text from "parts"
                content = message.get("content", {})
                if "parts" in content and isinstance(content["parts"], list) and content["parts"]:
                    queries.append(content["parts"][0])  # Add the first part of the query
    return queries

# Step 3: Perform K-Means clustering and visualization
def cluster_and_visualize_queries(queries, num_clusters=3):
    # Validate that queries is a list of strings
    if not isinstance(queries, list) or not all(isinstance(q, str) for q in queries):
        raise ValueError("The 'queries' variable must be a list of strings.")
    
    # Convert queries to embeddings
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(queries)

    # Check if embeddings are empty
    if len(embeddings) == 0:
        raise ValueError("The embeddings array is empty. No queries were provided for clustering.")

    # Apply K-Means clustering
    clustering_model = KMeans(n_clusters=num_clusters, random_state=42)
    clustering_model.fit(embeddings)
    cluster_labels = clustering_model.labels_

    # Organize queries by cluster
    clustered_queries = {i: [] for i in range(num_clusters)}
    for query, label in zip(queries, cluster_labels):
        clustered_queries[label].append(query)

    # Print clustered queries
    print("\nClustered Queries:")
    for cluster, items in clustered_queries.items():
        print(f"Cluster {cluster}:")
        for item in items:
            print(f"- {item}")

    # Create a horizontal bar graph
    cluster_sizes = [len(clustered_queries[i]) for i in range(num_clusters)]
    clusters = [f"Cluster {i}" for i in range(num_clusters)]

    plt.barh(clusters, cluster_sizes, color='skyblue')
    plt.xlabel("Number of Queries")
    plt.ylabel("Clusters")
    plt.title("Number of Queries per Cluster")
    plt.show()

# Main script
if __name__ == "__main__":
    # Load JSON file
    file_path = "conversations.json"  # Replace with the correct path to your JSON file
    chatgpt_json = load_json(file_path)

    # Extract user queries
    queries = extract_user_queries(chatgpt_json)
    print("Extracted Queries:", queries)
    print(f"Number of Queries Extracted: {len(queries)}")

    # Handle case where no queries are found
    if not queries:
        raise ValueError("No user queries were extracted. Check the JSON structure and extraction logic.")

    # Perform clustering and visualize results
    cluster_and_visualize_queries(queries, num_clusters=3)
