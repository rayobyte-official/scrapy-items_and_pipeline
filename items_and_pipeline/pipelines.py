# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class ItemsAndPipelinePipeline:
    def process_item(self, item, spider):  
        # Write the item to the file, and return the item      
        line = json.dumps(dict(item)) + "\n"  
        self.file.write(line)                
        return item
 
    def open_spider(self, spider):
        # Open the file when the spider starts
        self.file = open('plzscrape_result.json', 'w')
 
    def close_spider(self, spider):
        # Close the file when the spider ends
        self.file.close()

