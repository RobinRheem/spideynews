from scrapy.spiders import XMLFeedSpider


class RssKhanSpider(XMLFeedSpider):
    name = 'rss_khan'
    allowed_domains = ['khan.co.kr']
    start_urls = [
        'http://www.khan.co.kr/rss/rssdata/politic_news.xml',
        'http://www.khan.co.kr/rss/rssdata/economy_news.xml',
        'http://www.khan.co.kr/rss/rssdata/society_news.xml',
        'http://www.khan.co.kr/rss/rssdata/culture_news.xml',
        'http://www.khan.co.kr/rss/rssdata/kh_world.xml',
        'http://www.khan.co.kr/rss/rssdata/kh_sports.xml',
        'http://www.khan.co.kr/rss/rssdata/kh_entertainment.xml',
        'http://www.khan.co.kr/rss/rssdata/it_news.xml',
    ]
    namespaces = [
        ('dc', 'http://purl.org/dc/elements/1.1/'),
    ]
    iterator = 'xml'
    itertag = 'item'

    def parse_node(self, response, selector):
        item = {
            'title': selector.xpath('title/text()').get(),
            'url': selector.xpath('link/text()').get(),
            'description': selector.xpath('description/text()').get(),
            'published_at': selector.xpath('dc:date/text()').get(),
            'subject': 'none',
            'category': selector.xpath('category/text()').get(),
            'author': selector.xpath('author/text()').get(),
        }
        return item
