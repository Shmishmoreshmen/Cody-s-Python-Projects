#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from ipywidgets import interact, FloatSlider

# Generate some example data (you can replace this with your own data)
x_data = np.linspace(0, 10, 100)  # More data points for increased accuracy
y_data = 10 * np.exp(-0.5 * x_data)  # Example downward sloping data

# Define the model function for exponential decay
def model_function(x, a, b):
    return a * np.exp(-b * x)

# Interactive curve fitting function
def fit_curve(a_guess, b_guess):
    # Fit the curve to the data
    popt, _ = curve_fit(model_function, x_data, y_data, p0=[a_guess, b_guess])

    # Generate points for the fitted curve
    x_fit = np.linspace(min(x_data), max(x_data), 1000)  # More points for smoother curve
    y_fit = model_function(x_fit, *popt)

    # Clear previous plot
    plt.clf()

    # Plot the original data points
    plt.scatter(x_data, y_data, label='Original Data')

    # Plot the fitted curve
    plt.plot(x_fit, y_fit, 'r-', label='Fitted Curve')

    # Add labels and legend
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()

    # Show plot
    plt.show()

    # Print the parameters of the fitted curve
    print("Parameters of the fitted curve:")
    for i, param in enumerate(popt):
        print(f"Parameter {i+1}: {param}")

# Set up sliders for interactive control
a_slider = FloatSlider(value=10.0, min=0.1, max=20.0, step=0.01, description='a:')
b_slider = FloatSlider(value=0.5, min=0.1, max=1.0, step=0.001, description='b:')

# Create interactive plot
interact(fit_curve, a_guess=a_slider, b_guess=b_slider)


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from ipywidgets import interact, FloatSlider, Layout
from matplotlib.widgets import Cursor
from matplotlib.lines import Line2D

# Function to read data from a file
def read_data(file_path, x_column, y_column):
    data = np.loadtxt(file_path)
    x_data = data[:, x_column]
    y_data = data[:, y_column]
    return x_data, y_data

# Define the model function for exponential decay
def model_function(x, a, b):
    return a * np.exp(-b * x)

# Interactive curve fitting function
def fit_curve(file_path, x_column, y_column, a_guess, b_guess):
    # Read data from the file
    x_data, y_data = read_data(file_path, x_column, y_column)

    # Fit the curve to the data
    popt, _ = curve_fit(model_function, x_data, y_data, p0=[a_guess, b_guess])

    # Generate points for the fitted curve
    x_fit = np.linspace(min(x_data), max(x_data), 1000)  # More points for smoother curve
    y_fit = model_function(x_fit, *popt)

    # Clear previous plot
    plt.clf()

    # Plot the original data points
    plt.scatter(x_data, y_data, label='Original Data')

    # Plot the fitted curve
    plt.plot(x_fit, y_fit, 'r-', label='Fitted Curve')

    # Add labels and legend
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()

    # Add interactive points for modifying the curve
    cursor = Cursor(plt.gca(), useblit=True, color='blue', linewidth=1)
    line = Line2D(x_fit, y_fit, color='r', linewidth=1, pickradius=5)  # Pickradius enables dragging points
    plt.gca().add_line(line)

    def on_pick(event):
        if event.artist == line:
            x_event, y_event = event.mouseevent.xdata, event.mouseevent.ydata
            x_fit[event.ind[0]] = x_event
            y_fit[event.ind[0]] = y_event
            line.set_data(x_fit, y_fit)
            popt, _ = curve_fit(model_function, x_fit, y_fit, p0=[a_guess, b_guess])
            line.set_ydata(model_function(x_fit, *popt))
            plt.draw()

    plt.gcf().canvas.mpl_connect('pick_event', on_pick)

    # Show plot
    plt.show()

    # Print the parameters of the fitted curve
    print("Parameters of the fitted curve:")
    for i, param in enumerate(popt):
        print(f"Parameter {i+1}: {param}")

# Set up sliders for interactive control
a_slider = FloatSlider(value=10.0, min=0.1, max=20.0, step=0.01, description='a:', layout=Layout(width='50%'))
b_slider = FloatSlider(value=0.5, min=0.1, max=1.0, step=0.001, description='b:', layout=Layout(width='50%'))

# Get user input for file path and column indices
file_path = input("Enter the file path: ")
x_column = int(input("Enter the index of the column for x data: "))
y_column = int(input("Enter the index of the column for y data: "))

# Create interactive plot
interact(fit_curve, file_path=file_path, x_column=x_column, y_column=y_column, a_guess=a_slider, b_guess=b_slider)


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from ipywidgets import interact, FloatSlider, Layout
from matplotlib.widgets import Cursor
from matplotlib.lines import Line2D
import tkinter as tk
from tkinter import filedialog, simpledialog

import pandas as pd

def read_data(file_path, x_column_letter, y_column_letter, start_row):
    try:
        # Read data from Excel file, specifying columns by their letters
        df = pd.read_excel(file_path, usecols=[x_column_letter, y_column_letter])

        # Skip rows if necessary
        if start_row > 1:
            df = df.iloc[start_row - 1:]

        # Extract data from specified columns
        x_data = df.iloc[:, 0].values.astype(float)
        y_data = df.iloc[:, 1].values.astype(float)

        return x_data, y_data
    
    except Exception as e:
        print("Error reading data from file:", e)
        return None, None
    
# Function to convert Excel column letter to index
def column_letter_to_index(letter):
    return ord(letter.upper()) - ord('A')

# Define the model function for power law
def power_law_model(x, a, b):
    #return a * np.power(x, b)
    return a * np.exp(-b * x)

