## 文件监控工具

* 环境需求

该工具源码需要golang语言支持，开发版本为

 `go version go1.11.2 linux/amd64`

并需要如下库支持

```go
github.com/fsnotify/fsnotify
github.com/wonderivan/logger
```

若无上述环境，可以直接使用编译后的文件。

* 使用说明

*以编译后的二进制文件为例*

```bash
# 在命令行中，将需要监控的文件夹通过 "|" 传递给程序。程序会自动递归寻找子目录并对该目录下所有文件进行监控。
echo /tmp | yxrh_fsnotify #监控单一目录
echo /tmp /usr/loacl/nginx/conf /home | yxrh_fsnotify #监控多个目录
可以参照 github.com/wonderivan/logger 的配置，对日志输出进行配置。或者直接使用shell的重定向功能进行日志记录，使用方法如下：
echo /tmp /usr/loacl/nginx/conf /home | yxrh_fsnotify  > log.file # 打印日志
nohup echo /tmp /usr/loacl/nginx/conf /home | yxrh_fsnotify  > log.file & #后台使用
```

* 结合shell脚本使用

```bash
mv yxrh_fsnotify /usr/bin
chmod +x yxrh_fsnotify
echo '#!/bin/bash' > /usr/bin/fsnotify
echo 'echo $@ | yxrh_fsnotify '>> /usr/bin/fsnotify
fsnotify /tmp /home /data > log.file  & #后台使用
```

