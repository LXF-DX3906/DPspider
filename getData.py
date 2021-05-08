from CitySpider import CitySpider
from log import getLogger

logger = getLogger(__name__)

# citySpider = CitySpider('上海')
# # citySpider.get_area(save=True)
# # citySpider.get_category(save=True)
# citySpider.save_shop_info()
while True:
    try:
        citySpider = CitySpider('上海')
        # citySpider.get_area(save=True)
        # citySpider.get_category(save=True)
        citySpider.save_shop_info()
    except:
        print('重新执行程序')
        logger.debug(f'重新执行程序')
