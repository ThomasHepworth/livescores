from scrapy.crawler import CrawlerProcess
from apscheduler.schedulers.twisted import TwistedScheduler
from livescoresSpider import flashscoreSpider # import our spider
from finalscoresSpider import fulltimeSpider # import our fulltime spider
import json
from current_scores import print_pretty_scores_data
from check_livescores_difference import find_latest_scores_data
import time

def js_r(filename: str):
    with open(filename) as f_in:
        return json.load(f_in)

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

# set up our scheduler and time between each run
def create_old_scores():
    # read in our previous scores
    if __name__ == "__main__":
        old_scores = js_r('current_scores.json')
    # write to a new json file, "old_scores"
    writeToJSONFile('', 'old_scores', old_scores)
    print("old_scores successfully written to json")

def create_new_scores_v2():
    # read in our previous scores
    if __name__ == "__main__":
        current_scores = js_r('current_scores.json')
    # write to a new json file, "old_scores"
    writeToJSONFile('', 'current_scores_v2', current_scores)
    print("new_scores successfully written to json")

create_new_scores_v2() # run this to initialise our current_scores_v2.json file

def run_scrape():
    # read in our previous scores
    if __name__ == "__main__":
        old_scores = js_r('current_scores_v2.json')
    # write to a new json file, "old_scores"
    writeToJSONFile('', 'old_scores', old_scores)
    print("Old scores successfully written to json file - old_scores.json")


    process.crawl(flashscoreSpider)
    time.sleep(1) # give it a second to sleep...

    # read in our previous scores
    if __name__ == "__main__":
        current_scores = js_r('current_scores.json')
    # write to a new json file, "old_scores"
    writeToJSONFile('', 'current_scores_v2', current_scores)
    print("New scores successfully written to json file - current_scores_v2.json")

    score_changes = find_latest_scores_data()
    print_pretty_scores_data(score_changes['new_games'])
    print_pretty_scores_data(score_changes['new_league'])
    print_pretty_scores_data(score_changes['score_change'])
    print("Checked")

# setup process to output to a json file
process = CrawlerProcess(settings={
    "FEEDS": {
        "current_scores.json": {"format": "json",
                                "overwrite": "true"},
    },
})

process_fulltime = CrawlerProcess(settings={
    "FEEDS": {
        "final_scores.json": {"format": "json",
                                "overwrite": "true"},
    },
})
# set up our scheduler and time between each run
scheduler = TwistedScheduler()
scheduler.add_job(run_scrape, 'interval', id = 'checker', seconds=15)
# scheduler.add_job(process_fulltime.crawl, 'interval', args=[fulltimeSpider], id = 'scrape_fulltime_scores_data', minutes=30, max_instances=1)
scheduler.start()
process.start(False)
