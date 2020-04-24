#!/usr/bin/env bash
cd ~/code/bilibiliAutoUpdate || cd ~/01Code/private/bilibiliAutoUpdate || exit
cp config.py config-bak.py
cp timestamp.txt timestamp-bak.txt
git checkout .
git pull
mv -f config-bak.py config.py
mv -f timestamp-bak.txt timestamp.txt
echo 'code update done!'
