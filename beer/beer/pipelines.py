# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem
# from scrapy import log
import logging

settings = get_project_settings()

class BeerPipeline:
    def process_item(self, item, spider):
        return item


# class RecipesPipeline:
#     def process_item(self, item, spider):
#         return item


class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            # logging.msg("Recipe added to MongoDB database!",
            #         level=logging.DEBUG, spider=spider)
        return item
   