# Function to get user input for file path, column letters, and starting row
def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file explorer window to select file
    file_path = filedialog.askopenfilename(title="Select a file")

    # Get column letters for x and y data
    x_column_letter = simpledialog.askstring("Input", "Enter the column letter for x data:")
    y_column_letter = simpledialog.askstring("Input", "Enter the column letter for y data:")

    # Convert column letters to indices
    x_column_index = column_letter_to_index(str(x_column_letter))
    y_column_index = column_letter_to_index(str(y_column_letter))
    
    # Get starting row
    start_row = simpledialog.askinteger("Input", "Enter the starting row for data (1-indexed):")

    return file_path, x_column_index, y_column_index, start_row

def fit_curve(x_data, y_data):
    try:
        # Fit the curve to the data
        popt, _ = curve_fit(power_law_model, x_data, y_data)

        # Clear previous plot
        #plt.clf()
        
        # Plot the fitted curve without generating points
        x_fit = np.linspace(min(x_data), max(x_data), 20000)  # More points for smoother curve
        y_fit = power_law_model(x_fit, *popt)

        # Plot the original data points
        plt.scatter(x_data, y_data, label='Original Data')
        plt.plot(x_fit, y_fit, 'g-', label='Fitted Curve')  # Green color for the fitted curve

        # Add labels and legend
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()

        # Show plot
        plt.show()

        # Print the parameters of the fitted curve
        print("Parameters of the fitted curve:")
        for i, param in enumerate(popt):
            print(f"Parameter {i+1}: {param}")
    except Exception as e:
        print("Error fitting curve:", e)
        
# Set up sliders for interactive control
#a_slider = FloatSlider(value=10.0, min=0.1, max=20.0, step=0.01, description='a:', layout=Layout(width='50%'))
#b_slider = FloatSlider(value=0.5, min=0.1, max=1.0, step=0.001, description='b:', layout=Layout(width='50%'))

# Get user input for file path, column letters, and starting row
file_path, x_column, y_column, start_row = get_user_input()

# Read data from the file
x_data, y_data = read_data(file_path, x_column, y_column, start_row)

# Create interactive plot
fit_curve(x_data, y_data)


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from ipywidgets import interact, FloatSlider, Layout
from matplotlib.widgets import Cursor
from matplotlib.lines import Line2D
import tkinter as tk
from tkinter import filedialog, simpledialog

import pandas as pd

def read_data(file_path, x_column_letter, y_column_letter, start_row):
    try:
        # Read data from Excel file, specifying columns by their letters
        df = pd.read_excel(file_path, usecols=[x_column_letter, y_column_letter])

        # Skip rows if necessary
        if start_row > 1:
            df = df.iloc[start_row - 1:]

        # Extract data from specified columns
        x_data = df.iloc[:, 0].values.astype(float)
        y_data = df.iloc[:, 1].values.astype(float)

        return x_data, y_data
    
    except Exception as e:
        print("Error reading data from file:", e)
        return None, None
    
# Function to convert Excel column letter to index
def column_letter_to_index(letter):
    return ord(letter.upper()) - ord('A')

# Define the model function for power law
def power_law_model(x, a, b):
    return a * np.exp(-b * x)

# Function to get user input for file path, column letters, and starting row
def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file explorer window to select file
    file_path = filedialog.askopenfilename(title="Select a file")

    # Get column letters for x and y data
    x_column_letter = simpledialog.askstring("Input", "Enter the column letter for x data:")
    y_column_letter = simpledialog.askstring("Input", "Enter the column letter for y data:")

    # Convert column letters to indices
    x_column_index = column_letter_to_index(str(x_column_letter))
    y_column_index = column_letter_to_index(str(y_column_letter))
    
    # Get starting row
    start_row = simpledialog.askinteger("Input", "Enter the starting row for data (1-indexed):")

    return file_path, x_column_index, y_column_index, start_row

def fit_curve(x_data, y_data):
    try:
        # Fit a polynomial of degree 1 (a straight line) to the data
        coeffs = np.polyfit(x_data, y_data, 9.5)

        # Generate the line of best fit using the fitted coefficients
        line_of_best_fit = np.polyval(coeffs, x_data)

        # Clear previous plot
        plt.clf()
        
        # Plot the data points
        plt.scatter(x_data, y_data, label='Original Data')

        # Plot the line of best fit
        plt.plot(x_data, line_of_best_fit, 'g-', label='Line of Best Fit')

        # Add labels and legend
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()

        # Show plot
        plt.show()

        # Print the coefficients of the line of best fit
        print("Coefficients of the line of best fit:")
        print("Slope:", coeffs[0])
        print("Intercept:", coeffs[1])
    except Exception as e:
        print("Error fitting curve:", e)
        
# Set up sliders for interactive control
#a_slider = FloatSlider(value=10.0, min=0.1, max=20.0, step=0.01, description='a:', layout=Layout(width='50%'))
#b_slider = FloatSlider(value=0.5, min=0.1, max=1.0, step=0.001, description='b:', layout=Layout(width='50%'))

# Get user input for file path, column letters, and starting row
file_path, x_column, y_column, start_row = get_user_input()

# Read data from the file
x_data, y_data = read_data(file_path, x_column, y_column, start_row)

# Create interactive plot
fit_curve(x_data, y_data)


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from ipywidgets import interact, FloatSlider, Layout
from matplotlib.widgets import Cursor
from matplotlib.lines import Line2D
import tkinter as tk
from tkinter import filedialog, simpledialog

import pandas as pd

def read_data(file_path, x_column_letter, y_column_letter, start_row):
    try:
        # Read data from Excel file, specifying columns by their letters
        df = pd.read_excel(file_path, usecols=[x_column_letter, y_column_letter])

        # Skip rows if necessary
        if start_row > 1:
            df = df.iloc[start_row - 1:]

        # Extract data from specified columns
        x_data = df.iloc[:, 0].values.astype(float)
        y_data = df.iloc[:, 1].values.astype(float)

        return x_data, y_data
    
    except Exception as e:
        print("Error reading data from file:", e)
        return None, None
    
