
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("student.csv")

# Display first five records
print(df.head())

# Display dataset information
print(df.info())

# Calculate marks
print("Average:", df["Marks"].mean())
print("Maximum:", df["Marks"].max())
print("Minimum:", df["Marks"].min())

# Students scoring above 75
print(df[df["Marks"] > 75])

# Bar chart
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Name")
plt.ylabel("Marks")
plt.title("Student Performance")
plt.show()

# Histogram
plt.hist(df["Marks"])
plt.title("Marks Distribution")
plt.show()

# Scatter plot
plt.scatter(df["Study_Hours"], df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()

