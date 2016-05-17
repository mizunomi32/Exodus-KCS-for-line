# -*- coding: utf-8 -*-
import logging, random
import requests
import re

from datetime import datetime

from flask import Flask, request,Response

from bus import set_bus

app = Flask(__name__)
app.config.from_object(__name__)
app.logger.setLevel(logging.DEBUG)

LINE_ENDPOINT = "https://trialbot-api.line.me"
HEADERS = {
    "X-Line-ChannelID": "xxxxxxxxxx",
    "X-Line-ChannelSecret": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "X-Line-Trusted-User-With-ACL": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}

# 固定で返すメッセージ群
TALKS = [
    "バク、不具合はtwitter（@exodus_ksc_line)に教えてくれたら嬉しいな",
    "「バス」と送ると三宮発のバスの時間がわかるよ",
    "...",
    "(⌒-⌒)ﾆｺﾆｺ...",
    "~~~ヾ(＾∇＾)おはよー♪",
    "(⌒∇⌒)ﾉ""ﾏﾀﾈｰ!!",
    "バージョン0.2.2β(16/5/5更新)"

]

@app.route("/")
def hello():
     time = (datetime.now().hour * 100) + datetime.now().minute
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


     fname = set_bus(time,i)
     url=u"https://mizunomi.sakura.ne.jp/dev/py/"+fname
    #
     msg="line bot api<br><img src=\""+url+"\">"
     return msg


@app.route("/callback", methods=["POST"])
def callback():
    # TODO Signature validation

    app.logger.info(request.json)
    app.logger.info(request.headers)
    req = request.json["result"][0]

    if req["eventType"] == "138311609100106403":

        # 友だち申請
        #TODO 未検証



    elif req["eventType"] == "138311609000106303":

        time = (datetime.now().hour * 100) + datetime.now().minute
        to = [req["content"]["from"]]
        if req["content"]["text"] == u"time":


            strs = datetime.now().strftime('時間は%H時%M分です')

            send_text(to,strs)

        elif req["content"]["text"] == u"help":

            send_text(to,u"time:今の時間")


        elif re.match(u'バス',req["content"]["text"]) :
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


            send_text(to, u"ロータリー発のバスは")

            fname = set_bus(time,i)
            url=u"https://mizunomi.sakura.ne.jp/dev/py/"+fname
            img = {
            "origin": url,
            "thumb": url
            }
            send_picture(to, img)
        elif (req["content"]["text"] == u"dev") :

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


            send_text(to, u"ロータリー発のバスは")

            fname = set_bus(time,i)
            url=u"https://mizunomi.sakura.ne.jp/dev/py/"+fname
            img = {
            "origin": url,
            "thumb": url
            }
            send_picture(to, img)
            # send_text(to,u"https://mizunomi.sakura.ne.jp/dev/py/img/test.png")
        elif (req["content"]["text"] == u"out") :
            send_text(to, u"aa")

            w = datetime.now().weekday()
            send_text(to, str(w))
        else:
            # メッセージ送信
            i = random.randint(0, len(TALKS) - 1)
            send_text(to, TALKS[i])


    # 戻り値は200固定
    return Response(status=200)

def send_text(to, text):
    # テキスト送信
    content = {
        "contentType": 1,
        "toType": 1,
        "text": text
    }
    events(to, content)

def send_picture(to, img):
    # 画像送信
    content = {
        "contentType": 2,
        "toType": 1,
        "originalContentUrl": img["origin"],
        "previewImageUrl": img["thumb"]
    }
    events(to, content)
