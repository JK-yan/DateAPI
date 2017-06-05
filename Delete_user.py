import pymysql


# 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
conn=pymysql.connect(host='192.168.1.45',user='usercore_test',passwd='LtkG8BZJ',db='usercore_test',port=3306,charset='utf8')
cur=conn.cursor()#获取一个游标
user_id=None
try:
    cur.execute("SELECT * FROM usr_login WHERE login_id = '17717518326'")
    usr_login = cur.fetchall()
    user_id = usr_login[0][1]
except :
    print("查询账户不存在")
    # cur.execute("DELETE  FROM usr_login WHERE login_id = '%s'"%user_id)
    # cur.execute("DELETE  FROM usr_login_4uid WHERE user_id = '%s'"%user_id)
    # cur.execute("DELETE  FROM usr_user WHERE user_id = '%s'"%user_id)
    # cur.execute("DELETE  FROM usr_wechat_user WHERE user_id = '%s'"%user_id)


print(user_id)
# if user_id is not None:
#     try:
#         cur.execute("DELETE  FROM usr_login WHERE user_id = '%s'"%user_id)
#         cur.execute("DELETE  FROM usr_login_4uid WHERE user_id = '%s'" % user_id)
#         cur.execute("DELETE  FROM usr_user WHERE user_id = '%s'" % user_id)
#         cur.execute("DELETE  FROM usr_wechat_user WHERE user_id = '%s'" % user_id)
#         conn.commit()
#         print("删除用户数据")
#     except  Exception:
#         conn.rollback()
#         print("删除数据失败")
try:
    cur.execute("SELECT * FROM usr_login WHERE login_id = '17717518326'")
    usr_login=cur.fetchall()
    cur.execute("SELECT * FROM usr_login_4uid WHERE user_id = '%s'"%user_id)
    usr_login_4uid=cur.fetchall()
    cur.execute("SELECT * FROM usr_user WHERE user_id = '%s'"%user_id)
    usr_user=cur.fetchall()
    cur.execute("SELECT * FROM usr_wechat_user WHERE user_id = '%s'"%user_id)
    usr_wechat_user=cur.fetchall()
    print(usr_login[0][0])
    print(usr_login_4uid[0])
    print(usr_user[0])
    print(usr_wechat_user[0])
    # for d in data :
    #     #注意int类型需要使用str函数转义
    #     print(d+)
except Exception as e:
    print("Error: unable to fecth data")
cur.close()#关闭游标
conn.close()#释放数据库资源
