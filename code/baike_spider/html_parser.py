# coding:utf8
import re
from urllib.parse import urljoin
from urllib.parse import unquote

import math
from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, unquote(soup))
        new_data = self._get_new_data(page_url, unquote(soup))
        return new_urls, new_data

    @staticmethod
    def _get_new_urls(page_url, soup):
        new_urls = []
        # /item/解析器 使用正则表达式去匹配
        links = soup.find_all('a', href=re.compile(r'/item/[^a-zA-Z0-9\u4e00-\u9fa5]'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.append(new_full_url)
        return new_urls

    @staticmethod
    def _get_new_data(page_url, soup):
        res_data = {'url': page_url}

        # url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text().strip()

        return res_data
