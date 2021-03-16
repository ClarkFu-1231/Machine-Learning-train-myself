import pandas as pd

df = pd.read_csv("./diabetes.csv")
"""
9個資料欄位(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome)
"""
print(df.head())
print(df.shape)#shape屬性顯示資料集有幾筆紀錄和幾個欄位，也就是這個資料表的形狀