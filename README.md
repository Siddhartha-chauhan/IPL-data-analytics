# IPL Data Analytics Project

## Aim
Convert IPL raw data (ball-by-ball and match records) into charts that tell meaningful stories about the tournament.

## Raw Data
Primary dataset: [Kaggle: IPL Dataset](https://www.kaggle.com/manasgarg/ipl/version/5)  
> Additional sources may be needed, e.g., umpire countries.

## Guidelines
- Organize code in functions: `calculate()`, `plot()`, `execute()`. Call `execute()` at the end.  
- Use `csv.DictReader` for readable code.  
- Compute data while reading CSV to save memory.  
- Use descriptive variable names. Replace numeric indices with constants.  
- Include `.gitignore` for data/IDE/temp files ([Python gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)).  
- Ensure code passes **pylint** or **flake8**.  
- Include `requirements.txt` for libraries.





# Installation & Setup

Clone the repository

git clone <your-repo-url>
cd IPL-Data-Analytics


# Create and activate virtual environment

python3 -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate


# Install required libraries

pip install -r requirements.txt

# Running the Project

Each analysis script is located in the src/ folder.

Run any script using:

python src/<script_name>.py


Example:

python src/total_runs_by_each_team.py


Output charts are saved in the plots/ folder.

# Project Structure

IPL-Data-Analytics/
│
├── data/                 # CSV files (matches, deliveries, umpire data)
├── plots/                # Output charts
├── src/                  # Python scripts for analysis
├── venv/                 # Virtual environment
├── .gitignore
├── README.md
└── requirements.txt

# Notes

Make sure CSV files are present in the data/ folder.

Activate the virtual environment before running scripts.

Charts will automatically be saved in plots/.

Use pylint or flake8 to check code quality:

pylint src/*.py
