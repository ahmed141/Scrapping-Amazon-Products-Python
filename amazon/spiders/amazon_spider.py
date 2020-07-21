# -*- coding: utf-8 -*-
import scrapy
from amazon.items import AmazonItem

class AmazonProductSpider(scrapy.Spider):
  name = "AmazonDeals"
  allowed_domains = ["amazon.com"]
  
  #Use working product URL below
  start_urls = [
     "https://www.amazon.com/SanDisk-128GB-microSDXC-Memory-Adapter/dp/B073JYC4XM/ref=sr_1_1?dchild=1&fst=as%3Aoff&pf_rd_i=16225007011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=74069509-93ef-4a3c-8dca-a9e3fa773a64&pf_rd_r=Z9AA3C0H4WA03VDMHSM1&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1487012920&rnid=16225007011&s=computers-intl-ship&sr=1-1",
     "https://www.amazon.com/SAMSUNG-65-inch-Class-QLED-Built/dp/B0845ZSMWS?ref_=Oct_DLandingS_D_33c01d43_60&smid=ATVPDKIKX0DER",
     "https://www.amazon.com/dp/B07TZYFR71/ref=s9_acsd_al_bw_c2_x_1_i?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=AA0CBK9V1Q0D106GPYJK&pf_rd_t=101&pf_rd_p=2a3997e9-ef10-4d74-9499-6edc71eebb98&pf_rd_i=3003015011",
     "https://www.amazon.com/Apple-Watch-GPS-38mm-Space-Aluminium/dp/B07K39FRSL/ref=sr_1_3?dchild=1&fst=as%3Aoff&pf_rd_i=16225009011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=82d03e2f-30e3-48bf-a811-d3d2a6628949&pf_rd_r=T2Q96AHJC7XB8QG0SWTY&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1486423355&refinements=p_n_shipping_option-bin%3A3242350011&rnid=493964&s=electronics&sr=1-3"
     ]
 
  def parse(self, response):
    items = AmazonItem()
    title = response.xpath('//h1[@id="title"]/span/text()').extract()
    sale_price = response.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()').extract()
    category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
    availability = response.xpath('//div[@id="availability"]//text()').extract()
    items['product_name'] = ''.join(title).strip()
    items['product_sale_price'] = ''.join(sale_price).strip()
    items['product_category'] = ','.join(map(lambda x: x.strip(), category)).strip()
    items['product_availability'] = ''.join(availability).strip()
    yield items