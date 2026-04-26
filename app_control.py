# -*- coding: utf-8 -*-
import pyperclip
import pyautogui
import pygetwindow as gw
import time
import random
import os

class AppControl:
    def __init__(self, app_name):
        self.app_name = app_name

    def is_app_running(self):
        windows = gw.getWindowsWithTitle(self.app_name)
        return len(windows) > 0

    def start_app(self):
        if not self.is_app_running():
            os.system(f"start {self.app_name}")  # 假设是exe或快捷方式
            time.sleep(5)  # 等待启动

    def click_at(self, x, y):
        # 随机化坐标
        offset = random.randint(-5, 5)
        pyautogui.click(x + offset, y + offset)
        time.sleep(random.uniform(0.5, 2.0))

    def type_message(self, message):
        pyautogui.typewrite(message, interval=random.uniform(0.1, 0.3))
        pyautogui.press("enter")

    # 其他方法如找到好友窗口等，需要根据UI定制
