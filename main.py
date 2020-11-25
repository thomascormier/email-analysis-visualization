import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt, timedelta as td

########################################################################################
#                                   Milestone 1
#
# We clean and stock our data properly into the pandas dataframe df.
########################################################################################


def generate_clean_dataframe():
    # Loading data into dataframe
    filename = "data/enron_100K.csv"
    df = pd.read_csv(filename, low_memory=False)

    # Dropping every useless columns
    df = df.drop(columns=["Message-ID", "From", "To", "X-cc", "X-bcc", "X-Folder", "X-Origin", "X-FileName",
                          "Cat_1_level_1", "Cat_1_level_2", "Cat_1_weight", "Cat_2_level_1", "Cat_2_level_2",
                          "Cat_2_weight", "Cat_3_level_1", "Cat_3_level_2", "Cat_3_weight", "Cat_4_level_1",
                          "Cat_4_level_2", "Cat_4_weight", "Cat_5_level_1", "Cat_5_level_2", "Cat_5_weight",
                          "Cat_6_level_1", "Cat_6_level_2", "Cat_6_weight", "Cat_7_level_1", "Cat_7_level_2",
                          "Cat_7_weight", "Cat_8_level_1", "Cat_8_level_2", "Cat_8_weight", "Cat_9_level_1",
                          "Cat_9_level_2", "Cat_9_weight", "Cat_10_level_1", "Cat_10_level_2", "Cat_10_weight",
                          "Cat_11_level_1", "Cat_11_level_2", "Cat_11_weight", "Cat_12_level_1", "Cat_12_level_2",
                          "Cat_12_weight", "labeled"])

    # Renaming the columns
    df = df.rename(columns={"Unnamed: 0": "id_mail",
                            "X-From": "From",
                            "X-To": "To"})

    # Reordering the columns
    df = df[["id_mail", "Date", "From", "To", "Subject", "content", "user"]]

    # Taking only the 5 firsts rows
    # df = df.head()

    # Change Date type to date
    df.Date = pd.to_datetime(df.Date)
    # Sort rows by ascending date
    df = df.sort_values('Date')

    # create a csv from this dataframe
    # df.to_csv(r'data/df.csv', index=False, header=True)

    return df


df = generate_clean_dataframe()
print("Data is now cleaned and loaded in a Dataframe.")

########################################################################################
#                                   Milestone 2
#
# In this milestone, we want to plot graphs that give repartition of mails sent and received, during a day.
# Also, we want to display how many mails were sent and received every day between 1980 and 2020.
########################################################################################


def graph_number_of_mail_per_hour(df):
    repartition_per_hour = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
                            "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0,
                            "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0,
                            "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0}

    for index, row in df.iterrows():
        hour = row['Date'].hour
        hour_str = str(hour)
        repartition_per_hour[hour_str] = repartition_per_hour[hour_str] + 1

    # sorted by key, return a list of tuples
    lists = repartition_per_hour.items()
    # unpack a list of pairs into two tuples
    x, y = zip(*lists)
    # display results
    plt.plot(x, y)
    plt.title('Number of mail received and sent per hour')
    plt.ylabel('Number of mails')
    plt.xlabel('Hour')
    plt.grid(True)
    plt.show()


def graph_number_of_mail_per_day(df):
    start = '1980-01-01'
    end = '2021-01-01'
    sd = dt.strptime(start, '%Y-%m-%d')
    ed = dt.strptime(end, '%Y-%m-%d')
    delta = ed - sd
    repartition_per_day = {}
    for i in range(delta.days + 1):
        repartition_per_day[str(sd + td(days=i))[:-9]] = 0

    print('dict initialized')

    # Keep only date part when using pandas.to_datetime
    df['just_date'] = df['Date'].dt.date
    for row in df['just_date']:
        repartition_per_day[str(row)] += 1

    # sorted by key, return a list of tuples
    lists = repartition_per_day.items()
    # unpack a list of pairs into two tuples
    x, y = zip(*lists)
    print('Data is ready. Start Plotting')
    # display results
    plt.plot(x, y)
    plt.title('Number of mail received and sent per day')
    plt.ylabel('Number of mails')
    plt.xlabel('Date')
    plt.grid(True)
    plt.show()


# graph_number_of_mail_per_hour(df)
# graph_number_of_mail_per_day(df)

########################################################################################
#                                   Milestone 3
########################################################################################


def most_commons_subject_topic(df):
    pass


def most_commons_content_topic(df):
    pass


########################################################################################
#                                   Milestone 4
########################################################################################


def graph_relationships(df, minNumberOfArcsUsed):
    pass


########################################################################################
#                                   Milestone 5
########################################################################################


def keywords_cloud(df):
    pass


########################################################################################

# TODO Milestone 3
# In this Milestone, we worked on the most common topics in the subject and the content of the mails.
most_commons_subject_topic(df)
most_commons_content_topic(df)

# TODO Milestone 4
# Relationship graph :
#   -   Nodes size : number of occurrence as a sender or a receiver in the dataframe
#   -   Edge (noeuds) : between every people who exchanges at least n emails (so that it stay readable)
graph_relationships(df, 1)

# TODO Milestone 5
# We want to create a Decision Tree that determine the categories of the main topic of the mail.
# Then we want to display a Keywords Cloud to show the mains topics in our data
keywords_cloud(df)


