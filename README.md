# DataStruct-Yvan
数据结构学习笔记  
## 链表  
实现时需要注意  
1. 数组游标的确定：因为python可以直接用arr[-2]访问倒数第二个数组元素，所以我们需要在操作的时候需要先把游标统一。  
可以使用以下代码转换：  
```
index=len(arr)-abs(index)+1
```
假设arr中有4个元素时，访问游标为-2的元素也就是访问第3个元素，也就是4-abs(-2)+1=3.  

2. 一般实现顺序：先实现元素增加（append）、获取等功能。  

3. 注意插入操作和删除操作链表指向的顺序。

[具体代码](https://github.com/LIANGQINGYUAN/DataStruct_Notes/tree/master/%E9%93%BE%E8%A1%A8)

## 排序算法：
>排序算法分为比较排序和非比较排序  

基于比较的排序算法有：  
[冒泡排序，选择排序，快速排序，插入排序，希尔排序，归并排序](https://github.com/LIANGQINGYUAN/DataStruct-Yvan/tree/master/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95/%E5%9F%BA%E4%BA%8E%E6%AF%94%E8%BE%83%EF%BC%88%E5%86%92%E6%B3%A1%E3%80%81%E9%80%89%E6%8B%A9%E3%80%81%E5%BF%AB%E9%80%9F%E3%80%81%E6%8F%92%E5%85%A5%E3%80%81%E5%B8%8C%E5%B0%94%E3%80%81%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F%EF%BC%89)

非基于比较的排序算法有：  
[计数排序，基数排序，桶排序](https://github.com/LIANGQINGYUAN/DataStruct-Yvan/tree/master/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95/%E9%9D%9E%E5%9F%BA%E4%BA%8E%E6%AF%94%E8%BE%83%EF%BC%88%E6%A1%B6%E3%80%81%E8%AE%A1%E6%95%B0%E3%80%81%E5%9F%BA%E6%95%B0%E6%8E%92%E5%BA%8F%EF%BC%89)
   
