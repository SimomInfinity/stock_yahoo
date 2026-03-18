import schedule
import time
from datetime import datetime

def run_every_10seconds():
    print("每10 秒執行一次")

def run_every_60seconds():
    print("每60 秒執行一次")

def run_at_spec_time():
    now = datetime.now()
    print(f"我要你愛: {now}")

def run_and_cancelJob():
    cnt = True
    if (cnt):
        return schedule.cancel_job

# 只是安排一個任務
schedule.every(10).seconds.do(run_every_10seconds)
# schedule.every(1).minute.do(run_every_60seconds)
# schedule.every().day.at("14:48").do(run_at_spec_time)
# schedule.every().hours.at(":31").do()
# schedule.every().friday.at("16:31").do()

schedule.every(30).seconds.do(run_every_10seconds).until("15:17")
schedule.every().hours.at(":17").do(run_and_cancelJob)

# 隨機一個數值進行觸發
# schedule.every(2).to(10).seconds.do(run_at_spec_time).until("15:00")

while True:
    #要求 schedule 每n單位 檢查一次是否有任務需要執行
    schedule.run_pending()
    time.sleep(1)

