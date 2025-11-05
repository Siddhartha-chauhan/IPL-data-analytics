"""
top10_economical_bowlers_2015.py

This script calculates the top 10 most economical bowlers in IPL 2015
using match and delivery data from CSV files and visualizes the results
in a bar chart.
"""

import csv
import matplotlib.pyplot as plt

# Function to read CSV data and return a list of dictionaries
def read_data(file_path):
    """
    Reads IPL data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: List of dictionaries representing rows in the CSV.
    """
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # Append each row as a dictionary
        for match in reader:
            data.append(match)
    return data


# Function to calculate top 10 economical bowlers for IPL 2015
def calculate_economical_bowlers_2015(matches, deliveries):
    """
    Calculates the top 10 economical bowlers in IPL 2015.

    Args:
        matches (list): List of match records (dicts) from matches.csv.
        deliveries (list): List of delivery records (dicts) from deliveries.csv.

    Returns:
        dict: Dictionary of top 10 bowlers with their economy rates.
    """
    # Get all match IDs for the 2015 season
    match_ids_2015 = {match["id"] for match in matches if match["season"] == "2015"}

    # Dictionaries to track total runs and balls bowled per bowler
    bowler_runs = {}
    bowler_balls = {}

    # Loop through each delivery
    for delivery in deliveries:
        if delivery["match_id"] in match_ids_2015:
            bowler = delivery["bowler"]
            total_runs = int(delivery["total_runs"])

            # Add runs to the bowler's total
            bowler_runs[bowler] = bowler_runs.get(bowler, 0) + total_runs
            # Count the number of balls bowled
            bowler_balls[bowler] = bowler_balls.get(bowler, 0) + 1

    # Calculate economy rate for each bowler
    economy = {}
    for bowler in bowler_runs:
        overs = bowler_balls[bowler] / 6  # 6 balls per over
        economy[bowler] = bowler_runs[bowler] / overs if overs > 0 else 0

    # Sort bowlers by economy rate (ascending) and take top 10
    top_10 = dict(sorted(economy.items(), key=lambda x: x[1])[:10])
    return top_10


# Function to plot top 10 economical bowlers as a bar chart
def plot_economical_bowlers(top_10):
    """
    Plots a bar chart of top 10 economical bowlers in IPL 2015.

    Args:
        top_10 (dict): Dictionary of bowlers and their economy rates.
    """
    bowlers = list(top_10.keys())
    economies = list(top_10.values())

    plt.figure(figsize=(10, 6))
    plt.bar(bowlers, economies, color='orange')
    plt.title("Top 10 Economical Bowlers in IPL 2015")
    plt.xlabel("Bowler")
    plt.ylabel("Economy Rate")
    plt.xticks(rotation=45)           # Rotate names for readability
    plt.tight_layout()                # Adjust layout to fit labels
    plt.savefig("plots/top10_economical_bowlers_2015.png", dpi=300)  # Save figure
    plt.show()                        # Display the plot


# Main execution function
def execute():
    """
    Reads data, calculates top 10 economical bowlers, and plots the results.
    """
    matches = read_data("data/matches.csv")        # Read match data
    deliveries = read_data("data/deliveries.csv")  # Read delivery data
    top_10 = calculate_economical_bowlers_2015(matches, deliveries)  # Calculate top 10
    plot_economical_bowlers(top_10)               # Plot chart


# Run the script
execute()
