# -*- coding: utf-8 -*-
import schedule
import time
import random
from app_control import AppControl
from notifier import Notifier

class TaskScheduler:
    def __init__(self, config):
        self.config = config
        self.app_control = AppControl("QQ")  # 或抖音，根据需要
        self.notifier = Notifier()

    def schedule_tasks(self):
        for slot in self.config["time_slots"]:
            # 1. 分割时间段并去掉空格
            raw_start = slot.split("-")[0].strip()
            # 2. 核心：只保留数字和冒号（防止由于刚才的编码问题残余的各种不可见字符）
            start = "".join(c for c in raw_start if c in "0123456789:")
            
            print(f"正在设置任务，开始时间为: '{start}'") # 增加这一行监控输出
            schedule.every().day.at(start).do(self.perform_task)

    def perform_task(self):
        self.app_control.start_app()
        # 假设找到好友并发送消息
        message = random.choice(self.config["messages"])
        self.app_control.type_message(message)
        self.notifier.notify("任务完成", "已发送续火花消息")

    def run(self):
        self.schedule_tasks()
        while True:
            schedule.run_pending()
            time.sleep(1)
