from gevent.libev.corecext import os
from scrapy import cmdline
import time
import csv
path = "C:\\Users\\Yuriko\\Desktop\\origin.csv"
if os.path.exists(path):
    print("exists file")
else:
    print("not exists file")
    file = open(path, 'a', newline='')
    first_line = ["区", "区域", "小区", "成交价格", "单价", "成交周期", "交易时间", "房屋户型", "建筑面积", "屋内面积",
                  "朝向", "装修", "楼层", "户型结构", "建成年代", "梯户比例", "供暖方式"]
    writer = csv.writer(file)
    writer.writerow(first_line)
    file.close()
cmdline.execute("scrapy crawl lianjia".split())

