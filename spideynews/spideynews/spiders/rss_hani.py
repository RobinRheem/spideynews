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
            'title': selector.xpath('title/text()').get(),
            'url': selector.xpath('link/text()').get(),
            'description': selector.xpath('description/text()').get(),
            'published_at': selector.xpath('pubDate/text()').get(),
            'subject': selector.xpath('dc:subject/text()').get(),
            'category': selector.xpath('dc:category/text()').get(),
        }
        self.logger.info(f'item: {item}')
        return item
