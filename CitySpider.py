#  1.最小单位为城市的区，最大单位为城市，区为可选项，城市未必选项，当没有设定区时，默认爬取整个城市中的所有店铺
#  2.首先获取该城市的所有区以及有效店铺分类
#  3.对每个区每个分类进行爬取，每条数据的key为"city+area+category"，value为店铺列表
#  4.遍历所有店铺列表，爬取每个店铺下的评论
#  5.前三步不会出太大问题，第四步可能会出现中断，记录下中断时店铺的ID，重新开始爬取时，从头开始遍历到该店铺的ID，从该ID开始爬起
#  6.在爬取评论之前，可以先爬取城市的所有店铺，做一个持久化处理，在开始爬取评论时可以选择更不更新店铺数据，如果更新，就是爬取最新的评论数据，如果不更新也可以爬，但是可能信息比较旧
from city import City
from log import getLogger
from dbhelper import Database
from util.CitySpider import *

logger = getLogger(__name__)


class CitySpider(object):
    """
    爬取某城市中店铺评论
    """

    def __init__(self, cityName, area=None):
        self.cityName = cityName
        self.area = area
        self.city = City(cityName, searchDB=Database(MongoDB))
        self.city.get()
        self.category_list = []
        self.coa_category = []
        self.fin_category = []
        self.process_category(self.city.category, self.category_list)
        self.coarsness_category(self.category_list)
        self.fine_grained_category(self.category_list)

    def get_area(self, save=False):
        """
        获取该城市所有的区
        :param save: 是否将城市所有区保存到数据库
        """
        area_list = []
        for item in self.city.locations:
            try:
                if(item['text'] == '全部地区'):
                    continue
                area_list.append(item['text'])
            except:
                logger.debug(f'获取城市分区失败:[城市:{self.cityName}]')
        logger.info(f'获取 “{self.cityName}” 所有区成功.')
        if save:
            areaDB = init_area_db(Database(MongoDB))
            areaDB.save({self.cityName: area_list}, tname='Area')
            logger.info(f'已将 “{self.cityName}” 所有区信息保存到数据库中.')
        return area_list

    def process_category(self, obj, category_list):
        """
        处理分类数据
        :return: category_list
        """
        for item in obj:
            if 'children' in item.keys():
                category_list.append({item['text']: []})
                self.process_category(item['children'], category_list[len(category_list)-1][item['text']])
            else:
                category_list.append(item['text'])
        return category_list

    def coarsness_category(self, category_list):
        for item in category_list:
            if isinstance(item, str):
                self.coa_category.append(item)
            elif isinstance(item, dict):
                self.coa_category.append(list(item.keys())[0])

    def fine_grained_category(self, category_list):
        for item in category_list:
            if isinstance(item, str):
               self.fin_category.append(item)
            elif isinstance(item, dict):
                self.fine_grained_category(item[list(item.keys())[0]])

    def get_category(self, save=False):
        """
        获取该城市所有的店铺分类结果
        :param save: 是否将城市所有店铺分类保存到数据库
        """
        logger.info(f'获取 “{self.cityName}” 所有店铺分类成功.')
        if save:
            categoryDB = init_category_db(Database(MongoDB))
            categoryDB.save({self.cityName: self.category_list}, tname='Category')
            logger.info(f'已将 “{self.cityName}” 所有店铺分类信息保存到数据库中.')
        return self.city.category

    def save_shop_info(self):
        """
        获取该城市所有的店铺的信息，并保存在数据库中
        """
        self.process_category(self.city.category, self.category_list)
        for area in self.get_area():
            for category in self.fin_category:
                if category == '全部分类':
                    continue
                # self.city.search('', category=category, location=area, filter=None, sort='按人气排序', save=True, details=False, comments=False)
                self.city.async_search('', category=category, location=area, filter=None, sort='按人气排序', save=True, details=False, comments=False)