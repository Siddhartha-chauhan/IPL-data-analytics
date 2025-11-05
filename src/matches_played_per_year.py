"""
matches_per_year.py

This script calculates the total number of matches played in each IPL season
using match data from a CSV file and generates a bar chart visualization.
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


# Function to calculate number of matches played per season
def calculate(data):
    """
    Calculates the number of matches played in each IPL season.

    Args:
        data (list): List of IPL match records (dicts).

    Returns:
        dict: Dictionary where keys are seasons and values are total matches played.
              Example: { '2008': 58, '2009': 57, ... }
    """
    matches_per_year = {}

    for match in data:
        season = match["season"]
        # Increment count for the season; initialize if not present
        matches_per_year[season] = matches_per_year.get(season, 0) + 1

    return matches_per_year


# Function to plot number of matches per season as a bar chart
def plot(matches_per_year):
    """
    Plots a bar chart of the number of matches played per IPL season.

    Args:
        matches_per_year (dict): Dictionary of seasons and number of matches.
    """
    # Sort seasons for plotting
    years = sorted(matches_per_year.keys())
    matches = [matches_per_year[year] for year in years]

    # Create bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(years, matches, color='teal')
    plt.title("Number of Matches Played per Year in IPL")
    plt.xlabel("Season")
    plt.ylabel("Number of Matches")
    plt.tight_layout()                       # Adjust layout to fit labels
    plt.savefig("plots/matches_per_year.png", dpi=300)  # Save plot
    plt.show()                               # Display plot


# Main execution function
def execute():
    """
    Reads match data, calculates matches per season, and plots the results.
    """
    file_path = "data/matches.csv"
    data = read_data(file_path)               # Read match CSV data
    matches_per_year = calculate(data)       # Calculate matches per season
    plot(matches_per_year)                   # Generate bar chart


# Run the script
execute()
