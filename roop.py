#!/usr/bin/python
# coding: UTF-8

import os
import paramiko
import scp
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys
import numpy as np

CSV_NAME = "peasy_v2_result.csv"
# TARGET_IP = "192.168.20.11" # nikaie
# TARGET_IP = "192.168.225.5" # yoyogi
TARGET_IP = "192.168.13.19"  # huawei


def get_power_bin_file():
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh.connect(hostname=TARGET_IP, port=2022, username='pipi', password='xtonedocomo')
        ssh.connect(hostname=TARGET_IP, username="pipi", password="xtonedocomo")
        # scp clientオブジェクト生成
        with scp.SCPClient(ssh.get_transport()) as myscp:
            myscp.get("log/" + CSV_NAME, CSV_NAME)


#入出庫判定 ENTRY:入庫 EXIT:出庫 ERROR:エラー
def judge_entry_or_exit(data):
    error_flag = "ERROR"
    for i in range(len(data)):
        if data[i] > 30:
            error_flag = "OK"
            break
    
    if error_flag == "ERROR":
        return "ERROR"
    else:
        



    


# センサーの閾値
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


if __name__ == "__main__":
    if len(sys.argv) == 2:
        CSV_NAME = sys.argv[1]

    print(CSV_NAME)

    get_power_bin_file()
    df = pd.read_csv(CSV_NAME, header=None)
    data = df.iloc[0].tolist()
    label = [
        "15cm~17cm",
        "17cm~20cm",
        "20cm~22cm",
        "22cm~25cm",
        "25cm~27cm",
        "27cm~30cm",
        "30cm~32cm",
        "32cm~35cm",
        "35cm~37cm",
        "37cm~40cm",
        "40cm~42cm",
        "42cm~45cm",
        "45cm~47cm",
        "47cm~50cm",
        "50cm~52cm",
        "52cm~55cm",
        "55cm~57cm",
        "57cm~60cm",
    ]

    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    xi = 0
    x = [xi]
    y = []
    lines = []
    for i in range(len(data)):
        y.append([data[i]])
        line_tmp, = ax.plot(0, data[i], label=label[i], color=cm.jet(i / len(data)))
        lines.append(line_tmp)
    fig.legend()
    plt.ylim(0, 0)
    plt.pause(1)

    while True:
        # data再取得
        try:
            get_power_bin_file()
        except:
            print("except at %d" % xi)
            continue
        df = pd.read_csv(CSV_NAME, header=None)
        data = df.iloc[0].tolist()

        xi += 1
        x.append(xi)
        for i in range(len(data)):
            y[i].append(data[i])
            lines[i].set_xdata(x)
            lines[i].set_ydata(y[i])

        if xi > 10:
            xmin = xi - 10
        else:
            xmin = 0
        tmp_y = np.array(y)
        ax.set_xlim((xmin, x[-1]))
        ax.set_ylim((tmp_y[0:, xmin:].min(), tmp_y[0:, xmin:].max()))

        plt.pause(1)
        plt.draw()

        print(data[0])
        for i in range(len(data)):
            print(data[i])

        judge_entry_or_exit(data)

        #
