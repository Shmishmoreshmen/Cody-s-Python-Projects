#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Loading and Analyzing a CSV File
import pandas as pd

# Load a sample dataset (change 'data.csv' to your file)
df = pd.read_csv("data.csv")

# Display the first few rows
print(df.head())

# Get basic statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())


# In[ ]:


# Basic Statistical Analysis
import numpy as np

# Sample data
data = [12, 15, 14, 10, 9, 17, 21, 20]

# Mean, Median, Standard Deviation
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))

# Find the maximum and minimum values
print("Max:", np.max(data))
print("Min:", np.min(data))


# In[ ]:


# Data Visualization with Matplotlib
import matplotlib.pyplot as plt

# Sample data
years = [2015, 2016, 2017, 2018, 2019, 2020]
sales = [500, 600, 750, 900, 1100, 1300]

# Create a simple line plot
plt.plot(years, sales, marker="o", linestyle="-", color="b", label="Sales Growth")

# Add labels and title
plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Company Sales Over Years")
plt.legend()
plt.grid()

# Show the plot
plt.show()


# In[ ]:


# Grouping and Aggregation (Pandas)
# Create a sample DataFrame
df = pd.DataFrame({
    "Category": ["A", "B", "A", "C", "B", "C", "A"],
    "Sales": [100, 200, 150, 300, 250, 400, 120]
})

# Group by category and sum sales
category_sales = df.groupby("Category")["Sales"].sum()
print(category_sales)


# In[ ]:


# Correlation Analysis
# Create a simple DataFrame
df = pd.DataFrame({
    "Temperature": [30, 35, 40, 45, 50],
    "Ice Cream Sales": [200, 250, 300, 350, 400]
})

# Compute correlation
correlation = df.corr()
print(correlation)


# In[ ]:


# file reading from file path
file_path = r"C:\Users\JohnDoe\Desktop\data.txt"  # Update with your actual path

# Open the file and read its content
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# Print the content
print(content)


# In[ ]:


# Simple column selection from a csv file (excel)
import pandas as pd

# File path (update with your actual path)
file_path = r"C:\Users\John\Desktop\data.xlsx"  # Change this to your actual file path

# Read the Excel file
df = pd.read_excel(file_path)  # Reads the first sheet by default

# Select specific columns by name
selected_columns = df[['Column1', 'Column2']]  # Replace with actual column names

# Display the selected columns
print(selected_columns)


# In[ ]:


# Example of differant graphs
import pandas as pd
import matplotlib.pyplot as plt

# File path (update with your actual path)
file_path = r"C:\Users\John\Desktop\data.xlsx"  # Change this to your actual file path

# Read the Excel file
df = pd.read_excel(file_path)  # Reads the first sheet by default

# Select specific columns by name (update with actual column names)
selected_columns = df[['Date', 'Product']]  # Replace with your column names

# Plot the selected columns
plt.figure(figsize=(10, 5))  # Set figure size
plt.plot(df['Column1'], df['Column2'], marker='o', linestyle='-')  # Line plot with markers
# Bar graph
df.plot(kind='bar', x='Column1', y='Column2', figsize=(10, 5), legend=False)
plt.title("Bar Chart of Column1 vs Column2")

plt.scatter(df['Column1'], df['Column2'], color='red')

# Customize the graph
plt.xlabel('Column1 Label')  # Replace with actual label
plt.ylabel('Column2 Label')  # Replace with actual label
plt.title('Graph of Column1 vs Column2')  # Title of the graph
plt.grid(True)  # Add grid for better readability

# Show the plot
plt.show()


# In[ ]:


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


# In[ ]:


# If you're unsure of the column names, print them first:
print(df.columns)
# If your Excel file has multiple sheets, specify the sheet name:
df = pd.read_excel(file_path, sheet_name='Sheet1')
# If column names contain spaces or special characters, you might need:
df.columns = df.columns.str.strip()  # Removes spaces from column names


# In[ ]:


# adding in new columns to exsiting excel file

import pandas as pd

# File path (update with your actual path)
file_path = r"C:\Users\John\Desktop\data.xlsx"  # Change this to your actual file path

# Read the Excel file
df = pd.read_excel(file_path)

# Add a new column with data
df['New_Column'] = ['Value1', 'Value2', 'Value3', 'Value4']  # Adjust based on your data

# Save the modified DataFrame back to the Excel file
df.to_excel(file_path, index=False, engine='openpyxl')

print("New column added successfully!")


# In[ ]:


# grabbing columns from a excel file then graphing those columns based upon what 
# column x and column y given by the user and input.

import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

# Open file dialog to select an Excel file
Tk().withdraw()  # Hide the main Tkinter window
file_path = filedialog.askopenfilename(title="Select an Excel File", filetypes=[("Excel Files", "*.xlsx"), ("Excel Files", "*.xls")])

# Check if a file was selected
if not file_path:
    print("No file selected. Exiting program.")
    exit()

# Read the selected Excel file
df = pd.read_excel(file_path)

# Display column names
print("Available columns in the file:", df.columns.tolist())

# Ask user for column names
column_x = input("Enter a column name for x-axis: ").strip()
column_y = input("Enter a column name for y-axis: ").strip()

# Check if selected columns exist
if column_x not in df.columns or column_y not in df.columns:
    print(f"Error: Selected columns '{column_x}' or '{column_y}' not found in the file.")
    exit()

