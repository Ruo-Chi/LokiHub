#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for equipment_whereGet

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
import os

DEBUG_equipment_whereGet = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_can":["可以","可","適合"],"_pants":["褲子","褲","長褲","短褲","運動褲","瑜珈褲","單車褲"],"_rocks":["岩點","石頭","手點","點","岩石","攀岩鞋","攀岩鞋子"],"_shoes":["岩鞋","鞋子","抱石鞋","鞋"],"_sides":["東部","北部","南部","西部","中部"],"_levels":["難度","等級","階級","級數"],"_whatIs":["星光票"],"_clothes":["衣服","長袖","短袖","衣著","服裝","長袖衣服","上衣","短袖衣服","長袖上衣","短袖上衣","衣褲"],"_climbing":["上攀","速度攀","速度攀登","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石攀岩","抱石"],"_cityAlias":["縣市","縣","市","地區","都市","城市","區","區域"],"_gymsShort":["紅石","小岩館","Camp 4","角岩館","Corner","汐止抱石館","double8","double 8","原岩","Up聯盟","MegaSTONE","POGO","爬森","蕃薯藤","千手抱石","水美iClimb","風城","B-plus","新竹紅石","TheDepotCity","攀吶","Dapro","破舊二廠","破舊工廠","嗨翻","抱石基地","圓石","圓石空間","Boulder Space","K2","艾思博","禾匠","崩岩","久淘","宜蘭運動中心","嘉義攀岩會館","8a攀岩場","Y17"],"_peClothes":["運動衣","運動褲","運動服","瑜珈褲","單車褲"],"_rockTypes":["jug","pinch","sloper","edge","crimp","pocket","flat","horn","volume"],"_climbingGym":["岩館","攀岩館","攀岩場","抱石館","抱石場館","抱石場","岩場","上攀館","上攀場","上攀場館","攀石場","上攀場館","上攀岩館","先鋒攀岩館","速度攀岩館","速度攀登場館","速度攀場館","速度攀登岩館","速度攀場地"],"_taiwanAlias":["全台","全臺","全台各地","台灣","臺灣","全臺各地"],"_climbingEquip":["裝","裝備","岩粉","粉袋","攀岩粉袋","粉球","止滑粉","攀岩粉","攀岩粉袋","岩點刷","攀岩刷","鎂粉球","鎂粉","碳酸鎂粉"],"_normalWearings":["一般運動鞋","牛仔褲"],"_topRopingEquip":["手套","確保手套","垂降手套","耐磨手套","安全吊帶","確保器","安全扣","快扣","安全扣環","吊帶"],"_climbingGeneralGym":["岩館","攀岩館","攀岩場","攀岩場館"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_equipment_whereGet:
        print("[equipment_whereGet] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[你]知道[可以]去[哪買][岩粉]嗎":
        # write your code here
        pass

    if utterance == "[你]知道[岩粉]哪裡租得到嗎":
        # write your code here
        pass

    if utterance == "[你]知道[岩粉]哪裡買得到嗎":
        # write your code here
        pass

    if utterance == "[你]知道[岩粉]要去[哪買]嗎":
        # write your code here
        pass

    if utterance == "[岩粉][可以]去[哪買]？":
        # write your code here
        pass

    if utterance == "[岩粉]哪裡[可以]租得到？":
        # write your code here
        pass

    if utterance == "[岩粉]哪裡[可以]買得到？":
        # write your code here
        pass

    if utterance == "[岩粉]哪裡買得到？":
        # write your code here
        pass

    return resultDICT