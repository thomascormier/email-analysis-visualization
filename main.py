import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
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

    return df


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
    plt.title('Number of mails received and sent per hour')
    plt.ylabel('Number of mails')
    plt.xlabel('Hour')
    plt.grid(True)
    plt.savefig("res/repartition_per_hour.png")
    plt.close()


def graph_number_of_mail_per_day(df):
    start = '1980-01-01'
    end = '2021-01-01'
    sd = dt.strptime(start, '%Y-%m-%d')
    ed = dt.strptime(end, '%Y-%m-%d')
    delta = ed - sd
    repartition_per_day = {}
    for i in range(delta.days + 1):
        repartition_per_day[str(sd + td(days=i))[:-9]] = 0

    # Keep only date part when using pandas.to_datetime
    df['just_date'] = df['Date'].dt.date
    for row in df['just_date']:
        repartition_per_day[str(row)] += 1

    # sorted by key, return a list of tuples
    lists = repartition_per_day.items()
    # unpack a list of pairs into two tuples
    x, y = zip(*lists)
    # display results
    plt.plot(x, y)
    plt.title('Number of mails received and sent per day')
    plt.ylabel('Number of mails')
    plt.xlabel('Date')
    plt.savefig("res/repartition_per_day.png")
    plt.close()


########################################################################################
#                                   Milestone 3
#
# In this Milestone, we worked on the most common topics in the subject and the content of the mails.
########################################################################################


def most_commons_subject_topic(df):
    all_subjects = {}
    container = ""
    for sub in df.Subject:
        container = container + str(sub)

    split = container.split()

    for string in split:
        if string in all_subjects:
            all_subjects[string] += 1
        else:
            all_subjects[string] = 1

    # We only take the n most commons keys in the previous dict
    n = 22
    top_subjects = dict(sorted(all_subjects.items(), key=lambda item: item[1], reverse=True)[:n])

    useless_subject = ['-', 'for', 'of', 'to', 'and', 'and', 'on', 'the', 'in', '&', 'from', 'with', 'at', 'FW:', '--',
                       '2001', 'a', 'is', 'New', 'May']

    most_commons_subjects = top_subjects
    for us in useless_subject:
        most_commons_subjects.pop(us, None)

    keys = most_commons_subjects.keys()
    values = most_commons_subjects.values()
    plt.bar(keys, values)
    plt.title('Most common subjects topics')
    plt.ylabel('Number of occurrences')
    plt.xlabel('Topics')
    plt.savefig("res/most_commons_subjects.png")
    plt.close()

    # return most_commons_subjects


def most_commons_content_topic(df):
    all_contents = {}
    container = ""
    for c in df.content:
        container = container + str(c)

    split = container.split()

    for string in split:
        if string in all_contents:
            all_contents[string] += 1
        else:
            all_contents[string] = 1

    # We only take the n most commons keys in the previous dict
    n = 100
    top_contents = dict(sorted(all_contents.items(), key=lambda item: item[1], reverse=True)[:n])

    useless_contents = ['>', 'that', 'be', 'you', 'will', 'I', 'The', 'have', 'by', 'this', 'are', 'as', '=20',
                        'it', 'or', 'not', 'has', 'the', 'to', 'and', 'of', 'a', 'in', 'for', 'is', 'on', 'with', 'at',
                        '-', 'from','we', 'your', 'an', 'was', 'would', 'its', '=', 'if', 'can', 'but', 'our', 'he',
                        'any', 'which', 'all', 'about', 'they', 'more', 'been', 'AM', 'up', 'their', 'me', 'said',
                        'Subject:', 'To:', 'PM', 'cc:', 'If', 'From:', 'also', 'out', 'new', '--', '?', '&', 'other',
                        'get', 'who', 'some', 'one', 'do', 'had', 'were', 'his', 'We', 'may', 'than', 'This',
                        'state', 'should', 'last', 'so', 'could', 'know', 'In', 'like', 'company', 'Please', 'please',
                        'what', 'my', 'need', 'into', 'time', 'when', 'over', 'A', 'Sent:', 'these', 'no', 'two',
                        'there', 'Message-----']

    most_commons_contents = top_contents
    for uc in useless_contents:
        most_commons_contents.pop(uc, None)

    keys = most_commons_contents.keys()
    values = most_commons_contents.values()
    plt.bar(keys, values)
    plt.title('Most common contents topics')
    plt.ylabel('Number of occurrences')
    plt.xlabel('Topics')
    plt.savefig("res/most_commons_contents.png")
    plt.close()


########################################################################################
#                                   Milestone 4
#
# Relationship graph :
#   -   Nodes size : number of occurrence as a sender or a receiver in the dataframe
#   -   Edge : between every people who exchanges at least n emails (so that it stay readable)
########################################################################################


def build_network_graph(df, n):
    """
    Generate a new dataframe much more suited to the users treatment
    We create many tuples (sender, receiver) and we count their number occurrences.

    :param df: our initial dataframe
    :return: a new dataframe that only contains From, To
    """
    df = df.drop(columns=["id_mail", "Date", "Subject", "content", "user"])

    # We create the empty graph
    graph = {}

    # We create an array of string containing all correspondents
    correspondents = []

    # We iterate on the dataframe
    cpt = 0
    print("In progress, wait until 100 for 100 000 rows to be processed")
    for index, row in df.iterrows():
        cpt += 1
        if cpt % 1000 == 0:
            print(int(cpt/1000))

        # We rename our values for a better readability
        sender = row['From']
        receivers_field = row['To']
        # We create an array receivers that stores all the receivers
        receivers = []

        # type treatment so that nan values are now a string "nan" or "Nan"
        receivers_field = str(receivers_field)

        if not (sender in correspondents):
            correspondents.append(sender)

        # We test if the receiver is a NaN value, if so, we drop the row
        if receivers_field.lower() == "nan":
                df.drop(index, inplace=True)
            # Now the data is cleaner, we start our data processing
        else:

            # We test if there is several receivers by checking if their is a ", " in the receivers_field
            if ", " in receivers_field:
                receivers = receivers_field.split(", ")
            for r in receivers:
                if not(r in correspondents):
                    correspondents.append(r)

        for r in receivers:
            # If the tuple is already in the graph, we increment its value
            if tuple([sender, r]) in graph:
                graph[sender, r] = graph[sender, r] + 1
                # graph[r, sender] = graph[r, sender] + 1
            # If not, we insert the tuple and set its value to 1
            else:
                graph[sender, r] = 1
                # graph[r, sender] = 1

    top_n_data = dict(sorted(graph.items(), key=lambda item: item[1], reverse=True)[:n])

    print("Start building graph")

    graph = nx.Graph()

    for d in top_n_data:
        graph.add_edge(d[0][1], d[1][0])

    nx.draw(graph)
    plt.savefig("res/network_graph.png")
    plt.close()


########################################################################################

# Milestone 1
df = generate_clean_dataframe()
print("Data cleaned and loaded in a Dataframe.")

# Milestone 2
graph_number_of_mail_per_hour(df)
print("res/repartition_per_hour.png generated")
graph_number_of_mail_per_day(df)
print("res/repartition_per_day.png generated")

# Milestone 3
most_commons_subject_topic(df)
print("res/most_commons_subjects.png generated")
most_commons_content_topic(df)
print("res/most_commons_contents.png generated")

# Milestone 4
build_network_graph(df, 100)
print("res/network_graph.png generated")
