#Import statements
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import pandas as pd
import numpy as np

#Reading in data

# access = pd.read_csv('access.csv')
cost = pd.read_csv('archive/cost.csv')

#Data cleaning for cost csv

# baseline abortion provider (across all states - not the best but just get something working)

baseline = cost['No. of abortion providers'].median()

#Because California skewed the mean, I am using median.
#On average, tech hub cities have around 40 abortion providers. 

#Standard deviation:
copy = cost.copy()
data = copy['No. of abortion providers']
outliers = [419, 252]
copy = [x for x in data if x not in outliers]

# Calculate the absolute deviations from the median
absolute_deviations = [abs(x - baseline) for x in copy]
variance = np.mean(np.square(absolute_deviations))
std_based_on_median = np.sqrt(variance)
print("Standard deviation based on the median after removing outliers:", std_based_on_median)

#Determine access intervals 
#On average, tech hubs differ by 15 in terms of abortion providers
#High access to providers: 56+
#Low access to providers: 0-26
#Avg access to providers: 41-56

# Visual

input_state = 'Kansas'

def provider_by_state(input_state):
    # Check if the input_state is in the DataFrame
    if input_state in cost['State'].values:
        
        # Get the row from the DataFrame for the matching state
        state_row = cost[cost['State'] == input_state]
        # Extract the accessibility score for this state
        return state_row['No. of abortion providers'].iloc[0]
    else:
        return None

# Get the provider count for the input state
count = provider_by_state(input_state)

#High access to providers: 56+
#Low access to providers: 0-26
#Avg access to providers: 41-56

def categorize_access(count):
    avg_access = (41, 56)
    low_access = (0, 26)
    high_access = (56, max(cost['No. of abortion providers']))
    
    if high_access[0] <= count <= high_access[1]:
        return 'High'
    elif avg_access[0] <= count <= avg_access[1]:
        return 'Average'
    elif low_access[0] <= count <= low_access[1]:
        return 'Low'
    else:
        return 'Undefined'

access_level = categorize_access(count)
print(f"This state has a {access_level} number of providers: {count}")

    
# Visual for Annual Abortion Cost Saved Through Effective Contraceptives
title_x = cost[['State', 'Abortion Costs Saved at Title X Funded Centers']]
public = cost[['State', 'Abortion Costs Saved at Publicly Funded Family Planning Centers']]


def generate_chart(input_state):
    count = provider_by_state(input_state)
    if count is not None:
        access_level = categorize_access(count)
        print(f"This state has a {access_level} number of providers: {count}")
        
        # Filter the data for the given state
        state_data = cost[cost['State'] == input_state]
        title_x = state_data['Abortion Costs Saved at Title X Funded Centers'].iloc[0]
        public = state_data['Abortion Costs Saved at Publicly Funded Family Planning Centers'].iloc[0]
        
        # Check if costs saved in either Title X or public are less than $5
        if title_x < 5 and public < 5:
            print(f"Due to limited abortion options, the abortion costs via Title X are {title_x}.")
            print(f"Due to limited abortion options, the abortion costs via public centers are {public}.")
            
            
        elif title_x < 5 or public < 5:
            print(f"Due to limited abortion options, the abortion costs ($) via Title X are {title_x}")
            print(f"Due to limited abortion options, the abortion costs ($) via public centers are {public}")
            
        else:
            if access_level == "Low":
                plt.figure(figsize=(8, 6))
                bar_width = 0.35
                plt.bar(0, title_x, color='skyblue', width=bar_width, edgecolor='grey', label='Title X Funded Centers')
                plt.bar(1, public, color='salmon', width=bar_width, edgecolor='grey', label='Publicly Funded Centers')

            # Add title and axis labels
                plt.xlabel('Funding Source', fontsize=12, fontweight='bold')
                plt.ylabel('Cost ($)', fontsize=12, fontweight='bold')
                plt.title(f"Average Abortion Costs Saved in {input_state}", fontsize=14, fontweight='bold')

    # Customize ticks and legend
                plt.xticks([0, 1], ['Title X', 'Public'], fontsize=10)
                plt.yticks(fontsize=10)
                plt.legend(fontsize=10)

    # Display the chart
                plt.tight_layout()
                plt.show()
            elif access_level == "Avg":
                plt.figure(figsize=(8, 6))
                bar_width = 0.35
                plt.bar(0, title_x, color='skyblue', width=bar_width, edgecolor='grey', label='Title X Funded Centers')
                plt.bar(1, public, color='salmon', width=bar_width, edgecolor='grey', label='Publicly Funded Centers')

    # Add title and axis labels
                plt.xlabel('Funding Source', fontsize=12, fontweight='bold')
                plt.ylabel('Cost ($)', fontsize=12, fontweight='bold')
                plt.title(f"Average Abortion Costs Saved in {input_state}", fontsize=14, fontweight='bold')

    # Customize ticks and legend
                plt.xticks([0, 1], ['Title X', 'Public'], fontsize=10)
                plt.yticks(fontsize=10)
                plt.legend(fontsize=10)

    # Display the chart
                plt.tight_layout()
                plt.show()
            else:
                plt.figure(figsize=(8, 6))
                bar_width = 0.35
                plt.bar(0, title_x, color='skyblue', width=bar_width, edgecolor='grey', label='Title X Funded Centers')
                plt.bar(1, public, color='salmon', width=bar_width, edgecolor='grey', label='Publicly Funded Centers')

    # Add title and axis labels
                plt.xlabel('Funding Source', fontsize=12, fontweight='bold')
                plt.ylabel('Cost ($)', fontsize=12, fontweight='bold')
                plt.title(f"Average Abortion Costs Saved in {input_state}", fontsize=14, fontweight='bold')

    # Customize ticks and legend
                plt.xticks([0, 1], ['Title X', 'Public'], fontsize=10)
                plt.yticks(fontsize=10)
                plt.legend(fontsize=10)

    # Display the chart
                plt.tight_layout()
                plt.show()
                

