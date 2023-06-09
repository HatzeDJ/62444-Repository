import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import fastparquet


def create_scatterplot(df, x_col, y_col, title, xlabel, ylabel):
    """
    This function creates a scatter plot with a linear regression line from a DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    x_col (str): The column in the DataFrame to use for the x-axis.
    y_col (str): The column in the DataFrame to use for the y-axis.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    """

    # Create the plot
    plt.figure(figsize=(7, 7))
    sns.regplot(x=df[x_col], y=df[y_col], scatter_kws={"alpha": 0.3})

    # Add labels and title
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Show the plot
    plt.show()


def get_a_random_chunk_property(data):
    """
    This function only serves an example of fetching some of the properties
    from the data.
    Indeed, all the content in "data" may be useful for your project!
    """

    chunk_index = np.random.choice(len(data))

    date_list = list(data[chunk_index]["near_earth_objects"].keys())

    date = np.random.choice(date_list)

    objects_data = data[chunk_index]["near_earth_objects"][date]

    object_index = np.random.choice(len(objects_data))

    object = objects_data[object_index]

    properties = list(object.keys())
    property = np.random.choice(properties)

    print("date:", date)
    print("NEO name:", object["name"])
    print(f"{property}:", object[property])


def load_data_from_google_drive(url):
    url_processed='https://drive.google.com/uc?id=' + url.split('/')[-2]
    df = pd.read_csv(url_processed)
    return df


def split_date(df, DateColumn):
    #This function takes a dataframe, and a date coloumn, and splits it into
    #hour of the day
    #day of the week
    #month of the year
    #It returns the same dataframe/dataset with 3 new coloumns
    #Inputs are: 
    #df: a dataframe, or dataset
    #DateColumn: Name of datecoloumn as string
    df['Hour'] = pd.to_datetime(df[DateColumn]).dt.hour
    df['DayOfWeek'] = pd.to_datetime(df[DateColumn]).dt.day_name()
    df['Month'] = pd.to_datetime(df[DateColumn]).dt.month_name()
    return df


chronological_order_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

chronological_order_month = ['January', 'February', 'March']

