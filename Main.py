import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# Function to plot trends based on selected CSV file and parameter
def plot_trend():
    selected_file = file_var.get()
    selected_param = param_var.get()
    
    # Load the selected dataset
    data = pd.read_csv(selected_file, dtype={'DATE': str})
    
    plt.figure(figsize=(10, 6))
    
    # Plot parameter based on the selected CSV file
    plt.plot(data['DATE'], data[selected_param], label=selected_param)
    
    plt.title(f"Trend Over Time: {selected_param} ({selected_file})")
    plt.xlabel("Date")
    plt.ylabel(selected_param)
    plt.legend()
    plt.grid(True)
    plt.show()

# Create Tkinter GUI
root = tk.Tk()
root.title("Climate Data Analysis")

# Dropdown menu for selecting CSV file
file_var = tk.StringVar()
file_label = ttk.Label(root, text="Select CSV File:")
file_label.grid(row=0, column=0)
file_menu = ttk.OptionMenu(root, file_var, "hourly_data.csv", "daily_data.csv", "monthly_data.csv", "three_hour_data.csv")
file_menu.grid(row=0, column=1)

# Dropdown menu for selecting parameter
param_var = tk.StringVar()
param_label = ttk.Label(root, text="Select Parameter:")
param_label.grid(row=1, column=0)
param_menu = ttk.OptionMenu(root, param_var, "HourlyDryBulbTemperature", "")
param_menu.grid(row=1, column=1)

# Function to update parameter dropdown based on selected CSV file
def update_param_menu(*args):
    selected_file = file_var.get()
    if selected_file == "hourly_data.csv":
        param_menu['menu'].delete(0, 'end')
        for column in hourly_columns:
            param_menu['menu'].add_command(label=column, command=tk._setit(param_var, column))
    elif selected_file == "daily_data.csv":
        param_menu['menu'].delete(0, 'end')
        for column in daily_columns:
            param_menu['menu'].add_command(label=column, command=tk._setit(param_var, column))
    elif selected_file == "monthly_data.csv":
        param_menu['menu'].delete(0, 'end')
        for column in monthly_columns:
            param_menu['menu'].add_command(label=column, command=tk._setit(param_var, column))
    elif selected_file == "three_hour_data.csv":
        param_menu['menu'].delete(0, 'end')
        for column in three_hour_columns:
            param_menu['menu'].add_command(label=column, command=tk._setit(param_var, column))
    elif selected_file == "hourly_data.csv":
        param_menu['menu'].delete(0, 'end')
        for column in hourly_columns:
            param_menu['menu'].add_command(label=column, command=tk._setit(param_var, column))

file_var.trace('w', update_param_menu)

# Button to plot trend
plot_button = ttk.Button(root, text="Plot Trend", command=plot_trend)
plot_button.grid(row=2, column=0, columnspan=2)

# Define column names for each CSV file
hourly_columns = ["HourlyAltimeterSetting", "HourlyDewPointTemperature", "HourlyDryBulbTemperature", "HourlyPrecipitation", "HourlyRelativeHumidity", "HourlySeaLevelPressure", "HourlyStationPressure", "HourlyVisibility", "HourlyWetBulbTemperature", "HourlyWindDirection", "HourlyWindSpeed"]
daily_columns = ["DailyAverageDryBulbTemperature", "DailyCoolingDegreeDays", "DailyDepartureFromNormalAverageTemperature", "DailyHeatingDegreeDays", "DailyMaximumDryBulbTemperature", "DailyMinimumDryBulbTemperature", "DailyPeakWindDirection", "DailyPeakWindSpeed", "DailyPrecipitation", "DailySnowfall", "DailySustainedWindDirection", "DailySustainedWindSpeed"]
monthly_columns = ["MonthlyDaysWithGT001Precip", "MonthlyDaysWithGT010Precip", "MonthlyDaysWithGT32Temp", "MonthlyDaysWithGT90Temp", "MonthlyDaysWithLT0Temp", "MonthlyDaysWithLT32Temp", "MonthlyDepartureFromNormalAverageTemperature", "MonthlyDepartureFromNormalCoolingDegreeDays", "MonthlyDepartureFromNormalHeatingDegreeDays", "MonthlyDepartureFromNormalMaximumTemperature", "MonthlyDepartureFromNormalMinimumTemperature", "MonthlyDepartureFromNormalPrecipitation", "MonthlyGreatestPrecip", "MonthlyGreatestPrecipDate", "MonthlyGreatestSnowDepth", "MonthlyGreatestSnowfall", "MonthlyMaxSeaLevelPressureValue", "MonthlyMaxSeaLevelPressureValueDate", "MonthlyMaxSeaLevelPressureValueTime", "MonthlyMaximumTemperature", "MonthlyMeanTemperature", "MonthlyMinSeaLevelPressureValue", "MonthlyMinSeaLevelPressureValueDate", "MonthlyMinSeaLevelPressureValueTime", "MonthlyMinimumTemperature", "MonthlySeaLevelPressure", "MonthlyStationPressure", "MonthlyTotalLiquidPrecipitation", "NormalsHeatingDegreeDay", "WindEquipmentChangeDate"]
three_hour_columns = ["HourlyDewPointTemperature", "HourlyDryBulbTemperature", "HourlyPressureChange", "HourlyPressureTendency", "HourlyRelativeHumidity", "HourlySeaLevelPressure", "HourlyStationPressure", "HourlyVisibility", "HourlyWetBulbTemperature", "HourlyWindDirection", "HourlyWindSpeed", "WindEquipmentChangeDate"]

# Run Tkinter event loop
root.mainloop()
