"""
extra_runs_2016.py

This script calculates the extra runs conceded by each IPL team in the 2016 season
using match and delivery data from CSV files and generates a bar chart visualization.
"""

import csv
import matplotlib.pyplot as plt

# Function to read CSV file and return a list of dictionaries
def read_data(file_path):
    """
    Reads a CSV file and converts it into a list of dictionaries.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: List of dictionaries representing each row in the CSV.
    """
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # Append each row (match/delivery) as a dictionary
        for match in reader:
            data.append(match)
    return data


# Function to calculate extra runs conceded per team in 2016
def calculate(matches, deliveries):
    """
    Calculates the total extra runs conceded by each IPL team in 2016.

    Args:
        matches (list): List of match records from matches.csv.
        deliveries (list): List of delivery records from deliveries.csv.

    Returns:
        dict: Dictionary with team names as keys and total extra runs conceded as values.
    """
    # Get all match IDs from the 2016 season
    match_ids_2016 = {match["id"] for match in matches if match["season"] == "2016"}
    extra_runs_by_team = {}

    # Loop through each delivery
    for delivery in deliveries:
        if delivery["match_id"] in match_ids_2016:
            bowling_team = delivery["bowling_team"]
            extra_runs = int(delivery["extra_runs"])

            # Add extra runs to the team's total
            if bowling_team in extra_runs_by_team:
                extra_runs_by_team[bowling_team] += extra_runs
            else:
                extra_runs_by_team[bowling_team] = extra_runs

    return extra_runs_by_team


# Function to plot a bar chart of extra runs conceded
def plot(extra_runs_by_team):
    """
    Plots a bar chart showing extra runs conceded per team in IPL 2016.

    Args:
        extra_runs_by_team (dict): Dictionary of teams and their extra runs conceded.
    """
    teams = list(extra_runs_by_team.keys())
    extras = list(extra_runs_by_team.values())

    plt.figure(figsize=(10, 6))
    plt.bar(teams, extras, color='teal')
    plt.title("Extra Runs Conceded per Team in IPL 2016")
    plt.xlabel("Teams")
    plt.ylabel("Extra Runs")
    plt.xticks(rotation=90)           # Rotate team names for readability
    plt.tight_layout()                # Adjust layout to fit labels
    plt.savefig("plots/extra_runs_2016.png", dpi=300)  # Save plot as PNG
    plt.show()


# Main execution function
def execute():
    """
    Reads match and delivery data, calculates extra runs per team in 2016,
    and generates a bar chart.
    """
    matches = read_data("data/matches.csv")        # Read match data
    deliveries = read_data("data/deliveries.csv")  # Read delivery data
    extra_runs_by_team = calculate(matches, deliveries)  # Calculate extra runs
    plot(extra_runs_by_team)                        # Plot results


# Run the script
execute()
