#!/usr/bin/env python
import sys
import csv
import time
import datetime
#from datetime import date
from datetime import datetime
import pytz

def write_his(msg):
    with open('hiskabu.txt','a') as token:
            res=token.write(msg)
    return res         



def get_quote(preprice):
    if (preprice):
        fprice=float(preprice)+50
        price=str(fprice)
    else:
        with open('kabuprice.txt','r') as token:
            pr=token.read(10)
            price=pr.strip() 
    return price

def write_kessai(kessai):
    timeZ_J=pytz.timezone('Asia/Tokyo')
    dt_j=datetime.now(timeZ_J)    
    jdate=dt_j.strftime('%Y%m%d')
    with open('kessai.txt','w') as token:
            res=token.write(kessai+','+jdate+'\n')
    return res         


def auto2(initq,eki,loss,direction):
    
    timeZ_J=pytz.timezone('Asia/Tokyo')
    dt_j=datetime.now(timeZ_J)    
    jdate=dt_j.strftime('%Y%m%d')    
    jtime=dt_j.strftime('%H:%M')    
    preprice=0
    begin='08:30'
    end='16:15'
    while (jtime>=begin and jtime<=end):

        cprice=get_quote(preprice)
        preprice=cprice

        quote=float(cprice)
        write_his(cprice+','+jdate+','+jtime+'\n')
        
                
        print ("price",quote)
        if (not quote):
            breakflag='none'
            
            print ("NO quote because break session")

            
        elif (quote<=(initq-eki) and direction=='1'):
                
                mbuy=quote
                
                msell=initq
                
                ekiv=initq-mbuy
                print ('ekidahi-1',msell,quote,ekiv,'EKI-1')                
                
                breakflag=str(ekiv)
                
                break


        elif (quote>=(initq+loss)  and direction=='1' and ekionly=='NO'):
               
                mbuy=quote
                msell=initq
                
                lossv=initq-mbuy
                print ('losscut-1',msell,quote,lossv,'LCUT')
                breakflag=str(lossv)
                
                break              
  
                

        elif (quote>=(initq+eki)  and  direction=='2'):
                
                msell=quote
                mbuy=initq
                
                ekiv=msell-initq
                print ('ekidahi-2',mbuy,quote,ekiv,'EKI-2')                
                breakflag=str(ekiv)
                              
                break
                #for reverse losscut and new order
        
                              
        elif (quote<=(initq-loss)  and  direction=='2' and ekionly=='NO'):
                
                msell=quote
                mbuy=initq
                mlss=1
                lossv=initq-msell
                print ('losscut-2',mbuy,quote,lossv,'LCUT')                
                
                breakflag=str(lossv)
                              
                break

        else:
                print ("NO losscut/ekidashi")
                
        
        time.sleep(10)  
        timeZ_J=pytz.timezone('Asia/Tokyo')
        dt_j=datetime.now(timeZ_J)    
        jdate=dt_j.strftime('%Y%m%d')        
        jtime=dt_j.strftime('%H:%M')                      
    #exit from while                            
    else:
        print ("end of session ")
        hike=initq-quote
        breakflag=str(hike)
        

    return breakflag



if __name__ == '__main__':
    initq=26550
    direction='2'
    kessai=auto2(initq,100,100,direction)
    write_kessai(kessai)