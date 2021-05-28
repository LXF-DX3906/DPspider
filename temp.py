# from CitySpider import CitySpider
# cityList = ['深圳','天津','杭州']
#
# for city_name in cityList:
#     citySpider = CitySpider(city_name)
#     citySpider.get_area(save=True)
#     citySpider.get_category(save=True)
import requests

from util.http import *
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
HEADERS = {
    'Host': 'www.dianping.com',
    'User-Agent':USER_AGENT
}
session = requests.session()
url = 'https://www.dianping.com/ajax/json/shopDynamic/allReview?shopId=H9D3EhwmzEvErmdw&cityId=1&shopType=10&tcv=d6jo97e47s&_token=eJx1T9FugkAQ%2FJd7LYG7g4qQ%2BGCEtCrWlAPUGh8UrFA4PLmTE5v%2Be8%2FEJu1Dk01mdnZ2svsJmnEGXAQhtJAG2n0DXIB0qPeABgRXkx5Gdt%2ByYA9jrIH0r2ZBpe2axAPuug9tTeU4m5sSKmGNbAdrCGG40X5zE6q6ucbKBHIhGHcNQ0qpZ8W2ZkV90NMjNXh%2BZMaz45l%2BLunVb%2F2GZlJd9e8CUJk0UpkKyztu7yh%2B%2Bpn6T4Xw4lArtp9cIsItfnoPZzxK4q5zpoTgLkhRQGIzuPriJSbtvBv1h6TOV%2Be8sN9YVCcNXZzDXcUY8S7x7DRCE%2BG9mnFRimt6mQfTFpIUzcNssiorh1L6tKwWj6eassNyKv3hQzL%2B2MrBAHx9A1oFc34%3D&uuid=d89a1ec1-b844-9b2c-6caf-233b85d32020.1618127394&platform=1&partner=150&optimusCode=10&originUrl=https%3A%2F%2Fwww.dianping.com%2Fshop%2FH9D3EhwmzEvErmdw'
result = send_http(session=session,method='get',url=url,headers=HEADERS)
print(result)