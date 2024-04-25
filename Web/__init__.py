import webbrowser as web
import pyautogui as pyg
import requests


def url_setter(webName, **kwargs):
    if kwargs == True:
    	url = f"https://www.{webName}/"
    elif kwargs != True:
        url = f"https://www.{webName}.com/{kwargs}"
    return url


Input = input("Write the Website Name with (.com / .org / etc)\nand you can add the page name too.")
url = url_getter(Input)

web.open(url)

time.sleep(15)

image = pyg.screenshot("screenshot.png")


