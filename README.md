# bilibiliAutoUpdate

## 简介

借助工具 [soimort/you-get](https://github.com/soimort/you-get) 下载哔哩哔哩多个 up 的更新视频，并通知更新的视频，以及下载进度

## 效果图

<img src="https://i.loli.net/2020/09/01/INuxDAyfzHqjb6X.png" alt="image-2020090109443782" style="zoom: 33%;" />

## 安装

```shell
# 用文本编辑器修改 config.py config1.py
pip3 install -r ./requirements.txt
```

## 更新代码

```shell
./updateCode.sh
```

## crontab 设置

在 crontab 里设置空闲时间(17-20)运行脚本

```
# 自动下载哔哩哔哩视频
0 17-20 * * * python3 "/Users/zhangronghui/01Code/private/bilibiliAutoUpdate/updateVideoDL.py"
```

