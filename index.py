#Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Adjustments
sns.set(style = "whitegrid")

#Dataset Loading
df = pd.read_csv("PCOS_data.csv")
print(df.info())

#Dataset Cleaning
df.columns = df.columns.str.strip()
df.drop(columns=["Sl. No", "Patient File No.", "Unnamed: 44"], inplace = True)
print(df.info())

#Handling Non-Numeric Data
df["II    beta-HCG(mIU/mL)"] = pd.to_numeric(df["II    beta-HCG(mIU/mL)"], errors= "coerce")
df["AMH(ng/mL)"] = pd.to_numeric(df["AMH(ng/mL)"], errors= "coerce")

#Handling missing Values
df["Marraige Status (Yrs)"] = df["Marraige Status (Yrs)"].fillna(df["Marraige Status (Yrs)"].median())
df["Fast food (Y/N)"] = df["Fast food (Y/N)"].fillna(df["Fast food (Y/N)"].mode()[0])

#Check for Duplicate Rows
print("Duplicate rows:", df.duplicated().sum())

#PCOS Analysis
plt.figure(figsize = (6,4))
sns.countplot(x = "PCOS (Y/N)", data = df)
plt.title("PCOS Analysis")
plt.xlabel("PCOS (NO = 0, Yes = 1)")
plt.ylabel("Count")
plt.show()

#Histogram Analysis of Numerical Features
num_cols = df.select_dtypes(include=['int64', 'float64']).drop(columns=['PCOS (Y/N)']).columns
n_cols = 4
n_rows = (len(num_cols) + n_cols - 1) // n_cols
df[num_cols].hist(bins=20, figsize=(20, n_rows * 4), layout=(n_rows, n_cols))
plt.suptitle("Histograms of Numerical Features", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.98])
plt.show()


#Correlation Analysis
plt.figure(figsize=(18, 16))
corr = df.corr()
sns.heatmap(corr, annot=False, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

#Boxplot Analysis
plt.figure(figsize = (6,4))
sns.boxplot( x = "PCOS (Y/N)", y = "BMI", data = df)
plt.title("BMI vs PCOS")
plt.show()

plt.figure(figsize = (6,4))
df['Age Group'] = pd.cut(df['Age (yrs)'], bins=[15, 20, 25, 30, 35, 40])
df.groupby('Age Group')['PCOS (Y/N)'].mean().plot(kind='line')
plt.show()