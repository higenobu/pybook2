#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import psycopg2
import re
import io
import six
import codecs
from datetime import timedelta
import time
import datetime
import argparse
import json
import sys
import csv
import os.path
from os import path
#select seq,sum(predict::int) from res where predict='1' group by seq order by seq;
#select seq,cont,sum(predict::int) from res where predict='1' group by seq,cont order by seq;
#select resdate,seq,cont,sum(predict::int) from res where predict='1' group by seq,cont,resdate order by seq;
#create table action (id serial, adate character varying,action character varying,value character varying,msg character varying)
def sel_news(cont,filenm):
  dbname='news'
  #use news for news server
  now=datetime.datetime.now()
  nextdate=now + timedelta(days=1)
  tdate=now.strftime("%Y-%m-%d")
  ndate=nextdate.strftime("%Y-%m-%d")
  wfilenm='%'+filenm+'%'
  if (len(cont)>50):
    subcont='%'+cont[1:50]+'%'
  else:
    subcont='%'+cont[1:]+'%'
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  try:
    
    #sql = """select "a0" from  nsnote where "患者"=%s order by "ObjectID" desc limit 20"""
    sql ='select id from res where '
    where='  filenm like '+"'"+wfilenm+"'"+" and resdate="+"'"+ndate+"'"
    print (sql+where)
    cur.execute(sql+where)

    rows = cur.fetchall()
    if (len(rows)>0):
      return True
    else:
      return False
  except (Exception, psycopg2.DatabaseError) as error:

    pass
  finally:
    if conn is not None:
      conn.close()

def ins_action(ndate,a,b,c):
  dbname='news'
  

  
  conn = psycopg2.connect(dbname=dbname, user="medex", password="medex")
  cur = conn.cursor()
  
  
  try:
    sql = """INSERT INTO action(adate,action,value,msg) 
    VALUES(%s,%s,%s,%s) """
    cur.execute(sql, (ndate,a,b,c))
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print (error)
    print ("ERROR INS")
    pass
  finally:
    if conn is not None:
      conn.close()
  return 
def find_score(ls2,adate):
  for ll in ls2:
    if (ll[0]==adate):
      sc=ll[1]
      break
  else:
    sc=False
  return sc

#main

args = sys.argv
now=datetime.datetime.now()
nextdate=now + timedelta(days=1)
tdate=now.strftime("%Y%m%d")
ndate=nextdate.strftime("%Y%m%d")
filenm=args[1]
filenm2=args[2]
wfile=args[3]

if (path.exists(filenm)):
  print ("exist",filenm)
  with open(filenm) as f:
    reader = csv.reader(f, delimiter=',')
    ls = [row for row in reader]

if (path.exists(filenm2)):
  print ("exist",filenm2)
  with open(filenm2) as f2:
    reader = csv.reader(f2, delimiter=',')
    ls2 = [row for row in reader]

  res_rows = []
  predate=''
  for k in range(len(ls)):
    sc=find_score(ls2,ls[k][0])
    flag=ls[k][1]

    if (sc):
      print (sc)
      res_rows.append([ls[k][0],flag,sc])
      continue
    else:
      sc='NON'
      print ("no value in this date",ls[k][0])
      res_rows.append([ls[k][0],flag,sc])     
        
with open(wfile, 'w') as g:
    writer = csv.writer(g, delimiter=',')
    writer.writerows(res_rows)    
    


#end

      


    
  
