#coding:utf-8

import os
import random
import requests
from config import *
from w3lib.url import is_url


def gen_proxy(proxy):
    proxy = proxy.strip('\n')
    return {
        'http':f'http://{proxy}',
        'https': f'https://{proxy}',
    }

def get_proxy():
    if PROXY:
        if not is_url(PROXY):
            return gen_proxy(PROXY)
    if is_url(PROXY_POOL):
        # 根据proxy_pool接口修改
        p = requests.get(PROXY_POOL).json().get('proxy')
        return gen_proxy(p)
    if os.path.isfile(PROXY_POOL):
        with open(PROXY_POOL,'r') as f:
            p_txt = f.readlines()
        return random.choice([gen_proxy(i) for i in p_txt])
    if isinstance(PROXY_POOL,list):
        return random.choice([gen_proxy(i) for i in PROXY_POOL])
    if PROXY_HTTP_TUNNEL:
        # 代理服务器
        proxyHost = "http-dyn.abuyun.com"
        proxyPort = "9020"

        # 代理隧道验证信息
        proxyUser = "H1P8Y3G9A4E644TD"
        proxyPass = "96AAAB7ACE8FE201"

        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }

        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }
        return proxies
    return None


def delete_proxy(proxy):
    delres = requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
    return delres



