# Lovelace

Lovelace is a university Year 1 project that applies machine learning techniques to predict the likelihood of heart disease based on a dataset.

## Installation
### Prerequisites
- Python 3.7+
- Required Python libraries:
  ```bash
  pip install pandas numpy scikit-learn seaborn matplotlib
  ```

## Usage
1. **Load and Preprocess Data:**
   - `data_loader.py` loads the dataset from the `data/heart.csv` file.
   - `data_formatter.py` renames columns, handles missing values, and creates additional features.
2. **Data Visualization:**
   - `visualization.py` provides functions to generate various plots for exploratory data analysis.
3. **Model Training & Evaluation:**
   - `model.py` splits the dataset, trains a logistic regression model, and evaluates performance.
4. **Run the Project:**
   ```bash
   python main.py
   ```

## Features
- **Data Cleaning & Transformation:**
  - Renames ambiguous column names.
  - Handles missing values by filling with mean values.
  - Adds additional columns (`health_status`, `gender`).
- **Exploratory Data Analysis (EDA):**
  - Pie chart for health status distribution.
  - Gender distribution visualization.
  - Correlation heatmap and pair plots.
  - Box plots for age and cholesterol vs. health status.
- **Machine Learning Model:**
  - Uses Logistic Regression to predict heart disease.
  - Splits data into training, validation, and test sets.
  - Evaluates model performance with accuracy and confusion matrix.
