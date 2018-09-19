# coding=gbk
# 指定编码格式，防止乱码

import requests
import pandas as pd
wf = open(r"/Users/caiyang/Desktop/op_move_bike_.log", "w")
name = ['id', 'city', '银行', '移动', '酒店']
list1 = []

# 百度地图API搜索
def baidu_search(list, region):
    url = 'http://api.map.baidu.com/place/v2/search?'
    output = 'json'
    ak = 'vLyZjPkryKy5Mn2LG1fp6ColMGFfFFiu'
    page_number = '10'
    page_size = '0'
    item = []
    item.append(region)
    for query in list:
        uri = url + 'query=' + query + '&region=' + region + '&output=' + output + '&ak=' + ak + '&page_size=' + page_size + '&page_number=' + page_number
        response = requests.get(uri)  # get提交url,返回响应
        response_dict = response.json()
        # print(response_dict['total'])
        item.append(response_dict['total'])
    print(item)


    #
    # results = response_dict["results"]
    # for adr in results:
    #     name = adr['name']  # 热点名称
    #     location = adr['location']  # 坐标
    #     lng = float(location['lng'])  # 坐标经度
    #     lat = float(location['lat'])  # 坐标纬度
    #     address = adr['address']  # 地址
    #     print('名称：' + name + ' 坐标：%f,%f' % (lat, lng) + ' 地址：' + address)
    #     # print('坐标：%f,%f' % (lat, lng))
    #     # print('地址：' + address)


list = ['银行', '移动', '酒店']
baidu_search(list, '内乡县')
