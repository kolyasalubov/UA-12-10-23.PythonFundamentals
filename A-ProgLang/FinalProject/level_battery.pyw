import psutil
import time
from plyer import notification

def show_notification(message):
    notification.notify(
        title='Battery Control',
        message=message,
        timeout=10
    )

def battery_monitor():
    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        power_status = battery.power_plugged

        if power_status:  # Якщо живлення надходить від мережі
            if percent >= 80:
                show_notification('''Battery charge level is more than 80%
                \nIt is necessary to change the power source to a battery''')
        else:  # Якщо працюємо від батареї
            if percent <= 20:
                show_notification('''Battery charge level is less than 20%
                \nIt is necessary to change the power source to the mains''')

        time.sleep(30)  # Перевірка кожні 30 секунд

if __name__ == "__main__":
    battery_monitor()