from prettytable import PrettyTable
import json

# functions to read + write to json
# read
def js_r(filename: str):
    """Read in json file using filename"""
    with open(filename) as f_in:
        return json.load(f_in)
# write
def writeToJSONFile(path, fileName, data):
    """Write dictionary/list to json filepath"""
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

#### ===== CREATE OUR TABLES FROM THE ABOVE JSON FILE
# specify leagues we want to print the whole table for
leagues_to_produce_tables_for = [
    'ENGLAND: Premier League',
    'ENGLAND: Championship'
]

def print_latest_scores(json_data,
                        league_data):
    """
    pull out our required info to populate our prettyTable.
    """
    teams = json_data[league_data]['teams']
    time = json_data[league_data]['time']
    score = json_data[league_data]['scores']
    links = json_data[league_data]['links']
    # initialise prettytable
    live_scores = PrettyTable()
    columns = ["Time", "Teams", "Score", "Live Link"]
    live_scores.title = league_data
    live_scores.add_column(columns[0], time)
    live_scores.add_column(columns[1], teams)
    live_scores.add_column(columns[2], score)
    live_scores.add_column(columns[3], links)
    return(live_scores)


def print_pretty_scores_data(dictionary_league_data):
    """Pretty print our latest scores data. This function takes our scores dictionaries as arguments and outputs our final tables"""
    for league in dictionary_league_data:
        print(print_latest_scores(dictionary_league_data,league))