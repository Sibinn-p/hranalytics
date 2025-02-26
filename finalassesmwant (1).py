# -*- coding: utf-8 -*-
"""finalassesmwant.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Atz54n5uqIW2MnjsmoYQ75RVGCGTC49N
"""

# Commented out IPython magic to ensure Python compatibility.

# import python libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # visualizing data
# %matplotlib inline
import seaborn as sns

df=pd.read_csv('train_LZdllcl.csv')

dft=pd.read_csv('test_2umaH9m.csv')

df.shape

dft.shape

df.head()

dft.head()

df.info()

dft.info()

pd.isnull(df).sum()

pd.isnull(dft).sum()

df.duplicated().sum()

dft.duplicated().sum()

df.dropna(inplace=True)

dft.dropna(inplace=True)

def detect_outliers_iqr(data):
  Q1 = data.quantile(0.25)
  Q3 = data.quantile(0.75)
  IQR = Q3 - Q1
  lower_bound = Q1 - 1.5 * IQR
  upper_bound = Q3 + 1.5 * IQR
  outliers = data[(data < lower_bound) | (data > upper_bound)]
  return outliers
for column in df.select_dtypes(include=['number']):
  outliers = detect_outliers_iqr(df[column])
  if not outliers.empty:
    print(f"Outliers in '{column}': {outliers.tolist()}")

plt.figure(figsize=(15, 10))
for i, column in enumerate(df.select_dtypes(include=['number']).columns):
  plt.subplot(3, 3, i + 1)  # Adjust the subplot grid as needed
  sns.boxplot(x=df[column])
  plt.title(column)
plt.tight_layout()
plt.show()

plt.figure(figsize=(15, 10))
for i, column in enumerate(df.select_dtypes(include=['number']).columns):
  plt.subplot(3, 3, i + 1)  # Adjust the subplot grid as needed
  sns.boxplot(x=df[column])
  plt.title(column)
plt.tight_layout()
plt.show()

plt.figure(figsize=(15, 10))
for i, column in enumerate(df.select_dtypes(include=['number']).columns):
  plt.subplot(3, 3, i + 1)  # Adjust the subplot grid as needed
  sns.boxplot(x=df[column])
  plt.title(column)
plt.tight_layout()
plt.show()

df.columns

dft.columns

ax = sns.countplot(x = 'gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)

ax = sns.countplot(data = df, x = 'education', hue = 'gender')

for bars in ax.containers:
    ax.bar_label(bars)

# Commented out IPython magic to ensure Python compatibility.
# prompt: Modeling

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # visualizing data
import seaborn as sns

# import python libraries

# %matplotlib inline



# Gender distribution
plt.figure(figsize=(8, 6))  # Adjust figure size for better visualization
ax = sns.countplot(x='gender', data=df)
ax.set_title('Distribution of Gender') # Add a title
ax.set_xlabel('Gender') # Add x-axis label
ax.set_ylabel('Count') # Add y-axis label
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Education level distribution by gender
plt.figure(figsize=(10, 6))  # Adjust figure size
ax = sns.countplot(data=df, x='education', hue='gender')
ax.set_title('Distribution of Education Levels by Gender') # Add a title
ax.set_xlabel('Education Level') # Add x-axis label
ax.set_ylabel('Count') # Add y-axis label
ax.tick_params(axis='x', rotation=45) # Rotate x-axis labels if needed
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# prompt: label encoding

from sklearn.preprocessing import LabelEncoder

# Initialize LabelEncoder
le = LabelEncoder()

# Iterate through categorical columns and apply label encoding
for column in ['gender', 'education']:  # Replace with your actual categorical column names
    df[column] = le.fit_transform(df[column])
    dft[column] = le.transform(dft[column]) # Apply the same encoding to the test set

# Display the updated DataFrame
print(df.head())
print(dft.head())

# prompt: Impute missing values in df

# Check for missing values in the DataFrame
print(df.isnull().sum())

# Impute missing values using the mean for numerical columns
for col in df.select_dtypes(include=['number']).columns:
    df[col].fillna(df[col].mean(), inplace=True)

# Impute missing values using the mode for categorical columns
for col in df.select_dtypes(include=['object', 'category']).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Verify that there are no more missing values
print(df.isnull().sum())

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder  # Import LabelEncoder

# Assuming 'df' is your DataFrame and 'target_column' is the name of the target variable column

# Separate features (X) and target variable (y)
# Perform Label Encoding before train_test_split to avoid data leakage
X = df.drop('is_promoted', axis=1)  # Replace 'target_column' with the actual name
# Initialize LabelEncoder
for col in X.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col]) # Fit and transform on the entire feature set



y = df['is_promoted']


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Initialize models
models = {
    "Logistic Regression": LogisticRegression(),
    "Random Forest": RandomForestClassifier(),
    "Support Vector Machine": SVC()
}


# Train and evaluate models
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = accuracy

# Find the best model
best_model = max(results, key=results.get)
print(f"The best model is {best_model} with an accuracy of {results[best_model]}")

# Find the best model
best_model = max(results, key=results.get)
print(f"The best model is {best_model} with an accuracy of {results[best_model]}")



# : fine tubbing


# Fine-tuning visualizations

# Gender distribution
plt.figure(figsize=(8, 6))
ax = sns.countplot(x='gender', data=df)
ax.set_title('Distribution of Gender', fontsize=14)  # Increased font size
ax.set_xlabel('Gender', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.tick_params(axis='both', labelsize=10) # Adjust tick label size

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')  # Improved annotation placement

plt.show()


# Education level distribution by gender
plt.figure(figsize=(12, 6))  # Wider figure for better label readability
ax = sns.countplot(data=df, x='education', hue='gender')
ax.set_title('Distribution of Education Levels by Gender', fontsize=14)
ax.set_xlabel('Education Level', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.tick_params(axis='x', rotation=45, labelsize=10)  # Rotate and adjust label size
ax.tick_params(axis='y', labelsize=10)

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')


plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.show()

# prompt: Replace the target column with the prediction value

# ... (Your existing code) ...

# Assuming 'df' is your DataFrame and you want to scale numerical features
numerical_cols = df.select_dtypes(include=['number']).columns

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Fit and transform the numerical columns
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# ... (Your existing code) ...

# Predict on the test set using the best model
if best_model == "Logistic Regression":
    best_model_instance = LogisticRegression()
elif best_model == "Random Forest":
    best_model_instance = RandomForestClassifier()
elif best_model == "Support Vector Machine":
    best_model_instance = SVC()
else:
    raise ValueError("Invalid best model name.")




# Replace the target column in the test set with predictions


# Now X_test contains the original features and the predicted 'is_promoted' values
print(X_test.head())

# prompt: dowload employee_id and is_promoted

import pandas as pd

# Load the DataFrame (assuming it's already loaded as 'df')
# ... (Your existing code to load the DataFrame) ...

# Select the 'employee_id' and 'is_promoted' columns
employee_data = df[['employee_id', 'is_promoted']]

# Save the selected data to a CSV file
employee_data.to_csv('employee_data.csv', index=False)

# prompt: download this as csv file in device

from google.colab import files
files.download('employee_data.csv')