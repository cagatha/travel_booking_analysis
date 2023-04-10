# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:09:32 2022

@author: agath
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 10:51:59 2022

@author: agath
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import datetime



myheader={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

checkin=0

listtitles=[]
listrooms=[]
listratings=[]
listnum_ppls=[]
listprices=[]
listlocations=[]  
listcheckin=[]
listcheckout=[]
rowlist=[]
listcity=[]
listmonth=[]
listdate=[]
listweekday=[]

def myfunction(ss4,destid4):
    
    for checkin in range(1669824000,1669824000+2592000,86400):
        url="https://www.booking.com/searchresults.zh-tw.html?ss="+ss4+"&ssne="+ss4+"&ssne_untouched="+ss4+"&label=gen173nr-1DCAEoggI46AdIMFgEaOcBiAEBmAEwuAEXyAEM2AED6AEB-AECiAIBqAIDuALj4ZSbBsACAdICJGRjNmM3OWY5LWYzM2EtNGQ1MC1hZjU2LWJkZTU2OTFmZDE0M9gCBOACAQ&aid=304142&lang=zh-tw&sb=1&src_elem=sb&src=searchresults&dest_id="+destid4+"&dest_type=city&checkin=2022-12-01&checkout=2022-12-02&group_adults=2&no_rooms=1&group_children=1&age=2&sb_travel_purpose=leisure" 

        payLoad={"ss":ss4,
                     "ssne":ss4,
                     "ssne_untouched":ss4,
                     "efdco":"1",
                     "label": "gen173nr-1DCAEoggI46AdIM1gEaOcBiAEBmAEwuAEXyAEM2AED6AEBiAIBqAIDuAKW0o2bBsACAdICJDgyMzBkNmI5LTdjMTYtNGQ1My1hYzEwLThiYzA4MmEzYTdjZdgCBOACAQ",
                     "sid": "5707e60145567e07f32271b8385e2b2a",
                     "aid": "304142",
                     "lang": "zh-tw",
                     "sb":"1",
                     "src_elem": "sb",
                     "src":"searchresults",
                     "dest_id":destid4,
                     "dest_type":"city",
                     "checkin":time.strftime("%Y-%m-%d",time.localtime(checkin)),
                     "checkout":time.strftime("%Y-%m-%d",time.localtime(checkin+86400)),
                     "group_adults":"2",
                     "no_rooms":"1",
                     "group_children":"1",
                     "age":"2",
                     "sb_travel_purpose":"leisure"
                     }
                                 
            #url2=quote(url,safe='=?~()*!.\:/&')
            #url3=url2
        r = requests.post(url,headers=myheader,data=payLoad)
        r.encoding = 'utf-8'
        if r.status_code==200:
            #print(r.status_code)
            #temp=r.text
            soup=BeautifulSoup(r.text,"html.parser")
            titles=soup.select("div.dd023375f5 h3.a4225678b2 a div.fcab3ed991")
            rooms=soup.select("div.d22a7c133b span.df597226dd")
            ratings=soup.select("div.b5cd09854e.d10a6220b4")
            num_ppls=soup.select("div.d8eab2cf7f.c90c0a70d3.db63693c62")
            prices=soup.select("div.ca5bcdc79a.e702eddf3f span.fcab3ed991.bd73d13072")
            locations=soup.select("div.a1fbd102d9 a.fc63351294:first-child")
            for i,(title,room,rating,ppl,price,location,city) in enumerate(zip(titles,rooms,ratings,num_ppls,prices,locations)):
                print(str(i+1)+":")
                rowlist.append(i+1)
                print(time.strftime("%Y-%m-%d",time.localtime(checkin)))
                listcheckin.append((time.strftime("%Y-%m-%d",time.localtime(checkin))))
                listmonth.append((time.strftime("%Y-%m-%d",time.localtime(checkin))).split("-")[1])
                listdate.append((time.strftime("%Y-%m-%d",time.localtime(checkin))).split("-")[2])
                print(time.strftime("%Y-%m-%d",time.localtime(checkin+86400)))
                listcheckout.append((time.strftime("%Y-%m-%d",time.localtime(checkin+86400))))
                listweekday.append((datetime.datetime.fromtimestamp(checkin)).strftime('%A'))
                print(title.text)
                listtitles.append(title.text)
                print(room.text)
                listrooms.append(room.text)
                print(rating.text)
                listratings.append(rating.text)
                print(ppl.text[:-3])
                listnum_ppls.append(ppl.text[:-3])
                print(price.text[4:])
                listprices.append(price.text[4:])
                print(location.text.split("顯")[0])
                listlocations.append(location.text.split("顯")[0])
               
             
              
myfunction("宜蘭市","900048295")
myfunction("花蓮市","-2631690")
myfunction("台東市","-2637928")
myfunction("屏東市","-2635731")
myfunction("高雄市","-2632378")
myfunction("台南市","-2637868")
myfunction("嘉義市","-2627339")
myfunction("彰化市","-2627038")
myfunction("台中市","-2637824")
myfunction("苗栗市","-2634235")
myfunction("新竹市","900049575")


a=({"row":rowlist,
                             "checkin":listcheckin,
                             "checkout":listcheckout,
                             "hotel":listtitles,
                             "room":listrooms,
                             "rating":listratings,
                             "rate_ppl":listnum_ppls,
                             "price":listprices,
                             "location":listlocations,
                             "city":listcity,
                             "checkoutm":listmonth,
                             "checkoutd":listdate,
                             "weekday":listweekday
                             })
df= pd.DataFrame.from_dict(a, orient='index')
booking_df1 = df.transpose()

booking_df1.to_csv("D:/Alvin老師爬蟲課程/FinalProject/booking_combine.csv")
