# coding:utf8
from urllib.parse import unquote
from pymongo import MongoClient

class HtmlOutputer(object):
    def __init__(self):
        # self.data_all = []
        # 连接数据库
        conn = MongoClient('localhost', 27017)
        self.db = conn.baikedb

    def collect_data(self, data):
        if data is None:
            return
        # self.data_all.append(data)
        # 插入数据
        self.db.col.insert_one(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        # ascii
        for data in self.db.col.find():
            fout.write('<tr>')
            fout.write('<td>%s</td>' % unquote(data['url']))
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
