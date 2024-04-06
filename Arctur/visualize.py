import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def format_string(filename):
    # Extract the filename from the path
    filename_without_extension = filename.split('/')[-1]
    # Remove file extension
    filename_without_extension = filename_without_extension.split('.')[0]
    # Replace dashes with spaces and capitalize each word
    formatted_string = ' '.join(word.capitalize() for word in filename_without_extension.split('-'))
    return formatted_string

def plot_passing_data(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file, parse_dates=['datum'])

    # Set 'datum' column as the index
    df.set_index('datum', inplace=True)

    # Resample by month and sum the 'vhodi' and 'izhodi' columns
    monthly_passes = df.resample('ME')['vhodi', 'izhodi'].sum()
    monthly_passes['total_passes'] = monthly_passes['vhodi'] + monthly_passes['izhodi']

    # Resample by day and sum the 'vhodi' and 'izhodi' columns
    daily_passes = df.resample('D')['vhodi', 'izhodi'].sum()
    daily_passes['total_passes'] = daily_passes['vhodi'] + daily_passes['izhodi']

    # Plotting
    plt.figure(figsize=(12, 5))

    # Plotting monthly data as bars
    plt.subplot(1, 2, 1)
    plt.bar(monthly_passes.index, monthly_passes['total_passes'], label='Monthly Data', width=20, color='gray')
    plt.title('Monthly Passes')
    plt.xlabel('Month')
    plt.ylabel('Number of Passes')
    plt.xticks(rotation=45)
    plt.legend()

    # Fitting polynomial for monthly data
    coeffs_monthly = np.polyfit(range(len(monthly_passes)), monthly_passes['total_passes'], 5)
    poly_eqn_monthly = np.poly1d(coeffs_monthly)
    x_values_monthly = np.arange(len(monthly_passes))
    y_values_monthly = poly_eqn_monthly(x_values_monthly)
    plt.plot(monthly_passes.index, y_values_monthly, label='Polynomial Fit (Degree 5)', color='red')

    # Plotting daily data as bars
    plt.subplot(1, 2, 2)
    plt.bar(daily_passes.index, daily_passes['total_passes'], label='Daily Data', width=1, color='darkblue')
    plt.title('Daily Passes')
    plt.xlabel('Date')
    plt.ylabel('Number of Passes')
    plt.xticks(rotation=45)
    plt.legend()

    # Fitting polynomial for daily data
    coeffs_daily = np.polyfit(range(len(daily_passes)), daily_passes['total_passes'], 10)
    poly_eqn_daily = np.poly1d(coeffs_daily)
    x_values_daily = np.arange(len(daily_passes))
    y_values_daily = poly_eqn_daily(x_values_daily)
    plt.plot(daily_passes.index, y_values_daily, label='Polynomial Fit (Degree 10)', color='red')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script.py <csv_file>")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    plot_passing_data(csv_file)