#!/bin/bash
# 设置时区为中国香港
export TZ=Asia/Hong_Kong
# 从URL读取频道列表
CHANNEL_URL="https://raw.githubusercontent.com/hearofnight/YTBLive_Catcher/main/sources/ChannelNeed.txt"
CHANNELS=($(curl -s "$CHANNEL_URL"))
#初始化频道信息文件夹和日志文件
mkdir -p {newchannels,logs}
touch logs/youtube_live_`date +%Y%m%d`.log
# 遍历每个频道
for channel in "${CHANNELS[@]}"; do
    # 调用 xxx.py 脚本并传递频道参数
    python3 scripts/SingleChannelAnalysis.py "$channel" > "newchannels/$channel.m3u8"
done
#保存执行日志到logs/youtube_live_`date +%Y%m%d`.log
date +'最后一次链接捕获时间为 %Y 年 %m 月 %d 日 %H:%M:%S, %A' >> logs/youtube_live_`date +%Y%m%d`.log
#Log de Capturas
#date +'Última captura de links foi %A, %d de %B de %Y às %H:%M' >> captures.log

