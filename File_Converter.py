#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""

NewFields File Converter

This Program provides a graphical user interface (GUI) for converting Excel files to CSV files
with data extraction capabilities. It allows users to specify starting row, header indices,
and conversion types for columns. Supported conversions include Feet to Meters, TSF to KPA,
PSI to MPA, and PSI to KPA.

NewFields - Transforming Data into Insights

Author:     Cody Thompson
Date:       02/19/2024
Version #:  1.6.0

NOTE: This Program is subject to change to help facilitate a more productive and accurate program

"""

import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
from openpyxl.utils import column_index_from_string  # Import the function for converting column letters to indices

# Import xlsxwriter module
import xlsxwriter

# Defined hardcoded header names
hardcoded_headers = ["Depth: ", "Tip: ", "Friction: ", "Pore Pressure: "]

# Convert column letters or ranges to indices
def parse_column_indices(header_indices):
    indices = []
    for part in header_indices.split(','):
        if ':' in part:
            start, end = part.split(':')
            start_idx = column_index_from_string(start.strip().upper()) - 1
            end_idx = column_index_from_string(end.strip().upper()) - 1
            indices.extend(range(start_idx, end_idx + 1))
        else:
            indices.append(column_index_from_string(part.strip().upper()) - 1)
    return indices

# Function for converting files into csv files
def extract_data(starting_row, header_indices, conversion_data, sheet_name, user_info):
    try:
         # Validate input for starting row
        if not validate_input(starting_row):
            result_label.config(text="Error: Starting row must be a valid integer")
            return
        
        # Open file dialog to select Excel file
        file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
        if not file_path:
            return  # Exit function if no file is selected

        # Convert header indices from letters to a string integer indicating the row containing column names
        header_row = int(starting_row) - 1 if int(starting_row) > 0 else None
        
        # Convert column letters to indices
        selected_columns = parse_column_indices(header_indices)
        
        # Load Excel file into a pandas DataFrame
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=header_row)
        
        # Filter the DataFrame to include only the specified columns
        selected_columns_df = df.iloc[:, selected_columns]
         
        for conversion_type, column_to_convert in conversion_data:
            if not conversion_type == "None":
                # Convert column_to_convert from original DataFrame indices to selected columns indices
                if isinstance(column_to_convert, str) and column_to_convert.strip().upper().isalpha():
                    column_index = ord(column_to_convert.strip().upper()) - ord('A')
                if column_index in selected_columns:
                    column_to_convert = column_index
                else:
                    result_label.config(text=f"Error: Column {column_to_convert} is not selected for conversion.")
                    continue
                    
                if conversion_type == "Feet to Meters":
                    convert_ft_to_meters(selected_columns_df, column_to_convert)
                    hardcoded_headers[0] = "Depth: (m)"  # Append "(m)" to the "Depth" header
                elif conversion_type == "Feet to KPA":
                    convert_ft_to_kPa(selected_columns_df, column_to_convert)
                elif conversion_type == "TSF to MPA":
                    convert_tsf_to_MPa(selected_columns_df, column_to_convert)
                    hardcoded_headers[1] = "Tip: (MPa)"  # Append "(MPa)" to the "Tip" header
                elif conversion_type == "PSI to KPA":
                    convert_psi_to_kpa(selected_columns_df, column_to_convert)
                elif conversion_type == "TSF to KPA":
                    convert_tsf_to_kPa(selected_columns_df, column_to_convert)
                    hardcoded_headers[2] = "Friction: (kPa)"  # Append "(kPa)" to the "Friction" header
                    hardcoded_headers[3] = "Pore Pressure: (kPa)"  # Append "(kPa)" to the "Pore Pressure" header
                elif conversion_type == "BAR to KPA":
                    convert_bar_to_kPa(selected_columns_df, column_to_convert)
                else:
                    result_label.config(text=f"Error: Column index {str(column_to_convert)} is out of bounds, Type: {type(column_to_convert)}")

        # Read user info from the GUI
        user_info_df = pd.DataFrame({"Company Info: ": [user_info]})

        # Concatenate user info DataFrame with selected columns DataFrame
        concatenated_df = pd.concat([user_info_df, selected_columns_df], axis=1)

        # Update hardcoded headers to include the new "Company Info" header
        updated_headers = ["Company Info: "] + hardcoded_headers
        
        # Save extracted data to CSV file
        output_file_path = file_path.split('.')[0] + '_extracted.csv'
             
        concatenated_df.to_csv(output_file_path, index=False, header=updated_headers, float_format="%.5f")

        # Output print out to GUI window
        result_label.config(text=f"Data extracted and saved as {output_file_path}")

    except Exception as e:
        print("Error occured: ", e)
        result_label.config(text=f"Error: {e}")

# Sheet name entry field in the GUI
def add_sheet_name_entry():
    sheet_name_label = tk.Label(root, text="Sheet Name:")
    sheet_name_label.pack()
    sheet_name_entry = tk.Entry(root)
    sheet_name_entry.pack()
    return sheet_name_entry

    
# Conversion Functions
# ft to m	0.3048 //Needed for depth
def convert_ft_to_meters(df, column_to_convert):
    try:
        # Convert only numeric values to meters
        column_name = df.columns[column_to_convert]
        df.loc[:, column_name] = pd.to_numeric(df[column_name], errors='coerce')  # Convert to numeric
        df.loc[:, column_name] *= 0.3048
        # Error handler 
    except (ValueError, KeyError) as e:
        # If the conversion fails, or the column does not exist, show error message
        result_label.config(text=f"Error converting column: {e}")

# psi to kPa //Needed (Pore Pressure) u or u2
def convert_psi_to_kpa(df, column_to_convert):
    try:
        # Convert only numeric values to KPA
        column_name = df.columns[column_to_convert]
        df.loc[:, column_name] = pd.to_numeric(df[column_name], errors='coerce')  # Convert to numeric
        df.loc[:, column_name] *= 6.895
        # Error handler
    except (ValueError, KeyError) as e:
        # If the conversion fails, or the column does not exist, show error message
        result_label.config(text=f"Error converting column: {e}")
        
# psi to MPa = 0.0069
def convert_psi_to_mpa(df, column_to_convert):
    try:
        # Convert only numeric values to MPA
        column_name = df.columns[column_to_convert]
        df.loc[:, column_name] = pd.to_numeric(df[column_name], errors='coerce')  # Convert to numeric
        df.loc[:, column_name] *= 0.006895
        # Error handler
    except (ValueError, KeyError) as e:
        # If the conversion fails, or the column does not exist, show error message
        result_label.config(text=f"Error converting column: {e}")
        
# tsf to MPa	0.0958 //Needed (qc) cone tip
def convert_tsf_to_MPa(df, column_to_convert):
    try:
        # Convert only numeric values tsf to MPa
        column_name = df.columns[column_to_convert]
        df.loc[:, column_name] = pd.to_numeric(df[column_name], errors='coerce') # Convert to numeric
        df.loc[:, column_name] *= 0.09576
        # Error handler 
    except (ValueError, KeyError) as e:
        # If the conversion fails, or the column does not exist, show error message
        result_label.config(text=f"Error converting column: {e}")
        
# ft to kPa = 2.989 //Needed (Pore Pressure) u or u2
def convert_ft_to_kPa(df, column_to_convert):
    try:
        # Convert only numeric values to kPa
        column_name = df.columns[column_to_convert]
        df.loc[:, column_name] = pd.to_numeric(df[column_name], errors='coerce') # Convert to numeric
        df.loc[:, column_name] *= 2.989
        # Error handler
    except (ValueError, KeyError) as e:
        # If the conversion fails, or the column does not exist, show error message
        result_label.config(text=f"Error converting column: {e}")
        
# tsf to kPa = 4.88243 //Needed (friction sleeve) 
def convert_tsf_to_kPa(df, column_to_convert):
    try:
        # Convert only numeric values to kPa from tsf
        column_name = df.columns[column_to_convert]
        df.loc[:, column_name] = pd.to_numeric(df[column_name], errors='coerce') # Convert to numeric
        df.loc[:, column_name] *= 4.8824
        # Error handler 
    except (ValueError, KeyError) as e:
        # If the conversion fails, or the column does not exist, show error message
        result_label.config(text=f"Error converting column: {e}")
        
# bar to kPa = 100 //Needed (Pore Pressure) u or u2
def convert_bar_to_kPa(df, column_to_convert):
    try:
        # Convert only to numeric values to bar from kPa
        column_name = df.columns[column_to_convert]
        df.loc[:, column_name] = pd.to_numeric(df[column_name], errors='coerce') # Convert to numeric
        df.loc[:, column_name] *= 100
        # Error handler
    except (ValueError, KeyError) as e:
        # If the conversion fails, or the column does not exist, show error message
        result_label.config(text=f"Error converting column: {e}")
                
# Function for converting files into XLXS
def convert_to_xls():
    try:
        # Open file dialog to select CSV file
        file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
        if not file_path:
            return  # Exit function if no file is selected

        # Load CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)

        # Specify the output Excel file path
        output_file_path = file_path.split('.')[0] + '.xlsx'

        # Create a Pandas Excel writer using xlsxwriter as the engine
        with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)

        # Output print out to GUI window
        result_label.config(text=f"Data converted and saved as {output_file_path}")

    except Exception as e:
        result_label.config(text=f"Error: {e}")

        
# Function used to validate user input
def validate_input(input_str):
    if not input_str:
        return False  # Empty input
    try:
        int(input_str)
        return True
    except ValueError:
        return False

    
# Function to add a new conversion row
def add_conversion_row():
    conversion_row = tk.Frame(conversion_frame)
    conversion_row.pack()

    # Dropdown for conversion type
    conversion_type_var = tk.StringVar()
    conversion_type_dropdown = ttk.Combobox(conversion_row, textvariable=conversion_type_var, values=["None", "Feet to Meters", "TSF to KPA", "TSF to MPA", "PSI to KPA", "Feet to KPA", "BAR to KPA"])  # Update dropdown values
    conversion_type_dropdown.pack(side=tk.LEFT, padx=5)
    conversion_type_dropdown.current(0)  # Set default to "None"

    # Label for column to convert
    column_to_convert_label = tk.Label(conversion_row, text="Column to Convert (A, B, C, ...)")  # Update label text
    column_to_convert_label.pack(side=tk.LEFT, padx=5)
    
    # Entry for column to convert
    column_to_convert_entry = tk.Entry(conversion_row)
    column_to_convert_entry.pack(side=tk.LEFT, padx=5)

    # Append the references of the dropdown and entry widgets to the conversion_rows list
    conversion_rows.append((conversion_type_var, column_to_convert_entry))


# Ensures proper closing of the application
def on_closing():
    root.destroy()


# Create the Tkinter application GUI
root = tk.Tk()
root.title("File Converter")

# Add section for user information
user_info_label = tk.Label(root, text="Company Info:")
user_info_label.pack()

user_info_text = tk.Text(root, height=4, width=50)
user_info_text.pack()

# Add section for sheet name
sheet_name_entry = add_sheet_name_entry()

# Spacer label
instruction_label = tk.Label(root, text="\n")
instruction_label.pack(pady=10)

# Description label just in case the program needs more description on how to use the GUI
#instruction_label = tk.Label(root, text="Add More Comments if Needed")
#instruction_label.pack(pady=10)

# Label for headers entry
headers_label = tk.Label(root, text="Column Letter (comma-separated starting from A)\n Column Extraction:")
headers_label.pack()
# Headers entry
headers_entry = tk.Entry(root)
headers_entry.pack(pady=5)

# Label for column description
column_description_label = tk.Label(root, text="^,^,^,^,^,^.")
column_description_label.pack(anchor=tk.W, padx=(217.5,0))
# Label for column description
column_description_label = tk.Label(root, text="A,B,C,D,E,F. Letter-Based Index")
column_description_label.pack(anchor=tk.W, padx=(217.5,0))

# Label for starting row entry
starting_row_label = tk.Label(root, text="\nStarting Row (One row above input headers)\n Row Extraction:")
starting_row_label.pack()
# Starting row entry
starting_row_entry = tk.Entry(root)
starting_row_entry.pack(pady=5)

# Label for conversions dropdown
conversions_dropdown_label = tk.Label(root, text="Conversions Drop-down:")
conversions_dropdown_label.pack(anchor=tk.W, padx=20)  # Pack the label above the dropdown box and align the label
# Frame for conversion rows
conversion_frame = tk.Frame(root)
conversion_frame.pack()

# Add initial conversion row
conversion_rows = []
add_conversion_row()

# Button to add new conversion row
add_conversion_button = tk.Button(root, text="Add Conversion", command=add_conversion_row)
add_conversion_button.pack(pady=5)

# Convert to CSV button
convert_to_csv_button = tk.Button(root, text="Extract Data", command=lambda: extract_data(starting_row_entry.get(), headers_entry.get(), [(conversion_row[0].get(), conversion_row[1].get()) for conversion_row in conversion_rows], sheet_name_entry.get(), user_info_text.get("1.0", "end-1c").strip()))
convert_to_csv_button.pack(pady=10)

# Convert to XLS button
convert_to_xls_button = tk.Button(root, text="Convert to XLS", command= convert_to_xls)
convert_to_xls_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Bind the closing event to the on_closing function
root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the Tkinter event loop
root.mainloop()


# In[ ]:




