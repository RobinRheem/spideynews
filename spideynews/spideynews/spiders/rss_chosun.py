from scrapy.spiders import XMLFeedSpider


class RssChosunSpider(XMLFeedSpider):
    name = 'rss_chosun'
    allowed_domains = ['chosun.com']
    start_urls = [
        'http://www.chosun.com/site/data/rss/politics.xml',
        'http://biz.chosun.com/site/data/rss/rss.xml',
        'http://www.chosun.com/site/data/rss/national.xml',
        'http://www.chosun.com/site/data/rss/culture.xml',
        'http://www.chosun.com/site/data/rss/international.xml',
        'http://www.chosun.com/site/data/rss/sports.xml',
        'http://www.chosun.com/site/data/rss/ent.xml',
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
            'category': selector.xpath('category/text()').get(),
            'author': selector.xpath('author/text()').get(),
        }
        return item
