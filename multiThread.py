# 多核心示範 同一時間執行兩個以上的任務
from concurrent.futures import ThreadPoolExecutor
import time

def JobA():
    for i in range(20):
        print("這是 JobA")
        # time.sleep(1) #暫停一秒

def JobB():
    for i in range(20):
        print("任務 JobB....")
        # time.sleep(1) #暫停一秒

def JobC():
    for i in range(20):
        print("另一種任務這是 ..JobC..")
        # time.sleep(1) #暫停一秒

def JobD():
    for i in range(20):
        print("這是另一種 ....JobD")
        # time.sleep(1) #暫停一秒

# 沒有多執行行續的情況下
JobA()
JobB()
JobC()
JobD()

# 多工版本
# with ThreadPoolExecutor(max_workers=2) as ex:
#     ex.submit(JobA)
#     ex.submit(JobB)
#     ex.submit(JobC)
#     ex.submit(JobD)