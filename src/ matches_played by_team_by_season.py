"""
matches_played_by_team_per_season.py

This script calculates the number of matches played by each IPL team per season
using match data from a CSV file and generates a stacked bar chart visualization.
"""

import csv
import matplotlib.pyplot as plt

# Function to read CSV data and return a list of dictionaries
def read_data(file_path):
    """
    Reads IPL match data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing match data.

    Returns:
        list: List of dictionaries, each representing a match record.
    """
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        matches_reader = csv.DictReader(file)
        # Append each row (match) as a dictionary
        for match in matches_reader:
            data.append(match)
    return data


# Function to calculate number of matches played by each team per season
def calculate(data):
    """
    Calculates the number of matches played by each team per season.

    Args:
        data (list): List of IPL match records (dicts).

    Returns:
        dict: Nested dictionary where keys are seasons and values are dictionaries
              of teams and their total matches played.
              Example: { '2008': {'RCB': 14, 'MI': 14, ...}, ... }
    """
    matches_count = {}

    # Loop through each match
    for match in data:
        season = match["season"]
        team1 = match["team1"]
        team2 = match["team2"]

        # Initialize season dictionary if not exists
        if season not in matches_count:
            matches_count[season] = {}

        # Increment match count for both teams
        matches_count[season][team1] = matches_count[season].get(team1, 0) + 1
        matches_count[season][team2] = matches_count[season].get(team2, 0) + 1

    return matches_count


# Function to plot stacked bar chart of matches played by each team per season
def plot(matches_count):
    """
    Plots a stacked bar chart of matches played by each team per season.

    Args:
        matches_count (dict): Nested dictionary of seasons and team match counts.
    """
    seasons = sorted(matches_count.keys())
    # Get a sorted list of all teams across all seasons
    teams = sorted({team for season_data in matches_count.values() for team in season_data})

    # Prepare data: list of matches per team for each season
    team_data = {team: [matches_count[season].get(team, 0) for season in seasons] for team in teams}

    # Plot stacked bar chart
    plt.figure(figsize=(14, 8))
    bottom = [0] * len(seasons)  # Track cumulative bottom for stacking

    for team, values in team_data.items():
        plt.bar(seasons, values, bottom=bottom, label=team)
        # Update bottom for next team
        bottom = [bottom[i] + values[i] for i in range(len(values))]

    plt.title("Matches Played by Team per Season (Stacked Bar Chart)")
    plt.xlabel("Season")
    plt.ylabel("Number of Matches")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
    plt.tight_layout()  # Adjust layout to fit labels
    plt.savefig("plots/matches_played_by_team_per_season.png", dpi=300)  # Save figure
    plt.show()


# Main execution function
def execute():
    """
    Reads match data, calculates matches played by each team per season,
    and generates a stacked bar chart.
    """
    file_path = "data/matches.csv"
    data = read_data(file_path)             # Read match CSV data
    matches_count = calculate(data)         # Calculate matches per team per season
    plot(matches_count)                     # Generate stacked bar chart


# Run the script
execute()
