
BOT_NAME = 'basic_scrapy_spider'

SPIDER_MODULES = ['basic_scrapy_spider.spiders']
NEWSPIDER_MODULE = 'basic_scrapy_spider.spiders'



ROBOTSTXT_OBEY = False

SCRAPEOPS_API_KEY = 'df11f0bb-3df1-42e3-b3b2-e6c03a344ce8'
SCRAPEOPS_PROXY_ENABLED = True

DOWNLOADER_MIDDLEWARES ={
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

CONCURRENT_REQUESTS = 1 # Only have maxiumium of 1 :(
