# Live Football Scores Scraper

### Quick instructions to get the livescores spider up and running on an external machine

<hr>

### Installing required packages

**initial, pip install required packages through requirements.txt by running**
`pip install -r requirements.txt`

<hr>

### There are two ways to run the spider, depending on which method you'd prefer to use

#### Running in a python script
* Open up `main.py` and run the script. 
* This script uses schedule to automatically update current_scores.json every minute, so you should get consistent updates every few minutes (based on whatever you set it to). Obviously, be careful with how many requests you send... you don't want to get banned.

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
The code is currently setup to pull data from leagues that the user specifies.

If you want to edit this restriction (and instead create data for **_all_** live games), you simply need to remove all current leagues from `leagues_to_scrape`, which can be found within `livescoresSpider.py`.

To edit which leagues are selected, open up `livescoresSpider.py` (there are two versions of this script at present - one for shell, one for easier running in python - will be cleaned in the future) and edit `leagues_to_scrape`. To find league names, you'll need to log into flashscores and take a look at their naming conventions. Mobile link (easier to navgiate) can be accessed here - https://m.flashscore.co.uk/?s=2.
