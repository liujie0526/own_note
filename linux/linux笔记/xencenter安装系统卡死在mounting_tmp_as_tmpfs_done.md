### xencenter安装系统卡死在mounting_tmp_as_tmpfs_done



解决方案：

首先通过 `xe vm-list` 获取UUID

然后再执行 `xe vm-param-set uuid=uuid_of_your_virtual_machine platform:viridian=false `

接着重新启动你要安装的那个系统

<http://serverfault.com/questions/535492/rhel-clones-centos-scientific-cern-network-installation-on-xenserver-6-2>

