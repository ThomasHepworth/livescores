import scrapy
import itertools # used to remove lists of lists
from scrapy.crawler import CrawlerProcess

# url for the main flashscores website (we're not scraping directly from this)
# links can be pasted to the end of this to pull out further info on the game in a web browser
fs_url = 'https://www.flashscore.co.uk'

# specify the leagues you want to scrape from
leagues_to_scrape = [
    'ENGLAND: Premier League',
]

class flashscoreSpider(scrapy.Spider):
    name = "flashscore"
    start_urls = ['https://m.flashscore.co.uk/?s=2']

    def parse(self, response):
        core_xpath = response.xpath('//*[@id="score-data"]')

        scores = {}
        for cnt, h4 in enumerate(core_xpath.xpath('h4'), start=1):
            # pull our h4 tags (these contain the names of each league)
            key = h4.xpath('normalize-space()').get().strip()
            # if our league is in our list of leagues to scrape, pull data
            if key in leagues_to_scrape:
                # pull info on each team playing
                # to do this, we're using the knowledge that each team name is bounded by a span tag (which contains the match time)
                # if we pull all text between span tags, we can avoid having spaces (which are used when there has been a red card)
                # calculate how many span tags we've had so far (for the entire page)
                span_total_len = len(
                    response.xpath(
                        '//div[@id = "score-data"]/h4[$count]//preceding-sibling::span', count=cnt).getall()
                )
                # calc span tags in current header section we're looking at
                span_tags = core_xpath.xpath(
                    '//span[count(preceding-sibling::h4)=$count]',
                    count=cnt
                )

                teams = []
                # pull out team names and use string to concatenate
                for count, span in enumerate(span_tags, start=1):
                    teams.append(core_xpath.xpath(
                            'string(//text()[count(preceding-sibling::span)=$count])',
                            count=count + span_total_len).getall())
                teams = list(itertools.chain(*teams))

                # pull game time
                to_scrape = {
                    "time": ('span[count(preceding-sibling::h4)=$count]', './/text()'),
                    "scores": ('a[count(preceding-sibling::h4)=$count]', './/text()'),
                    "links": ('a[count(preceding-sibling::h4)=$count]', './/@href'),
                }

                game_info = {
                    key: core_xpath.xpath(xpath, count=cnt).xpath(html_tag).getall()
                    for key, (xpath, html_tag) in to_scrape.items()
                }
                game_info["links"] = ["%s%s" % (fs_url, i) for i in game_info["links"]]

                # save data to list
                scores[key] = {
                    'teams': teams,
                    **game_info
                }
        yield scores
