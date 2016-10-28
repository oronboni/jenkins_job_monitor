#!/bin/bash
FILE=access_log_Jul95
for ip in $(cat access_log_Jul95 |cut -d '-' -f 1 | sort|uniq); do
	COUNT=$(grep ^$ip access_log_Jul95 |wc -l);
	if [ ${#ip} -ge 10 ]; then echo $COUNT -- $ip >> data;
	fi
done
sort -k1 -n data