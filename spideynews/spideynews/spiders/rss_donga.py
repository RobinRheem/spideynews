from scrapy.spiders import XMLFeedSpider


class RssDongaSpider(XMLFeedSpider):
    name = 'rss_donga'
    allowed_domains = ['rss.donga.com']
    start_urls = [
        'https://rss.donga.com/politics.xml',
        'https://rss.donga.com/economy.xml',
        'https://rss.donga.com/national.xml',
        'https://rss.donga.com/culture.xml',
        'https://rss.donga.com/international.xml',
        'https://rss.donga.com/sports.xml',
    ]
    namespaces = [
        ('media', 'http://search.yahoo.com/mrss/'),
    ]
    iterator = 'xml'
    itertag = 'item'

    def parse_node(self, response, selector):
        item = {
            'title': selector.xpath('title/text()').get(),
            'url': selector.xpath('link/text()').get(),
            'description': selector.xpath('description/text()').get(),
            'published_at': selector.xpath('pubDate/text()').get(),
            'subject': 'none',
            'category': 'none',
            'media': selector.xpath('content/text()').get(),
        }
        return item
