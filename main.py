from scrapy.crawler import CrawlerProcess
from apscheduler.schedulers.twisted import TwistedScheduler
from livescoresSpider import flashscoreSpider # import our spider
import boto3
from botocore.client import Config
import pandas
import json

ACCESS_KEY_ID = 'AKIAJV4RWLDFYXCBP7XQ'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'livescores-jeffbot'

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


def write_to_s3():
    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )
    # write to s3
    s3.Bucket(BUCKET_NAME).upload_file('old_scores.json', 'current_scores.json')

    print("Sent files to S3 successfully")


# setup process to output to a json file
process = CrawlerProcess(settings={
    "FEEDS": {
        "current_scores.json": {"format": "json",
                                "overwrite": "true"},
    },
})

# set up our scheduler and time between each run
scheduler = TwistedScheduler()
scheduler.add_job(create_old_scores, 'interval', id = 'create_old_scores', seconds=180)
scheduler.add_job(process.crawl, 'interval', args=[flashscoreSpider], id = 'scrape_scores_data', seconds=180)
# scheduler.add_job(write_to_s3, 'interval', id = 'write_to_s3', seconds=10)
scheduler.start()
process.start(False)
