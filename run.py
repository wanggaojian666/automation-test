# @Time     :2020.6.17
# @Author   :wanggaojian
# @File     :lesson
# -*- coding:utf-8 -*-


from lemon.R_W_excel import read_data
from lemon.HTTP_requests import http_requests
from lemon.R_W_excel import write_data
Token=None#全局变量，初始值为None
def run(file_name,sheet_name,c1,c2):
    global Token#在这里声明，函数外的Token和函数内的Token是同一个值
    all_case=read_data(file_name,sheet_name)
    print("所有的测试数据：",all_case)
    for test_data in all_case:
         # if test_data[0]==1:
         # if test_data[1]=='登录':
        ip = 'http://120.78.128.25:8766'
        response = http_requests(ip + test_data[4], eval(test_data[5]), token=Token, method=test_data[3])
        if 'login' in test_data[4]:
            Token='Bearer '+response['data']['token_info']['token']
        print("最后的结果是：",response)
        write_data(file_name, sheet_name, test_data[0]+1, c1, str(response))
        actual={'code':response['code'],'msg':response['msg']}
        if eval(test_data[6])==actual:
            print('测试用例通过')
            write_data(file_name, sheet_name, test_data[0] + 1, c2, 'PASS')
        else:
            print('测试用例不通过')
            write_data(file_name, sheet_name, test_data[0] + 1, c2, 'FAIL')
run('test_case6.xlsx','Sheet1',8,9)




