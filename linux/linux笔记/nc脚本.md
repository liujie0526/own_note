```shell
cat 2 |while read IPPORT
do  

    IP=`echo $IPPORT | awk '{print $1}'`
    PORT=`echo $IPPORT | awk '{print $2}'` 

    cat 1| while read A 
    do
        nc -w 1 ${IP} ${PORT}
    done
    if [[ $? = 0 ]]; then
        echo "${IPPORT} is ok" >> 3
    else
        echo "${IPPORT} is error" >> 3
    fi

done
```

