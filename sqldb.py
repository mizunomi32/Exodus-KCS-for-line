# -*- coding: utf-8 -*-

import sqlite3

def open_sql():
    #データベースと接続、無ければ作a成
    con = sqlite3.connect("linebot.db")
    # cursorオブジェクトを作る
    cur = con.cursor()
    #テーブルの作成(存在しなければ）
    sql = "create table if not exists user(uid text,debuger integer,mode integer)"
    con.execute(sql)
    sql = "create table if not exists request(mesid integer,date text,time text,type integer)"
    con.execute(sql)
    sql = "create table if not exists request(mesid integer,uid text,mes text)"
    con.execute(sql)

    return [con, cur]

def useradd(uid,debuger=0):
    con, cur = open_sql()
    if (check_uid(uid,con)):
        # データを登録する
        sql = "insert into user values('%s',%d,0)" % (uid,debuger)
        con.execute(sql)
        con.commit()

        cur.close()
        con.close()
        return True
    else:
        cur.close()
        con.close()
        return False

# uidの重複チェックする
def check_debuger(target):
    con, cur = open_sql()
    sql = 'SELECT debuger FROM user WHERE uid ="' + target + '"'
    cur = con.execute(sql)
    rs =cur.fetchall()
    con.close()
    return rs[0][0]

def check_mode(target):
    con, cur = open_sql()
    sql = 'SELECT mode FROM user WHERE uid ="' + target + '"'
    cur = con.execute(sql)
    rs =cur.fetchall()
    con.close()
    return rs[0][0]

def set_mode1(target):
    if(check_debuger==1):
        con, cur = open_sql()
        sql = 'UPDATE user SET mode=1 WHERE  uid="' + target + '"'
        cur = con.execute(sql)
        rs =cur.fetchall()
        con.close()
        return True
    else:
        return False

def check_uid(target,con):
    sql = 'SELECT uid FROM user WHERE uid ="' + target + '"'
    cur = con.execute(sql)
    if len(cur.fetchall()):
        return False
    else:
        return True

def showuser():
    con, cur = open_sql()
    sql = 'SELECT * FROM user'
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        print "=========="
        print "id -- " + unicode(row[0])
        print "debuger -- " + unicode(row[1])
        print "mode -- " + unicode(row[2])
    cur.close()
    con.close()
