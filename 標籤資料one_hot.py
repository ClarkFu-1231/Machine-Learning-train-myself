import numpy as np
#one_hot_encoding(欲編碼陣列,非類數)
def one_hot_encoding(raw, num):
    result = []
    for ele in raw:
        arr = np.zeros(num)
        np.put(arr, ele, 1)
        result.append(arr)
        
    return np.array(result)
#digits是欲編碼的數字標籤陣列
digits = np.array([1, 8, 5, 4])

one_hot = one_hot_encoding(digits, 10)
print(digits)
print(one_hot)