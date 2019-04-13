# ulimit与内核优化



ulimit

```shell
vim /etc/security/limits.d/90-nproc.conf

vim /etc/security/limits.conf
```


内核

```shell
vim /etc/sysctl.conf
```


查看句柄及PID

```shell
lsof -n|awk '{print $2}'|sort|uniq -c|sort -nr|more
```