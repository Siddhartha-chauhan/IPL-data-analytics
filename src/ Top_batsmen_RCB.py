"""
top10_batsmen_rcb.py

This script calculates the top 10 batsmen for Royal Challengers Bangalore (RCB)
using IPL delivery data from a CSV file and generates a bar chart visualization
of their total runs.
"""

import csv
import matplotlib.pyplot as plt

# Function to read CSV data and return a list of dictionaries
def read_data(file_path):
    """
    Reads IPL delivery data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing delivery data.

    Returns:
        list: List of dictionaries representing each delivery record.
    """
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        deliveries_data = csv.DictReader(file)
        # Append each delivery row as a dictionary
        for match in deliveries_data:
            data.append(match)
    return data


# Function to calculate top 10 RCB batsmen by total runs
def calculate(data):
    """
    Calculates the top 10 batsmen for Royal Challengers Bangalore by total runs.

    Args:
        data (list): List of IPL delivery records (dicts).

    Returns:
        dict: Dictionary of top 10 batsmen and their total runs.
    """
    batsman_runs = {}

    # Loop through each delivery
    for match in data:
        # Consider only deliveries where RCB is batting
        if match["batting_team"] == "Royal Challengers Bangalore":
            batsman = match["batsman"]
            runs = int(match["batsman_runs"])

            # Sum runs for each batsman
            if batsman in batsman_runs:
                batsman_runs[batsman] += runs
            else:
                batsman_runs[batsman] = runs

    # Sort batsmen by total runs and take top 10
    top_batsmen = dict(sorted(batsman_runs.items(), key=lambda x: x[1], reverse=True)[:10])
    return top_batsmen


# Function to plot top 10 RCB batsmen
def plot(top_batsmen):
    """
    Plots a bar chart of the top 10 RCB batsmen by total runs.

    Args:
        top_batsmen (dict): Dictionary of batsmen names and their total runs.
    """
    batsmen = list(top_batsmen.keys())
    runs = list(top_batsmen.values())

    plt.figure(figsize=(10, 6))
    plt.bar(batsmen, runs, color='red')
    plt.title('Top 10 Batsmen for Royal Challengers Bangalore')
    plt.xlabel('Batsmen')
    plt.ylabel('Total Runs')
    plt.xticks(rotation=45)             # Rotate labels for readability
    plt.tight_layout()                  # Adjust layout
    plt.savefig("plots/top10_batsmen_rcb.png", dpi=300)  # Save figure
    plt.show()


# Main execution function
def execute():
    """
    Reads delivery data, calculates top 10 RCB batsmen, and plots the results.
    """
    file_path = "data/deliveries.csv"
    data = read_data(file_path)           # Read delivery CSV data
    top_batsmen = calculate(data)         # Calculate top 10 batsmen
    plot(top_batsmen)                     # Generate bar chart


# Run the script
execute()
