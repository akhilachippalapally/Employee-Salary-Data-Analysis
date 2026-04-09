# =========================================================
# EMPLOYEE SALARY DATA ANALYSIS - FINAL CODE
# =========================================================

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================================================
# STEP 1: CREATE DATASET
# =========================================================

data = pd.DataFrame({
    'Employee_ID': [101,102,103,104,105,106,107,108,109,110],
    'Age': [22, 35, 45, 29, 41, 38, 26, 33, 50, 28],
    'Experience': [1, 5, 10, 3, 8, 6, 2, 4, 12, 3],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 
                   'IT', 'HR', 'Finance', 'IT'],
    'Salary': [25000, 60000, 90000, 45000, 75000, 70000, 
               30000, 50000, 95000, 40000]
})

print("\n========== DATASET CREATED ==========")
print(data)

# =========================================================
# STEP 2: DATA UNDERSTANDING
# =========================================================

print("\n--- FIRST 5 ROWS ---")
print(data.head())

print("\n--- LAST 5 ROWS ---")
print(data.tail())

print("\n--- DATASET INFO ---")
print(data.info())

# =========================================================
# STEP 3: DATA CLEANING
# =========================================================

print("\n--- MISSING VALUES ---")
print(data.isnull().sum())

print("\n--- DUPLICATES ---")
print(data.duplicated().sum())

# =========================================================
# STEP 4: DESCRIPTIVE STATISTICS
# =========================================================

print("\n--- STATISTICAL SUMMARY ---")
print(data.describe())

# =========================================================
# STEP 5: SALARY DISTRIBUTION ANALYSIS
# =========================================================

plt.figure()
plt.hist(data['Salary'], bins=5)
plt.title("Salary Distribution of Employees")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.show()

# =========================================================
# STEP 6: DEPARTMENT-WISE ANALYSIS
# =========================================================

dept_salary = data.groupby('Department')['Salary'].mean()

print("\n--- AVERAGE SALARY BY DEPARTMENT ---")
print(dept_salary)

plt.figure()
plt.bar(dept_salary.index, dept_salary.values)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

# =========================================================
# STEP 7: EXPERIENCE-BASED SEGMENTATION
# =========================================================

data['Experience_Level'] = pd.cut(
    data['Experience'],
    bins=[0, 3, 6, 12],
    labels=['Low', 'Medium', 'High']
)

exp_salary = data.groupby('Experience_Level')['Salary'].mean()

print("\n--- SALARY BASED ON EXPERIENCE LEVEL ---")
print(exp_salary)

plt.figure()
plt.bar(exp_salary.index.astype(str), exp_salary.values)
plt.title("Salary vs Experience Level")
plt.xlabel("Experience Level")
plt.ylabel("Average Salary")
plt.show()

# =========================================================
# STEP 8: AGE VS SALARY ANALYSIS
# =========================================================

plt.figure()
plt.scatter(data['Age'], data['Salary'])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

# =========================================================
# STEP 9: CORRELATION ANALYSIS
# =========================================================

correlation = data.corr(numeric_only=True)

print("\n--- CORRELATION MATRIX ---")
print(correlation)

# =========================================================
# STEP 10: FINAL INSIGHTS
# =========================================================

print("\n========== FINAL INSIGHTS ==========")
print("1. Employees with higher experience tend to earn higher salaries.")
print("2. Salary differs across departments based on job roles.")
print("3. Positive relationship exists between age and salary.")
print("4. Experience is the most important factor influencing salary.")