# coding: utf-8

##
##  画像描写処理関係
##

from PIL import Image, ImageDraw, ImageFont


def rotari(data,time=9999):
    ##
    ##  大学ロータリー発の画像生成＋ファイル名返す
    ##
    # data      :   バスの時間（１０要素のリスト）
    # times     :   現在時刻(ファイル名用)
    #
    # return    :   ファイル名

    # データ分解
    txt1f = data[0][1]
    txt1l = data[1][1]
    txt2f = data[2][1]
    txt2l = data[3][1]
    txt3f = data[4][1]
    txt3l = data[5][1]
    txt4f = data[6][1]
    txt4l = data[7][1]
    txt5f = data[8][1]
    txt5l = data[9][1]

    bus1f = str(data[0][0]/100).zfill(2)+u":"+str(data[0][0]%100).zfill(2)
    if data[0][0] == 9999:
        bus1f = u"--:--"
    bus1l = str(data[1][0]/100).zfill(2)+u":"+str(data[1][0]%100).zfill(2)
    if data[1][0] == 9999:
        bus1l = u"--:--"
    bus2f = str(data[2][0]/100).zfill(2)+u":"+str(data[2][0]%100).zfill(2)
    if data[2][0] == 9999:
        bus2f = u"--:--"
    bus2l = str(data[3][0]/100).zfill(2)+u":"+str(data[3][0]%100).zfill(2)
    if data[3][0] == 9999:
        bus2l = u"--:--"
    bus3f = str(data[4][0]/100).zfill(2)+u":"+str(data[4][0]%100).zfill(2)
    if data[4][0] == 9999:
        bus3f = u"--:--"
    bus3l = str(data[5][0]/100).zfill(2)+u":"+str(data[5][0]%100).zfill(2)
    if data[5][0] == 9999:
        bus3l = u"--:--"
    bus4f = str(data[6][0]/100).zfill(2)+u":"+str(data[6][0]%100).zfill(2)
    if data[6][0] == 9999:
        bus4f = u"--:--"
    bus4l = str(data[7][0]/100).zfill(2)+u":"+str(data[7][0]%100).zfill(2)
    if data[7][0] == 9999:
        bus4l = u"--:--"
    bus5f = str(data[8][0]/100).zfill(2)+u":"+str(data[8][0]%100).zfill(2)
    if data[8][0] == 9999:
        bus5f = u"--:--"
    bus5l = str(data[9][0]/100).zfill(2)+u":"+str(data[9][0]%100).zfill(2)
    if data[9][0] == 9999:
        bus5l = u"--:--"

    # tテンプレ画像から画像描写
    base = Image.open('img/0.png').convert('RGBA')
    txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt)

    # IPAフォント使用
    fnt = ImageFont.truetype(font='font/ipaexg.ttf', size=18)

    # 文字描写
    # 1
    draw.text((110, 15),bus1f, font=fnt, fill='#ffffff')
    draw.text((170, 15),txt1f, font=fnt, fill='#ffffff')
    draw.text((110, 40),bus1l, font=fnt, fill='#ffffff')
    draw.text((170, 40),txt1l, font=fnt, fill='#ffffff')
    # 2
    draw.text((110, 75),bus2f, font=fnt, fill='#ffffff')
    draw.text((170, 75),txt2f, font=fnt, fill='#ffffff')
    draw.text((110, 100),bus2l, font=fnt, fill='#ffffff')
    draw.text((170, 100),txt2l, font=fnt, fill='#ffffff')
    # 3
    draw.text((110, 135),bus3f, font=fnt, fill='#ffffff')
    draw.text((170, 135),txt3f, font=fnt, fill='#ffffff')
    draw.text((110, 170),bus3l, font=fnt, fill='#ffffff')
    draw.text((170, 170),txt3l, font=fnt, fill='#ffffff')
    # 4
    draw.text((110, 205),bus4f, font=fnt, fill='#ffffff')
    draw.text((170, 205),txt4f, font=fnt, fill='#ffffff')
    draw.text((110, 230),bus4l, font=fnt, fill='#ffffff')
    draw.text((170, 230),txt4l, font=fnt, fill='#ffffff')
    # 5
    draw.text((110, 265),bus5f, font=fnt, fill='#ffffff')
    draw.text((170, 265),txt5f, font=fnt, fill='#ffffff')
    draw.text((110, 290),bus5l, font=fnt, fill='#ffffff')
    draw.text((170, 290),txt5l, font=fnt, fill='#ffffff')

    # テンプレ画像と文字合成
    out = Image.alpha_composite(base, txt)

    # 画像を出力します。
    fname = u"img/test"+str(time)+u".png"
    out.save(fname, 'png', quality=95, optimize=True)
    return fname
