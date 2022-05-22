# !/usr/bin/env python
# -*- coding: utf-8 -*-

file = open('happy.txt')
for kurikaeshi in range(1,20):
  memo = file.readline()
  print (memo)
file.close()
