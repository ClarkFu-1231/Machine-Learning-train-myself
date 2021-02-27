import numpy as np

class Perceptron:#Perceptron類別的AND邏輯感知器
    def __init__(self, input_length, weights=None, bias=None):#建構子初始輸入的數量、權重、偏向量
        if weights is None:
            self.weights = np.ones(input_length) * 1
        else:
            self.weights = weights
        if bias is None:
            self.bias = -1
        else:
            self.bias = bias
            
    @staticmethod
    def activation_function(x):#啟動函數的靜態方法，使用@staticmethod修飾
        if x >0:
            return 1
        return 0
    
    def __call__(self, input_data):#讓物件實力如同函式方式來呼叫
        weighted_input = self.weights * input_data
        weighted_sum = weighted_input.sum() + self.bias
        return Perceptron.activation_function(weighted_sum)
#AND邏輯感知器
print('AND邏輯感知器')
weights = np.array([1, 1])
bias= -1
AND_Gate = Perceptron(2, weights, bias)
    
input_data = [np.array([0, 0]), np.array([0, 1]),
              np.array([1, 0]), np.array([1, 1])]
for x in input_data:
    out = AND_Gate(np.array(x))
    print(x, out)
print('--'*20)#-----------
#OR邏輯感知器
print('OR邏輯感知器')
weights = np.array([1, 1])
bias = -0.5
OR_Gate = Perceptron(2, weights, bias)

input_data = [np.array([0, 0]), np.array([0, 1]),
              np.array([1, 0]), np.array([1, 1])]
for x in input_data:
    out = OR_Gate(np.array(x))
    print(x, out)
print('--'*20)#-----------
