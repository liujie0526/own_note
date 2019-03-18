#!/bin/bash

#for put jianlaixiaoshuo 

OLD=`cat MARK1`

NEW=`curl -s 'https://www.5atxt.com/0_1' |grep 'latest_chapter_url'| awk -F '"' '{print $4}'`
URL="https://www.5atxt.com$NEW"

ACCESS_TOKEN=`curl 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwe6753c349e5a217a&corpsecret=hPj-UgVbcnUHYXe6uOgUiYWZTKW0YDySwID8RGcCkvI' | awk -F\" '{print $10}'`
PURL="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=$ACCESS_TOKEN"
function body() {
    local int AppID=1000003
    local PartyID=1
    local Msg=$(echo "$@" | cut -d" " -f1-)
    printf '{\n'
    printf '\t"touser": "'"$UserID"\"",\n"
    printf '\t"toparty": "'"$PartyID"\"",\n"
    printf '\t"msgtype": "text",\n'
    printf '\t"agentid": "'"$AppID"\"",\n"
    printf '\t"text": {\n'
    printf '\t\t"content": "'"$Msg"\""\n"
    printf '\t},\n'
    printf '\t"safe":"0"\n'
    printf '}\n'
}

if [[ ${NEW} != ${OLD} ]]; then
	echo "${NEW}" > MARK1
	/usr/bin/curl --data-ascii  "$(body `echo ${URL} `|sed 's/\ /\n/g')" $PURL
fi

