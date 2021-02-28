import schedule
import time
import os
from livescores.spiders.livescoresSpider import flashscoreSpider

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
schedule.every(5).minutes.do()
print('Next job is set to run at: ' + str(schedule.next_run()))

while True:
    schedule.run_pending()
    time.sleep(1)