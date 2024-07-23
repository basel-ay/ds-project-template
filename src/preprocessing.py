import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist


# Load the training and test datasets into pandas DataFrames.
df = pd.read_csv('dataset\departments_dataset.csv')

# Replace 'not_applicable', 'not_available', and 'not_specified' with NaN
df = df.replace(['not_applicable', 'not_available', 'not_specified'], np.nan)

# Replace NaN ID with the normal sequence value
df['ID'] = df['ID'].interpolate().astype(int)

# Replace invalid dates
df['Date_of_Birth'] = pd.to_datetime(df['Date_of_Birth'], errors='coerce')

# Replace missing dates with the mean age
mean_age = (pd.to_datetime('today') - df['Date_of_Birth']).mean()
df['Date_of_Birth'] = df['Date_of_Birth'].fillna(
    pd.to_datetime('today') - mean_age)

# Convert Date_of_Birth to only show date part
df['Date_of_Birth'] = df['Date_of_Birth'].dt.date

# Replace non-numeric salary values
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# Replace negative salaries with their absolute values
df['Salary'] = df['Salary'].abs()

# Fill missing salaries with the overall mean salary
mean_salary = df['Salary'].mean()
df['Salary'] = df['Salary'].fillna(mean_salary)

# Extract the row with the missing Department
target_row = df[df['Department'].isna()]

# Calculate the distance to other rows based on Salary


def calculate_distance(row, df):
    df = df.drop(row.index)
    distances = cdist(df[['Salary']], row[['Salary']], metric='euclidean')
    return distances, df


distances, df_with_departments = calculate_distance(target_row, df)

# Find the row with the smallest distance
min_distance_idx = distances.argmin()
most_similar_row = df_with_departments.iloc[min_distance_idx]

# Assign the Department of the most similar row to the target row
inferred_department = most_similar_row['Department']
df.loc[df['Department'].isna(), 'Department'] = inferred_department

# Ensure Date_of_Birth is in datetime format
df['Date_of_Birth'] = pd.to_datetime(df['Date_of_Birth'], errors='coerce')

# Calculate the age based on Date_of_Birth
df['Age'] = (pd.to_datetime('today') - df['Date_of_Birth']).dt.days // 365

# Identify and cap outliers using the IQR method
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR  # -255312.5
upper_bound = Q3 + 1.5 * IQR  # 570187.5

df['Salary'] = np.where(df['Salary'] < lower_bound, lower_bound, df['Salary'])
df['Salary'] = np.where(df['Salary'] > upper_bound, upper_bound, df['Salary'])

# Normalizing department names
df['Department'] = df['Department'].replace('not_specified', np.nan)
df['Department'] = df['Department'].fillna('Unknown')

# Calculate the average salary per department
average_salary_per_dept = df.groupby('Department')['Salary'].mean()
print("Average Salary per Department:")
print(average_salary_per_dept)

# Find the top 3 highest-paid employees
top_3_employees = df.nlargest(3, 'Salary')
print("\nTop 3 Highest Paid Employees:")
print(top_3_employees[['Name', 'Salary']])

# Determine the number of employees in each department
employee_count_per_dept = df['Department'].value_counts()
print("\nNumber of Employees per Department:")
print(employee_count_per_dept)
