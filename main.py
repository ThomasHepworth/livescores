from scrapy.crawler import CrawlerProcess
from apscheduler.schedulers.twisted import TwistedScheduler
from livescoresSpider import flashscoreSpider # import our spider

# setup process to output to a json file
process = CrawlerProcess(settings={
    "FEEDS": {
        "current_scores.json": {"format": "json"},
    },
})
# set up our scheduler and time between each run
scheduler = TwistedScheduler()
scheduler.add_job(process.crawl, 'interval', args=[flashscoreSpider], minutes=1)
scheduler.start()
process.start(False)
