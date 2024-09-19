import scrapy
from items_and_pipeline.items import ItemsAndPipelineItem

class PlzscrapeSpider(scrapy.Spider):
    name = "plzscrape"
    allowed_domains = ["plzscrape.com"]
    start_urls = ["https://plzscrape.com/basic/html-elements"]

    def parse(self, response):
        # Extract the h1 heading
        itemAndPipelineItem = ItemsAndPipelineItem()

        h1_heading = response.css('h1::text').get()
        
        # extract all sections
        sections = response.css('section')
        
        for section in sections:
            # Extract the h2 heading and all paragraphs
            itemAndPipelineItem['h1'] = h1_heading
            itemAndPipelineItem['h2'] = section.css('h2::text').get()
            itemAndPipelineItem['paragraphs'] = section.css('p::text').getall()
            # Yield a dictionary with the extracted data
            yield itemAndPipelineItem