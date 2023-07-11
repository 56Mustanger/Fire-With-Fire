
from itemadapter import ItemAdapter


class BasicScraperPipeline:
    def process_item(self, item, spider):
        return item
