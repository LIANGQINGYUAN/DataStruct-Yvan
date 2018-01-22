# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 19:53:27 2018

@author: liang
"""

'''
桶排序
'''
def bucket(datalist):
    #设置桶的大小
    buckets = [0] * ((max(datalist) - min(datalist))+1)
    #设置桶中元素的值
    for i in range(len(datalist)):
        buckets[datalist[i]-min(datalist)] += 1
    #将桶中元素存到B，此时B有序
    B=[]
    for i in range(len(buckets)):
        if buckets[i] != 0:
            B += [i+min(datalist)]*buckets[i]
    return B
        
'''
计数排序
'''
def CountSort(datalist):
    #最终排好序的数组
    B=[0]*len(datalist)
    
    #计算用来存储计数的数组C的长度
    maxNum=max(datalist)
    minNum=min(datalist)
    cLength=maxNum-minNum+1
    buckets=[0]*cLength
    #将原数组中数字出现的次数存储到C中
    for i in range(len(datalist)):
        #datalist[i]-min表示datalist中下标为i的值应该放到C中哪个位置去
        buckets[datalist[i]-minNum]+=1

    #将C中数组元素的值（每个值出现的次数）加上前一个数字出现的次数
    for i in range(1,cLength):
        buckets[i]+=buckets[i-1]

    #遍历A中元素，将它放入B中最终应该在的位置
    for i in range(len(datalist)):
        #C[datalist[i]-minNum]表示截止datalist[i]，小于等于datalist[i]的有多少
        B[buckets[datalist[i]-minNum]-1]=datalist[i]
        #c中记录的值得数量应该减1，因为那个对应的元素已经到B里面了
        buckets[datalist[i]-minNum]-=1
    
    return B




'''打印函数'''
def print_data(data):
    for i in data:
        print(i,end=' ')
    print()         
    
if __name__=='__main__':
    #计数排序
    data=[4,-1,0,3,3]
    B=CountSort(data)
    print_data(B)
    
    #桶排序
    res=bucket(data)
    print_data(res)
    
