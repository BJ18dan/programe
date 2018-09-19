# -*- coding: utf-8 -*-
"""
Created on Wed May 02 17:19:32 2018


@author: Administrator
"""
from bs4 import BeautifulSoup
from collections import Counter
from time import sleep
import pymysql
import requests
import time
import math
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def get_support_info(item, xiaoqu_id, support_class, support_type):
    xiaoqu_id = xiaoqu_id
    support_class = support_class
    support_type = support_type
    support_name = item.find('name').text
    support_lat = item.find('lat').text
    support_lng = item.find('lng').text
    address = item.find('address').text
    uid = item.find('uid').text
    distance = item.find('distance').text
    try:
        tag = item.find('tag').text
    except (ZeroDivisionError, Exception) as e:
        tag = u'暂无数据'
        print(e)
        pass

    try:
        tel = item.find('telephone').text
    except (ZeroDivisionError, Exception) as e:
        tel = u'暂无数据'
        print(e)
        pass
        # 创建时间
    created_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    return (xiaoqu_id, support_class, support_type, support_name, support_lat, support_lng, address,
            uid, distance, tag, tel, created_date)


def to_sql(data):
    conn = pymysql.connect("localhost", "root", "tiger", "test", charset="utf8")
    cursor = conn.cursor()
    sql_create_database = 'create database if not exists test'
    cursor.execute(sql_create_database)
    #    try :
    #        cursor.select_db('test')
    #    except (ZeroDivisionError,Exception) as e:
    #        print e
    # cursor.execute("set names gb2312")
    cursor.execute(
        '''create table if not exists test.xiaoqu_support(xiaoqu_id bigint(80),
                                                              support_class varchar(50),
                                                              support_type varchar(50),
                                                              support_name varchar(50),
                                                              support_lat varchar(20),
                                                              support_lng varchar(20),
                                                              address varchar(200),
                                                              uid varchar(50),
                                                              distance bigint,
                                                              tag varchar(30),
                                                              tel varchar(30),
                                                              created_date DATETIME,
                                                              primary key (xiaoqu_id,uid));'''
    )
    cursor.executemany('insert ignore into test.xiaoqu_support values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);', data)

    conn.commit()
    cursor.close()
    conn.close()



conn = pymysql.connect("localhost", "root", "tiger", "test", charset="utf8")
cursor = conn.cursor()
sql = 'select * from xiaoqu'
cursor.execute(sql)
# 获取查询结果
data = cursor.fetchall()

infos = []
for i in range(len(data)):
    xiaoqu_id = data[i][0]
    # 一级分类
    support_class = u'旅游景点'
    # 其他配套自己根据需求获取，如'交通','教育','医疗','银行','购物','影剧院','旅游景点'等
    # 二级分类
    support_type = ['旅游景点,公园', '旅游景点,植物园', '旅游景点,动物园', '旅游景点,博物馆']
    ak = ['***', '***']  # 自己的ak，最好多申请几个
    for j in range(len(support_type)):
        url = 'http://api.map.baidu.com/place/v2/search?query=' + support_class + '&tag=' + support_type[
            j] + '&location=' + data[i][4] + ',' + data[i][5] + '&radius=3000&output=xml&ak=' + ak[
                  0] + '&scope=2&page_size=20'
        soup = BeautifulSoup(requests.get(url).text, "lxml")
        if soup.find('status').text == 200:
            url = 'http://api.map.baidu.com/place/v2/search?query=' + support_class + '&tag=' + support_type[
                j] + '&location=' + data[i][4] + ',' + data[i][5] + '&radius=3000&output=xml&ak=' + ak[
                      1] + '&scope=2&page_size=20'
            soup = BeautifulSoup(requests.get(url).text, "lxml")

        totals = soup.find('total').text
        if totals == 0:
            continue
        page_nums = range(int(math.ceil(float(totals) / 20)))
        for page_num in page_nums:
            url = url + '&page_num=' + str(page_num)
            soup = BeautifulSoup(requests.get(url).text, "lxml")
            items = soup.find_all('result')
            for item in items:
                try:
                    print
                    "Getting information of the", i, j, "-th infos."
                    infos.append(get_support_info(item, xiaoqu_id, support_class, support_type[j]))
                    # sleep(0.5)
                except Exception as e:
                    print(e)
print(to_sql(infos))