# Convert Date column if it's selected
if column_x.lower() == "date":
    df[column_x] = pd.to_datetime(df[column_x], errors='coerce')  # Convert to datetime format
    df = df.dropna(subset=[column_x])  # Drop invalid dates
    df = df.sort_values(by=column_x)  # Sort data by date

# Convert numeric data properly
df[column_y] = pd.to_numeric(df[column_y], errors='coerce')

# Drop NaN rows
df = df.dropna(subset=[column_x, column_y])

# If no valid data remains
if df.empty:
    print("\nNo valid data available after cleaning. Check the Excel file.")
    exit()

# Plot the selected columns
plt.figure(figsize=(10, 5))
plt.plot(df[column_x], df[column_y], marker='o', linestyle='-')

# Customize the graph
plt.xlabel(column_x)
plt.ylabel(column_y)
plt.title(f'Graph of {column_x} vs {column_y}')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)

# Show the plot
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog, Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create main Tkinter window
root = Tk()
root.title("Excel Data Plotter")
root.geometry("800x600")  # Set window size

# Open file dialog to select an Excel file
root.withdraw()  # Hide the main Tkinter window while selecting file
file_path = filedialog.askopenfilename(
    title="Select an Excel File", 
    filetypes=[("Excel Files", "*.xlsx"), ("Excel Files", "*.xls")]
)
root.deiconify()  # Show the main window again

# Check if a file was selected
if not file_path:
    print("No file selected. Exiting program.")
    exit()

# Read the selected Excel file
df = pd.read_excel(file_path)  # Reads the first sheet by default

# Display column names to help the user
print("Available columns in the file:", df.columns.tolist())

# Ask user for column names
#column_x = input("Enter a column name for x-axis: ").strip()  # Remove leading/trailing spaces
#column_y = input("Enter a column name for y-axis: ").strip()
column_x = simpledialog.askstring("Input", "Enter a column name for x-axis:")
column_y = simpledialog.askstring("Input", "Enter a column name for y-axis:")


# Check if selected columns exist
if column_x not in df.columns or column_y not in df.columns:
    print(f"Error: Selected columns '{column_x}' or '{column_y}' not found in the file.")
    exit()

# Convert data to numeric to avoid plotting errors
df[column_x] = pd.to_numeric(df[column_x], errors='coerce')  # Convert to numbers, set errors to NaN
df[column_y] = pd.to_numeric(df[column_y], errors='coerce')

# Drop rows where data is missing
df = df.dropna(subset=[column_x, column_y])

if df.empty:
    print("No valid data available for plotting. Exiting.")
    exit()

# Create Matplotlib figure
fig, ax = plt.subplots(figsize=(8, 5))  # Set figure size
ax.plot(df[column_x].to_numpy(), df[column_y].to_numpy(), marker='.', linestyle='-')  # ✅ FIXED

# Customize the graph
ax.set_xlabel(column_x)
ax.set_ylabel(column_y)
ax.set_title(f'Graph of {column_x} vs {column_y}')
ax.grid(True)

# Embed Matplotlib figure into Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)  # Create canvas for figure
canvas.draw()
canvas.get_tk_widget().pack(fill="both", expand=True)  # Display graph

# Add an exit button
Button(root, text="Exit", command=root.quit).pack(pady=10)

# Run the Tkinter main loop
root.mainloop()


# In[ ]:


# updated version of grabbing columns based upon users input and graphing that information
# on a x and y axis.
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog, simpledialog, Toplevel, Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys

# Open file dialog to select an Excel file
Tk().withdraw()  # Hide the main Tkinter window
file_path = filedialog.askopenfilename(
    title="Select an Excel File", 
    filetypes=[("Excel Files", "*.xlsx"), ("Excel Files", "*.xls")]
)

# Check if a file was selected
if not file_path:
    print("No file selected. Exiting program.")
    sys.exit()

# Read the selected Excel file
df = pd.read_excel(file_path)  # Reads the first sheet by default

# Display column names to help the user
print("Available columns in the file:", df.columns.tolist())

# Ask user for column names using a GUI dialog
root = Tk()
root.withdraw()  # Hide main Tkinter window

column_x = simpledialog.askstring("Input", "Enter a column name for x-axis:")
column_y = simpledialog.askstring("Input", "Enter a column name for y-axis:")

# Check if user provided input
if not column_x or not column_y:
    print("No input provided. Exiting.")
    sys.exit()

# Check if selected columns exist
if column_x not in df.columns or column_y not in df.columns:
    print(f"Error: Selected columns '{column_x}' or '{column_y}' not found in the file.")
    sys.exit()

# Drop rows where data is missing
df = df.dropna(subset=[column_x, column_y])

if df.empty:
    print("No valid data available for plotting. Exiting.")
    sys.exit()

# Function to display the graph in a new window
def show_graph():
    graph_window = Toplevel()  # Create a new top-level window
    graph_window.title("Graph Window")
    graph_window.geometry("900x600")  # Set window size

    # Create a Matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(df[column_x].to_numpy(), df[column_y].to_numpy(), marker='.', linestyle='-')

    # Customize the graph
    ax.set_xlabel(column_x)
    ax.set_ylabel(column_y)
    ax.set_title(f'Graph of {column_x} vs {column_y}')
    ax.grid(True)

    # Embed Matplotlib figure into Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # Add an exit button
    Button(graph_window, text="Close", command=graph_window.destroy).pack(pady=10)

# Open the graph window
show_graph()

# Run the Tkinter main loop
root.mainloop()


# In[ ]:




