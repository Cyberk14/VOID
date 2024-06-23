import webbrowser as web
import pyautogui as pyg
from time import sleep

phone_book = {
    "Nasser": "256740941194",
    "DAD": "256755880949",
    "MOM": "256708126618",
    "Joel": "267753097074",
}

nums = phone_book.values()
phone_nums = []
for num in nums:
    num = int(num)
    phone_nums.append(num)

names = phone_book.keys()

messg = []
for name in names:
    text = f"Hello {name}, this is a robot texting you so please calm down as the age of AI has arrived!!!!"
    text = text.replace(" ", "%20")
    messg.append(text)


def main():
    i = 0
    while i != len(messg):
        web.open_new_tab(f"https://wa.me/{phone_nums[i]}?text={messg[i]}")
        sleep(30)
        pyg.press("enter")
        i+=1
    print("The main func is running properly....")


if __name__ == "__main__":
    main()
