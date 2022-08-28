import psutil
# pip install py-notifier
# pip install win10toast
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent <= 98 and plugged is not True:
    from pynotifier import Notification
    Notification(
        title="Battery Low",
        description=str(percent) + "% Battery remain!",
        duration=5
    ).send()
