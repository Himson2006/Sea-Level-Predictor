import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('/workspace/boilerplate-sea-level-predictor/epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(x, y, color = 'b', s = 10, marker = 'o')

    # Create first line of best fit
    years_extended = pd.Series(range(x.min(), 2051))
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    best_fit_line = slope * years_extended + intercept
    plt.plot(years_extended, best_fit_line, color = 'r')


    # Create second line of best fit
    years_2 = pd.Series(range(2000, 2051))
    x2 = df[df['Year'] >= 2000]['Year']
    y2 = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x2, y2)
    best_fit_line2 = slope2 * years_2 + intercept2
    plt.plot(years_2, best_fit_line2, color = 'g')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()