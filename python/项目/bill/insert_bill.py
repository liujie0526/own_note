import mysql.connector

def insert_bill_weixin(date,detail,jine):
        conn = mysql.connector.connect(user='root', password='1', host='127.0.0.1', database='Bill')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO bill2019 (`date`, `detail`, `weixin`) VALUES ( %s ,%s ,%s) ;', (date,detail,jine))
        conn.commit()
        cursor.close()
        return

def insert_bill_zhifubao(date,detail,jine):
        conn = mysql.connector.connect(user='root', password='1', host='127.0.0.1', database='Bill')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO bill2019 (`date`, `detail`, `zhifubao`) VALUES ( %s ,%s ,%s) ;', (date,detail,jine))
        conn.commit()
        cursor.close()
        return

def insert_bill_bankcard(date,detail,jine):
        conn = mysql.connector.connect(user='root', password='1', host='127.0.0.1', database='Bill')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO bill2019 (`date`, `detail`, `bankcard`) VALUES ( %s ,%s ,%s) ;', (date,detail,jine))
        conn.commit()
        cursor.close()
        return

def insert_bill_account(date,detail,jine):
        conn = mysql.connector.connect(user='root', password='1', host='127.0.0.1', database='Bill')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO bill2019 (`date`, `detail`, `account`) VALUES ( %s ,%s ,%s) ;', (date,detail,jine))
        conn.commit()
        cursor.close()
        return

def insert_bill_ccbcredit(date,detail,jine):
        conn = mysql.connector.connect(user='root', password='1', host='127.0.0.1', database='Bill')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO bill2019 (`date`, `detail`, `ccbcredit`) VALUES ( %s ,%s ,%s) ;', (date,detail,jine))
        conn.commit()
        cursor.close()
        return

def insert_bill_bcmcredit(date,detail,jine):
        conn = mysql.connector.connect(user='root', password='1', host='127.0.0.1', database='Bill')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO bill2019 (`date`, `detail`, `bcmcredit`) VALUES ( %s ,%s ,%s) ;', (date,detail,jine))
        conn.commit()
        cursor.close()
        return

def insert_bill_cmbcredit(date,detail,jine):
        conn = mysql.connector.connect(user='root', password='1', host='127.0.0.1', database='Bill')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO bill2019 (`date`, `detail`, `cmbcredit`) VALUES ( %s ,%s ,%s) ;', (date,detail,jine))
        conn.commit()
        cursor.close()
        return

def insert_bill_zhongxincredit(date,detail,jine):
        conn = mysql.connector.connect(user='root', password='1', host='127.0.0.1', database='Bill')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO bill2019 (`date`, `detail`, `zhongxincredit`) VALUES ( %s ,%s ,%s) ;', (date,detail,jine))
        conn.commit()
        cursor.close()
        return

def insert_bill_cmbccredit(date,detail,jine):
        conn = mysql.connector.connect(user='root', password='1', host='127.0.0.1', database='Bill')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO bill2019 (`date`, `detail`, `cmbccredit`) VALUES ( %s ,%s ,%s) ;', (date,detail,jine))
        conn.commit()
        cursor.close()
        return

def insert_bill_huabei(date,detail,jine):
        conn = mysql.connector.connect(user='root', password='1', host='127.0.0.1', database='Bill')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO bill2019 (`date`, `detail`, `huabei`) VALUES ( %s ,%s ,%s) ;', (date,detail,jine))
        conn.commit()
        cursor.close()
        return

def insert_bill_baitiao(date,detail,jine):
        conn = mysql.connector.connect(user='root', password='1', host='127.0.0.1', database='Bill')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO bill2019 (`date`, `detail`, `baitiao`) VALUES ( %s ,%s ,%s) ;', (date,detail,jine))
        conn.commit()
        cursor.close()
        return

def insert_bill_jiebei(date,detail,jine):
        conn = mysql.connector.connect(user='root', password='1', host='127.0.0.1', database='Bill')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO bill2019 (`date`, `detail`, `jiebei`) VALUES ( %s ,%s ,%s) ;', (date,detail,jine))
        conn.commit()
        cursor.close()
        return

def insert_bill_jingdongjinrong(date,detail,jine):
        conn = mysql.connector.connect(user='root', password='1', host='127.0.0.1', database='Bill')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO bill2019 (`date`, `detail`, `jingdongjinrong`) VALUES ( %s ,%s ,%s) ;', (date,detail,jine))
        conn.commit()
        cursor.close()
        return

