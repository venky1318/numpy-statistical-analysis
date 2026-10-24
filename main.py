import csv
from pathlib import Path
import numpy as np

DATASET_PATH = Path(__file__).with_name("dataset.csv")


def load_numeric_data(file_path):
    """Load numerical observations from a CSV file."""
    values = []

    with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames or "value" not in reader.fieldnames:
            raise ValueError("CSV must contain a 'value' column.")

        for row in reader:
            raw = (row.get("value") or "").strip()
            if raw:
                values.append(float(raw))

    if len(values) < 3:
        raise ValueError("Enter at least three numerical observations.")

    data = np.asarray(values, dtype=float)

    if not np.all(np.isfinite(data)):
        raise ValueError("All values must be finite numbers.")

    return data


def analyze_data(data):
    """Calculate descriptive statistics and potential outliers."""
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1

    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr

    outliers = data[
        (data < lower_fence) | (data > upper_fence)
    ]

    return {
        "count": len(data),
        "mean": np.mean(data),
        "median": np.median(data),
        "std_dev": np.std(data),
        "minimum": np.min(data),
        "maximum": np.max(data),
        "q1": q1,
        "q3": q3,
        "iqr": iqr,
        "lower_fence": lower_fence,
        "upper_fence": upper_fence,
        "outliers": outliers,
    }


def main():
    try:
        data = load_numeric_data(DATASET_PATH)
        result = analyze_data(data)
    except (OSError, ValueError) as error:
        print(f"Error: {error}")
        return

    print("=" * 55)
    print("          NUMPY STATISTICAL ANALYSIS")
    print("=" * 55)
    print(f"Dataset       : {DATASET_PATH.name}")
    print(f"Observations  : {result['count']}")
    print(f"Values        : {data.tolist()}")
    print("-" * 55)

    print(f"Mean          : {result['mean']:.2f}")
    print(f"Median        : {result['median']:.2f}")
    print(f"Std deviation : {result['std_dev']:.2f}")
    print(f"Minimum       : {result['minimum']:.2f}")
    print(f"Maximum       : {result['maximum']:.2f}")
    print(f"Q1            : {result['q1']:.2f}")
    print(f"Q3            : {result['q3']:.2f}")
    print(f"IQR           : {result['iqr']:.2f}")
    print("-" * 55)

    if np.isclose(result["mean"], result["median"]):
        print("Mean and median are approximately equal.")
    elif result["mean"] > result["median"]:
        print("Mean is higher than median.")
        print("High values may be pulling the mean upward.")
    else:
        print("Mean is lower than median.")
        print("Low values may be pulling the mean downward.")

    if result["outliers"].size:
        print(f"Potential outliers: {result['outliers'].tolist()}")
    else:
        print("Potential outliers: None detected.")

    print("-" * 55)
    print("Note: Outliers are potential unusual values, not")
    print("necessarily errors.")
    print("=" * 55)


if __name__ == "__main__":
    main()