# Function to convert Excel column letter to index
def column_letter_to_index(letter):
    return ord(letter.upper()) - ord('A')

# Define the model function for power law
def gaussian_model(x, A, mu, sigma, offset):
    return A * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) + offset

def power_law_model(x, a, b):
    #return a * np.log(x) + b
    return a * np.power(x, b)
    #return a * np.exp(-b * x)

# Function to get user input for file path, column letters, and starting row
def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file explorer window to select file
    file_path = filedialog.askopenfilename(title="Select a file")

    # Get column letters for x and y data
    x_column_letter = simpledialog.askstring("Input", "Enter the column letter for x data:")
    y_column_letter = simpledialog.askstring("Input", "Enter the column letter for y data:")

    # Convert column letters to indices
    x_column_index = column_letter_to_index(str(x_column_letter))
    y_column_index = column_letter_to_index(str(y_column_letter))
    
    # Get starting row
    start_row = simpledialog.askinteger("Input", "Enter the starting row for data (1-indexed):")

    return file_path, x_column_index, y_column_index, start_row

def fit_curve(x_data, y_data, model_function):
    try:
        # Fit the curve to the data
        popt, _ = curve_fit(model_function, x_data, y_data)

        # Generate x values for the fitted curve
        x_fit = np.linspace(min(x_data), max(x_data), 200)  # Adjust the number of points for smoother curve

        # Calculate y values for the fitted curve using the optimized parameters
        y_fit = model_function(x_fit, *popt)

        # Clear previous plot
        plt.clf()

        # Plot the original data points
        plt.scatter(x_data, y_data, label='Original Data')

        # Plot the fitted curve
        plt.plot(x_fit, y_fit, 'g-', label='Fitted Curve')  # Green color for the fitted curve

        # Add labels and legend
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()

        # Show plot
        plt.show()

        # Print the parameters of the fitted curve
        print("Parameters of the fitted curve:")
        for i, param in enumerate(popt):
            print(f"Parameter {i+1}: {param}")
    except Exception as e:
        print("Error fitting curve:", e)
        
# Set up sliders for interactive control
#a_slider = FloatSlider(value=10.0, min=0.1, max=20.0, step=0.01, description='a:', layout=Layout(width='50%'))
#b_slider = FloatSlider(value=0.5, min=0.1, max=1.0, step=0.001, description='b:', layout=Layout(width='50%'))

# Get user input for file path, column letters, and starting row
file_path, x_column, y_column, start_row = get_user_input()

# Read data from the file
x_data, y_data = read_data(file_path, x_column, y_column, start_row)

# Create interactive plot
fit_curve(x_data, y_data, power_law_model)


# In[ ]:


pip install scipy


# In[ ]:


# Current working version of the program 

"""
Program Title: Curve Fitting Tool

Description:
This program provides a curve fitting tool for analyzing and visualizing data from Excel files. It allows users to fit various mathematical models to their data and visualize the fitted curve. Key features include:

1. Data Import: Users can import data from Excel files, specifying the columns containing the x and y data.

2. Interactive Interface: The program offers an interactive interface for selecting data files and adjusting parameters.

3. Curve Fitting: The core functionality includes fitting the selected model to the imported data, optimizing parameters for the best fit.

4. Initial Guess Estimation: Automatic estimation of initial guess parameters based on the imported data, facilitating the fitting process.

5. Visualization: The fitted curve is visualized alongside the original data points, providing insights into the relationship between variables.

6. Error Handling: The program includes error handling mechanisms to address issues such as incorrect file formats or fitting failures.

This tool is designed to be user-friendly, enabling researchers, engineers, and analysts to efficiently analyze and interpret their experimental or observational data.

Author: Cody Thompson

Version: 1.0

Date: March 25, 2024

"""

# Import Statements
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from ipywidgets import interact, FloatSlider, Layout
from matplotlib.widgets import Cursor
from matplotlib.lines import Line2D
import tkinter as tk
from tkinter import filedialog, simpledialog
import pandas as pd

# Function to read data from a excel file
def read_data(file_path, x_column_letter, y_column_letter, start_row):
    try:
        # Read data from Excel file, specifying columns by their letters
        df = pd.read_excel(file_path, usecols=[x_column_letter, y_column_letter])

        # Skip rows if necessary
        if start_row > 1:
            df = df.iloc[start_row - 1:]

        # Extract data from specified columns
        x_data = df.iloc[:, 0].values.astype(float)
        y_data = df.iloc[:, 1].values.astype(float)

        return x_data, y_data
    
    # Error Handler
    except Exception as e:
        print("Error reading data from file:", e)
        return None, None
    
# Function to convert Excel column letter to index
def column_letter_to_index(letter):
    return ord(letter.upper()) - ord('A')

# Define the model function for gaussian_model for fitted curve
# x: The independent variable, typically representing the input values.
# A: Amplitude or height of the Gaussian curve, controlling the peak value.
# mu: Mean of the Gaussian distribution, determining the center or peak location along the x-axis.
# sigma: Standard deviation of the Gaussian distribution, influencing the width of the curve.
# offset: An optional offset parameter, allowing the Gaussian curve to be shifted up or down along the y-axis.
#def gaussian_model(x, A, mu, sigma, offset):
    #return A * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) + offset

# Code blcok used for quick testing other models to fit the curve
##########################################################################

# power_law_model function for fitted curve
# a represents the coefficient that scales the power term.
# b represents the exponent.
# x is the independent variable

#def power_law_model(x, a, b):
    #return a * np.power(x, b)
    
# exponential_model function for fitted curve
# a represents the coefficient that scales the exponential term.
# b represents the rate of decay.
# x is the independent variable.

#def exponential_model(x, a, b)
    #return a * np.exp(-b * x)
    
# logarithmic_model function for fitted curve
# a represents the coefficient that scales the logarithmic term.
# np.log(x) is the natural logarithm of the independent variable x.
# b represents the intercept or offset.

