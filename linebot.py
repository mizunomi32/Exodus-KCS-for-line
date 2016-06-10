# -*- coding: utf-8 -*-

## TODO: メッセージの同時受信に対応
## TODO:平日授業日ダイヤ以外を実装
## TODO:人口無能
## TODO:テスターモード実装

import logging, random
import requests
import re
import sqlite3
import sqldb
from datetime import datetime
from flask import Flask, request,Response
from bus import set_bus
from config import HEADERS




app = Flask(__name__)
app.config.from_object(__name__)
app.logger.setLevel(logging.DEBUG)

LINE_ENDPOINT = "https://trialbot-api.line.me"

# 固定で返すメッセージ群
TALKS = [
    "バク、不具合はtwitter（@exodus_ksc_line)に教えてくれたら嬉しいな",
    "「バス」と送ると三宮発のバスの時間がわかるよ",
    "...",
    "(⌒-⌒)ﾆｺﾆｺ...",
    "~~~ヾ(＾∇＾)おはよー♪",
    "(⌒∇⌒)ﾉ""ﾏﾀﾈｰ!!",
    "バージョン0.2.4β(16/6/10更新)"
]
@app.route("/")
def hello():
    ##
    ## ブラウザアクセス時
    ##

     f = open("log.txt","a")

     time = (datetime.now().hour * 100) + datetime.now().minute
     f.writelines(datetime.now().strftime('%Y-%m-%d:%H:%M:%S:web\n'))
     f.close()
     w = datetime.now().weekday()

     if w < 5:
         i=0
     else:
         i=2

     fname = set_bus(time,i)
     url=u"https://mizunomi.sakura.ne.jp/dev/py/"+fname
     msg="line bot api<br><img src=\""+url+"\">"

     return msg

@app.route("/callback", methods=["POST"])
def callback():

    f = open("log.txt","a")
    f.writelines(datetime.now().strftime('%Y-%m-%d:%H:%M:%S:line'))
    f.close()

    # リクエストの取得
    app.logger.info(request.json)
    app.logger.info(request.headers)
    req = request.json["result"][0]
    #if req["eventType"] == "138311609100106403":
    if (req["eventType"] == "138311609000106303"):
        ##
        ## メッセージ受信
        ##


        to = [req["content"]["from"]]
        if req["content"]["text"] == u"time":

            strs = datetime.now().strftime('時間は%H時%M分です')
            send_text(to,strs)

        elif req["content"]["text"] == u"help":

            send_text(to,u"time:今の時間")

        elif re.match(u'バス',req["content"]["text"]) :
            ##
            ## メッセージ中に「バス」が含まれるとき
            ##

            # 曜日取得
            # TODO:祝日判定
            w = datetime.now().weekday()
            # 0:授業日平日
            # 1:授業なし平日
            # 2:土日祝
            # 3:臨時平日
            # 4:臨時土日祝
            if w < 5:
                i=0
            else:
                i=2

            time = (datetime.now().hour * 100) + datetime.now().minute
            send_text(to, u"ロータリー発のバスは")
            # 画像の描写とファイル名の取得
            fname = set_bus(time,i)
            url=u"https://mizunomi.sakura.ne.jp/dev/py/"+fname
            img = {
            "origin": url,
            "thumb": url
            }
            send_picture(to, img)

            # ログファイル書き込み
            f = open("log.txt","a")
            f.writelines(datetime.now().strftime('%Y-%m-%d:%H:%M:%S:bus\n'))
            f.close()
        elif (req["content"]["text"] == u"dev") :

            w = datetime.now().weekday()
            if w < 5:
                i=0
            else:
                i=2

            time = (datetime.now().hour * 100) + datetime.now().minute
            send_text(to, u"ロータリー発のバスは")
            # 画像の描写とファイル名の取得
            fname = set_bus(time,i)
            url=u"https://mizunomi.sakura.ne.jp/dev/py/"+fname

            img = {
            "origin": url,
            "thumb": url
            }
            send_picture(to, img)
        elif (req["content"]["text"] == u"login") :
            sqldb.useradd(to[0],1)

            send_text(to,to[0])
        elif (req["content"]["text"] == u"dmode") :
            try:
                if (sqldb.check_debuger(to[0])==1):
                    sqldb.set_mode1(to[0])
                    send_text(to,u"dmode")
                else:
                    send_text(to, u"you are not debuger")
            except Exception as e:
                send_text(to, u"エラー")
        else:
            # ランダムメッセージ送信
            i = random.randint(0, len(TALKS) - 1)
            send_text(to, TALKS[i])

    return Response(status=200)

def send_text(to, text):
    ##
    ## テキスト送信情報生成
    ##

    content = {
        "contentType": 1,
        "toType": 1,
        "text": text
    }
    events(to, content)

def send_picture(to, img):
    ##
    ## 画像送信情報生成
    ##

    content = {
        "contentType": 2,
        "toType": 1,
        "originalContentUrl": img["origin"],
        "previewImageUrl": img["thumb"]
    }
    events(to, content)

def events(to, content):
    ##
    ## イベントリクエスト
    ##

    app.logger.info(content)
    data = {
        "to": to,
        "toChannel": "1383378250",
        "eventType": "138311608800106203",
        "content": content
    }
    # json データを生成して送信
    r = requests.post(LINE_ENDPOINT + "/v1/events", json=data, headers=HEADERS)
    app.logger.info(r.text)
