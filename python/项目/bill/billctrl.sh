#!/bin/bash
#source ~/.bash_profile 
#source ~/.bashrc 

WD=/home/python/bill/
pidfile=${WD}pid.file
cd ${WD}

#start
start () {
nohup python3 tornado_helloworld.py &
pid=`ps -ef| grep tornado_helloworld |grep python3 |awk '{print $2}'`
echo ${pid} >${pidfile}
echo "server start as ${pid}"
}

#status
status () {
if [[ -s ${pidfile} ]]; then
	pid=`ps -ef| grep tornado_helloworld |grep python3 |awk '{print $2}'`
	echo "server is starting as ${pid}"
else
	echo "server is stoping"
fi
}

#stop
stop () {
pid=`ps -ef| grep tornado_helloworld |grep python3 |awk '{print $2}'`
kill -9 ${pid}
> ${pidfile}
echo "server stop"
}

#restart
restart () {
stop
start
}

case $1 in
	start )
	start;;
	stop )
	stop;;
	status )
	status ;;
	restart )
	restart ;;
esac
