#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Simplified data analysis program that has the user enter column names to extract and 
# graph from a excel file.
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

# Open file dialog to select an Excel file
Tk().withdraw()  # Hide the main Tkinter window
file_path = filedialog.askopenfilename(
    title="Select an Excel File", 
    filetypes=[("Excel Files", "*.xlsx"), ("Excel Files", "*.xls")]
)

# Check if a file was selected
if not file_path:
    print("No file selected. Exiting program.")
    exit()

# Read the selected Excel file
df = pd.read_excel(file_path)  # Reads the first sheet by default

# Display column names to help the user
print("Available columns in the file:", df.columns.tolist())

# Ask user for column names
column_x = input("Enter a column name for x-axis: ").strip()  # Remove leading/trailing spaces
column_y = input("Enter a column name for y-axis: ").strip()

# Check if selected columns exist
if column_x not in df.columns or column_y not in df.columns:
    print(f"Error: Selected columns '{column_x}' or '{column_y}' not found in the file.")
    exit()

# Convert data to numeric to avoid plotting errors
#df[column_x] = pd.to_numeric(df[column_x], errors='coerce')  # Convert to numbers, set errors to NaN
#df[column_y] = pd.to_numeric(df[column_y], errors='coerce')

print("\nData Types After Conversion:")
print(df[[column_x, column_y]].dtypes)


# Drop rows where data is missing
#df = df.dropna(subset=[column_x, column_y])
if df.empty:
    print("No valid data available for plotting. Exiting.")
    exit()

# Plot the selected columns
plt.figure(figsize=(10, 5))  # Set figure size
plt.plot(df[column_x].to_numpy(), df[column_y].to_numpy(), marker='.', linestyle='-')  # Convert to NumPy before plotting

# Customize the graph
plt.xlabel(column_x)
plt.ylabel(column_y)
plt.title(f'Graph of {column_x} vs {column_y}')
plt.grid(True)

# Show the plot
plt.show()