#def logarithmic_model(x, a, b)
    #return a * np.log(x) + b
    
##########################################################################

# Function to get user input for file path, column letters, and starting row
def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file explorer window to select file
    file_path = filedialog.askopenfilename(title="Select a file")

    # Get column letters for x and y data
    x_column_letter = simpledialog.askstring("Input", "Enter the column letter for x data:")
    y_column_letter = simpledialog.askstring("Input", "Enter the column letter for y data:")

    # Convert column letters to indices
    x_column_index = column_letter_to_index(str(x_column_letter))
    y_column_index = column_letter_to_index(str(y_column_letter))
    
    # Get starting row
    start_row = simpledialog.askinteger("Input", "Enter the starting row for data (1-indexed):")

    return file_path, x_column_index, y_column_index, start_row

# Function to get user input for initial guess of U0
def get_initial_U0_guess():
    global initial_U0_guess
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt the user to enter the initial guess for U0
    initial_U0_guess = simpledialog.askfloat("Input", "Enter the initial guess for U0:")

    return initial_U0_guess

# Get user input for initial guess of U0
#initial_U0 = get_initial_U0_guess()

def pore_pressure_model(t, Umax, initial_U0=123, a=0.018, Ch=3.171e-7, T50=0.245, SQLr=0.8, B=1.5):
    U = Umax - (1 - 1 / (1 + (t * Ch / (T50 * a ** 2 * SQLr)))) * np.exp(B) * (Umax - initial_U0)
    return U

# Update fit_curve function to accept additional parameters
def fit_curve(x_data, y_data, model_function, initial_U0):
    try:
        
        if isinstance(initial_guess, (int, float)):
            initial_U0 = [initial_U0]
            
        # Fit the curve to the data with increased maxfev and different method
        popt, _ = curve_fit(pore_pressure_model, x_data, y_data, maxfev=50000, method='trf')
        
        # Generate x values for the fitted curve
        x_fit = np.linspace(min(x_data), max(x_data) + 1000, 5000)  # Adjust the number of points for smoother curve

        # Calculate y values for the fitted curve using the optimized parameters
        y_fit = pore_pressure_model(x_fit, *popt)

        # Clear previous plot
        plt.clf()

        # Plot the original data points
        plt.scatter(x_data, y_data, label='Original Data')

        # Plot the fitted curve
        plt.plot(x_fit, y_fit, 'g-', label='Fitted Curve')  # Green color for the fitted curve

        # Add labels and legend
        plt.xlabel('Time')
        plt.ylabel('Pore Pressure Dissipation (u2)')
        plt.legend()

        # Show plot
        plt.show()

        # Print the parameters of the fitted curve
        #print("Parameters of the fitted curve:")
        #print(f"Umax: {popt[0]}")
        #print(f"U0: {popt[1]}")
        #print(f"a: {popt[2]}")
        #print(f"Ch: {popt[3]}")
        #print(f"T50: {popt[4]}")
        #print(f"SQLr: {popt[5]}")
        #print(f"B: {popt[6]}")
        #print(f"Amplitude (A): {popt[0]}")
        #print(f"Mean (mu): {popt[1]}")
        #print(f"Standard Deviation (sigma): {popt[2]}")
        #print(f"Offset: {popt[3]}")
    
    # Error Handler        
    except Exception as e:
        print("Error fitting curve:", e)

# Function to handle automatic guessing for fitted curve based upon data given by user
#def estimate_initial_guess(x_data, y_data):
    #initial_A = np.max(y_data)
    #initial_mu = np.mean(x_data)  # Use the mean of x_data as initial guess for the mean parameter
    #initial_sigma = np.std(x_data)  # Use the standard deviation of x_data as initial guess for the sigma parameter
    #initial_offset = np.min(y_data)
    #return [initial_A, initial_mu, initial_sigma, initial_offset]

# Function to handle automatic guessing for fitted curve based upon data given by user 
#def estimate_initial_guess(x_data, y_data):
    #initial_A = np.max(y_data)
    #initial_mu = x_data[np.argmax(y_data)]
    #initial_sigma = 0.245 * (np.max(x_data) - np.min(x_data))
    #initial_offset = np.min(y_data)
    #return [initial_A, initial_mu, initial_sigma, initial_offset]
    
#def estimate_initial_guess(x_data, y_data):
    #initial_Umax = np.max(y_data)
    #initial_U0 = np.min(y_data)
    # Adjust other initial guesses if needed
    #return [initial_Umax, initial_U0]
    
# Function to handle automatic guessing for fitted curve based upon data given by user
def estimate_initial_guess(x_data, y_data):
    initial_Umax = np.max(y_data)
    #initial_U0_guess = get_initial_U0_guess()  # Prompt user for initial guess for U0
    initial_a = 0.018
    initial_Ch = 3.171e-7
    initial_T50 = 0.245
    initial_SQLr = 0.8
    initial_B = 1.5
    print("Parameters of the fitted curve:")
    print("U0: ", initial_U0_guess)
    print("Ch: ", initial_Ch)
    print("T50: ", initial_T50)
    print("SQLr: ", initial_SQLr)
    print("B: ", initial_B)
    
    # Adjust other initial guesses if needed
    return [initial_Umax, initial_U0_guess, initial_a, initial_Ch, initial_T50, initial_SQLr, initial_B]

# Get user input for file path, column letters, and starting row
file_path, x_column, y_column, start_row = get_user_input()

# Read data from the file
x_data, y_data = read_data(file_path, x_column, y_column, start_row)

# Estimate initial guess for parameters
initial_guess = estimate_initial_guess(x_data, y_data)
#initial_guess.append(get_initial_U0_guess())  # Append the user-supplied guess for U0

# Create interactive plot with estimated initial guess
fit_curve(x_data, y_data, pore_pressure_model, initial_guess)


# In[ ]:


