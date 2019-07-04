import sys
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

# コマンドライン引数にcsvの名前入れる
csv_file = sys.argv[1]
print(csv_file)

# データ読み込み
df = pd.read_csv("./csv_logs/" + csv_file)

# ある閾値以下のものはカット
divide = 30
df = df[
    (df["data#1"] > divide)
    & (df["data#2"] > divide)
    & (df["data#3"] > divide)
    & (df["data#4"] > divide)
    & (df["data#5"] > divide)
    & (df["data#6"] > divide)
    & (df["data#7"] > divide)
    & (df["data#8"] > divide)
    & (df["data#9"] > divide)
    & (df["data#10"] > divide)
    & (df["data#11"] > divide)
    & (df["data#12"] > divide)
    & (df["data#13"] > divide)
    & (df["data#14"] > divide)
    & (df["data#15"] > divide)
    & (df["data#16"] > divide)
    & (df["data#17"] > divide)
    & (df["data#18"] > divide)
]


list_data = [
    "data#1",
    "data#2",
    "data#3",
    "data#4",
    "data#5",
    "data#6",
    "data#7",
    "data#8",
    "data#9",
    "data#10",
    "data#11",
    "data#12",
    "data#13",
    "data#14",
    "data#15",
    "data#16",
    "data#17",
    "data#18",
]

list_threshould = [
    244,
    165,
    139,
    97,
    182,
    132,
    101,
    71,
    118,
    146,
    133,
    79,
    125,
    95,
    58,
    48,
    53,
    39,
]

# flag テスト用
flag = 0
# countの値が3以上だったら入庫判定
count = 0
for index, item in df.iterrows():
    for i in range(18):
        if item[list_data[i]] > list_threshould[i]:
            count += 1

    if count >= 3:
        print("入庫")
    else:
        print("出庫")

    count = 0

    # テストのため10行だけ実行
    flag += 1
    if flag > 10:
        break

