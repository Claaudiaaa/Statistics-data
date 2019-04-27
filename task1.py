import requests
import sqlite3
from bs4 import BeautifulSoup
import json
import attachment


if __name__=='__main__':
    #获取网页指定数据
    url, headers, keyvalue=attachment.getinfo_year()
    s=requests.session()
    r=s.post(url,headers=headers,params=keyvalue)
    keyvalue['dfwds']='[{"wdcode":"sj","valuecode":"LAST20"}]'
    r=s.post(url,headers=headers,params=keyvalue)
    hjson=r.json()
    stats=hjson['returndata']['datanodes']
    #整理数据存入list中
    stats_sort = attachment.webinfo(stats,3)

    # 建立连接
    conn=sqlite3.connect('population.db')
    c=conn.cursor()
    # 创建表
    c.execute('create table if not exists user (year text primary key, total int,male int,female int)')
    #将整理好的数据添加到本地数据库中去
    c.executemany('insert or ignore into user values(?,?,?,?)',stats_sort)
    conn.commit()
    conn.close()

    #从数据库中读取信息

    conn = sqlite3.connect('population.db')
    c = conn.cursor()
    c.execute('select year,total,male,female from user')
    info = c.fetchall()


    #绘图
    attachment.draw_task1(info)


















