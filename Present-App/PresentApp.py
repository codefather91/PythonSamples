import tkinter as tk
import tkinter.font as font
import ctypes
import time

# Initialise global variable for app start
app_start = 0

# Set DPI awareness for Win10 systems
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Function to simulate space bar press every 1 second
def run_app():
    global app_start
    user32 = ctypes.windll.user32
    while app_start == 1:
        time.sleep(1)
        user32.keybd_event(0x29, 0, 0x0002, 0)
        time.sleep(1)
        user32.keybd_event(0x29, 0, 0, 0)
    return

# Function to start the app on button click
def start_app():
    global app_start
    #status.config(text="Working")
    app_start = 1
    run_app()
    return

# Function to stop the app on button click
def stop_app():
    global app_start
    app_start = 0
    #status.config(text="Ready")
    return

# Main GUI code
def main():
    root = tk.Tk()
    root.geometry('240x240')
    root.title('Present v1')
    root.resizable(False, False)

    mainFrame = tk.Frame(root, bg='gray')
    mainFrame.pack(fill="both", expand=True)

    status = tk.Label(root, text="Use it well!", relief='sunken', anchor=tk.W, bd=1)
    status.pack(side="bottom", fill="x")

    controlBox = tk.Frame(mainFrame)
    controlBox.pack(padx=10, pady=(10, 0), fill="both", expand=True)

    startButton = tk.Button(controlBox, text="START", width=10, font=font.Font(family='Calibri', size=12, weight='bold'),
                          command=start_app)
    startButton.pack(side="left", padx=10, pady=10, expand=True)

    stopButton = tk.Button(controlBox, text="STOP", width=10,
                            font=font.Font(family='Calibri', size=12, weight='bold'), command=stop_app)
    stopButton.pack(side="right", padx=10, pady=10, expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
