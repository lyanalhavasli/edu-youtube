import json
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

def load_and_process_data(file_path):
    """
    Load JSON data and process it to extract queries with day and hour information.
    
    Args:
        file_path (str): Path to the JSON file.
        
    Returns:
        pd.DataFrame: DataFrame with columns 'Day' and 'Hour'.
    """
    # Load the JSON data
    with open(file_path, 'r') as file:
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
    return pd.DataFrame(queries)


def plot_queries_for_day(df, day):
    """
    Plot the number of queries for a specific day of the week.
    
    Args:
        df (pd.DataFrame): DataFrame containing 'Day' and 'Hour' columns.
        day (str): Day of the week (e.g., 'Monday').
    """
    # Filter data for the specified day
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
    
    # Set y-axis ticks to increments of 5
    max_queries = max(hour_counts.values)
    plt.yticks(range(0, max_queries + 5, 5))
    
    plt.tight_layout()
    plt.show()


def main():
    """
    Main function to load data and generate graphs for each day of the week.
    """
    # Load and process the data
    file_path = 'conversations.json'
    df = load_and_process_data(file_path)

    # Define the order of days
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Plot a graph for each day
    for day in days_of_week:
        plot_queries_for_day(df, day)


# Run the main function
if __name__ == "__main__":
    main()
