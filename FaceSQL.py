import pymysql

class FaceSQL:
    def __init__(self):
        self.conn = pymysql.connect(
            # 数据库的IP地址
            host="127.0.0.1",
            # 数据库用户名称
            user="root",
            # 数据库用户密码
            password="",
            # 数据库名称
            db="stzg",
            # 数据库端口名称
            port=3306,
            # 数据库的编码方式 注意是utf8
            charset="utf8"
        )

    def processFaceData(self, sqlstr, args=()):
        print(sqlstr)
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.conn.cursor()
        try:
            # 执行sql语句
            cursor.execute(sqlstr, args)
            # 提交到数据库执行
            self.conn.commit()
        except Exception as e:
            # 如果发生错误则回滚并打印错误信息
            self.conn.rollback()
            print(e)
        finally:
            # 关闭游标
            cursor.close()

    def saveFaceData(self,id,encoding_str):
        self.processFaceData("insert into face(学号,encoding) values(%s,%s)", (id, encoding_str))

    def updateFaceData(self, id, encoding_str):
        self.processFaceData("update face set encoding = %s where 学号 = %s", (encoding_str, id))

    def execute_float_sqlstr(self, sqlstr):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.conn.cursor()
        # SQL插入语句

        results = []
        try:
            # 执行sql语句
            cursor.execute(sqlstr)
            # 获取所有记录列表
            results = cursor.fetchall()
        except Exception as e:
            # 如果发生错误则回滚并打印错误信息
            self.conn.rollback()
            print(e)
        finally:
            # 关闭游标
            cursor.close()
        return results

    def sreachFaceData(self, id):
        return self.execute_float_sqlstr( "select * from face where 学号="+id)

    def allFaceData(self):
        return self.execute_float_sqlstr( "select * from face ")

    def sreach_Info(self,id):
        return self.execute_float_sqlstr( "select * from zstustu where 学号='" + id + "'")