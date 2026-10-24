# NumPy Statistical Analysis

## Project Overview

This project analyzes numerical data using Python and NumPy. It calculates descriptive statistics, compares the mean and median, and identifies potential outliers using the interquartile range (IQR) method.

## Technologies Used

- Python
- NumPy
- CSV
- VS Code or Jupyter Notebook

## Project Files

- `main.py` — Main statistical analysis program
- `dataset.csv` — Sample numerical dataset
- `requirements.txt` — Required Python library
- `analysis_report.md` — Analysis and interpretation
- `project_report.pdf` — Formal project report
- `screenshots/program_output.png` — Execution evidence

## How to Run

1. Install Python.
2. Open this folder in VS Code.
3. Open the terminal.
4. Install the dependency:

   `python -m pip install -r requirements.txt`

5. Run the program:

   `python main.py`

## Statistical Measures

- Mean: Arithmetic average.
- Median: Middle value after sorting.
- Standard deviation: Measures data spread.
- Minimum and maximum: Smallest and largest values.
- IQR: Difference between the third and first quartiles.

The program uses population standard deviation (`ddof=0`). Potential outliers are identified using the 1.5 × IQR rule.

## Conclusion

This project demonstrates basic descriptive statistics and potential outlier detection using NumPy. These concepts are useful in data analysis and machine learning.