pip install ipywidgets


# In[ ]:


# Define the model function for gaussian_model for fitted curve
# x: The independent variable, typically representing the input values.
# A: Amplitude or height of the Gaussian curve, controlling the peak value.
# mu: Mean of the Gaussian distribution, determining the center or peak location along the x-axis.
# sigma: Standard deviation of the Gaussian distribution, influencing the width of the curve.
# offset: An optional offset parameter, allowing the Gaussian curve to be shifted up or down along the y-axis.
#def gaussian_model(x, A, mu, sigma, offset):
    #return A * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) + offset
    

# Code blcok used for quick testing other models to fit the curve
##########################################################################

# power_law_model function for fitted curve
# a represents the coefficient that scales the power term.
# b represents the exponent.
# x is the independent variable

#def power_law_model(x, a, b):
    #return a * np.power(x, b)
    
# exponential_model function for fitted curve
# a represents the coefficient that scales the exponential term.
# b represents the rate of decay.
# x is the independent variable.

#def exponential_model(x, a, b)
    #return a * np.exp(-b * x)
    
# logarithmic_model function for fitted curve
# a represents the coefficient that scales the logarithmic term.
# np.log(x) is the natural logarithm of the independent variable x.
# b represents the intercept or offset.

#def logarithmic_model(x, a, b)
    #return a * np.log(x) + b
    
##########################################################################


# In[ ]:


# Import Statements
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from ipywidgets import interact, FloatSlider, Layout
from matplotlib.widgets import Cursor
from matplotlib.lines import Line2D
import tkinter as tk
from tkinter import filedialog, simpledialog
import pandas as pd


# Function to read data from a excel file
def read_data(file_path, x_column_letter, y_column_letter, start_row):
    try:
        # Read data from Excel file, specifying columns by their letters
        df = pd.read_excel(file_path, usecols=[x_column_letter, y_column_letter])

        # Skip rows if necessary
        if start_row > 1:
            df = df.iloc[start_row - 1:]

        # Extract data from specified columns
        x_data = df.iloc[:, 0].values.astype(float)
        y_data = df.iloc[:, 1].values.astype(float)

        return x_data, y_data
    
    # Error Handler
    except Exception as e:
        print("Error reading data from file:", e)
        return None, None

def save_data_to_excel(x_data, y_data, output_file_path, x_column_name, y_column_name):
    try:
        # Create a DataFrame with x_data and y_data
        data = {'x': x_data, 'y': y_data}
        df = pd.DataFrame(data)
        
        # Add column names to the DataFrame
        df.columns = [x_column_name, y_column_name]
        
        # Write the DataFrame to an Excel file
        df.to_excel(output_file_path, index=False)
        
        print("Data saved successfully to:", output_file_path)
    
    except Exception as e:
        print("Error saving data to Excel:", e)
        
# Function to convert Excel column letter to index
def column_letter_to_index(letter):
    return ord(letter.upper()) - ord('A')

def get_column_names(file_path):
    # Read data from the file to determine column headers
    df = pd.read_excel(file_path)
    columns = df.columns
    x_column_name = columns[0]
    y_column_name = columns[4]
    return x_column_name, y_column_name

def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file explorer window to select file
    file_path = filedialog.askopenfilename(title="Select a file")

    # Get column letters for x and y data
    x_column_letter = simpledialog.askstring("Input", "Enter the column letter for x data:")
    y_column_letter = simpledialog.askstring("Input", "Enter the column letter for y data:")

    # Convert column letters to indices
    x_column_index = column_letter_to_index(str(x_column_letter))
    y_column_index = column_letter_to_index(str(y_column_letter))

    # Read data from the file to determine column headers
    x_column_name, y_column_name = get_column_names(file_path)

    # Prompt the user to enter the starting row for data
    start_row = simpledialog.askinteger("Input", "Enter the starting row for data (1-indexed):")

    root.destroy()  # Close the root window
    return file_path, x_column_index, y_column_index, x_column_name, y_column_name, start_row

# Function to get user input for initial guess of U0
def get_initial_U0_guess():
    
    # Reset the variable at the start of the function
    initial_U0_guess = None
    
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt the user to enter the initial guess for U0
    initial_U0_guess = simpledialog.askfloat("Input", "Enter the initial guess for U0:")

    # Explicitly destroy the root window
    root.destroy()
    
    return initial_U0_guess

# Function to get user input for initial guess of t
def get_initial_t_guess():
    
    # Reset the variable at the start of the function
    initial_t_guess = None
    
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt the user to enter the initial guess for U0
    initial_t_guess = simpledialog.askfloat("Input", "Enter the initial guess for t:")

    # Explicitly destroy the root window
    root.destroy()
    
    return initial_t_guess
    
def pore_pressure_model(initial_t_guess, initial_Umax, initial_U0_guess, a=0.018, Ch=3.17e-7, T50=0.245, SQLr=0.8, B=1.45):
    U = initial_Umax - (1 - 1 / (1 + (initial_t_guess * Ch / (T50 * a ** 2 * SQLr)))) * np.exp(B) * (initial_Umax - initial_U0_guess)
    #print("Pore pressure model U: ", U)
    return U

def objective_function(params, x_data, y_data):
    # Unpack parameters
    Umax, U0 = params
    
    # Calculate model predictions using pore_pressure_model
    predicted = pore_pressure_model(x_data, Umax, U0)
    
    # Calculate sum of squared residuals
    residuals = y_data - predicted
    return np.sum(residuals**2)

    
