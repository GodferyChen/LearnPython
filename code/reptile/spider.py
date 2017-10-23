from urllib import request

response = request.urlopen(r'www.baidu.com')
page = response.read()
page = page.decode('utf-8')