import pyautogui
import webbrowser as web 
from time import sleep
import sys

# ------
# You have to login to the Whatsapp web on your browsers before you could run this file
# ------ 

web.open("https://web.whatsapp.com/send?phone=+13125######") # change your friend's number
sleep(10)

pyautogui.typewrite("Hello,  this is a test message, sent from python")
pyautogui.press("enter")

'''
# If you want to send message using a text file
with open("message.txt","r") as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
'''
