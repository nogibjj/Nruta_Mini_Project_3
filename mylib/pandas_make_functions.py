"""
Purpose of the file:
Library file for the Pandas script
Compare the time taken to run the code with Pandas and compare it with Polars
"""

# importing libraries
import pandas as pd
import matplotlib.pyplot as plt


# loading dataset
def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df


# Defining functions for summary statistics
def calculate_mean(df, col):
    if df[col].empty:
        return None
    return df[col].mean()


def calculate_median(df, col):
    if df[col].empty:
        return None
    return df[col].median()


def calculate_std_dev(df, col):
    if df[col].empty:
        return None
    if len(df[col]) == 1:
        return 0
    return df[col].std()


# Plotting functions
# creating a bar chart
def bar_plot(
    dataframe,
    x_column,
    y_column,
    title,
    xlabel,
    ylabel,
    color="skyblue",
    rotation=45,
    jupyter_render=False,
):
    plt.figure(figsize=(12, 8))
    dataframe.plot(kind="bar", x=x_column, y=y_column, color=color, legend=False)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotation)
    plt.grid(axis="y")
    if not jupyter_render:
        plt.savefig("bar_plot.png")
    else:
        plt.show()


# creating a pie chart
def pie_chart(dataframe, column, title, jupyter_render=False):
    plt.figure(figsize=(10, 10))
    dataframe[column].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=140)
    plt.title(title)
    plt.ylabel("")
    if not jupyter_render:
        plt.savefig("pie_chart.png")
    else:
        plt.show()
