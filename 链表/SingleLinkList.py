# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class SingleLinkedList(object):

    '''初始化链表'''
    def __init__(self):
        self.head=Node(None)


    '''链表增加元素'''    
    def append(self,data):
        node=Node(data)
        pre=self.head
        while pre.next:
            pre=pre.next
        pre.next=node

    '''打印链表'''
    def show(self):
        pre=self.head.next
        while pre:
            print(pre.data,end=' ')
            pre=pre.next
        print()

    ''''获取链表长度'''
    def __len__(self):
        length=0
        pre=self.head.next
        while pre:
            length+=1
            pre=pre.next
        return length

    '''插入元素'''
    def insert(self,index,data):
        '''index转换'''
        '''
        插入的时候方便操作
        如有 1 2 3 4 链表
        插入-2位置相当于插入到index=4的位置
        插入-3位置相当于插入到index=3的位置
        '''
        if index<0: 
            index=len(self)+2-abs(index)


        if (index>len(self)+1):
            return False
        node=Node(data)
        pre = self.head
        while index-2>=0:
            pre=pre.next
            index-=1
        temp=pre.next
        pre.next=node
        node.next=temp

    ''''删除元素'''
    def delete(self,index):
        '''
        index转换
        这里是len(self)+1-abs(index)
        和insert不同
        '''

        if index<0: 
            index=len(self)+1-abs(index)

        pre = self.head        
        while index-2>=0:
            pre=pre.next
            index-=1
        temp=pre.next
        pre.next=temp.next

    '''获取节点'''
    def get(self,index):
        '''
        index转换
        这里是len(self)+1-abs(index)
        和insert不同
        '''
        if index<0: 
            index=len(self)+1-abs(index)

        if(index>len(self)):
            print('index error for get')
            return 
        pre = self.head
        while index>0:
            pre=pre.next
            index-=1
        print(pre.data)




sl=SingleLinkedList()
sl.append(1)
sl.append(2)
sl.append(3)
sl.show()
sl.insert(4,5)
sl.show()
sl.insert(-2,10)
sl.show()
sl.delete(2)
sl.show()
sl.delete(-2)
sl.show()
sl.get(-2)