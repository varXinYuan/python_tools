#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re

#tmp = os.popen("ping -c 10 www.qq.com").readlines()
#print tmp

# 从配置文件里取出
# ping 10 次 存放到变量里
# 遍历数组，正则匹配出时间，相加 / 10，得出的数据放在{IP:{time}}字典里
# 遍历取出最大的值

def getIPs():
    path = os.path.split(os.path.realpath(__file__))[0] + '/VPNips.conf'
    ips = open(path, 'rb').readlines()
    return ips

if __name__ == '__main__':
    ips = getIPs()
    pingInfo = {}
    for item in ips:
        pingDomain = item.strip().rstrip('\n')
        pings = os.popen("ping -c 10 " + pingDomain).readlines()
        pingInfo[pingDomain] = [];
        for n,ping in enumerate(pings):
            match = re.search(r'time=(\S+)', ping)
            if match is not None:
                #print match
                pingSeconds = match.group(1)
                pingInfo[pingDomain].append(float(pingSeconds))
    #print pingInfo
    print "ping包发完，准备处理数据..."

    for domain in pingInfo:
        if pingInfo[domain]:
            pingInfo[domain] = sum(pingInfo[domain]) / len(pingInfo[domain])
        else:
            pingInfo[domain] = 0;

    print "将平均值排序输出..."
    pingInfo = sorted(pingInfo.items(), lambda x, y: cmp(x[1], y[1]), reverse=False)
    print pingInfo
    #for i in pingInfo:
    #    print i + ":" + pingInfo[i]

