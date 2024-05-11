# HonYou2BeLive
## 测试 stream-link
```
 wget --user-agent "(Windows NT 10.0; Win64; x64) PotPlayer/23.11.02"  https://www.stream-link.org/stream-link.m3u
```
## 测试 HONTV官方
```
curl --user-agent "(Windows NT 10.0; Win64; x64) PotPlayer/23.11.02" https://hoytv-live-stream.hoy.tv/ch78/index-fhd-3-v-fhd.m3u8
```
# 另一种获取m3u8文件的工具
# https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file
 .\yt-dlp.exe -f b -g "https://www.youtube.com/@TVBSNEWS01/live"
https://manifest.googlevideo.com/api/manifest/hls_playlist/expire/1711727951/ei/75AGZqD3HI2M0-kP-4O9cA/ip/103.75.70.214/id/m_dhMSvUCIc.4/itag/96/source/yt_live_broadcast/requiressl/yes/ratebypass/yes/live/1/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D137/rqh/1/hdlc/1/hls_chunk_host/rr4---sn-oguesn6k.googlevideo.com/xpc/EgVo2aDSNQ%3D%3D/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/4706250/mh/V0/mm/44/mn/sn-oguesn6k/ms/lva/mv/m/mvi/4/pl/24/dover/11/pacing/0/keepalive/yes/fexp/51141542/mt/1711705952/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,sgoap,sgovp,rqh,hdlc,xpc,playlist_duration,manifest_duration,vprv,playlist_type/sig/AJfQdSswRQIgSFjotXTyQdkASFWvSQkWWQIE3Pa77ddZ-MgtR39-S6gCIQC1gqOkPCPWj4EG-pJAORUrdGhy5Q6fcqy9AwSBQ7bi1w%3D%3D/lsparams/hls_chunk_host,initcwndbps,mh,mm,mn,ms,mv,mvi,pl/lsig/ALClDIEwRgIhAMUPxqfHufQvJCUQQnC2lzwIV9YwAyVMlZmds-Ewyc9jAiEA-AdfWLR0kbvQOTMpU9EjCz7QAQSBb4sCcUKjE9nI1j8%3D/playlist/index.m3u8
# CentOS 7.9 上安装 yt-dlp
## 安装依赖项：
```
sudo yum install -y epel-release
sudo yum install -y python3 python3-pip
sudo pip3 install --upgrade pip
```
## 下载 yt-dlp：
```
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
```
## 添加执行权限：
```
sudo chmod a+rx /usr/local/bin/yt-dlp
```
# php
## php.ini打开shell_exec 
```
<?php
// 获取传递的 URL 参数
if (isset($_GET['url'])) {
    // 获取 YouTube 视频链接
    $video_url = $_GET['url'];

    // 构建 yt-dlp 命令
    $command = "/path/to/yt-dlp -f b -g \"$video_url\"";

    // 执行命令
    $output = shell_exec($command);

    // 检查是否成功获取 m3u8 文件链接
    if (!$output) {
        die("Failed to fetch m3u8 file.");
    }

    // 输出 m3u8 文件链接
    echo $output;
} else {
    // 如果未传递 URL 参数，则输出错误信息
    echo "Error: URL parameter is missing.";
}
?>
```
# hls常用命令
## 获取用户ip去重
```
netstat -anlp|grep "192.168.8.202:8881"|awk '{ print $5 }'|grep -Ev '192.168'|cut -d: -f1|sort -u
```
