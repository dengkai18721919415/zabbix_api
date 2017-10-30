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
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
            return 0
        else:
            response = json.loads(result.read())
            result.close()
            return response
        
    def host_get(self,hostip):
        #hostip = raw_input("\033[1;35;40m%s\033[0m" % 'Enter Your Check Host:Host_ip :')
        data = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "host.get",
                    "params": {
                        "output":["hostid","name","status","host"],
                        "filter": {"host": [hostip]}
                    },
                    "auth":self.authID,
                    "id": 1
                })
        res = self.get_data(data)['result']
        if (res != 0 ) and (len(res) != 0):
            host = res[0]
            if host['status'] == '1':
                print "\t","\033[1;31;40m%s\033[0m" % "Host_IP:","\033[1;31;40m%s\033[0m" %host['host'].ljust(15),'\t',"\033[1;31;40m%s\033[0m" % "Host_Name:","\033[1;31;40m%s\033[0m"% host['name'].encode('GBK'),'\t',"\033[1;31;40m%s\033[0m" % u'unmonitor'.encode('GBK')
                return host['hostid']
            elif host['status'] == '0':
                print "\t","\033[1;32;40m%s\033[0m" % "Host_IP:","\033[1;32;40m%s\033[0m" %host['host'].ljust(15),'\t',"\033[1;32;40m%s\033[0m" % "Host_Name:","\033[1;32;40m%s\033[0m"% host['name'].encode('GBK'),'\t',"\033[1;32;40m%s\033[0m" % u'monitor'.encode('GBK')
                return host['hostid']
        else:
            print '\t',"\033[1;31;40m%s\033[0m" % "Get Host Error or cannot find this host,please check !"
            return 0
    
    def get_grouphost(self):
        groupid = raw_input("\033[1;35;40m%s\033[0m" % 'Enter Your groupid:')
        data = json.dumps(
            {
                "jsonrpc":"2.0",
                "method":"host.get",
                "params":{
                    "output":["hostid","name","status","host"],
                    #"output":"extend",
                    "groupids":groupid,
                },
                "auth":self.authID,
                "id":1,
            })
        res = self.get_data(data)
        if 'result' in res.keys():
            res = res['result']
            if (res !=0) or (len(res) != 0):
                print "\033[1;32;40m%s\033[0m" % "Number Of Hosts: ","\033[1;31;40m%d\033[0m" % len(res)
                for host in res:
                    print "Host ID:",host['hostid'],"Visible name:",host['name'],"Host-status:",host['status'],"HostName:",host['host']
        else:
            print "Host
                   
                     
            
