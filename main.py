import pyautogui as pyg
import time

time.sleep(2)
screen = pyg.screenshot(allScreens=True)
screen = screen.save("screen.png")

time.sleep(7)
pyg.locateOnScreen("screen.png", grayscale=True)
