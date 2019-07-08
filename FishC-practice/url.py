from html.parser import HTMLParser
# from html.entities import name2codepoint
from urllib import request
import re

class MyHTMLParser(HTMLParser):
    #     def __init__(self):

    # super(MyHTMLParser,self).__init__()
    #     MyHTMLParser.parsedata='' # 设置一个空的标志位
    parsedata = ''

    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            MyHTMLParser.parsedata = 'name'  # 通过属性判断如果该标签是我们要找的标签，设置标志位
        if tag == 'time':
            MyHTMLParser.parsedata = 'time'
        if ('class', 'say-no-more') in attrs:
            MyHTMLParser.parsedata = 'year'
        if ('class', 'event-location') in attrs:
            MyHTMLParser.parsedata = 'location'

    def handle_endtag(self, tag):
        MyHTMLParser.parsedata = ''# 在HTML 标签结束时，把标志位清空

    def handle_data(self, data):
        if MyHTMLParser.parsedata == 'name':
            print('会议名称:%s' % data) # 通过标志位判断，输出打印标签内容

        if MyHTMLParser.parsedata == 'time':
            print('会议时间:%s' % data)

        if MyHTMLParser.parsedata == 'year':
            if re.match(r'\s\d{4}', data): # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
                print('会议年份:%s' % data.strip())

        if MyHTMLParser.parsedata == 'location':
            print('会议地点:%s' % data)
            print('----------------------------------')

parser = MyHTMLParser()

URL = 'https://www.python.org/events/python-events/'

with request.urlopen(URL, timeout=15) as f:  # 打开网页并取到数据
    data = f.read()
parser.feed(data.decode('utf-8'))