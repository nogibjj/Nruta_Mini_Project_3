"""
Defining the library functions
"""

# importing libraries
import polars as pl
import matplotlib.pyplot as plt


# loading dataset
def load_dataset(filepath):
    df = pl.read_csv(filepath)
    return df


# Defining functions for summary statistics
def calculate_mean(df, col):
    if df[col].is_empty():
        return None
    return df[col].mean()


def calculate_median(df, col):
    if df[col].is_empty():
        return None
    return df[col].median()


def calculate_std_dev(df, col):
    if df[col].is_empty():
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
    # Convert Polars DataFrame to NumPy arrays
    x = dataframe[x_column].to_numpy()
    y = dataframe[y_column].to_numpy()

    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color=color)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotation)
    plt.grid(axis="y")

    if not jupyter_render:
        plt.savefig("bar_plot.png")  # saving it as an image
    else:
        plt.show()


# creating a pie chart
def pie_chart(dataframe, col, title, jupyter_render=False):
    # Count occurrences of each category in the specified column
    counts = dataframe[col].value_counts()

    # Extract values and labels by index position
    labels = counts[:, 0].to_numpy()
    values = counts[:, 1].to_numpy()

    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90, labeldistance=1.05)
    plt.title(title, pad=40)
    plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    if not jupyter_render:
        plt.savefig("pie_chart.png")  # saving to an image
    else:
        plt.show()
