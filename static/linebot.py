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
    "X-Line-ChannelID": "1462740768",
    "X-Line-ChannelSecret": "fcfc1c1198e63441a5e553031946444d",
    "X-Line-Trusted-User-With-ACL": "ucf06e2c2f2901d71aacf5e196ccd10b3"
}
"""
バス時刻表データ
ここから
"""

#
## 三宮発KSC行き(平日) 46便
sannnomiya_to_ksc1   = [
    0,
    720,
    740,
    755,
    810,
    830,
    850,
    910,
    930,
    950,
    1000,
    1020,
    1040,
    1100,
    1150,
    1210,
    1220,
    1250,
    1320,
    1350,
    1420,
    1450,
    1520,
    1540,
    1600,
    1615,
    1630,
    1700,
    1715,
    1730,
    1745,
    1800,
    1830,
    1845,
    1900,
    1930,
    2000,
    2015,
    2030,
    2045,
    2100,
    2130,
    2200,
    2220,
    2300,
]
ex_sannnomiya_to_ksc1= [
    9,
    0,
    2,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    3,
    0,
    4,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]
"""
バス時刻表データ
ここまで
"""

# 固定で返すメッセージ群
TALKS = [
    "バク、不具合はtwitter（@exodus_ksc_line)に教えてくれたら嬉しいな",
    "「バス」と送ると三宮発のバスの時間がわかるよ",
    "...",
    "(⌒-⌒)ﾆｺﾆｺ...",
    "~~~ヾ(＾∇＾)おはよー♪",
    "(⌒∇⌒)ﾉ""ﾏﾀﾈｰ!!",

]

# 画像群
IMAGES = [
    {"origin": "https://storage.googleapis.com/linebot-1275.appspot.com/monaka1.jpg",
     "thumb": "https://storage.googleapis.com/linebot-1275.appspot.com/monaka1thum.jpg"}
]


@app.route("/")
def hello():
    return "line bot api"


@app.route("/callback", methods=["POST"])
def callback():
    # TODO Signature validation

    app.logger.info(request.json)
    app.logger.info(request.headers)
    req = request.json["result"][0]

    if req["eventType"] == "138311609100106403":
        """
        友だち申請の受信はここに来る。
        申請されたらすぐお礼メッセージを送る。
        TODO 未検証
        """

       #send_text([req["from"]], u"友だち申請ありがと。")

    elif req["eventType"] == "138311609000106303":

        time = (datetime.now().hour * 100) + datetime.now().minute
        to = [req["content"]["from"]]
        if req["content"]["text"] == u"time":
            # 写真送付
            #i = random.randint(0, len(IMAGES) - 1)
            #send_picture(to, IMAGES[i])
            #send_text(to, "よんだー？")

            strs = datetime.now().strftime('時間は%H時%M分です')

            send_text(to,strs)

        elif req["content"]["text"] == u"help":

            send_text(to,u"time:今の時間")


        elif re.match(u'バス',req["content"]["text"]) :
            # time = (datetime.now().hour * 100) + datetime.now().minute
            bus = now_sannomiya_bus(time)
            bustime = bus[0]

            send_text(to,u'次の三宮発KSC行きのバスは\n'+
                str(bustime/100)+u'時'
                +str(bustime%100)+u'分発です')

        elif (req["content"]["text"] == u"dev") :

            fname = set_bus(time)
            url=u"https://mizunomi.sakura.ne.jp/dev/py/"+fname
            img = {
            "origin": url,
            "thumb": url
            }
            send_picture(to, img)
            # send_text(to,u"https://mizunomi.sakura.ne.jp/dev/py/img/test.png")
        elif (req["content"]["text"] == u"dev2") :

            img = {
            "origin": "https://mizunomi.sakura.ne.jp/dev/py/img/test.png",
            "thumb": "https://mizunomi.sakura.ne.jp/dev/py/img/test.png"
            }
            #send_picture(to, img)
            send_text(to,u"https://mizunomi.sakura.ne.jp/dev/py/img/test.png")

        else:
            # メッセージ送信
            i = random.randint(0, len(TALKS) - 1)
            send_text(to, TALKS[i])

    # 戻り値は200固定
    return Response(status=200)

def now_sannomiya_bus(time):
    if time>2300:
        time =1

    low = 0
    high = len(sannnomiya_to_ksc1)# t は中央番目の数
    t = (low + high) / 2
    # 探索の下限のlowが上限のhighになるまで探索
    # lowがhighに達すると数は見つからなかったということ
    while (low<=high):
        if ((time<=sannnomiya_to_ksc1[t])and(time>sannnomiya_to_ksc1[t-1])):
            break
        elif (time > sannnomiya_to_ksc1[t]):
            low = t + 1

        elif (time < sannnomiya_to_ksc1[t]):
            high = t - 1
        t = (low + high) / 2
    return [sannnomiya_to_ksc1[t],ex_sannnomiya_to_ksc1[t]]





def send_text(to, text):
    """
    toに対してテキストを送る
    """
    content = {
        "contentType": 1,
        "toType": 1,
        "text": text
    }
    events(to, content)


def send_picture(to, img):
    """
    toに対して画像を送る
    """
    content = {
        "contentType": 2,
        "toType": 1,
        "originalContentUrl": img["origin"],
        "previewImageUrl": img["thumb"]
    }
    events(to, content)


def events(to, content):
    """
    toに対してデータ(テキスト・画像・動画)を送る
    """
    app.logger.info(content)
    data = {
        "to": to,
        "toChannel": "1383378250",
        "eventType": "138311608800106203",
        "content": content
    }
    r = requests.post(LINE_ENDPOINT + "/v1/events", json=data, headers=HEADERS)
    app.logger.info(r.text)
