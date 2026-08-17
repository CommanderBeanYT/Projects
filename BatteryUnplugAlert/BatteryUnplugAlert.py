# Gives a notification when your charger is unplugged
# Run pythonw BatterAlert.py to run in the background
# Run taskkill /IM pythonw.exe /F to end the program
import psutil, time
from plyer import notification

unplugged = False
accepted = False

while not accepted:
    checkFrequency = input("How often the status of your charger will be checked in seconds: ")
    try:
        checkFrequency = float(checkFrequency)
        if checkFrequency > 0:
            print(f"Your charger will now be checked every {checkFrequency} seconds.")
            accepted = True
        else:
            print("Number must be positive")
    except ValueError:
        print("Please enter a number")

while True:
    time.sleep(checkFrequency)
    # Check if it is plugged in
    if unplugged == False and psutil.sensors_battery().power_plugged == False:
        # make sure it doesn't send the notification every 12 seconds!
        unplugged = True
        #notify user
        notification.notify(
            title = 'Warning!',
            message = "Someone has unplugged your charger",
            app_icon = None,
            timeout = 10,
        )
    # If it is plugged in again allow the notification to be send again
    if psutil.sensors_battery().power_plugged:
        unplugged = False
