"""
total_runs_by_eac_team.py

This script calculates the total runs scored by each IPL team
over the history of the IPL using CSV match and delivery data,
and generates a bar chart visualization.
"""

import csv
import matplotlib.pyplot as plt

# Function to read data from a CSV file
def read_data(file_path):
    """
    Reads IPL delivery data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing delivery data.

    Returns:
        list: List of dictionaries, each representing a delivery record.
    """
    data = []
    # Open the CSV file with UTF-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        deliveries_data = csv.DictReader(file)
        # Append each delivery row as a dictionary to the data list
        for match in deliveries_data:
            data.append(match)
    return data


# Function to calculate total runs scored by each team
def calculate(data):
    """
    Calculates total runs scored by each IPL team.

    Args:
        data (list): List of IPL delivery records (dicts).

    Returns:
        dict: Dictionary with team names as keys and total runs as values.
    """
    total_runs_by_team = {}

    # Loop through each delivery in the data
    for match in data:
        team = match["batting_team"]             # Get the batting team
        runs = int(match["total_runs"])          # Convert total_runs to integer

        # Add runs to the existing team total or initialize if first occurrence
        if team in total_runs_by_team:
            total_runs_by_team[team] += runs
        else:
            total_runs_by_team[team] = runs

    return total_runs_by_team


# Function to plot total runs by team as a bar chart
def plot(total_runs_by_team):
    """
    Plots a bar chart of total runs scored by each IPL team.

    Args:
        total_runs_by_team (dict): Team names as keys and total runs as values.
    """
    teams = list(total_runs_by_team.keys())
    runs = list(total_runs_by_team.values())

    # Create a figure for the plot
    plt.figure(figsize=(12, 6))
    plt.bar(teams, runs, color='crimson')            # Bar chart
    plt.title("Total Runs Scored by Each IPL Team")  # Title
    plt.xlabel("Teams")                              # X-axis label
    plt.ylabel("Total Runs")                         # Y-axis label
    plt.xticks(rotation=90)                          # Rotate team names for readability
    plt.tight_layout()                               # Adjust layout to fit labels
    plt.savefig("plots/total_runs_by_team.png", dpi=300)  # Save plot as PNG
    plt.show()                                      # Display plot


# Main execution function
def execute():
    """
    Main function to execute the data reading, calculation, and plotting steps.
    """
    file_path = "data/deliveries.csv"       # Path to CSV file
    data = read_data(file_path)             # Read delivery data
    total_runs_by_team = calculate(data)    # Calculate total runs by team
    plot(total_runs_by_team)                # Generate bar chart


# Run the program
execute()
