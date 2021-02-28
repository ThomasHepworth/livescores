# Live Football Scores Scraper

### Quick instructions to get the livescores spider up and running on an external machine

<hr>

**initial, pip install required packages through requirements.txt by running**
`$pip install -r requirements.txt`

<br>
<hr>

### Teere are two ways to run the spider, depending on which method you'd prefer to use

#### Running in a python script
* Open up main.py and run the script. 
* This script uses schedule to automatically update current_scores.json every minute.

#### Running using the shell
Similarly to the above, you can also run the spider freely in the shell.

* To do so, first open up a fresh terminal session.
* From here, move your directory into the first folder to allow scrapy to recognise the scrapy.cfg file. To do this, simply run
`cd livescores`. 
* To run the spider, simply use `scrapy crawl livescores` in the terminal. Scrapy will automatically scan your python files and find any available spiders, then run the code using this.
* If you'd like to output your data to a json file with the resulting live football, you can instead use
`scrapy crawl livescores -O livescores.json`

<br>
<hr>

### Editing internal variables to change the outputs
The code is currently setup to only pull data from specific leagues.

If you want to remove this restriction (and instead create data for **_all_** live games), you either need to change how `leagues_to_scrape` is defined in `livescoresSpider.py`, or just remove the if statement which filters for only leagues on interest.

To edit which leagues are selected, open up `livescoresSpider.py` (there are two versions of this script at present, will be cleaned in the future) and edit `leagues_to_scrape`. To find league names, you'll need to log into flashscores and take a look at their naming convent
