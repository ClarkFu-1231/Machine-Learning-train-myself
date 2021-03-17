'''使用全部訓練資料'''
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
np.random.seed(7)#亂數種子
'''匯入資料集'''
df = pd.read_csv("./boston_data.csv")
dataset = df.values
np.random.shuffle(dataset)

'''資料預處理'''
X = dataset[:, 0:13]
Y = dataset[:, 13]
X -= X.mean(axis=0)
X /= X.std(axis=0)
X_train, Y_train = X[:283], Y[:283]  #訓練資料
X_test, Y_test = X[283:], Y[283:]  #測試資料

'''建立模型'''
def build_model():
    model = Sequential()
    model.add(Dense(32, input_shape=(X_train.shape[1], ),
                    activation="relu"))
    model.add(Dense(32, activation="relu"))
    model.add(Dense(1))
    model.compile(loss="mse", optimizer="adam", metrics=["mae"])
    return model

'''K-fold交叉驗證'''
k=4
nb_val_samples = len(X_train) //k
np_epochs = 80
mse_scores = []  #每一折的樣本數
mae_scores = []  #訓練週期數
'''利用迴圈紀錄'''
for i in range(k):
    print("Processing Fold #" +str(i))
    X_val = X_train[i*nb_val_samples: (i+1)*nb_val_samples]
    Y_val = Y_train[i*nb_val_samples: (i+1)*nb_val_samples]
    X_train_p = np.concatenate(
            [X_train[:i*nb_val_samples],
             X_train[(i+1)*nb_val_samples:]], axis=0)
    Y_train_p = np.concatenate(
            [Y_train[:i*nb_val_samples],
             Y_train[(i+1)*nb_val_samples:]], axis=0)
    
    model = build_model()
    '''使用全部訓練資料'''
    model.fit(X_train_p, Y_train_p, epochs=80, batch_size=16, verbose=0)
    mse, mae = model.evaluate(X_val, Y_val)
    mse_scores.append(mse)
    mae_scores.append(mae)

print("MSE_val: ", np.mean(mse_scores))
print("MAE_val: ", np.mean(mae_scores))
mse, mae= model.evaluate(X_test, Y_test)
print("MSE_test: ",mse)
print("MAE_test: ",mae)

    
    
