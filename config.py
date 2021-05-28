import time 

#是否使用代理
PROXY_ENABLE = False

#使用单个的代理ip，优先级最高
#此项若有填写，则使用此代理，后面的不会考虑
# 格式可以为下面几种:
# 1.  "1.1.1.1:1111"
# 2.  "username:password@1.1.1.1:1111"
# 3.  "www.dailiurl.com/path/xxxx"
# 4.  "username:password@www.dailiurl.com/path/xxxx"
PROXY = ''
PROXY_HTTP_TUNNEL = False

#IP代理池，优先级低于PROXY高于PROXY_POOL_RAW
# * 建议使用购买的代理池API，一次请求一个代理，每次请求不重复，请求间隔为INTERVAL
# * 或者是一个代理IP文件，文件的一行便是一个代理如:<ip>:<port>
# * 或者是一个代理池IP列表，如:[<ip>:<port>,..]
# 格式可以为下面几种:
# 1、 "http:http://39.108.59.38:8888/Tools/proxyIP.ashx?OrderNumber=xxxx&poolIndex=xxx&cache=1&qty=1"
# 2、 ['1.1.1.1:1111','1.1.1.1:1112','1.1.1.1:1113',...]
# 3、 "D://proxyfile.txt"
PROXY_POOL = 'http://127.0.0.1:5010/get'
# PROXY_POOL = ''

#未经过验证有效性的代理池文件,如:'txt/rawproxy.txt'，如果PROXY_POOL是一个文件
#那么程序会进行自动检测代理的有效性后将可用代理写入PROXY_POOL
#后进行使用，优先级最低,测试代理url为PROXY_TEST_URL
PROXY_POOL_RAW = 'txt/rawproxy.txt'
#当PROXY_POOL_RAW不为空时，检测代理可用性使用此url
PROXY_TEST_URL = 'http://www.dianping.com/'
#测试代理池可用性的最大线程数
PROXY_TEST_MAX = 200

# 城市的店铺种类分类文件，存储在本地，再次获取某个城市的店铺分类时
# 如果存在此文件，读取此文件，文件中存有此城市的店铺分类数据时，不再
# 重新请求获取，没有的话请求获取后更新进此文件.删除此文件会重新更新存储.
CATEGORY_FILE_PATH = 'JSON/category.json'

# 城市的激活地区文件，存储在本地，再次获取某个城市的某些地区时
# 如果存在此文件，读取此文件，文件中存有此城市的地区数据时，不再
# 重新请求获取，没有的话请求获取后更新进此文件.删除此文件会重新更新存储.
LOCATIONS_FILE_PATH = 'JSON/locations.json'

# 城市搜索结果进行排序的选项字典文件，存储在本地，再次获取某个城市的某个关键词
# 的搜索结果进行排序时，如果存在此文件，读取此文件，可以根据文件内容进行选择
# 排序搜索结果。没有的话请求获取后更新进此文件.删除此文件会重新更新存储.
SORTS_FILE_PATH = 'JSON/sorts.json'

# 全国城市地区链接文件，存储在本地，访问某个城市时，会查询文件中是否有
# 这个城市。如果没有此文件，会进行请求获取下载。删除此文件会重新更新存储.
CITY_LIST_FILE_PATH = 'JSON/cityList.json'

# 全国所有激活注册大众点评的地区城市详细的信息json文件，
# 本地存储.删除此文件会重新更新存储.
CITY_DETAIL_FILE_PATH = 'JSON/active_cities.json'

# 全国各个省份的ID及地区ID文件，本地存储.删除此文件会重新更新存储.
PROVINCE_FILE_PATH = 'JSON/province.json'

#MongoDB数据库设置
MongoDB = {
    'host'          :'127.0.0.1',
    'port'          :27017,
    'database'      :'DPdb',
    'records'       :'Records',
    'searchDB'      :'DPSearchdb',
    'commentsDB'    :'commentsDB',
    'areaDB'        :'areaDB',
    'categoryDB'    :'categoryDB',
    'user'          :'',
    'password'      :'',
}

#允许网络请求的HTTP方法
HTTP_METHODS = ['get','head','post','put','options']

# 大众点评 加密标签 数字与字符的不定期改变的名称
TAG_CHANGED = {
	'number':'d',
	'string':'e',
}

COMMENT_TAGS = {
    'number':'svgmtsi',
    'string':'svgmtsi',
}

