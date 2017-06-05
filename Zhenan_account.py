import random

import pymysql
# 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
conn=pymysql.connect(host='192.168.1.45',user='accountcore_test',passwd='DUyBMqWe',db='accountcore_test',port=3306,charset='utf8')
cur=conn.cursor()#获取一个游标9621079212437634307


def input_SQL():
    a = random.randint(150000000000000000000, 999999999999999999999)
    trade_nos = '%s' % a
    out_trade_nos = '1000018%s' % trade_nos
    user_ids = '39024679217909760'
    amounts = '100'
    statuss = "FINISH"
    products = "ZHENAN_BAG_AMOUNT"
    account_types = "ZHENAN_BAG_AMOUNT"
    gmt_creates = "2017-05-26 16:52:46"
    gmt_modifieds = "2017-05-26 16:52:49"

    sql = "INSERT INTO acc_user_account_withdrawal_order (trade_no,out_trade_no,user_id,amount,status,product,account_type,gmt_create,gmt_modified)VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    print(sql % (
        trade_nos, out_trade_nos, user_ids, amounts, statuss, products, account_types, gmt_creates, gmt_modifieds))
    cur.execute(sql % (
        trade_nos, out_trade_nos, user_ids, amounts, statuss, products, account_types, gmt_creates, gmt_modifieds))
    conn.commit()

count = int(input())

while(0<count):
    try:
        input_SQL()
    except Exception as e:
        conn.rollback()
        continue
    count-=1
cur.close()#关闭游标
conn.close()#释放数据库资源


