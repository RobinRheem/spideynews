from scrapy.spiders import XMLFeedSpider


class RssHaniSpider(XMLFeedSpider):
    name = 'rss_hani'
    allowed_domains = ['hani.co.kr']
    start_urls = [
        'http://www.hani.co.kr/rss/politics/',
        'http://www.hani.co.kr/rss/economy/',
        'http://www.hani.co.kr/rss/society/',
        'http://www.hani.co.kr/rss/culture/',
        'http://www.hani.co.kr/rss/international/',
        'http://www.hani.co.kr/rss/sports/',
    ]
    iterator = 'xml'
    itertag = 'item'

    def parse_node(self, response, selector):
        item = {
            'title': selector.xpath('title').get(),
            'url': selector.xpath('link').get(),
            'description': selector.xpath('description').get(),
        }
        self.logger.info(f'item: {item}')
        return item
