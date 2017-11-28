# coding:utf8

from urllib import request


class HtmlDownloader(object):
    @staticmethod
    def download(url):
        if url is None:
            return None

        response = request.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()
