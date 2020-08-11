#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

curpath = '/Users/zhangronghui/01Code/private/bilibiliAutoUpdate'
os.chdir(curpath)
dlDir = "/Volumes/My Passport/data/ut下载/0  未分类/ytdl videos/bilibili/update/"
icon = 'https://i.loli.net/2020/04/18/nBN5TZRKFfzsjkg.jpg'
ups = {
    # asmr
    'asmr-是莲生呦': 18391063,
    '萝莉一凡': 31470014,
    # 解说
    '解说-电影最TOP': 17819768,
    '解说-木鱼水心': 927587,
    '解说-小片片说大片': 10119428,
    '解说-蔡老板家的长工': 17171565,
    # '解说-大蓝雀': 362767725,
    '解说-大聪看电影': 253350665,
    '解说-阿斗归来了': 21837784,
    # 编程
    '编程-一俩三四五': 97228279,
    '编程-zerotrac': 3203291,
    # 搞笑
    '搞笑-凉风Kaze': 14110780,
    '搞笑-黄一刀有毒': 297242063,
    # 生活 科普
    '科普-回形针PaperClip': 258150656,
    '科普-飞碟说': 5581898,
    '教育-TED君学演讲': 8188433,
    '教育-青知字幕组': 21416270,
    '医学-人民医学': 26709183,
    '医学-白石菊姐姐': 544339847,
    '生活-妙招姐': 287051252,
    '法律-罗翔说刑法': 517327498,
    '手工-硬核拆解': 427494870,

    # '丁香医生': 15982391,
    # '狂野飙车/湿雨': 8410278,
    # '17_Xtreme': 26982531,
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
