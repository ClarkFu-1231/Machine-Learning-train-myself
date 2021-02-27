import numpy as np
#正規化
def normalization(raw):
    max_value = max(raw)
    min_value = min(raw)
    norm = [(float(i)-min_value)/(max_value-min_value) for i in raw]
    return norm
#變數X是樣本資料陣列其範圍0~255
x = np.array([255, 128, 45, 0])

print(x)#原始資料
norm = normalization(x)
print(norm)#呼叫normalization()函數式
print(x/255)#除以255
print('--'*20)

#標準化
from scipy.stats import zscore

#變數X是樣本資料陣列其範圍0~255
x = np.array([255, 128, 45, 0])

z_score = zscore(x)
print(z_score)

print(zscore([[1,2,3],
              [6,7,8]], axis= 1))