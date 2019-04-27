import requests
import sqlite3
from bs4 import BeautifulSoup
import json
import attachment



if __name__=='__main__':

    #获取网页中指定数据
    url, headers, keyvalue = attachment.getinfo_year()
    keyvalue['dfwds']='[{"wdcode":"zb","valuecode":"A0201"}]'
    s = requests.session()
    r = s.post(url, headers=headers, params=keyvalue)
    keyvalue['dfwds'] ='[{"wdcode":"sj","valuecode":"LAST20"}]'
    r = s.post(url, headers=headers, params=keyvalue)
    hjson=r.json()
    stats = hjson['returndata']['datanodes']
    #整理数据
    stats_sort = attachment.webinfo(stats,6)

    # 建立连接
    conn = sqlite3.connect('economy.db')
    c = conn.cursor()
    # 创建表
    c.execute('create table if not exists user (year text primary key, GNI real,GDP real,PRI real,SEC real,TER real,per real)')

    # 将整理好的数据添加到本地数据库中去
    c.executemany('insert or ignore into user values(?,?,?,?,?,?,?)', stats_sort)
    conn.commit()
    conn.close()

    # 读取数据
    conn = sqlite3.connect('economy.db')
    c = conn.cursor()
    c.execute('select year,GNI,GDP,PRI,SEC,TER,per from user')
    info = c.fetchall()

    attachment.draw_task2(info)












