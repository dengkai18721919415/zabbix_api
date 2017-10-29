#!/usr/bin/env python
#coding:utf-8
import json
import urllib2
import sys


calss zabbixtools:
    def __init__(self):
        self.url = "http://company/zabbix/api_jsonrpc.php"
        self.header = {"Content-Type":"application/json"}
        self.authID = self.user_login()
    
    def user_login(self):
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "user.login",
                "params": {
                    "user": "Admin",
                    "password" :"xxxx"
                },
                "id": 0
            })
    request = urllib2.Request(self.url,data)
    for key in self.header:
        request.add_header(key,self.header[key])
    try:
        result = urllib2.urlopen(request)
    except URLError as e:
        response = json.loads(result.read())
        result.close()
        authID = response['result']
        return authID
    
    def get_data(self,data,hostip=""):
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key,self.header[key])
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'Error:We have failed to reach the server!'
                print 'Reason: ',e.reason
        elif hasattr(e, 'code'):
            
