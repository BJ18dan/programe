# coding=gbk
# ָ�������ʽ����ֹ����

import requests
import pandas as pd
wf = open(r"/Users/caiyang/Desktop/op_move_bike_.log", "w")
name = ['id', 'city', '����', '�ƶ�', '�Ƶ�']
list1 = []

# �ٶȵ�ͼAPI����
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
        response = requests.get(uri)  # get�ύurl,������Ӧ
        response_dict = response.json()
        # print(response_dict['total'])
        item.append(response_dict['total'])
    print(item)


    #
    # results = response_dict["results"]
    # for adr in results:
    #     name = adr['name']  # �ȵ�����
    #     location = adr['location']  # ����
    #     lng = float(location['lng'])  # ���꾭��
    #     lat = float(location['lat'])  # ����γ��
    #     address = adr['address']  # ��ַ
    #     print('���ƣ�' + name + ' ���꣺%f,%f' % (lat, lng) + ' ��ַ��' + address)
    #     # print('���꣺%f,%f' % (lat, lng))
    #     # print('��ַ��' + address)


list = ['����', '�ƶ�', '�Ƶ�']
baidu_search(list, '������')
