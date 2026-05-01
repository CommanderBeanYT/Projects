# Gives a notification when your charger is unplugged
# Run pythonw BatterAlert.py to run in the background
# Run taskkill /IM pythonw.exe /F to end the program

# Import required functions
import psutil
import time
from plyer import notification

unplugged = False

while True:
          time.sleep(12)
          # Check if it is plugged in
          if(unplugged == False and psutil.sensors_battery().power_plugged == False):
                    # make sure it doesn't send the notification every 12 seconds!
                    unplugged = True
                    #notify user
                    notification.notify(
                              title = 'Warning!', 
                              message = "Someone has unpluged your charger",
                              app_icon = None,
                              timeout = 10,
                    )
          # If it is plugged in again allow the notification to be send again
          if(psutil.sensors_battery().power_plugged == True):
                    unplugged = False
