# -*- coding: utf-8 -*-
import json
from task_scheduler import TaskScheduler

def main():
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    scheduler = TaskScheduler(config)
    scheduler.run()

if __name__ == "__main__":
    main()