# Update fit_curve function to accept additional parameters
def fit_curve(x_data, y_data, objective_function, initial_U0_guess, initial_t_guess):
    try:
        initial_Umax = np.max(y_data) 

        # Set initial guess
        initial_guess = (initial_Umax, initial_U0_guess)

        # Minimize the objective function
        from scipy.optimize import minimize
        
        # Optimize parameters using minimize
        result = minimize(objective_function, initial_guess, args=(x_data, y_data), method='trust-constr')

        # Extract optimized parameters
        popt = result.x
        
        
        # Generate x values for the fitted curve
        x_fit = np.linspace(min(x_data), max(x_data) + 2000, 5000)

        # Calculate y values for the fitted curve using the optimized parameters
        y_fit = pore_pressure_model(x_fit, *popt, initial_t_guess)

        # Plot the original data points
        plt.plot(x_data, y_data, 'b-', label='Original Data')
        plt.xlim(left=min(x_data))

        # Plot the fitted curve
        plt.plot(x_fit, y_fit, 'r-', label='Fitted Curve')

        # Add labels and legend
        plt.xlabel('Time')
        plt.ylabel('Pore Pressure Dissipation (u2)')
        plt.legend()

        # Show plot
        plt.show()
    
    except Exception as e:
        print("Error fitting curve:", e)
        
# Get user input for file path, column letters, and starting row
file_path, x_column_index, y_column_index, x_column_name, y_column_name, start_row = get_user_input()
#file_path, x_column, y_column, start_row = get_user_input()

# Read data from the file
x_data, y_data = read_data(file_path, x_column_index, y_column_index, start_row)

# Get initial guess for U0
initial_U0_guess = get_initial_U0_guess()
initial_t_guess = get_initial_t_guess()

# Call the function to save the data
output_file_path = "output_data_PPD_curve_fit.xlsx"
save_data_to_excel(x_data, y_data, output_file_path, x_column_name, y_column_name)

# Create interactive plot with estimated initial guess
#fit_curve(x_data, y_data, pore_pressure_model, initial_U0_guess, initial_t_guess, initial_Umax)
fit_curve(x_data, y_data, objective_function, initial_U0_guess, initial_t_guess)


# In[ ]:


# Estimate initial guess for parameters
#initial_guess = estimate_initial_guess(x_data, y_data, initial_U0_guess, initial_t_guess)
#initial_guess.append(get_initial_U0_guess())  # Append the user-supplied guess for U0
# Function to handle automatic guessing for fitted curve based upon data given by user

#def estimate_initial_guess(x_data, y_data):
    #initial_A = np.max(y_data)
    #initial_mu = np.mean(x_data)  # Use the mean of x_data as initial guess for the mean parameter
    #initial_sigma = np.std(x_data)  # Use the standard deviation of x_data as initial guess for the sigma parameter
    #initial_offset = np.min(y_data)
    #return [initial_A, initial_mu, initial_sigma, initial_offset]

# Function to handle automatic guessing for fitted curve based upon data given by user 
#def estimate_initial_guess(x_data, y_data):
    #initial_A = np.max(y_data)
    #initial_mu = x_data[np.argmax(y_data)]
    #initial_sigma = 0.245 * (np.max(x_data) - np.min(x_data))
    #initial_offset = np.min(y_data)
    #return [initial_A, initial_mu, initial_sigma, initial_offset]
    
#def estimate_initial_guess(x_data, y_data):
    #initial_Umax = np.max(y_data)
    #initial_U0 = np.min(y_data)
    # Adjust other initial guesses if needed
    #return [initial_Umax, initial_U0]
    
def adjust_parameters(x_data, y_data):
    # Define interactive sliders for each parameter
    Umax_slider = FloatSlider(value=np.max(y_data), min=np.min(y_data), max=np.max(y_data)*2, step=1, description='Umax:', layout=Layout(width='75%'))
    U0_slider = FloatSlider(value=np.min(y_data), min=np.min(y_data), max=np.max(y_data), step=1, description='U0:', layout=Layout(width='75%'))
    t_slider = FloatSlider(value=np.mean(x_data), min=np.min(x_data), max=np.max(x_data), step=1, description='t:', layout=Layout(width='75%'))
    
    # Define function to update plot based on slider values
    def update_plot(Umax, U0, t):
        plt.clf()  # Clear previous plot
        
        # Generate x values for the fitted curve
        x_fit = np.linspace(min(x_data), max(x_data), len(x_data))
        
        # Calculate fitted curve using updated parameters
        y_fit = pore_pressure_model(x_fit, Umax, U0, t)
        
        # Plot original data
        plt.plot(x_data, y_data, 'b-', label='Original Data')
        
        # Plot updated fitted curve
        plt.plot(x_data, y_fit, 'r-', label='Adjusted Fitted Curve')
        
        plt.xlim(left=0)
        plt.ylim(bottom=0)
        plt.xlabel('Time')
        plt.ylabel('Pore Pressure Dissipation (u2)')
        plt.legend()
        plt.show()
    
    # Display interactive sliders and plot
    interact(update_plot, Umax=Umax_slider, U0=U0_slider, t=t_slider)
    
    # Function to handle automatic guessing for fitted curve based upon data given by user
def estimate_initial_guess(x_data, y_data, initial_U0_guess, initial_t_guess):
    initial_Umax = np.max(y_data)
    initial_U0 = initial_U0_guess  # Prompt user for initial guess for U0
    initial_t = initial_t_guess
    #initial_a = 0.018
    #initial_Ch = 3.17e-7
    #initial_T50 = 0.245
    #initial_SQLr = 0.8
    #initial_B = 1.45
    print("Parameters of the original data:")
    print("Umax: ", initial_Umax)
    print("Parameters given by users:")
    print("U0", initial_U0)
    print("t: ", initial_t)
    #print("a: ", initial_a)
    #print("Ch: ", initial_Ch)
    #print("T50: ", initial_T50)
    #print("SQLr: ", initial_SQLr)
    #print("B: ", initial_B)
    # Adjust other initial guesses if needed
    return initial_Umax, initial_U0_guess, initial_t_guess
