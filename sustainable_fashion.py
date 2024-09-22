"""
Main python script which will be running on Polars
"""

# importing packages
import polars as pl
import time

from mylib.make_functions import (
    load_dataset,
    calculate_mean,
    calculate_median,
    calculate_std_dev,
    bar_plot,
    pie_chart,
)

start_time = time.time()

filepath = "sustainable_fashion_trends_2024.csv"


# loading the data
def load_df(filepath):
    return load_dataset(filepath)


# generate statistics
def generate_statistics(df, analysis_col):
    # calculating statistics
    mean = calculate_mean(df, analysis_col)
    median = calculate_median(df, analysis_col)
    std_dev = calculate_std_dev(df, analysis_col)

    # creating a DataFrame for the markdown table
    stats_dict = {
        "Statistic": ["Mean", "Median", "Standard Deviation"],
        "Value": [mean, median, std_dev],
    }

    stats_df = pl.DataFrame(stats_dict)

    return stats_df


# generating the plots
def generate_plots(
    df, x_col, y_col, plot_title, xlabel, ylabel, pie_col, pie_title, jupyter_render
):
    # formatting the data such that it is in the right format to be consumed by the bar_plot function
    grouped_data = df.group_by(x_col).agg(pl.len().alias(y_col))

    # calling the function to create a bar plot
    bar_plot(
        grouped_data,
        x_col,
        y_col,
        plot_title,
        xlabel,
        ylabel,
        color="skyblue",
        rotation=45,
        jupyter_render=jupyter_render,
    )

    # calling the pie chart function
    pie_chart(df, pie_col, pie_title, jupyter_render)


def save_to_md(
    df, analysis_col, x_col, y_col, plot_title, xlabel, ylabel, pie_col, pie_title
):
    # write the markdown table to a file
    describe_df = generate_statistics(df, analysis_col)
    markdown_table = describe_df.to_pandas().to_markdown()
    generate_plots(
        df,
        x_col,
        y_col,
        plot_title,
        xlabel,
        ylabel,
        pie_col,
        pie_title,
        jupyter_render=False,
    )
    with open("sustainable_fashion.md", "w") as file:
        file.write("Describe:\n")
        file.write(markdown_table)
        file.write("\n\n")
        file.write("![sustainablebrand_viz1](bar_plot.png)\n")
        file.write("\n\n")
        file.write("![sustainablebrand_viz2](pie_chart.png)")


# parameters for the analysis
analysis_col = "Carbon_Footprint_MT"
x_col = "Country"
y_col = "Number of Brands"
plot_title = "Number of Sustainable Brands per Country"
xlabel = "Country"
ylabel = "Number of Brands"
pie_col = "Material_Type"
pie_title = "Distribution of Material Types"

# loading the data
df = load_df(filepath)

# call generate_statistics
generate_statistics(df, analysis_col)

# call generate_plots
generate_plots(
    df,
    x_col,
    y_col,
    plot_title,
    xlabel,
    ylabel,
    pie_col,
    pie_title,
    jupyter_render=False,
)

# saving it to markdown
save_to_md(
    df, analysis_col, x_col, y_col, plot_title, xlabel, ylabel, pie_col, pie_title
)

end_time = time.time()
exec_time = end_time - start_time
print("Execution time:", exec_time)
