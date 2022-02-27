#! /bin/env python3
#-*- coding: utf-8 -*-

from user_list import *
from datetime import datetime

def remove_num(string):
    tmp = string.strip()
    first_space = tmp.find(" ")
    if first_space < 0:
        return string
    tmp= tmp[first_space : len(tmp)]
    return tmp.strip()

def history(account):
    ret= exec_cmd("sudo -H -u %s bash -i -c 'history -r; hitory'" % account)
    ret_split = ret.strip("\n")
    i= len(ret_split) - 1
    history_list= []
    while i > 0:
        cmd= ret_split[i].strip()
        timestamp = ret_split[i-1]
        i= i-2
        
        if timestamp.find("#") < 0:
            break
        cmd= remove_num(cmd)
        timestamp= remove_num(timestamp)
        
        timestamp= timestamp.replace("#", "")
        date= str(datetime.fromtimestamp(float(timestamp)))
        history_list.append((date, cmd))
    return History_list

if __name__ == '__main__':
    accouts= get_accounts()
    for account in accouts:        
        print "계정 : ", account
        history_list= history(account)
        
        if len(history_list) == 0:
            print("\t 기록된 이력이 없음")
            for h in history_list:
                print "\t %s \t %s" % h
            print "-" * 70
            
