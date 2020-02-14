from scrapy.spiders import XMLFeedSpider


class RssJtbcSpider(XMLFeedSpider):
    name = 'rss_jtbc'
    allowed_domains = ['jtbc.joins.com']
    start_urls = [
        'http://fs.jtbc.joins.com/RSS/politics.xml',
        'http://fs.jtbc.joins.com/RSS/economy.xml',
        'http://fs.jtbc.joins.com/RSS/society.xml',
        'http://fs.jtbc.joins.com/RSS/culture.xml',
        'http://fs.jtbc.joins.com/RSS/international.xml',
        'http://fs.jtbc.joins.com/RSS/sports.xml',
        'http://fs.jtbc.joins.com/RSS/entertainment.xml',
        'http://fs.jtbc.joins.com//RSS/newsflash.xml',
    ]
    iterator = 'xml'
    itertag = 'item'

    def parse_node(self, response, selector):
        item = {
            'title': selector.xpath('title/text()').get(),
            'url': selector.xpath('link/text()').get(),
            'description': selector.xpath('description/text()').get(),
            'published_at': selector.xpath('pubDate/text()').get(),
        }
        return item
