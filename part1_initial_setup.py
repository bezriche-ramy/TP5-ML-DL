#!/usr/bin/env python3
"""
Part 1 — Initial Setup
- Load the dataset `sample dataset/traffic_sample.csv`.
- Display first rows.
- Display dataset dimensions.
"""

from pathlib import Path
import sys

try:
    import pandas as pd
except ImportError:
    print("pandas is required. Install with: pip install -r requirements.txt")
    sys.exit(1)


def main():
    repo_dir = Path(__file__).resolve().parent
    data_path = repo_dir / 'sample dataset' / 'traffic_sample.csv'

    print(f"Looking for dataset at: {data_path}")

    if not data_path.exists():
        print("Dataset not found. Please ensure the file exists at the path above.")
        sys.exit(1)

    # Load dataset
    df = pd.read_csv(data_path)

    # Display first rows
    print("\nFirst 5 rows:")
    print(df.head().to_string(index=False))

    # Display dataset dimensions
    print(f"\nDataset dimensions: {df.shape[0]} rows, {df.shape[1]} columns")


if __name__ == '__main__':
    main()
