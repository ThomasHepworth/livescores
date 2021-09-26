from scrapy.crawler import CrawlerProcess
from apscheduler.schedulers.twisted import TwistedScheduler
from livescoresSpider import flashscoreSpider # import our spider
import boto3
from botocore.client import Config
import pandas
import json


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


# setup process to output to a json file
process = CrawlerProcess(settings={
    "FEEDS": {
        "current_scores.json": {"format": "json",
                                "overwrite": "true"},
    },
})

# set up our scheduler and time between each run
scheduler = TwistedScheduler()
scheduler.add_job(create_old_scores, 'interval', id = 'create_old_scores', seconds=10)
scheduler.add_job(process.crawl, 'interval', args=[flashscoreSpider], id = 'scrape_scores_data', seconds=10)
# scheduler.add_job(write_to_s3, 'interval', id = 'write_to_s3', seconds=10)
scheduler.start()
process.start(False)
