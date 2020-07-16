# @Time     :2020.6.17
# @Author   :wanggaojian
# @File     :lesson

#run  执行文件  获取到所有的测试数据
# from lemon.R_W_excel import read_data
# from lemon.HTTP_requests import http_requests
# all_case=read_data('test_case6.xlsx','Sheet1')
# # print("所有的测试数据：",all_case)
#
# #执行数据  先执行第一条
# # print('第一条的测试数据是：',all_case)
#
# login_test_data=all_case[0]
# method=login_test_data[3]
# ip='http://120.78.128.25:8766'
#
# log_response=http_requests(ip+login_test_data[4],eval(login_test_data[5]),token=None,method=login_test_data[3])
# print('最后的结果是：',log_response)
#
# for i in range(1,len(all_case)):
#     test_data=all_case[i]
#     token=log_response['data']['token_info']['token']
#     response=http_requests(ip+test_data[4],eval(test_data[5]),token='Bearer '+token,method=test_data[3])
#     print('充值的结果是：',response)




#全局变量进行充值


# from lemon.R_W_excel import read_data
# from lemon.HTTP_requests import http_requests
# from openpyxl import load_workbook
# Token=None#全局变量，初始值为None
# def run():
#     global Token#在这里声明，函数外的Token和函数内的Token是同一个值
#     all_case=read_data('test_case6.xlsx','Sheet1')
#     print("所有的测试数据：",all_case)
#     for i in range(len(all_case)):
#         test_data=all_case[i]
#         ip = 'http://120.78.128.25:8766'
#         response = http_requests(ip + test_data[4], eval(test_data[5]), token=Token, method=test_data[3])
#         # if test_data[0]==1:
#         # if test_data[1]=='登录':
#         if 'login' in test_data[4]:
#             Token='Bearer '+response['data']['token_info']['token']
#         print("最后的结果是：",response)
#         wb=load_workbook('test_case6.xlsx')
#         sheet=wb['Sheet1']
#         sheet.cell(row=test_data[0]+1,column=8).value=str(response)
#         actual={'code':response['code'],'msg':response['msg']}
#         if eval(test_data[6])==actual:
#             print('测试用例通过')
#             sheet.cell(row=test_data[0]+1,column=9).value='PASS'
#         else:
#             print('测试用例不通过')
#             sheet.cell(row=test_data[0] + 1, column=9).value = 'FAIL'
#         wb.save('test_case6.xlsx')
# run()
#以上内容为写入Excel内容

#以下为优化代码

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




