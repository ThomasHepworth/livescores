import schedule
import time
import os
from livescoresSpider import flashscoreSpider
from scrapy.crawler import CrawlerProcess

def run_spider():
    # specify setting for when running through our script
    process = CrawlerProcess(settings={
        "FEEDS": {
            "current_scores.json": {"format": "json"},
        },
    })
    # Code to make script run like normal Python script
    process.crawl(flashscoreSpider)
    process.start()  # the script will block here until the crawling is finished

print('Scheduler initialised')
schedule.every(1).minutes.do(run_spider)
print('Next job is set to run at: ' + str(schedule.next_run()))

while True:
    schedule.run_pending()
    time.sleep(1)