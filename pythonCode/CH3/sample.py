#!/bin/env python
#-*- coding: utf-8 -*-

mymessages = open("mymessages.log", encoding= 'cp949')
print (mymessages.read())
mymessages.close()
