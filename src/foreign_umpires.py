"""
foreign_umpire_analysis.py

This script analyzes the foreign umpires in IPL using hardcoded data,
counts the number of umpires by country (excluding India), and plots a bar chart.
"""

import matplotlib.pyplot as plt

# List of umpires with their country (directly in code)
umpires = [
    ("Aleem Dar", "Pakistan"),
    ("Asad Rauf", "Pakistan"),
    ("Billy Bowden", "New Zealand"),
    ("Bruce Oxenford", "Australia"),
    ("Ian Gould", "England"),
    ("Marais Erasmus", "South Africa"),
    ("Nigel Llong", "England"),
    ("Richard Illingworth", "England"),
    ("Rod Tucker", "Australia"),
    ("Kumar Dharmasena", "Sri Lanka"),
    ("Simon Taufel", "Australia"),
    ("Tonny Hill", "New Zealand"),
    ("Steve Davis", "Australia"),
    ("Jeff Crowe", "New Zealand"),
    ("Richard kettleborough", "England"),
]

# Count foreign umpires by country (ignore India)
counts = {}
for _, country in umpires:
    if country.lower() == "india":
        continue
    counts[country] = counts.get(country, 0) + 1

# Plot bar chart
plt.figure(figsize=(10, 6))
plt.bar(counts.keys(), counts.values(), color="skyblue")
plt.title("Number of Foreign Umpires in IPL by Country (Excl. India)")
plt.xlabel("Country")
plt.ylabel("Number of Umpires")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/foreign_umpires_by_country.png", dpi=300)
plt.show()
