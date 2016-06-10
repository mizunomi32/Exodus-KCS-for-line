# coding: utf-8

##
## バス処理
##

from wimg import rotari

def set_bus(time,w = 0):
    ##
    ## 現在時刻からバス出発時間取得し画像描写
    ##

    bus1 = search_bus(time,1,w)
    bus1[1]=bus_to(bus1[1])
    buf = bus1[0]+1
    bus2 = search_bus(buf,1,w)
    bus2[1]=bus_to(bus2[1])
    bus3 = search_bus(time,2,w)
    bus3[1]=bus_to(bus3[1])
    buf = bus3[0]+1
    bus4 = search_bus(buf,2,w)
    bus4[1]=bus_to(bus4[1])
    bus5 = search_bus(time,3,w)
    bus5[1]=bus_to(bus5[1])
    buf = bus5[0]+1
    bus6 = search_bus(buf,3,w)
    bus6[1]=bus_to(bus6[1])
    bus7 = search_bus(time,4,w)
    bus7[1]=bus_to(bus7[1])
    buf = bus7[0]+1
    bus8 = search_bus(buf,4,w)
    bus8[1]=bus_to(bus8[1])
    bus9 = search_bus(time,5,w)
    bus9[1]=bus_to(bus9[1])
    buf = bus9[0]+1
    bus10 = search_bus(buf,5,w)
    bus10[1]=bus_to(bus10[1])
    busx = [9999,99]
    data = [
        bus1,
        bus2,
        bus3,
        bus4,
        bus5,
        bus6,
        bus7,
        bus8,
        bus9,
        bus10
        ]
    return rotari(data,time)

def bus_to(bus_id = 0):
    ##
    ## bus_idからバスの行き先を返す
    ##

    if (bus_id == 1):
        return u"関学エクスプレス 　　　　 三宮"
    elif (bus_id == 2):
        return u"関学エクスプレス 新神戸駅 三宮"
    elif (bus_id == 3):
        return u"特急   新神戸駅   三宮"
    elif (bus_id == 4):
        return u"KG link 連節 JR新三田駅"
    elif (bus_id == 5):
        return u"KG link 　　 JR新三田駅"
    elif (bus_id == 6):
        return u"55 準急     JR新三田駅"
    elif (bus_id == 7):
        return u"46 快速     JR新三田駅"
    elif (bus_id == 8):
        return u"46 急行     JR新三田駅"
    elif (bus_id == 9):
        return u"48 　　     JR新三田駅"
    elif (bus_id == 10):
        return u"46 　　     JR新三田駅"
    elif (bus_id == 11):
        return u"市立図書館前 三田駅"
    elif (bus_id == 12):
        return u"連節 市立図書館前 三田駅"
    elif (bus_id == 13):
        return u"フラワータウン 三田駅"
    elif (bus_id == 14):
        return u"フラワータウン 富士が丘６"
    elif (bus_id == 15):
        return u"観音山 三田駅"
    elif (bus_id == 16):
        return u"55 つつじヶ丘北口"
    elif (bus_id == 17):
        return u"55 相野駅 つつじヶ丘北口"
    elif (bus_id == 18):
        return u"63 神戸三田ﾌﾟﾚﾐｱﾑｱｳﾄﾚｯﾄ"
    elif (bus_id == 19):
        return u" 西宮上ケ原キャンパス"
    else:
        return u"本日の運行は終了しました"


## 関数　search_bus
## 2分探索でバスを検索
# 引数　time type
#   type
#   1 : KSCロータリー発三宮行き 平日
# 返り値 リスト　[bustime, bus_id]
def search_bus(time,type = 1,w=0):

    if(type ==1):
        bustimes, bus =to_sannnomiya(w)
    elif(type == 2):
        bustimes, bus = to_sinsanda(w)
    elif(type == 3):
        bustimes, bus = to_sanda(w)
    elif(type == 4):
        bustimes, bus = to_tutuzi(w)
    elif (type == 5):
        bustimes, bus = to_uegahara(w)

    # 2分探索
    high = len(bustimes)
    if time>bustimes[high-1]:
        return [9999,89]
    low = 0
    t = (low + high) / 2
    while (low<=high):
        if ((time<=bustimes[t])and(time>bustimes[t-1])):
            break
        elif (time > bustimes[t]):
            low = t + 1
        elif (time < bustimes[t]):
            high = t - 1
        t = (low + high) / 2
    return [bustimes[t],bus[t]]

