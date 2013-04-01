#!/bin/bash

src='219.245.64.'
#src='192.168.0.'
resss=''

for((i=1;i<255;i=i+1))
do
    ipadd=$src$i
    ping -c 1 -w 1 $ipadd >/dev/null
    if [ $? -eq 0 ];then
        echo "ip: "$ipadd" is useful."
        result=`nmap -F -O $ipadd | grep 'Running'`
        if [ $? -eq 0 ];then
            resss="$resss$ipadd $result
"
        fi
    else
        continue
    fi
done
echo "$resss">/tmp/os
