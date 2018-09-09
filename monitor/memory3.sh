#!/bin/bash
sh /home/zqxt_form2/monitor/memory2.sh $1 |grep stdout |grep % |awk '{print $3}'|awk -F '%' '{print $1}'
