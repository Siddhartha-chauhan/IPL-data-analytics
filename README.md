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

## Installation
```bash
# Create & activate virtual environment
python3 -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

# Install libraries
pip install -r requirements.txt



