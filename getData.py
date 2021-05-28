from CitySpider import CitySpider
from log import getLogger

logger = getLogger(__name__)

# cityList = ['上海','北京','天津','广州','杭州','深圳']
# for cityName in cityList:
#     citySpider = CitySpider(cityName)
#     citySpider.get_area(save=True)
#     citySpider.get_category(save=True)
# citySpider.save_shop_info()
while True:
    try:
        cityList = ['大连','滁州']
        for cityName in cityList:
            citySpider = CitySpider(cityName)
            # citySpider.get_area(save=True)
            # citySpider.get_category(save=True)
            if citySpider.save_shop_info():
                continue
        break
    except:
        print('重新执行程序')
        logger.debug(f'重新执行程序')
