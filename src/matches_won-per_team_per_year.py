"""
matches_won_per_team_per_year.py

This script calculates the number of matches won by each IPL team per season
using match data from CSV files and generates a stacked bar chart visualization.
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
        # Append each match row as a dictionary to the data list
        for match in matches_reader:
            data.append(match)
    return data


# Function to calculate number of matches won per team per season
def calculate(data):
    """
    Calculates the number of matches won by each team per season.

    Args:
        data (list): List of IPL match records (dicts).

    Returns:
        dict: Nested dictionary where keys are seasons and values are
              dictionaries of team names and their number of wins.
              Example: { '2008': {'RCB': 9, 'MI': 8}, ... }
    """
    matches_won = {}

    for match in data:
        season = match["season"]
        winner = match["winner"]

        # Skip matches with no winner (e.g., abandoned matches)
        if winner == "":
            continue

        # Initialize season dictionary if not exists
        if season not in matches_won:
            matches_won[season] = {}
        # Initialize team count if not exists
        if winner not in matches_won[season]:
            matches_won[season][winner] = 0

        # Increment the win count for the team
        matches_won[season][winner] += 1

    return matches_won


# Function to plot stacked bar chart of matches won per team per season
def plot(matches_won):
    """
    Plots a stacked bar chart showing the number of matches won per team per season.

    Args:
        matches_won (dict): Nested dictionary of seasons and team wins.
    """
    seasons = sorted(matches_won.keys())

    # Get a sorted list of all teams across all seasons
    teams = sorted({team for year_data in matches_won.values() for team in year_data.keys()})

    # Prepare data for plotting: list of wins per team for each season
    team_wins = {team: [matches_won[season].get(team, 0) for season in seasons] for team in teams}

    # Plot stacked bar chart
    plt.figure(figsize=(12, 7))
    bottom = [0] * len(seasons)  # Track cumulative bottom position for stacking

    for team in teams:
        plt.bar(seasons, team_wins[team], bottom=bottom, label=team)
        # Update bottom for next team
        bottom = [bottom[i] + team_wins[team][i] for i in range(len(seasons))]

    plt.title("Number of Matches Won per Team per Year in IPL")
    plt.xlabel("Season")
    plt.ylabel("Number of Matches Won")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
    plt.tight_layout()
    plt.savefig("plots/matches_won_per_team_per_year.png", dpi=300)
    plt.show()


# Main execution function
def execute():
    """
    Reads match data, calculates matches won per team per season, and plots the results.
    """
    file_path = "data/matches.csv"
    data = read_data(file_path)          # Read match CSV data
    matches_won = calculate(data)        # Calculate matches won per team per season
    plot(matches_won)                    # Generate stacked bar chart


# Run the script
execute()
