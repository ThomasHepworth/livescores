# Live Football Scores Scraper

### Quick instructions to get the livescores spider up and running on an external machine

<hr>

**initial, pip install required packages through requirements.txt by running:**
`$pip install -r requirements.txt`

**You then need to move your working directory to into the first folder to allow scrapy to recognise the scrapy.cfg file. To do this, simply run:**
`cd livescores`

**To edit the leagues you want to pull data from, manually change "leagues_to_scrape" variable within livescores/spider/livescoresSpider.py**

**With that setup, you can create a json file with the resulting live football scores using:**
`scrapy crawl livescores -O livescores.json`
