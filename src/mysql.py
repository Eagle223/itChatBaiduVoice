#coding:utf-8
import pymysql

#数据库配置信息 Dict
config={'host':'localhost',
        'port':3306,
        'user':'root',
        'password':'Eagle520',
        'db':'HomeCommand'
}


def insert_mysql(Command):
    mysql_db = pymysql.connect(**config)
    cursor = mysql_db.cursor()
    sql='update Command set com='+str(Command)+' where ID=1'
    print(sql)
    try:
        cursor.execute(sql)
        #提交修改
        mysql_db.commit()
        print 'update ok'
        return '状态更新成功'
    except Exception as e:
#        raise e
        error = '插入发生错误'
        print error
        return error
    finally:
        mysql_db.close()
        #关闭连接  