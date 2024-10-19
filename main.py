import pandas as pd
import matplotlib.pyplot as plt

# Load the COVID-19 dataset
df = pd.read_csv('covid_data.csv')

# For this example, let's assume we're interested in plotting 'Total Cases' vs. 'Total Deaths'
# You can modify these columns based on your dataset's actual structure.
x = df['Total Cases']
y = df['Total Deaths']

# Create a basic scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Total Cases vs. Total Deaths')
plt.title('Total COVID-19 Cases vs. Total Deaths')
plt.xlabel('Total Cases')
plt.ylabel('Total Deaths')
plt.legend()
plt.grid()
plt.show()

# Show Plot in Various Shapes and Colors
# Show scatter plot in various shapes and colors
plt.figure(figsize=(10, 6))

# Different styles
plt.scatter(x, y, color='blue', marker='o', label='Circle')    # Blue circles
plt.scatter(x + 1000000, y, color='green', marker='^', label='Triangle')  # Green triangles
plt.scatter(x - 1000000, y, color='red', marker='s', label='Square')      # Red squares

plt.title('Total COVID-19 Cases vs. Total Deaths - Different Styles')
plt.xlabel('Total Cases')
plt.ylabel('Total Deaths')
plt.legend()
plt.grid()
plt.show()
#  Plotting Equations on the Screen
# Define the equation y = mx + b
m = 0.0005  # slope
b = 0      # y-intercept
x_eq = range(0, 10000000, 100000)  # x values from 0 to 10,000,000
y_eq = [m * i + b for i in x_eq]  # Calculate y values based on the equation

# Plotting the equation
#you can plot equations, such as 
#Here’s an example of how to plot a linear equation:
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x_eq, y_eq, color='orange', label='y = 0.0005x', linewidth=2)  # Plot the equation
plt.title('Total COVID-19 Cases vs. Total Deaths with Equation')
plt.xlabel('Total Cases')
plt.ylabel('Total Deaths')
plt.legend()
plt.grid()
plt.show()



