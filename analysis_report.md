# Task 15: NumPy Statistical Analysis

## 1. Introduction

This project uses Python and NumPy to analyze numerical data. It calculates descriptive statistics and identifies potentially unusual observations.

## 2. Objective

The objective is to practice statistical calculations, compare the mean and median, and identify potential outliers.

## 3. Dataset

The sample dataset contains 15 numerical observations. Most values range from 45 to 80, while 150 is included as an unusually high observation for demonstration.

## 4. Methodology

1. Load numerical observations from the CSV file.
2. Validate the dataset.
3. Calculate mean and median.
4. Calculate population standard deviation.
5. Find minimum and maximum values.
6. Calculate Q1, Q3 and IQR.
7. Identify potential outliers.
8. Compare mean and median and interpret the results.

## 5. Statistical Calculations

Mean = Sum of all observations / Number of observations

Median = Middle observation after sorting the data.

Standard deviation = Square root of the average squared deviation from the mean, using the population formula.

IQR = Q3 - Q1

Lower fence = Q1 - 1.5 × IQR

Upper fence = Q3 + 1.5 × IQR

Values outside these fences are flagged as potential outliers.

## 6. Results

The program prints the exact mean, median, standard deviation, minimum, maximum, quartiles, IQR and potential outliers when executed.

The high value 150 can pull the mean upward. The median is generally less sensitive to extreme observations.

## 7. Interpretation

A mean greater than the median can indicate that high values are pulling the average upward. Standard deviation describes how spread out the observations are.

The IQR method identifies potentially unusual values but does not establish whether those values are errors.

## 8. Applications

These statistical techniques can support exploratory data analysis, student performance analysis, sales analysis and data quality checks.

## 9. Conclusion

The project demonstrates how NumPy simplifies statistical calculations and supports initial exploration of numerical datasets.
