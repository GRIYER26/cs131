# -*- coding: utf-8 -*-
"""a5-Rajshri.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R3ezyjCAY4yJWNUTUmKxOHBRfTVhvGg2

**Assignment 5 - Rajshri Ganesh Iyer**

**Dataset** **used**: Breast Cancer Wisconsin Dataset (Diagnostic)

**Link to Dataset** https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic

**Link to Kaggle Dataset**: https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data/data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

#Reading the csv as a dataframe
bc_df = pd.read_csv('/content/data.csv')
bc_df

#replacing Malignant with 1 and Benign with 0 in the data frame
bc_df['diagnosis'] = bc_df['diagnosis'].replace('M', 1)
bc_df['diagnosis'] = bc_df['diagnosis'].replace('B', 0)
bc_df

#Printing Row and Column Info
print(f'row information: {bc_df.index}')
print(f'col information: {bc_df.columns}')

# Dropping Standard Error Values and Worst values for the 10 physical features, and only retaining Mean values
columns_to_delete = ['radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst', 'Unnamed: 32']
bc_df = bc_df.drop(columns=columns_to_delete)

#Printing updated row and columnn information
print(f'row information: {bc_df.index}')
print(f'col information: {bc_df.columns}')

#Printing the count, mean, min, max, std deviation, percentiles for each feature
bc_df.describe()

#Calculating and printing the correlation matrix for all the features
correlation_matrix = bc_df.corr()
print(correlation_matrix)

#Plotting the Correlation Matrix
plt.figure(figsize=(10, 10))
sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Matrix')
plt.show()

#Plotting a Cluster map for the Correlation Matrix for better visualization"
plt.figure(figsize=(10, 10))
sns.clustermap(correlation_matrix, annot=True)
plt.title('Cluster map for Correlation Matrix')
plt.show()

#Plotting Violin Plots for the features that showed high correlation with diagnosis

#Violin Plot of Diagnosis vs. Mean Compactness Values
sns.violinplot(data=bc_df, x='diagnosis', y='compactness_mean', hue='diagnosis')
plt.legend(loc='upper right')
plt.xticks(ticks=[0, 1], labels=['Benign', 'Malignant'])
plt.xlabel('Diagnosis')
plt.ylabel('Mean Compactness')
plt.title('Violin Plot of Diagnosis vs. Mean Compactness Values')
plt.show()

#Violin Plot of Diagnosis vs. Mean Concavity Values
sns.violinplot(data=bc_df, x='diagnosis', y='concavity_mean', hue='diagnosis')
plt.legend(loc='upper right')
plt.xticks(ticks=[0, 1], labels=['Benign', 'Malignant'])
plt.xlabel('Diagnosis')
plt.ylabel('Mean Concavity')
plt.title('Violin Plot of Diagnosis vs. Mean Concavity Values')
plt.show()

#Violin Plot of Diagnosis vs. Mean Concave Points Values
sns.violinplot(data=bc_df, x='diagnosis', y='concave points_mean', hue='diagnosis')
plt.legend(loc='upper right')
plt.xticks(ticks=[0, 1], labels=['Benign', 'Malignant'])
plt.xlabel('Diagnosis')
plt.ylabel('Mean Concave Points')
plt.title('Violin Plot of Diagnosis vs. Mean Concave Points Values')
plt.show()

#Violin Plot of Diagnosis vs. Mean Perimeter Values
sns.violinplot(data=bc_df, x='diagnosis', y='perimeter_mean', hue='diagnosis')
plt.legend(loc='upper right')
plt.xticks(ticks=[0, 1], labels=['Benign', 'Malignant'])
plt.xlabel('Diagnosis')
plt.ylabel('Mean Perimeter')
plt.title('Violin Plot of Diagnosis vs. Mean Perimeter Values')
plt.show()

#Violin Plot of Diagnosis vs. Mean Radius Values
sns.violinplot(data=bc_df, x='diagnosis', y='radius_mean', hue='diagnosis')
plt.legend(loc='upper right')
plt.xticks(ticks=[0, 1], labels=['Benign', 'Malignant'])
plt.xlabel('Diagnosis')
plt.ylabel('Mean Radius')
plt.title('Violin Plot of Diagnosis vs. Mean Radius Values')
plt.show()

#Violin Plot of Diagnosis vs. Mean Area Values
sns.violinplot(data=bc_df, x='diagnosis', y='area_mean', hue='diagnosis')
plt.legend(loc='upper right')
plt.xticks(ticks=[0, 1], labels=['Benign', 'Malignant'])
plt.xlabel('Diagnosis')
plt.ylabel('Mean Area')
plt.title('Violin Plot of Diagnosis vs. Mean Area Values')
plt.show()

#Step 1 - Reading Feature Names as X and target name as y
X = bc_df[['compactness_mean','concavity_mean','concave points_mean','perimeter_mean','radius_mean','area_mean']] #feature names
y = bc_df['diagnosis'] #target name

#Step 2 - Splitting data for testing and training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Step 3 - Using a Linear Regression model for fitting
model = LinearRegression()
model.fit(X_train, y_train)

#Step 5 - Predicting the y values
y_pred = model.predict(X_test)

#Step 6 - Evaluating the Linear Regression model - R2, MSE, model intercept and coeff
print("Mean squared error:", mean_squared_error(y_test, y_pred))
print("R-squared:", r2_score(y_test, y_pred))
print(f'b0 (model intercept)         = {model.intercept_}')
print(f'b1 (coeff for compactness)   = {model.coef_[0]}')
print(f'b2 (coeff for concavity)     = {model.coef_[1]}')
print(f'b3 (coeff for concave points)= {model.coef_[2]}')
print(f'b4 (coeff for perimeter)     = {model.coef_[3]}')
print(f'b5 (coeff for radius)        = {model.coef_[4]}')
print(f'b6 (coeff for area)          = {model.coef_[5]}')

#Plotting the regression lines for the 6 features used for Linear Regression model
sns.pairplot(bc_df, x_vars=['compactness_mean', 'concavity_mean', 'concave points_mean'], y_vars="diagnosis", kind="reg")
plt.show()
sns.pairplot(bc_df, x_vars=['area_mean', 'perimeter_mean', 'radius_mean'], y_vars="diagnosis", kind="reg")
plt.show()