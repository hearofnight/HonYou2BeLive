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
# python3 更新脚本
## vim update_python.sh
```
#!/bin/bash

# 如果没有传入版本号，则提示用户输入
if [ -z "$1" ]; then
  echo "请输入要升级的 Python 版本，例如 3.9.2"
  read -p "Python 版本: " PYTHON_VERSION
  # 如果用户没有输入版本号，脚本退出
  if [ -z "$PYTHON_VERSION" ]; then
    echo "没有输入 Python 版本，退出脚本。"
    exit 1
  fi
else
  PYTHON_VERSION=$1
fi

# 提取 Python 的主版本号（如 3.9）
MAJOR_VERSION=$(echo $PYTHON_VERSION | cut -d'.' -f1-2)

# 更新系统并安装必要的依赖
sudo yum -y update
sudo yum groupinstall "Development Tools" -y
sudo yum install gcc openssl-devel bzip2-devel libffi-devel zlib-devel -y

# 下载 Python 源码包
cd /usr/src
sudo wget --no-check-certificate https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz

# 解压并进入 Python 目录
sudo tar xvf Python-$PYTHON_VERSION.tgz
cd Python-$PYTHON_VERSION

# 创建安装目录
sudo mkdir -p /usr/local/python3

# 配置 Python 安装路径
sudo ./configure --prefix=/usr/local/python3

# 编译并安装 Python
sudo make && sudo make install

# 备份现有的 Python3 和 pip3
sudo \cp -rf /usr/local/python3/bin/python3 /usr/local/python3/bin/python3_bak$(date +%Y%m%d%H%M%S)
sudo \cp -rf /usr/local/python3/bin/pip3 /usr/local/python3/bin/pip3_bak$(date +%Y%m%d%H%M%S)

# 如果 /usr/bin/python3 和 /usr/bin/pip3 存在，先删除它们
if [ -e /usr/bin/python3 ]; then
  sudo rm -rf /usr/bin/python3
fi

if [ -e /usr/bin/pip3 ]; then
  sudo rm -rf /usr/bin/pip3
fi

# 创建新的符号链接
sudo ln -sf /usr/local/python3/bin/python$MAJOR_VERSION /usr/bin/python3
sudo ln -sf /usr/local/python3/bin/pip$MAJOR_VERSION /usr/bin/pip3

# 验证 python 和 pip 安装
python3 --version
pip3 --version
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
# docker
## 检查 docker-compose 是否安装
```
docker-compose --version
```
## 安装 docker-compose
```
sudo curl -L "https://github.com/docker/compose/releases/download/v2.27.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
## 缺少 jq
```
sudo yum install -y jq
```
## 查看容器镜像版本
```
docker image inspect pixman/pixman|grep version
```
## 查看远端镜像版本
```
curl -sS "https://registry.hub.docker.com/v2/repositories/pixman/pixman/tags/latest" | jq -r '.name'
```
## 获取远程仓库latest标签的digest
```
curl -sS "https://registry.hub.docker.com/v2/repositories/pixman/pixman/tags/latest" | jq -r '.digest'
```
## 获取本地镜像latest标签的digest
```
docker inspect --format='{{index .RepoDigests 0}}' pixman/pixman:latest
```
## 手动触发 Watchtower：使用以下命令手动触发 Watchtower 进行一次更新检查，以测试配置是否生效
```
docker exec watchtower /watchtower --run-once
```