##  TODO : ダイヤのsqliteへの書き換え

def to_sannnomiya(w=0):
    ##
    ## KSCロータリー発三宮行きバスダイヤ
    ##
    time=[]
    bus=[]
    if w == 0 :
        time=[
            0,
            1335,
            1337,
            1510,
            1515,
            1517,
            1552,
            1650,
            1655,
            1657,
            1727,
            1830,
            1835,
            1837,
            1907,
            1937,
            2016,
            2041,
            2116,
            2136,
            2206,
            9999
            ]
        bus=[
            99,
            2,
            3,
            1,
            2,
            3,
            3,
            1,
            2,
            3,
            3,
            1,
            2,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            999
            ]
    elif w == 1:
            time=[
                0,
                1335,
                1337,
                1515,
                1517,
                1552,
                1655,
                1657,
                1727,
                1835,
                1837,
                1907,
                1937,
                2016,
                2041,
                2116,
                2136,
                2206,
                9999
                ]
            bus=[
                99,
                2,
                3,
                2,
                3,
                3,
                2,
                3,
                3,
                2,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                999
                ]
    elif w == 2:
        time=[
            0,
            1553,
            1728,
            9999
            ]
        bus=[
            99,
            3,
            3,
            999
            ]

    return [time, bus]

def to_sinsanda(w=0):
    ##
    ## KSCロータリー発新三田行きバスダイヤ
    ##
    time=[]
    bus=[]
    if (w == 0):
        time = [
            0,
            812,
            858,
            1037,
            1250,
            1337,
            1510,
            1513,
            1516,
            1519,
            1525,
            1533,
            1550,
            1558,
            1638,
            1643,
            1648,
            1651,
            1654,
            1657,
            1700,
            1703,
            1706,
            1736,
            1814,
            1820,
            1828,
            1832,
            1835,
            1838,
            1842,
            1853,
            1908,
            1935,
            2004,
            2025,
            2111,
            2140,
            2158,
            9999
        ]#38
        bus = [
            99,
            6,
            6,
            6,
            7,
            6,
            4,
            5,
            8,
            7,
            8,
            7,
            7,
            7,
            8,
            8,
            4,
            5,
            8,
            8,
            7,
            8,
            7,
            7,
            8,
            8,
            4,
            8,
            8,
            7,
            9,
            10,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            999
        ]
    return [time, bus]

def to_sanda(w=0):
    ##
    ## KSCロータリー発三田行きバスダイヤ
    ##
    time=[]
    bus=[]
    if (w==0):
        time=[
            0,
            1040,
            1140,
            1250,
            1300,
            1410,
            1440,
            1510,
            1515,
            1540,
            1545,
            1600,
            1630,
            1650,
            1655,
            1700,
            1710,
            1740,
            1810,
            1825,
            1830,
            1835,
            1840,
            1850,
            1900,
            1920,
            1950,
            2020,
            2050,
            2120,
            2220,
            9999
        ]
        bus=[
            99,
            11,
            12,
            11,
            11,
            11,
            11,
            12,
            13,
            15,
            14,
            13,
            13,
            12,
            11,
            13,
            13,
            13,
            13,
            11,
            11,
            11,
            13,
            13,
            13,
            11,
            11,
            11,
            11,
            11,
            11,
            999
        ]

    return [time, bus]

def to_tutuzi(w=0):

    time=[]
    bus=[]
    if (w == 0):
        time=[
            0,
            1128,
            1130,
            1228,
            1428,
            1510,
            1628,
            1655,
            1705,
            1831,
            9999
        ]
        bus=[
            99,
            16,
            18,
            17,
            16,
            18,
            16,
            18,
            16,
            16,
            999
        ]

    return [time, bus]
def to_uegahara(w=0):
    ##
    ## KSCロータリー発上ケ原行きバスダイヤ
    ##
    time=[]
    bus=[]
    if (w == 0):
        time=[
            0,
            930,
            1120,
            1340,
            1520,
            1700,
            1840,
            9999
        ]
        bus=[
            99,
            19,
            19,
            19,
            19,
            19,
            19,
            999
        ]

    return [time, bus]
