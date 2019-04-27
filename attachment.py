import time
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']




def gettime():
    return int(round(time.time()*1000))

def getinfo_year():
    headers={}
    keyvalue = {}
    url = 'http://data.stats.gov.cn/easyquery.htm?cn=C01'
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    keyvalue['m'] = 'QueryData'
    keyvalue['dbcode'] = 'hgnd'
    keyvalue['rowcode'] = 'zb'
    keyvalue['colcode'] = 'sj'
    keyvalue['wds'] = '[]'
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A0301"}]'
    keyvalue['k1'] = str(gettime())
    return url,headers,keyvalue


#整理数据
def webinfo(stats,kind):
    stats_info=[]
    for i in range (0,20):
        list=[]
        list.append(str(i+1999))
        for k in range(0,kind):
            list.append((stats[20*(k+1)-1-i])['data']['data'])
        stats_info.append(list)
    return stats_info



def  draw_task1(info):
    year_list = []
    data_list = []
    male_prop = []
    female_prop = []

    for item in info:
        year_list.append(item[0])
        data_list.append(item[1])
        male_prop.append(item[2] / item[1])
        female_prop.append(item[3] / item[1])
    #     绘制年份—年末总人口条状图
    plt.figure(figsize=(18, 6))
    plt.subplot(1, 2, 1)
    plt.title("年末总人口条形图")
    plt.bar(range(len(year_list)), data_list, tick_label=year_list)
    plt.ylabel('年末总人口数/万人')
    plt.xlabel('年份')
    plt.legend()

    #     绘制男女人口占比折线图
    plt.subplot(1, 2, 2)
    x = range(len(year_list))
    plt.title("男性和女性人口占比折线图")
    plt.plot(year_list, male_prop, label='男性', color='b')
    plt.plot(year_list, female_prop, label='女性', color='r')
    plt.xticks(np.arange(1999, 2019, 1), rotation=45)
    plt.xlabel("年份")
    plt.ylabel('占比')
    plt.legend()
    plt.grid()

    plt.show()


def draw_task2(info):
    year_list = []
    GNI_list = []
    GDP_list = []
    PRI_list = []
    SEC_list = []
    TER_list = []
    per_list = []
    for item in info:
        year_list.append(item[0])
        GNI_list.append(item[1])
        GDP_list.append(item[2])
        PRI_list.append(item[3])
        SEC_list.append(item[4])
        TER_list.append(item[5])
        per_list.append(item[6])


    # 绘图
    # 并列柱状图
    plt.figure(figsize=(14,8))
    plt.subplot(2,1,2)
    plt.title("GNI、GDP及各产业生产总值")
    x=np.linspace(1,42,20)
    plt.bar(x,GNI_list,width=0.3,color='orange',align='center',label='GNI')
    plt.bar(x+0.3,GNI_list,width=0.3,color='skyblue',align='center',label='GDP',tick_label=year_list)
    plt.bar(x+0.6,PRI_list,width=0.3,color='plum',align='center',label='GDP')
    plt.bar(x + 0.9, SEC_list, width =0.3, color='lightcoral', align='center', label='SEC')
    plt.bar(x + 1.2, TER_list, width = 0.3, color='c', align='center', label='TER')
    plt.xlabel('年份')
    plt.ylabel('数据值/亿元')
    plt.legend()

    #2018年三大产业生产总值饼状图
    plt.subplot(2,2,1)
    plt.title('2018年三大产业生产总值')
    labels=['第一产业','第二产业','第三产业']           #定义标签
    size=[PRI_list[-1],SEC_list[-1],TER_list[-1]]      #数据值
    colors=['lightcoral','orange','skyblue']           #颜色
    explode=(0.01,0.02,0.2)
    plt.pie(size,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%')
    plt.legend()

    #GDP与GIN
    plt.subplot(2,2,2)
    plt.title('中国20年来人均国内生产总值')
    plt.plot(year_list,per_list,color='b',label='人均国内生产总值')
    plt.xticks(np.arange(1999,2019,1),rotation=40)
    plt.xlabel('年份')
    plt.ylabel('总值/亿元')
    plt.grid()
    plt.legend()


    plt.show()














