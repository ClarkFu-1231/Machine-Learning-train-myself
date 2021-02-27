### 內建函數
#---(1)整數練習
#宣告一個整數
a=100
print(a)
print('型態',type(a))
print('-'*30)
#宣告另一個整數
b=200
print(b)
print('型態',type(b))
print('-'*30)

print('a和b是否是同一個物件',a is b)

#---(2)整數練習
import sys
#宣告一個整數
c=123456789123456890
print(c)
print('物建大小',sys.getsizeof(c))
print('-'*30)
#宣告另一個整數
d=12345678912345689012342451235
print(d)
print('物件大小',sys.getsizeof(d))
print('-'*30)

#---(3)浮點數練習
#宣告一個浮點數
e=100.1234
print('e=',e)
print('物件大小',sys.getsizeof(e))
print('-'*30)
#宣告另一個浮點數
e=100.1234
print('e=',e)
print('型態',type(e))
print('物件大小',sys.getsizeof(e))
print('-'*30)
# 宣告另一個浮點數
f=1234567890123456789012345.1234567890123456789012345
print(f)
print('型態:', type(f))
print('物件大小', sys.getsizeof(f))
print('-'*30)
#宣告一個整數
g=int(e)
print(g)
print('型態:', type(g))
print('物件大小', sys.getsizeof(g))
print('-'*30)

#---(4)str 宣告字串
#宣告一個字串
a='hello'
print(a)
print(type(a))
print('-'*30)
#宣告另一個字串
b='你好'
print(b)
print(type(b))
print('-'*30)
#字串相加
c=a+b
print(c)
print('-'*30)
#取出字串中每個長度為1的字串
for c in a:
    print(c)
print('-'*30)
#---(5)boolean 
#宣告一個布林
a=True
print(a)
print(type(a))
print('-'*30)
#宣告另一個布林
b=False
print(b)
print(type(b))
print('-'*30)
#一個邏輯運算結果
c=10>20 or 20<=30
print(c)
print('-'*30)