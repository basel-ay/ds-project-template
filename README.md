## Overview

This assessment is designed to get hands-on experience with the DS project workflow (missing values, outlier handling, standardization, visualization, APIs, etc..). It comprises two main components:
1. **Python Project**: Missing values, outlier handling, standardization, visualization.
2. **Flask App**: Provides RESTful APIs to interact with the dataset.

The assessment is divided into three parts:

1. **Data Cleaning and Preparation**
2. **Statistical Analysis**
3. **Data Visualization**

## Part 1: Data Cleaning and Preparation

### Objective
Clean a dataset by handling missing values, treating outliers, and standardizing data formats.

### Dataset
- The dataset includes columns such as `ID`, `Name`, `Date_of_Birth`, `Salary`, and `Department`.

### Steps
1. **Handling Missing Values:**
   - Filled missing IDs with unique values.
   - Imputed missing dates of birth using a default date or placeholder.
   - Replaced missing salary values with the mean salary.
   
2. **Outlier Treatment:**
   - Identified and removed or adjusted salary outliers.
   - Corrected negative salary values.

3. **Standardization:**
   - Converted all date formats to a consistent `YYYY-MM-DD` format.

### Code
The data cleaning process is implemented in `data_cleaning.py`.

## Part 2: Statistical Analysis

### Objective
Perform linear regression analysis to predict house prices based on features like size, number of bedrooms, and location.

### Dataset
- The dataset includes columns such as `Size`, `Bedrooms`, `Location`, and `Price`.

### Steps
1. **Data Preparation:**
   - Encoded the `Location` column using one-hot encoding.
   - Split the data into training and testing sets.

2. **Model Training:**
   - Trained a linear regression model on the training set.

3. **Model Evaluation:**
   - Evaluated the model using Mean Absolute Error (MAE) and R² score.

### Model Saving
- The trained model is saved using `joblib` and can be reloaded for future use.

### Code
The regression analysis and model saving are implemented in `regression_analysis.py`.

## Part 3: Data Visualization

### Objective
Create visualizations to explore and present the dataset's insights.

### Dashboard
- **Tools Used:** Power BI
- **Visualizations Included:**
  - Total sales over time
  - Sales breakdown by product category
  - Top-performing sales regions

### Interactive Visualization
- **Tools Used:** Plotly
- **Dataset:** stock prices
- **Features:**
  - Interactive line chart with hover information and filters for dynamic data exploration.

### Code
The data visualization scripts are included in `data_visualization.py`.

## How to Use

1. **Setup:**

### Prerequisites
  - Python 3.7+
  - Git
  - Ensure all necessary Python packages are installed (`pandas`, `numpy`, `scikit-learn`, `joblib`, `plotly`).

3. **Running the Scripts:**
   - Run `data_cleaning.py` for data cleaning tasks.
   - Run `regression_analysis.py` for statistical analysis and model training.
   - Run `data_visualization.py` to generate visualizations.

4. **Dashboard:**
   - Access the dashboard through the specified data visualization tool.
     

### Python Project Setup
1. **Clone the Repository:**
    ```sh
    git clone https://github.com/basel-ay/ds-project-template.git
    ```

2. **Create and Activate a Virtual Environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Python Application:**
    ```sh
    python app.py
    ```

## Dashboard and Interactive Visualization

![Stock Price Trends Over Time](https://github.com/user-attachments/assets/449a7c2d-3066-414c-9031-8e422f17dec4)
![Stock Price Trends Over Time 2](https://github.com/user-attachments/assets/6658e0cc-ad95-459b-a752-78549a44960a)
![Stock Price Trends Over Time 3](https://github.com/user-attachments/assets/082b1b0f-8b1a-4a8e-9d51-9b9039b4f652)
![image](https://github.com/user-attachments/assets/06d556e8-7ea3-4ea2-ae6a-c1084897f020)
