#!/bin/bash
#rrdtool create cpu.rrd --step 5 DS:cpuds:GAUGE:8:0:U   RRA:AVERAGE:0.5:1:17280  RRA:MIN:0.5:1:17280  RRA:MAX:0.5:1:17280 RRA:AVERAGE:0.5:10:3456 RRA:MIN:0.5:10:3456 RRA:MAX:0.5:10:3456  RRA:AVERAGE:0.5:100:1210  RRA:MIN:0.5:100:1210 RRA:MAX:0.5:100:1210
while true;do 
    cpu=`vmstat 1 1 |tail -n 1 |awk  '{print $15}'`
    memory=`free -m |grep "Mem" |awk '{print $4+$6}'`
    disk=`df -h |head -n 2 |tail -n 1 |awk '{print $5}'|awk -F '%' '{print $1}'`
    rrdtool update ./cpu.rrd N:${cpu}
    rrdtool update ./memory.rrd N:${memory}
    rrdtool update ./disk.rrd N:${disk}
    sleep 5
done

#1minute=`date --date '1 minute ago ' +%s`
#3minute=`date --date '3 minute ago ' +%s`
#5minute=`date --date '5 minute ago ' +%s`

#rrdtool graph cpu1.jpg --step 5 -s ${1minute} -t "cpu  1 minute monitor" -v cpu DEF:cpu=./cpu.rrd:cpuds:AVERAGE LINE1:cpu#FF0000:'cpu avg'
#rrdtool graph cpu3.jpg --step 5 -s ${3minute} -t "cpu  3 minute monitor" -v cpu DEF:cpu=./cpu.rrd:cpuds:AVERAGE LINE1:cpu#FF0000:'cpu avg'
#rrdtool graph cpu5.jpg --step 5 -s ${5minute} -t "cpu  5 minute monitor" -v cpu DEF:cpu=./cpu.rrd:cpuds:AVERAGE LINE1:cpu#FF0000:'cpu avg'

