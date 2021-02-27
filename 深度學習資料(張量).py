import numpy as np 

#0D張量
x = np.array(10.5)#純量值
print(x)
print(x.ndim)#軸數是0(ndim屬性)
print('--'*20)#--------------
#1D張量(一維陣列)
x = np.array([1.5, 6.6, 8.6])#純量值
print(x)
print(x.ndim)#軸數是1(ndim屬性)
print('--'*20)#--------------
#2D張量(二維陣列)
x = np.array([[1.5, 6.6, 8.3],
             [2.5, 7.6, 8.6],
             [3.5, 5.6, 2.6]])#純量值
print(x)
print(x.ndim)#軸數是2(ndim屬性)
print(x.shape)#顯示形狀(shpae屬性)
print('--'*20)#--------------
#3D張量(三維陣列):擁有時間間距
x = np.array([[[1.5, 6.6, 8.3],
               [2.5, 7.6, 8.6]],
              [[5.5, 6.6, 8.3],
               [12.5, 7.6, 8.6]],
              [[61.5, 6.6, 8.3],
               [2.5, 7.6, 8.6]]])#純量值
print(x)
print(x.ndim)#軸數是3(ndim屬性)
print(x.shape)#顯示形狀(shpae屬性)
print('--'*20)#--------------
#張量運算
a = np.array([[1,2],[3,4]])
print("a=")
print(a)
s = np.array([[5,6],[7,8]])
print('s=')
print(s)
b = a+s
print('a+s=')
print(b)
b = a-s
print('a-s=')
print(b)
b = a*s
print('a*s=')
print(b)
b = a/s
print('a/s=')
print(b)
print('--'*20)#-----
#點積運算
a = np.array([[1,2],[3,4]])
print("a=")
print(a)
s = np.array([[5,6],[7,8]])
print('s=')
print(s)
b = a.dot(s)
print('a.dot(s)=')
print(b)
print('--'*20)