NUM_SVG_PATH = f'svg/num{time.strftime("%Y-%m-%d",time.localtime(time.time()))}.svg'
STR_SVG_PATH = f'svg/str{time.strftime("%Y-%m-%d",time.localtime(time.time()))}.svg'
COMMENT_SVG_PATH =f'svg/comment{time.strftime("%Y-%m-%d",time.localtime(time.time()))}.svg'

#记录搜索爬取痕迹，下次搜索爬取便不会重复下载存储
RECORD_ENABLE = True

#请求失败后的重试次数：
# -1表示无限次请求；
# 0表示不重试；
# >0的表示重试次数
MAX_RETRY = -1

#店铺间的抓取时间间隔:秒
SLEEP = 1

#每一次请求或者重试失败后的等待延时时间：秒，
#也是使用代理时失败再次使用代理API提取代理的间隔
INTERVAL = 0

#随机请求等待时间间隔，秒
#数组表示(a,b)返回a到b范围内的随机秒数
#开始随机等待将RANDOM_SLEEP置True
RANDOM_SLEEP = True
RANDOM_INTERVAL = (1,3)

#请求超时时间设置：秒
TIMEOUT = 10

#哪些请求状态码视为被禁
FORBIDDEN_CODE = [403,]

#被禁多少次之后进行User-Agent的更换
FORBIDDEN_MAX_TO_CHANGE = 3

#404状态返回多少次后放弃该请求
NOT_FOUND_MAX_TO_DROP = 6

#请求失败多少次之后放弃当前请求
FAIL_MAX_TO_DROP = 200

#搜索相关结果返回的条数，
# -1表示全部返回
# >0返回最多该条数
SEARCH_RESULTS = -1

#店铺点评下载返回的条数，
# -1表示全部返回
# >0返回最多该条数
COMMENTS_RESULTS = -1

#商铺点评 获取的默认条数
# -1 表示获取全部
# >0获取最多该条数
COMMENTS_COUNT_DEFAULT = -1

#点评页获取时间间隔，秒
#(a,b)为a到b的随机秒数
COMMENTS_SLEEP = (50,60)

#日志设置
#启用日志
LOG_ENABLE = True
#日志级别
LOG_LEVEL = 'INFO'
#日志文件编码
LOG_FILE_ENCODING = 'UTF-8'
#日志文件路径
LOG_FILE_SAVE_PATH = r'txt/log.txt'
#日志时间格式
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
#日志级别对应格式
LOG_FORMAT = {
    'DEBUG'     : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'INFO'      : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'WARNING'   : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'ERROR'     : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'CRITICAL'  : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
}

#获取所有点评必须使用大众点评注册用户的登陆cookie
COOKIE = '__mta=248291256.1621005254909.1621005254909.1621005254909.1; _lxsdk_cuid=178bfe8940cc8-0bd0ef51260b1c-336b7c08-1ea000-178bfe8940cc8; _hc.v=d89a1ec1-b844-9b2c-6caf-233b85d32020.1618127394; ctu=6e10f35fb298c44e14d504f5dcffdfefaed2ffb9502c21661dc68e214237b515; s_ViewType=10; _dp.ac.v=4ed4c8fc-5559-4c43-81b1-6d6af0b68ba0; fspop=test; uuid=B6CC1CD25A17BC07CFD7F786CDE52D96AB46DD7114D99341C4AFF282FF83511D; iuuid=B6CC1CD25A17BC07CFD7F786CDE52D96AB46DD7114D99341C4AFF282FF83511D; _lxsdk=B6CC1CD25A17BC07CFD7F786CDE52D96AB46DD7114D99341C4AFF282FF83511D; _ga=GA1.2.1278990306.1621841235; cy=1; cye=shanghai; dplet=47c9d2ac9f7a3afb46d95ecd73c95fd2; dper=105274e19f11bef99cec936ba91d4b29c88892a727572a986b63d0e6cde556533313b713e2e7faafd9b368f5e8c731afd29b7611a62860ebecfcc91fdd5c8de9f043328e11509ccc9bb682957aa8170e6f74adce4fecd3798ab616c0bde465a5; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_1733493889; _lx_utm=utm_source=Baidu&utm_medium=organic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1621841606,1622026763,1622028872,1622178793; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1622178803; _lxsdk_s=179b164022d-fe-824-743||26'