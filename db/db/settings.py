# -*- coding: utf-8 -*-

# Scrapy settings for db project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'db'

SPIDER_MODULES = ['db.spiders']
NEWSPIDER_MODULE = 'db.spiders'

'''
设置redis配置
'''
# SCHEDULER="scrapy_redis.scheduler.Scheduler"
# DUPEFILTER_CLASS="scrapy_redis.dupefilter.RFPDupeFilter"
#
# REDIS_HOST = 'LOCALHOST' #主机名
# REDIS_PORT = '6379'      #端口
# REDIS_URL = 'redis：//userLpass@hostname:9001'
'''
设置代理user-agent
'''

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

'''
设置代理ip池
'''

IPPOOL=[
    {"ipaddr":"119.128.172.105:8118"},
    {"ipaddr":"175.42.125.195:8118"},
    {"ipaddr":"49.79.192.143:61234"},
    {"ipaddr":"121.62.56.78:61234"},
    {"ipaddr":"183.159.90.127:18118"},
    {"ipaddr":"221.202.178.235:61202"},
    {"ipaddr":"182.88.212.46:8123"},
    {"ipaddr":"183.159.92.52:18118"},
    {"ipaddr":"123.8.84.143:61202"},
    {"ipaddr":"60.177.230.127:18118"},
    {"ipaddr":"60.177.231.248:18118"},
    {"ipaddr":"118.180.125.206:8123"},
    {"ipaddr":"27.193.172.125:61202"},
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'db (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 设置爬虫的默认并发数，并发指的是同时处理request的请求个数
CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

#设置下载延迟
DOWNLOAD_DELAY = 5
#重新请求
RETRY_ENABLED = False
#重试次数
# RETRY_TIMES = 3

#设置下载超时
DOWNLOAD_TIMEOUT = 15

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
  'Accept-Language': 'en',
  'Cookies': 'bid=D3VeUmdS2xM; ll="118267"; _vwo_uuid_v2=D036E792B19965F77F65F1A6ACCED5ADF|bd161d23b8c487b24d1933da0dfa5a38; gr_user_id=7e780f55-10cf-4e15-87ac-685c125212b8; __utmc=30149280; __utmc=223695111; viewed="30170596_27008704_4289836"; ap=1; __utmz=223695111.1523438767.9.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=30149280.1523450282.16.10.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ct=y; __utma=30149280.1914999939.1519826275.1523689619.1523692425.25; __utma=223695111.745632772.1515342962.1523689619.1523692425.21; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1523944610%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DuvH3wsfsrnKyNNxRGARy2LHp_M-9C6uYaiwjXKBxNeVbbsxGsVu8s9adoH7P1Mrd%26wd%3D%26eqid%3Df75096940003e3fa000000055acdd4d0%22%5D; _pk_id.100001.4cf6=1b692747a2e89ea7.1515342824.21.1523944610.1523694804.; _pk_ses.100001.4cf6=*',
  'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 OPR/52.0.2871.64',
  'Referer': 'https://movie.douban.com/',
  'Host': 'movie.douban.com'
}

# USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 OPR/52.0.2871.40'

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'db.middlewares.DbSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #启用自己的user-agent代理
    'db.middlewares.RandomUserAgent': 1,
    'db.middlewares.DbDownloaderMiddleware': 543,
    # 禁用Scrapy默认启动的UserAgentMiddleware
    'scrapy.downloadmiddlewares.useragent.UserAgentMiddleware': None,
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 543,
    # 'db.middlewares.MyproxiesSpiderMiddleware': 125


}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'db.pipelines.DbPipeline': 300,
}

LOG_LEVEL = 'INFO'
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
