from urllib import request

response = request.urlopen('https://baike.baidu.com/item/Python/407313')
page = response.read()
page = page.decode('utf-8')
print(page)