# Estimate initial guess for parameters
#initial_guess = estimate_initial_guess(x_data, y_data, initial_U0_guess, initial_t_guess)
#initial_guess.append(get_initial_U0_guess())  # Append the user-supplied guess for U0


# In[ ]:


# Import Statements
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from ipywidgets import interact, FloatSlider, Layout
from matplotlib.widgets import Cursor
from matplotlib.lines import Line2D
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog, simpledialog
import pandas as pd

# Function to read data from a excel file
def read_data(file_path, x_column_letter, y_column_letter, start_row):
    try:
        # Read data from Excel file, specifying columns by their letters
        df = pd.read_excel(file_path, usecols=[x_column_letter, y_column_letter])

        # Skip rows if necessary
        if start_row > 1:
            df = df.iloc[start_row - 1:]

        # Extract data from specified columns
        x_data = df.iloc[:, 0].values.astype(float)
        y_data = df.iloc[:, 1].values.astype(float)

        return x_data, y_data
    
    # Error Handler
    except Exception as e:
        print("Error reading data from file:", e)
        return None, None

def save_data_to_excel(x_data, y_data, output_file_path, x_column_name, y_column_name):
    try:
        # Create a DataFrame with x_data and y_data
        data = {'x': x_data, 'y': y_data}
        df = pd.DataFrame(data)
        
        # Add column names to the DataFrame
        df.columns = [x_column_name, y_column_name]
        
        # Write the DataFrame to an Excel file
        df.to_excel(output_file_path, index=False)
        
        print("Data saved successfully to:", output_file_path)
    
    except Exception as e:
        print("Error saving data to Excel:", e)
        
# Function to convert Excel column letter to index
def column_letter_to_index(letter):
    return ord(letter.upper()) - ord('A')

def get_column_names(file_path):
    # Read data from the file to determine column headers
    df = pd.read_excel(file_path)
    columns = df.columns
    x_column_name = columns[0]
    y_column_name = columns[4]
    return x_column_name, y_column_name

def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file explorer window to select file
    file_path = filedialog.askopenfilename(title="Select a file")

    # Get column letters for x and y data
    x_column_letter = simpledialog.askstring("Input", "Enter the column letter for x data:")
    y_column_letter = simpledialog.askstring("Input", "Enter the column letter for y data:")

    # Convert column letters to indices
    x_column_index = column_letter_to_index(str(x_column_letter))
    y_column_index = column_letter_to_index(str(y_column_letter))

    # Read data from the file to determine column headers
    x_column_name, y_column_name = get_column_names(file_path)

    # Prompt the user to enter the starting row for data
    start_row = simpledialog.askinteger("Input", "Enter the starting row for data (1-indexed):")

    root.destroy()  # Close the root window
    return file_path, x_column_index, y_column_index, x_column_name, y_column_name, start_row

# Function to get user input for initial guess of U0
def get_initial_U0_guess():
    
    # Reset the variable at the start of the function
    initial_U0_guess = None
    
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt the user to enter the initial guess for U0
    initial_U0_guess = simpledialog.askfloat("Input", "Enter the initial guess for U0:")

    # Explicitly destroy the root window
    root.destroy()
    
    return initial_U0_guess

# Function to get user input for initial guess of t
def get_initial_t_guess():
    
    # Reset the variable at the start of the function
    initial_t_guess = None
    
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt the user to enter the initial guess for U0
    initial_t_guess = simpledialog.askfloat("Input", "Enter the initial guess for t:")

    # Explicitly destroy the root window
    root.destroy()
    
    return initial_t_guess
    
def pore_pressure_model(initial_t_guess, initial_Umax, initial_U0_guess, a=0.018, Ch=3.17e-7, T50=0.245, SQLr=0.8, B=1.45):
    U = initial_Umax - (1 - 1 / (1 + (initial_t_guess * Ch / (T50 * a ** 2 * SQLr)))) * np.exp(B) * (initial_Umax - initial_U0_guess)
    #print("Pore pressure model U: ", U)
    return U

def objective_function(params, x_data, y_data):
    # Unpack parameters
    Umax, U0 = params
    
    # Calculate model predictions using pore_pressure_model
    predicted = pore_pressure_model(x_data, Umax, U0)
    
    # Calculate sum of squared residuals
    residuals = y_data - predicted
    return np.sum(residuals**2)

    
# Update fit_curve function to accept additional parameters
def fit_curve(x_data, y_data, initial_U0_guess, initial_t_guess):
    try:
        initial_Umax = np.max(y_data) 

        # Set initial guess
        initial_guess = (initial_Umax, initial_U0_guess)

        # Define the objective function for optimization
        def objective_function(params):
            Umax, U0 = params
            predicted = pore_pressure_model(x_data, Umax, U0)
            residuals = y_data - predicted
            return np.sum(residuals**2)

        # Minimize the objective function
        from scipy.optimize import minimize
        result = minimize(objective_function, initial_guess, method='trust-constr')

        # Extract optimized parameters
        popt = result.x

        # Generate x values for the fitted curve
        x_fit = np.linspace(min(x_data), max(x_data) + 5000, 50000)

        # Calculate y values for the fitted curve using the optimized parameters
        y_fit = pore_pressure_model(x_fit, *popt, initial_t_guess)

        # Plot the original data points
        plt.plot(x_data, y_data, 'b-', label='Original Data')
        plt.xlim(left=0)

        # Plot the fitted curve
        plt.plot(x_fit, y_fit, 'r-', label='Fitted Curve')

        # Add labels and legend
        plt.xlabel('Time')
        plt.ylabel('Pore Pressure Dissipation (u2)')
        plt.legend()

        # Show plot
        plt.show()

        # Print the parameters of the fitted curve
        print("Associated parameters of the fitted curve:")
        print(f"Umax: {popt[0]}")
        print(f"U0: {popt[1]}")
    
    except Exception as e:
        print("Error fitting curve:", e)
