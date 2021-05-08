from config import  MongoDB
from log import getLogger

logger = getLogger(__name__)


def init_area_db(db):
    if db and not db.connected:
        db.connect()
        db.use_db(MongoDB['areaDB'])
        logger.info(f'连接到数据库:areaDB')
    return db


def init_category_db(db):
    if db and not db.connected:
        db.connect()
        db.use_db(MongoDB['categoryDB'])
        logger.info(f'连接到数据库:categoryDB')
    return db