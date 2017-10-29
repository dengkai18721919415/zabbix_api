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
