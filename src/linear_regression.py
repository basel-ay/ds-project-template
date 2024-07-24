import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from io import StringIO

# Load the dataset
data = """
Size,Bedrooms,Location,Price
2000,3,Urban,500000
1500,2,Suburban,350000
2500,4,Urban,750000
1800,3,Rural,200000
2200,3,Suburban,450000
1600,2,Urban,400000
2400,4,Rural,300000
1900,3,Urban,520000
1700,2,Suburban,370000
2300,4,Urban,680000
2100,3,Suburban,490000
1550,2,Rural,220000
2600,5,Urban,800000
1750,3,Suburban,410000
2000,3,Rural,280000
1650,2,Urban,390000
2450,4,Suburban,610000
1850,3,Rural,240000
1700,2,Urban,370000
2250,4,Suburban,640000
"""

df = pd.read_csv(StringIO(data))

# Encode 'Location' as a categorical variable using one-hot encoding
df = pd.get_dummies(df, columns=['Location'], drop_first=True)

# Define features (X) and target variable (y)
X = df.drop('Price', axis=1)
y = df['Price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Output the results
print(f'Mean Absolute Error: {mae}')
print(f'R² Score: {r2}')
print('Model Coefficients:')
for feature, coef in zip(X.columns, model.coef_):
    print(f'{feature}: {coef}')
