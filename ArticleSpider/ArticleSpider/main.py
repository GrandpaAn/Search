# -*- coding: utf-8 -*-
from scrapy.cmdline import execute

import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))  #"F:\Django\Search\ArticleSpider"
# execute(["scrapy", "crawl", "jobbole"])
execute(["scrapy", "crawl", "zhihu"])