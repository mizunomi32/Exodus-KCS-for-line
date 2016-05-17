# coding: utf-8
from PIL import Image, ImageDraw, ImageFont

# bustimes : バスの時間（１０要素のリスト）
def rotari(data,time=9999):

    # TODO : bus idから行き先を返す関数
    bus1=data[0]
    bus2=data[1]
    bus3=data[2]
    bus4=data[3]
    bus5=data[4]
    bus6=data[5]
    bus7=data[6]
    bus8=data[7]
    bus9=data[8]
    bus10=data[9]


    txt1f = bus1[1]
    txt1l = bus2[1]
    txt2f = u"連節 KG Link 新三田駅直行"
    txt2l = u"KG Link 新三田駅直行"
    txt3f = u"市立図書館 三田駅"
    txt3l = u"連節 市立図書館 三田駅"
    txt4f = u"KG Amuse Lineｲｵﾝﾓｰﾙ・ｱｳﾄﾚｯﾄ"
    txt4l = u"相野駅 つつじヶ丘北口"
    txt5f = u"上ケ原ｷｬﾝﾊﾟｽ直行シャトルバス"
    txt5l = u"上ケ原ｷｬﾝﾊﾟｽ直行シャトルバス"

    bus1f = str(bus1[0]/100)+u":"+str(bus1[0]%100)
    bus1l = str(bus2[0]/100)+u":"+str(bus2[0]%100)
    bus2f = str(bus3[0]/100)+u":"+str(bus3[0]%100)
    bus2l = str(bus4[0]/100)+u":"+str(bus4[0]%100)
    bus3f = str(bus5[0]/100)+u":"+str(bus5[0]%100)
    bus3l = str(bus6[0]/100)+u":"+str(bus6[0]%100)
    bus4f = str(bus7[0]/100)+u":"+str(bus7[0]%100)
    bus4l = str(bus8[0]/100)+u":"+str(bus8[0]%100)
    bus5f = str(bus9[0]/100)+u":"+str(bus9[0]%100)
    bus5l = str(bus10[0]/100)+u":"+str(bus10[0]%100)

    # 透かしを入れる画像を使って、画像オブジェクトを取得します。
    base = Image.open('img/0.png').convert('RGBA')

    # テキストを描画する画像オブジェクトを作成します。
    txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt)

    # フォントを取得します。
    fnt = ImageFont.truetype(font='font/ipaexg.ttf', size=18)

    # 透かし文字の横幅、縦幅を取得します。
    #textw, texth = draw.textsize(watermark, font=fnt)

    # 透かし文字を中央に入れます。
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


    # 画像オブジェクトを重ねます。
    out = Image.alpha_composite(base, txt)

    # 画像を出力します。
    fname = u"img/test"+str(time)+u".png"
    out.save(fname, 'png', quality=95, optimize=True)
    return fname
