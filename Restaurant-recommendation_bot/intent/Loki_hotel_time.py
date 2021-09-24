#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for hotel_time

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_hotel_time = True
userDefinedDICT = {"房間": ["房"], "旅館": ["青年旅館", "飯店", "休息處", "住宿處", "休息的地方"], "預定": ["預約", "訂位", "預訂"], "餐廳": ["餐館", "店家", "吃飯的地方", "吃飯處", "店"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_hotel_time:
        print("[hotel_time] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[大約][幾點][可以]開始入住":
        # write your code here
        pass

    if utterance == "[幾點]開始[可以]入住":
        # write your code here
        pass

    if utterance == "什麼[時候][可以]入住":
        # write your code here
        pass

    if utterance == "入住時間是[幾點]開始":
        # write your code here
        pass

    return resultDICT