# Function to handle mouse click and drag
def motion(event, x_data, y_data, initial_U0_guess, initial_t_guess, ax):
    if event.xdata is not None and event.ydata is not None:
        x = event.xdata
        y = event.ydata
        
        # Update U0 and t guesses based on mouse click
        initial_U0_guess = y
        initial_t_guess = x
        
        # Clear previous plot
        ax.clear()
        
        # Plot the original data
        ax.plot(x_data, y_data, 'b-', label='Original Data')
        
        # Fit the curve and plot
        x_fit, y_fit = fit_curve(x_data, y_data, initial_U0_guess, initial_t_guess)
        if x_fit is not None and y_fit is not None:
            ax.plot(x_fit, y_fit, 'r-', label='Fitted Curve')
        
        # Add labels and legend
        ax.set_xlabel('Time')
        ax.set_ylabel('Pore Pressure Dissipation (u2)')
        ax.legend()
        
        # Update canvas
        canvas.draw()

        


# Get user input for file path, column letters, and starting row (unchanged)
file_path, x_column_index, y_column_index, x_column_name, y_column_name, start_row = get_user_input()

# Read data from the file (unchanged)
x_data, y_data = read_data(file_path, x_column_index, y_column_index, start_row)

# Get initial guess for U0 (unchanged)
initial_U0_guess = get_initial_U0_guess()
initial_t_guess = get_initial_t_guess()

# Call the function to save the data (unchanged)
output_file_path = "output_data_PPD_curve_fit.xlsx"
save_data_to_excel(x_data, y_data, output_file_path, x_column_name, y_column_name)

# Create interactive plot with estimated initial guess
fit_curve(x_data, y_data, initial_U0_guess, initial_t_guess)

root = tk.Tk()
root.title("Interactive Plot")

# Create a Figure and Axes for plotting
fig, ax = plt.subplots()
ax.set_xlabel('Time')
ax.set_ylabel('Pore Pressure Dissipation (u2)')
ax.plot(x_data, y_data, 'b-', label='Original Data')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
canvas.mpl_connect('motion_notify_event', lambda event: motion(event, x_data, y_data, initial_U0_guess, initial_t_guess, ax))

# Start GUI event loop
root.mainloop()


# In[ ]:


def fit_curve(x_data, y_data, pore_pressure_model):
    try:
        # Fit the curve to the data
        popt, pcov = curve_fit(pore_pressure_model, x_data, y_data, maxfev=500000)

        # Generate x values for the fitted curve
        x_fit = np.linspace(min(x_data), max(x_data), 5000)

        # Calculate y values for the fitted curve using the optimized parameters
        y_fit = pore_pressure_model(x_fit, *popt)

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(x_data, y_data, 'b-', label='Original Data')
        plt.plot(x_fit, y_fit, 'r-', label='Fitted Curve')
        plt.xlabel('Time')
        plt.ylabel('Pore Pressure Dissipation (u2)')
        plt.legend()
        plt.show()

        # Print the parameters of the fitted curve
        print("Parameters of the fitted curve:")
        for i, param in enumerate(popt):
            print(f"Parameter {i+1}: {param}")

    except Exception as e:
        print(f"Error fitting curve: {e}")


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import tkinter as tk
from tkinter import filedialog, simpledialog

# Function to read data from an Excel file
def read_data(file_path, x_column_letter, y_column_letter, start_row):
    try:
        # Read data from Excel file, specifying columns by their letters
        df = pd.read_excel(file_path, usecols=[x_column_letter, y_column_letter])

        # Skip rows if necessary
        if start_row > 1:
            df = df.iloc[start_row - 1:]

        # Extract data from specified columns
        x_data = df.iloc[:, 0].values.astype(float)
        y_data = df.iloc[:, 1].values.astype(float)

        return x_data, y_data
    
    except Exception as e:
        print("Error reading data from file:", e)
        return None, None

# Function to get user input for file path, column letters, and starting row
def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file explorer window to select file
    file_path = filedialog.askopenfilename(title="Select a file")

    # Get column letters for x and y data
    x_column_letter = simpledialog.askstring("Input", "Enter the column letter for x data:")
    y_column_letter = simpledialog.askstring("Input", "Enter the column letter for y data:")

    # Convert column letters to indices
    x_column_index = column_letter_to_index(str(x_column_letter))
    y_column_index = column_letter_to_index(str(y_column_letter))

    # Read data from the file to determine column headers
    x_column_name, y_column_name = get_column_names(file_path)

    # Prompt the user to enter the starting row for data
    start_row = simpledialog.askinteger("Input", "Enter the starting row for data (1-indexed):")

    root.destroy()  # Close the root window
    return file_path, x_column_index, y_column_index, x_column_name, y_column_name, start_row

# Exponential function to fit
def exponential_func(x, a, b, c):
    return a * np.exp(-b * x) + c

# Function to fit an exponential curve to the data
def fit_curve(x_data, y_data):
    try:
        # Fit exponential curve to the data
        popt, pcov = curve_fit(exponential_func, x_data, y_data)

        # Generate y values for the fitted curve
        y_fit = exponential_func(x_data, *popt)

        # Plot the original data points
        plt.scatter(x_data, y_data, color='blue', label='Original Data')

        # Plot the fitted curve
        plt.plot(x_data, y_fit, color='red', label='Fitted Curve (Exponential)')

        # Add labels and legend
        plt.xlabel('Time')
        plt.ylabel('Pore Pressure Dissipation (u2)')
        plt.legend()

        # Show plot
        plt.show()
    
    except Exception as e:
        print("Error fitting curve:", e)

# Get user input for file path, column letters, and starting row
file_path, x_column_index, y_column_index, x_column_name, y_column_name, start_row = get_user_input()

# Read data from the file
x_data, y_data = read_data(file_path, x_column_index, y_column_index, start_row)

# Fit an exponential curve to the data
fit_curve(x_data, y_data)


# In[ ]:




