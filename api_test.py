#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


#read url_file into send_param
file = open("./url_file.txt")
send_param = {}

while 1:
    line = file.readline()
    if line == '\n' or not line:
        break
    line_index = line.index(':')
    send_param[line[0:line_index]] = line[line_index+1:len(line)-1]
    #print send_param
#read body data into body
file = open("./body_file.txt")
json_string = '';
while 1:
    line = file.readline()
    if line == '\n' or not line:
        break
    json_string += line.strip(' \t\n\r')
    #print json_string
json_param = json.loads(json_string)
#print j['detail']['course_id']


#send http request
body = json_param
headers = {'Content-Type':'application/json'}
cookies = dict(PHPSESSID='tujfgc3naac5229ijmss3bbt20', dx_un='%E6%96%B0%E5%85%83',dx_avatar='http%3A%2F%2F7xil0e.com1.z0.glb.clouddn.com%2Fuser_578efea29ec32.png', dx_token='29fb3ed07e465767f3b2c9c120b7f7d2')
if send_param['type'] == 'get':
    r = requests.get(send_param['url'], params=body, headers=headers, cookies=cookies)
elif send_param['type'] == 'post':
    r = requests.post(send_param['url'], params=body, headers=headers, cookies=cookies)

#print json.dumps(r.text, indent=4, separators=(',', ': '))
#print r.json()
#print r.headers
#print r.cookies['PHPSESSID']
#print r.text
s = json.dumps(r.text.encode('utf-8').decode('unicode_escape'), indent=1)
print r.text.encode('utf-8').decode('unicode_escape')

