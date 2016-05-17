# coding: utf-8
from wimg import rotari


def set_bus(time):
    bus1 = search_bus(time,1)
    bus1[1]=bus_to(bus1[1])
    buf = bus1[0]+1
    bus2 = search_bus(buf,1)
    bus2[1]=bus_to(bus2[1])
    busx = [9999,99]
    data = [
        bus1,
        bus2,
        busx,
        busx,
        busx,
        busx,
        busx,
        busx,
        busx,
        busx,
        ]
    return rotari(data,time)


## 関数　bus_to
## bus id からバスの行き先を返す関数
# 引数　bus_id
# 返り値 文字列
#   1 : 関学エクスプレス 新神戸駅 三宮
#   2 : 関学エクスプレス 　　　　 三宮
def bus_to(bus_id = 0):
    if (bus_id == 1):
        return u"関学エクスプレス 新神戸駅 三宮"
    elif (bus_id == 2):
        return u"関学エクスプレス 　　　　 三宮"
    elif (bus_id == 3):
        return u"特急   新神戸駅   三宮"
    else:
        return u"error"


## 関数　search_bus
## 2分探索でバスを検索
# 引数　time type
#   type
#   1 : KSCロータリー発三宮行き 平日
# 返り値 リスト　[bustime, bus_id]
def search_bus(time,type = 1):
    if(type ==1):
        buf=to_sannnomiya()

    bustimes = buf[0]
    bus = buf[1]
    high = len(bustimes)

    if time>bustimes[high-1]:
        return [9999,89]

    low = 0
    # t は中央番目の数
    t = (low + high) / 2
    # 探索の下限のlowが上限のhighになるまで探索
    # lowがhighに達すると数は見つからなかったということ
    while (low<=high):
        if ((time<=bustimes[t])and(time>bustimes[t-1])):
            break
        elif (time > bustimes[t]):
            low = t + 1

        elif (time < bustimes[t]):
            high = t - 1
        t = (low + high) / 2
    return [bustimes[t],bus[t]]

##  TODO : sqliteへの書き換え
## 関数　to_sannnomiya
## KSCロータリー発三宮行きバスダイヤ
# bus
#   0 : 授業時のみ関学エクスプレス(新神戸通過)
#   1 : 休講期間運行関学エクスプレス
#   2 : 平日　三宮行き

def to_sannnomiya():
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
        2206
    ]
    bus=[
        99,
        1,
        2,
        0,
        1,
        2,
        2,
        0,
        1,
        2,
        2,
        0,
        1,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2
    ]
    return [time, bus]
