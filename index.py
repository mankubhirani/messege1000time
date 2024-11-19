import pyautogui
import time

# Message details
message = "Hi dear dost, enter your custom message here!"
repeat_count = 1000  # Kitni baar message bhejna hai

# Delay for preparation
print("Prepare WhatsApp Web. You have 5 seconds...")
time.sleep(5)

# Send messages
for i in range(repeat_count):
    pyautogui.typewrite(message)  # Message type karega
    pyautogui.press("enter")  # Enter press karega message bhejne ke liye
    time.sleep(0.2)  # Thoda delay daalo taaki process smooth chale

print("Messages sent successfully!")
