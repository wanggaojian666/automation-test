# @Time     :2020.6.17
# @Author   :wanggaojian
# @File     :lesson
# -*- coding:utf-8 -*-


import requests

def http_requests(url,data,token=None,method='post'):
    header = {'X-Lemonban-Media-Type': 'lemonban.v2',
                'Authorization': token}
    if method=='get':
        res=requests.get(url,json=data,headers=header)
    else:
        res=requests.post(url, json=data, headers=header)
    return res.json()

if __name__ == '__main__':

    url_1='http://120.78.128.25:8766/futureloan/member/register'
    data_1={'mobile_phone': "15816541769","pwd": 'lemon123456'}
    header_1={'X-Lemonban-Media-Type':'lemonban.v2'}

    url_2='http://120.78.128.25:8766/futureloan/member/login'
    data_2= {'mobile_phone': '15816541769','pwd': 'lemon123456'}
    header_2={'X-Lemonban-Media-Type':'lemonban.v2'}

    # http_requests(url_1,data_1,header_1)
    # http_requests(url_2,data_2,header_2)
    response=http_requests(url_2,data_2)
    token=response['data']['token_info']['token']
    url_3='http://120.78.128.25:8766/futureloan/member/recharge'
    data_3={"member_id": "148","amount": 100}
    header_3={'X-Lemonban-Media-Type':'lemonban.v2',
              'Authorization':'Bearer '+token}

    url_4='http://120.78.128.25:8766/futureloan/member/withdraw'
    data_4={"member_id": "148","amount": "100"}
    header_4={'X-Lemonban-Media-Type':'lemonban.v2',
              'Authorization':'Bearer '+token}

    print(http_requests(url_3,data_3,'Bearer '+token))
    # http_requests(url_4,data_4,header_4)

