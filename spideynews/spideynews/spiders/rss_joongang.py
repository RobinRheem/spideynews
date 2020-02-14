# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider


class RssJoongangSpider(XMLFeedSpider):
    name = 'rss_joongang'
    allowed_domains = ['rss.joins.com']
    start_urls = [
        'https://rss.joins.com/joins_politics_list.xml',
        'https://rss.joins.com/joins_money_list.xml',
        'https://rss.joins.com/joins_life_list.xml',
        'https://rss.joins.com/joins_culture_list.xml',
        'https://rss.joins.com/joins_world_list.xml',
        'https://rss.joins.com/joins_sports_list.xml',
        'https://rss.joins.com/joins_star_list.xml',
        'https://rss.joins.com/joins_it_list.xml',
    ]
    iterator = 'xml'
    itertag = 'item'

    def parse_node(self, response, selector):
        item = {
            'title': selector.xpath('title/text()').get(),
            'url': selector.xpath('link/text()').get(),
            'description': selector.xpath('description/text()').get(),
            'published_at': selector.xpath('pubDate/text()').get(),
            'author': selector.xpath('author/text()').get(),
            'subject': 'none',
            'category': 'none',
        }
        return item
