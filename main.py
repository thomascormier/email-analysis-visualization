import pandas as pd

########################################################################################
#                                   Milestone 1
########################################################################################


def generate_clean_dataframe():
    # Loading data into dataframe
    filename = "data/enron_100K.csv"
    df = pd.read_csv(filename, low_memory=False)

    # Dropping every useless columuns
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


########################################################################################
#                                   Milestone 2
########################################################################################


def graph_number_of_mail_received_per_hour(df):
    pass


def graph_number_of_mail_sent_per_hour(df):
    pass


def graph_number_of_mail_received_per_day(df):
    pass


def graph_number_of_mail_sent_per_day(df):
    pass


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

# Milestone 1
# We clean and stock our data properly into the pandas dataframe df
df = generate_clean_dataframe()

# TODO Milestone 2
# In this milestone, we want to plot graphs that give repartition of mails sent and received, during a day.
# Also, we want to display how many mails were sent and received every day between 1980 and 2020.
graph_number_of_mail_received_per_hour(df)
graph_number_of_mail_sent_per_hour(df)
graph_number_of_mail_received_per_day(df)
graph_number_of_mail_sent_per_day(df)

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


