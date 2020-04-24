#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import funcy

import requests

import config
from config import dlDir, icon

if not os.path.exists(dlDir):
    sys.exit()


@funcy.print_enters
# @funcy.print_exits
def readTS():
    with open('timestamp.txt') as f:
        return int(f.read().strip())


@funcy.print_enters
# @funcy.print_exits
def updateTS():
    with open('timestamp.txt', 'w') as f:
        f.write(str(int(time.time())))


@funcy.print_enters
@funcy.print_durations
# @funcy.print_exits
def updatesOfUp(upName, mid, timestamp):
    params = (
        ('mid', str(mid)),
        ('pagesize', '100'),
        ('tid', '0'),
        ('page', '1'),
        ('keyword', ''),
        ('order', 'pubdate'),
    )

    response = requests.get('http://space.bilibili.com/ajax/member/getSubmitVideos',
                            headers=config.headers, params=params)
    j = response.json()
    for i in j['data']['vlist']:
        if i['created'] > timestamp:
            notify(upName, i['title'])
            dl(i['aid'], upName)


@funcy.print_enters
@funcy.print_durations
# @funcy.print_exits
def dl(videoid, upName):
    if not os.path.exists(dlDir + upName):
        os.system(f'mkdir -p "{dlDir + upName}"')
    os.system("cd '{}'; you-get -l https://www.bilibili.com/video/av{}".format(dlDir + upName, videoid))


def notify(title, message, icon=icon):
    os.system("/usr/local/bin/notify --title '{}' --message '{}' --icon {} -s".format(title, message, icon))


if __name__ == '__main__':
    notify('bilibili update', 'start')
    os.chdir(config.curpath)
    print(os.getcwd())
    timestamp = readTS()
    for upName, mid in config.ups.items():
        updatesOfUp(upName, mid, timestamp)
    updateTS()
    notify('bilibili update', 'end')
