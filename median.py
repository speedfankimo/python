def median(X):
  x= sorted(X)
  print x
  counts = len(x)
  mid = counts /2.0
  #print x
  #print counts
  #print mid
  if len(x)%2 != 0:  #odd
    index = len(x)//2 # // 代表只取整除 - 返回商的整数部分
    return x[index]
  elif len(x)%2 == 0:  #even
    index_1=len(x)//2-1
    index_2=len(x)//2
    med = x[index_1]+x[index_2] / 2.0 # 除2.0表示需要小數點位
    return med
  
print median([5,4,6,7,1,99,7,5,14,5])  
