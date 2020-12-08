import ctypes
import time

user32 = ctypes.windll.user32

# Repeat indefinetely
while True:
    user32.keybd_event(0x29, 0, 0x0002, 0) # Space Bar down
    time.sleep(1)
    user32.keybd_event(0x29, 0, 0, 0) # Space Bar Up
    time.sleep(1

#fin