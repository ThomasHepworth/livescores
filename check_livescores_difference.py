from prettytable import PrettyTable
import json
import numpy as np

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

# find new leagues
# read in current and old scores
current_scores = js_r("current_scores.json")
old_scores = js_r("old_scores.json")
new_league_data = {k: current_scores[0][k] for k in set(current_scores[0]) - set(old_scores[0])}

### find new games and score changes of existing games
# loop around our new games and find the corresponding info
def find_data_on_new_games(new_games, key):
    # create blank lists to store our values to
    new_teams = []
    new_time = []
    new_scores = []
    new_links = []
    # loop around our new_games
    for i in new_games:
        index = current_scores_data_for_league['teams'].index(i)
        new_teams.append(current_scores_data_for_league['teams'][index])
        new_time.append(current_scores_data_for_league['time'][index])
        new_scores.append(current_scores_data_for_league['scores'][index])
        new_links.append(current_scores_data_for_league['links'][index])
    # build a new dictionary with our new teams in it
    dictionary_to_output = {
            'teams': new_teams,
            'time': new_time,
            'scores': new_scores,
            'links': new_links,
        }
    return(dictionary_to_output)

def check_score_change(old_games, key):
    # create blank lists to store our values to
    score_change_team = []
    score_change_time = []
    score_change_score = []
    score_change_links = []

    for i in old_games:
        # find the current score and previous score so we can compare the two
        current_score = current_scores_data_for_league['scores']
        old_score = old_scores_data_for_league['scores']
        # if there's a new goal in the game, then add to our "updated_scores" dictionary
        if(old_score != current_score):
            index = current_scores_data_for_league['teams'].index(i)
            score_change_team.append(current_scores_data_for_league['teams'][index])
            score_change_time.append(current_scores_data_for_league['time'][index])
            score_change_score.append(current_scores_data_for_league['scores'][index])
            score_change_links.append(current_scores_data_for_league['links'][index])

        # build a new dictionary with our new teams in it
        if len(score_change_team) > 0: # only run and return a dictionary if we have items to report
            dictionary_to_output = {
                    'teams': score_change_team,
                    'time': score_change_time,
                    'scores': score_change_score,
                    'links': score_change_links,
                }
        else:
            dictionary_to_output = {}
        return(dictionary_to_output)

# find both new games that have recently started and existing games with changes
new_games_dict = {}
score_change_dict = {}
for key in old_scores[0]:
    # find new and old data for scores
    old_scores_data_for_league = old_scores[0][key]
    current_scores_data_for_league = current_scores[0][key]
    # find new games that didn't exist in the old scores
    new_games = set(current_scores_data_for_league['teams']) - set(old_scores_data_for_league['teams'])
    # find existing games so we can check for score changes
    old_games = set(current_scores_data_for_league['teams']) & set(old_scores_data_for_league['teams'])
    if len(new_games) > 0:
        new_games_dict[key] = find_data_on_new_games(new_games=new_games,
                                                    key=key)
    if len(old_games) > 0:
         dict_output = check_score_change(old_games=old_games,
                                                    key=key)
         print(dict_output)
         if len(dict_output) != 0:
             score_change_dict[key] = dict_output
