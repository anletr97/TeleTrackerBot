import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import Product

class ProductSpider(Spider):
    name = "product"
    allowed_domains=["www.tiki.vn"]
    start_urls=["https://tiki.vn/microsoft-surface-pro-2018-core-i5-8250u-8g-256gb-hang-chinh-hang-p8286081.html",
    "https://tiki.vn/dien-thoai-iphone-12-pro-max-128gb-hang-chinh-hang-p70771651.html"]

    def parse(self, res):
        #return item
        item = Product()
        # product header
        product_name = Selector(res).css('div.header')
        # product price css
        product_image = Selector(res).css('div.container')
        # product price
        product_price = Selector(res).css('div.product-price')
        item['pName'] = product_name.css('h1.title::text').get()
        item['pPrice'] = res.xpath("//meta[@itemprop='price']/@content").extract_first()
        item['pImage'] = product_image.css('img::attr(src)').extract()
        yield item