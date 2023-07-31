# https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer

# Public execution and test:
# https://replit.com/@ToniG4/boilerplate-page-view-time-series-visualizer


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 'date', parse_dates = True)

# Clean data
df = df[
    (df['value'] > df['value'].quantile(0.025)) &
    (df['value'] < df['value'].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot

    fig, axes = plt.subplots(figsize=(16, 9))

    axes.plot(df['value'])
    axes.set_xlabel('Date')
    axes.set_ylabel('Page Views')
    axes.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar.reset_index(inplace = True)

    df_bar['date'] = pd.to_datetime(df_bar['date'])
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month_name()

    df_bar = df_bar.groupby(['year', 'month'], sort = False)['value'].mean()

    df_bar = df_bar.reset_index()

    df_bar = df_bar.rename(columns = {
        'value' : 'Average Page Views',
        'year' : 'Years',
        'month' : 'Months'
    })

    missing_data = {
            "Years": [2016, 2016, 2016, 2016],
            "Months": ['January', 'February', 'March', 'April'],
            "Average Page Views": [0, 0, 0, 0]
        }
    df_bar = pd.concat( [pd.DataFrame(missing_data), df_bar] )    


    # Draw bar plot
    fig, ax = plt.subplots(figsize = (16, 9))
    sns.barplot(data = df_bar, x = 'Years', y = 'Average Page Views', hue = 'Months')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]


    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize=(14, 6))

    sns.boxplot(x = df_box['year'], y = df_box['value'], ax = ax1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')

    x_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x = df_box['month'], y = df_box['value'], ax = ax2, order = x_order)
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
