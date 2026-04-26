# -*- coding: utf-8 -*-
from plyer import notification

class Notifier:
    def notify(self, title, message):
        notification.notify(
            title=title,
            message=message,
            timeout=10
        )
