#! /bin/env python3
#-*- coding: utf-8 -*-

from subprocess import *

def exec_cmd(cmd):
    p= Popen(cmd, shell= True, stdout=PIPE)
    (ret, err)= p.communicate()
    return ret

def grep_login_defs(keyword):
    ret= exec_cmd("grep '%s' /etc/login.defs" % keyword)
    return ret.split()[1]
    
def get_accounts():
    min_u= grep_login_defs("^UID_MIN")
    max_u= grep_login_defs("^UID_MAX")
    
    cmd= "awk -F':' -v 'min=%s'" % min_u
    cmd= cmd + " -v 'max=%s'" % max_u
    cmd= cmd + " '{ if ($3 >= min && $3 <= max) print $1}' /etc/passwd"
    return exec_cmd(cmd).split()

if __name__ == '__main__':
    accouts= get_accounts()
    for account in accouts:
        print account
