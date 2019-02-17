# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

#

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
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
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 ",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",

]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

PROXIES = [
    {'ip_port': '182.88.124.220:9797', 'user_pass': ''},
    {'ip_port': '123.232.126.82:8118', 'user_pass': ''},
    {'ip_port': '123.162.196.81:808', 'user_pass': ''},
    {'ip_port': '60.168.56.112:9999', 'user_pass': ''},
    {'ip_port': '119.163.121.122:8080', 'user_pass': ''},
    {'ip_port': '112.13.93.43:8088', 'user_pass': ''},
    {'ip_port': '123.7.177.20:9999', 'user_pass': ''},
    {'ip_port': '117.70.131.94:808', 'user_pass': ''},
    {'ip_port': '218.244.46.6:8118', 'user_pass': ''},
    {'ip_port': '42.6.249.60:80', 'user_pass': ''},
    {'ip_port': '58.221.179.234:8081', 'user_pass': ''},
    {'ip_port': '113.227.189.107:80', 'user_pass': ''},
    {'ip_port': '211.103.208.244:80', 'user_pass': ''},
    {'ip_port': '125.211.202.26:53281', 'user_pass': ''},
    {'ip_port': '60.214.155.243:53281', 'user_pass': ''},
    {'ip_port': '112.192.18.230:8118', 'user_pass': ''},
    {'ip_port': '183.136.232.149:9999', 'user_pass': ''},
    {'ip_port': '61.152.230.26:8080', 'user_pass': ''},
    {'ip_port': '42.178.202.180:8888', 'user_pass': ''},
    {'ip_port': '124.90.27.96:8118', 'user_pass': ''},
    {'ip_port': '203.74.4.1:80', 'user_pass': ''},
    {'ip_port': '180.110.151.92:8118', 'user_pass': ''},
    {'ip_port': '212.200.246.24:80', 'user_pass': ''},
    {'ip_port': '219.150.189.212:9999', 'user_pass': ''},
    {'ip_port': '114.229.32.37:25660', 'user_pass': ''},
    {'ip_port': '112.30.130.66:9000', 'user_pass': ''},
    {'ip_port': '183.63.101.62:52225', 'user_pass': ''},
    {'ip_port': '222.186.45.57:63229', 'user_pass': ''},
    {'ip_port': '59.63.178.203:52225', 'user_pass': ''},
    {'ip_port': '60.176.200.235:8888', 'user_pass': ''},
    {'ip_port': '222.216.195.118:808', 'user_pass': ''},
    {'ip_port': '122.231.39.72:808', 'user_pass': ''},
    {'ip_port': '203.74.4.4:80', 'user_pass': ''},
    {'ip_port': '59.40.51.46:8010', 'user_pass': ''},
    {'ip_port': '222.240.233.154:80', 'user_pass': ''},
    {'ip_port': '183.61.9.25:8118', 'user_pass': ''},
    {'ip_port': '112.248.228.13:8888', 'user_pass': ''},
    {'ip_port': '119.36.92.47:81', 'user_pass': ''},
    {'ip_port': '111.62.251.66:80', 'user_pass': ''},
    {'ip_port': '120.9.4.16:8888', 'user_pass': ''},
    {'ip_port': '222.220.34.74:1337', 'user_pass': ''},
    {'ip_port': '36.57.208.131:51225', 'user_pass': ''},
    {'ip_port': '183.64.111.243:80', 'user_pass': ''},
    {'ip_port': '61.38.236.98:808', 'user_pass': ''},
    {'ip_port': '111.22.113.234:53281', 'user_pass': ''},
    {'ip_port': '111.62.243.64:8080', 'user_pass': ''},
    {'ip_port': '111.242.193.78:53281', 'user_pass': ''},
    {'ip_port': '114.222.83.106:8118', 'user_pass': ''},
    {'ip_port': '124.72.216.106:808', 'user_pass': ''},
    {'ip_port': '113.116.157.16:53281', 'user_pass': ''},
    {'ip_port': '27.40.141.142:61234', 'user_pass': ''},
    {'ip_port': '124.234.240.207:8118', 'user_pass': ''},
    {'ip_port': '211.143.112.138:8118', 'user_pass': ''},
    {'ip_port': '125.41.109.121:8118', 'user_pass': ''},
    {'ip_port': '118.114.77.47:8080', 'user_pass': ''},
    {'ip_port': '101.68.73.54:53281', 'user_pass': ''},
    {'ip_port': '223.241.118.135:8010', 'user_pass': ''},
    {'ip_port': '61.135.155.82:443', 'user_pass': ''},
    {'ip_port': '115.171.76.254:8888', 'user_pass': ''},
    {'ip_port': '117.92.117.5:36470', 'user_pass': ''},
    {'ip_port': '123.163.164.251:30500', 'user_pass': ''},
    {'ip_port': '124.202.214.26:8118', 'user_pass': ''},
    {'ip_port': '117.22.144.137:8118', 'user_pass': ''},
    {'ip_port': '202.108.31.64:8080', 'user_pass': ''},
    {'ip_port': '183.63.140.82:52225', 'user_pass': ''},
    {'ip_port': '139.201.17.66:808', 'user_pass': ''},
    {'ip_port': '202.110.80.203:80', 'user_pass': ''},
    {'ip_port': '203.74.4.0:80', 'user_pass': ''},
    {'ip_port': '123.196.124.230:10000', 'user_pass': ''},
    {'ip_port': '180.153.58.154:8088', 'user_pass': ''},
    {'ip_port': '117.34.72.251:8082', 'user_pass': ''},
    {'ip_port': '171.12.164.116:47326', 'user_pass': ''},
    {'ip_port': '115.194.124.19:8118', 'user_pass': ''},
    {'ip_port': '114.230.30.225:808', 'user_pass': ''},
    {'ip_port': '122.193.188.236:8118', 'user_pass': ''},
    {'ip_port': '122.140.57.243:8118', 'user_pass': ''},
    {'ip_port': '223.241.119.252:8010', 'user_pass': ''},
    {'ip_port': '1.30.229.5:808', 'user_pass': ''},
    {'ip_port': '171.212.141.50:8118', 'user_pass': ''},
    {'ip_port': '221.10.159.234:1337', 'user_pass': ''},
    {'ip_port': '60.178.174.201:8081', 'user_pass': ''},
    {'ip_port': '27.40.128.82:61234', 'user_pass': ''},
    {'ip_port': '203.74.4.6:80', 'user_pass': ''},
    {'ip_port': '117.146.19.161:3128', 'user_pass': ''},
    {'ip_port': '60.169.19.66:9000', 'user_pass': ''},
    {'ip_port': '113.227.142.164:53281', 'user_pass': ''},
    {'ip_port': '223.241.116.123:8010', 'user_pass': ''},
    {'ip_port': '221.206.5.100:8080', 'user_pass': ''},
    {'ip_port': '85.105.206.237:8080', 'user_pass': ''},
    {'ip_port': '39.91.85.177:8118', 'user_pass': ''},
    {'ip_port': '203.74.4.2:80', 'user_pass': ''},
    {'ip_port': '60.208.44.228:80', 'user_pass': ''},
    {'ip_port': '125.37.175.144:8118', 'user_pass': ''},
    {'ip_port': '111.62.245.189:80', 'user_pass': ''},
    {'ip_port': '58.56.128.84:9001', 'user_pass': ''},
    {'ip_port': '124.89.33.59:52225', 'user_pass': ''},
    {'ip_port': '119.36.92.41:81', 'user_pass': ''},
    {'ip_port': '111.62.251.130:8080', 'user_pass': ''},
    {'ip_port': '123.170.246.35:8118', 'user_pass': ''},
    {'ip_port': '182.101.252.252:4383', 'user_pass': ''},
    {'ip_port': '123.146.235.230:53281', 'user_pass': ''},
    {'ip_port': '119.36.92.42:81', 'user_pass': ''},
    {'ip_port': '114.227.87.125:808', 'user_pass': ''},
    {'ip_port': '111.56.5.41:8080', 'user_pass': ''},
    {'ip_port': '119.36.92.46:81', 'user_pass': ''},
    {'ip_port': '218.4.101.130:83', 'user_pass': ''},
    {'ip_port': '49.84.140.137:8118', 'user_pass': ''},
    {'ip_port': '117.65.45.176:52225', 'user_pass': ''},
    {'ip_port': '120.199.115.184:8118', 'user_pass': ''},
    {'ip_port': '61.187.251.235:80', 'user_pass': ''},
    {'ip_port': '116.30.249.168:8118', 'user_pass': ''},
    {'ip_port': '122.228.179.178:80', 'user_pass': ''},
    {'ip_port': '120.35.203.19:808', 'user_pass': ''},
    {'ip_port': '58.56.149.198:53281', 'user_pass': ''},
    {'ip_port': '111.192.139.197:8888', 'user_pass': ''},
    {'ip_port': '106.39.160.135:8888', 'user_pass': ''},
    {'ip_port': '61.160.208.222:8080', 'user_pass': ''},
    {'ip_port': '60.23.41.194:8118', 'user_pass': ''},
    {'ip_port': '203.74.4.3:80', 'user_pass': ''},
    {'ip_port': '220.181.136.21:1080', 'user_pass': ''},
    {'ip_port': '222.76.118.158:808', 'user_pass': ''},
    {'ip_port': '211.159.171.58:80', 'user_pass': ''},
    {'ip_port': '123.160.174.215:808', 'user_pass': ''},
    {'ip_port': '113.121.244.64:808', 'user_pass': ''},
    {'ip_port': '221.192.134.92:8081', 'user_pass': ''},
    {'ip_port': '220.80.174.36:80', 'user_pass': ''},
    {'ip_port': '117.159.145.215:9999', 'user_pass': ''},
    {'ip_port': '49.4.2.76:80', 'user_pass': ''},
    {'ip_port': '118.123.147.82:63000', 'user_pass': ''},
    {'ip_port': '27.40.138.66:61234', 'user_pass': ''},
    {'ip_port': '101.27.199.154:8118', 'user_pass': ''},
    {'ip_port': '101.132.151.49:8080', 'user_pass': ''},
    {'ip_port': '114.101.131.236:40988', 'user_pass': ''},
    {'ip_port': '59.125.177.31:8080', 'user_pass': ''},
    {'ip_port': '113.121.245.235:808', 'user_pass': ''},
    {'ip_port': '124.133.230.254:80', 'user_pass': ''},
    {'ip_port': '111.56.5.42:8080', 'user_pass': ''},
    {'ip_port': '221.4.133.67:53281', 'user_pass': ''},
    {'ip_port': '27.40.137.180:61234', 'user_pass': ''},
    {'ip_port': '27.40.147.176:61234', 'user_pass': ''},
    {'ip_port': '111.3.108.44:8118', 'user_pass': ''},
    {'ip_port': '42.243.138.32:4336', 'user_pass': ''},
    {'ip_port': '123.114.207.183:8118', 'user_pass': ''},
    {'ip_port': '218.204.74.61:808', 'user_pass': ''},
    {'ip_port': '121.8.164.59:3128', 'user_pass': ''},
    {'ip_port': '101.53.101.172:9999', 'user_pass': ''},
    {'ip_port': '203.74.4.7:80', 'user_pass': ''},
    {'ip_port': '111.202.189.17:80', 'user_pass': ''},
    {'ip_port': '114.45.127.209:8080', 'user_pass': ''},
    {'ip_port': '117.23.56.4:808', 'user_pass': ''},
    {'ip_port': '221.176.180.170:808', 'user_pass': ''},
    {'ip_port': '123.54.236.108:808', 'user_pass': ''},
    {'ip_port': '111.62.243.58:80', 'user_pass': ''},
    {'ip_port': '112.16.9.198:81', 'user_pass': ''},
    {'ip_port': '111.13.7.42:83', 'user_pass': ''},
    {'ip_port': '218.203.56.228:80', 'user_pass': ''},
    {'ip_port': '222.128.13.94:8081', 'user_pass': ''},
    {'ip_port': '203.74.4.5:80', 'user_pass': ''},
    {'ip_port': '27.8.62.212:8888', 'user_pass': ''},
    {'ip_port': '39.69.15.245:53281', 'user_pass': ''},
    {'ip_port': '210.71.198.230:8118', 'user_pass': ''},
    {'ip_port': '61.160.41.65:9090', 'user_pass': ''},
    {'ip_port': '106.42.99.90:808', 'user_pass': ''},
    {'ip_port': '27.219.36.127:8118', 'user_pass': ''},
    {'ip_port': '120.199.64.163:8081', 'user_pass': ''},
    {'ip_port': '220.174.236.211:80', 'user_pass': ''},
    {'ip_port': '218.201.98.196:3128', 'user_pass': ''},
    {'ip_port': '182.88.177.79:8118', 'user_pass': ''},
    {'ip_port': '111.62.251.68:8080', 'user_pass': ''},
    {'ip_port': '114.235.82.126:8118', 'user_pass': ''},
    {'ip_port': '221.7.1.99:8080', 'user_pass': ''},
    {'ip_port': '117.93.23.23:8118', 'user_pass': ''},
    {'ip_port': '27.40.144.97:61234', 'user_pass': ''},
    {'ip_port': '111.62.245.195:80', 'user_pass': ''},
]

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'tutorial.middlewares.RandomUserAgent': 1,
    'tutorial.middlewares.ProxyMiddleware': 100,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'tutorial.pipelines.TutorialPipeline': 300,
    'tutorial.pipelines.DetailPipeline': 200
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
