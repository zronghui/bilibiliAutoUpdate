#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

curpath = '/Users/zhangronghui/01Code/private/bilibiliAutoUpdate'
os.chdir(curpath)
dlDir = "/Volumes/My Passport/data/ut下载/0  未分类/ytdl videos/bilibili/update/"
icon = 'https://i.loli.net/2020/04/18/nBN5TZRKFfzsjkg.jpg'
ups = {
    '电影最TOP': 17819768,
    '丁香医生': 15982391,
    '人民医学': 26709183,
    'TED君学演讲': 8188433,
    '木鱼水心': 927587,
    '小片片说大片': 10119428,
    '飞碟说': 5581898,
    '青知字幕组': 21416270,
    '大聪看电影': 253350665,
    '妙招姐': 287051252,
    '一俩三四五': 97228279,
    '罗翔说刑法': 517327498,
    '罗翔说刑法/罗翔说刑法1': 6155452,
    '罗翔说刑法/迫害张三': 353021696,
    '罗翔说刑法/张三的传奇一生': 485092296,
    '回形针PaperClip': 258150656,
    '狂野飙车/湿雨': 8410278,
    '凉风Kaze': 14110780,
    '黄一刀有毒': 297242063,
    '蔡老板家的长工': 17171565,
    '17_Xtreme': 26982531,
}
# with open('upUrls.txt') as f:
#     up = re.findall(r'https://space.bilibili.com/(\d+)/.*?', f.read())
#     ups.extend(up)

headers = {
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,und;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://space.bilibili.com/14110780/video',
    'Connection': 'keep-alive',
}
