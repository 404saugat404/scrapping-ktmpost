from typing import Any
import scrapy
from scrapy.http import Response


class news_extraction(scrapy.Spider):
    
    name='news'
    allowed_domain='https://kathmandupost.com/'
    start_urls=[
        'https://kathmandupost.com/'
    ]

    def parse(self, response):
        title_links = response.css('ul.trending-topics-list li a')
        
        

        for link in title_links:
            href = link.css('::attr(href)').get()
            yield response.follow(href, callback=self.parse_news)

        title2=response.css('div.row.order h3 a')
        for link2 in title2:
            href = link2.css('::attr(href)').get()
            yield response.follow(href, callback=self.parse_news2)

    def parse_news(self, response):
        

        topic = response.css('div.col-sm-8 h1::text').get()
        news = response.css('div.col-sm-8 section.story-section p::text').extract()
        image = response.css('div.col-sm-8 img::attr(src)').get()

        yield{
                    'topic':topic,
                    'news':news,
                    'image':image
                    }

    def parse_news2(self, response):
        

        topic2 = response.css('div.col-sm-8 h1::text').get()
        news2 = response.css('div.col-sm-8 section.story-section p::text').extract()
        image2 = response.css('div.col-sm-8 img::attr(src)').get()

        yield{
                    'topic':topic2,
                    'news':news2,
                    'image':image2
                    }        
    

   

   
    
        # title2=response.css('div.row.order h3 a::text').extract()
        # news_details=response.css('div.row.order div p::text').extract()
        # img_links=response.css('div.row.order article img.img-responsive::attr(data-src)').extract()
        # print(img_links)

        # print(news_details)


        


        
        # items['title']=title
        # items['title2']=title2
        # items['news_details']=news_details
        # items['img_links']=img_links
        



        # yield items