# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:58:35 2018

@author: liang
"""

import math

'''
基排序
BaseSort将数据的负数分开分别使用基排序
sort为实际排序方法
'''
#分开数据
def RadixSort(a):
    a_minus=[]
    a_positive=[]
    for i in range(len(a)):
        if a[i]<0:
            a_minus.append(abs( a[i]))
        else:
            a_positive.append(a[i])

    a=[]
    if len(a_minus)>0:
        a_minus=sort(a_minus)
        a_minus.reverse()
        a_minus=[i*(-1) for i in a_minus]
        a.extend(a_minus)
    if len(a_positive)>0:  
        a_positive=sort(a_positive)
        a.extend(a_positive)
    
    return a
#排序方法
def sort(a,radix=10):
    K = int(math.ceil(math.log(max(a)+1, radix))) # 最大的数用几位数表示，如91用两位数表示
    bucket = [[] for i in range(radix)] # 不能用 [[]]*radix
    bucketBack = [] #桶的缓存，便于观察桶中元素的变化
    for i in range(1, K+1): # K次循环,如两次循环的话，先将个位排序，在排序10位数
        for val in a:            
            temp=int(val%(radix**i)/(radix**(i-1)))
            print(temp,end=' ')  
            bucket[temp].append(val) # 获得整數第K位數字 （从低到高），如91，先看个位数是1
        print()
        del a[:]
    
        for each in bucket:
            a.extend(each)
        
        
        bucketBack.append(bucket)#将目前桶中元素存储起来
        bucket = [[] for i in range(radix)]#清空当前桶，便于下一次入桶
    return a

"""a为整数列表， radix为基数"""
a=[-12,-2,-20,10,200,-155,10000]
a=RadixSort(a)