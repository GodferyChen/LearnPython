# coding:utf8
from urllib.parse import unquote

class HtmlOutputer(object):
    def __init__(self):
        self.data_all = []

    def collect_data(self, data):
        if data is None:
            return
        self.data_all.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        # ascii
        for data in self.data_all:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % unquote(data['url']))
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
