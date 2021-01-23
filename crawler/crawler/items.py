# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

"""
    Product crawled will be mapped by this model
"""
class Product(scrapy.Item):
    pName = scrapy.Field()
    pPrice = scrapy.Field()
    # pDiscountPrice = scrapy.Field()
    # pCode = scrapy.Field()
    pImage = scrapy.Field()
    # pFeature = scrapy.Field()
    # pSeller = scrapy.Field()
    pass
