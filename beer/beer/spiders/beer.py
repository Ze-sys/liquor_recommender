import scrapy
import itertools
from scrapy.selector import Selector

import pandas as pd

import glob

product_type='beer'

def url_(prdct_type, page):

   url = f'https://www.bcliquorstores.com/product-catalogue?search={prdct_type}&sort=consumerRating:desc&page={page}'
   return url

urls = [url_(product_type,k) for k in range(1,3)] 

class AllrecipesSpider(scrapy.Spider):
    name = 'beerdb'
    allowed_domains = ['http://www.bcliquorstores.com']
    start_urls = urls  
    print(urls[0])
    def parse(self, response):
         my_dict = {
               'product_name ': response.xpath("//div[@class='product-name']/text()").extract()

            }
         print(my_dict)
         yield my_dict


