import numpy as np
import matplotlib.pyplot as plt
#L()和dL()分別是L(w)函數和其微分
def L(w):
    return w*w
def dL(w):
    return 2*w
#梯度下降法gradient_descent(起點、微分函式名稱、學習率、走幾步的訓練週期)函式
def gradient_descent(w_start, df, lr, epochs):
    w_gd = []#使用清單保留每一步計算的新位址
    w_gd.append(w_start)
    pre_w = w_start
    #使用for 迴圈重複部署來計算下一個梯度的下降位子
    for i in range(epochs):
        w = pre_w - lr*df(pre_w)
        w_gd.append(w)
        pre_w = w
    return np.array(w_gd)

w0 = 5
epochs = 5 
lr =0.4
w_gd = gradient_descent(w0, dL, lr, epochs)
print(w_gd)    

t = np.arange(-5.5, 5.5, 0.01)
plt.plot(t, L(t), c='b')
plt.plot(w_gd, L(w_gd), c='r', label='lr={}'.format(lr))
plt.scatter(w_gd, L(w_gd), c='r')
plt.lengend()
plt.show()    