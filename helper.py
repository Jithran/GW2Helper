# Install tesseract: https://github.com/tesseract-ocr/tesseract/wiki

import re
import time
from random import randint

import pyautogui
import pytesseract
from PIL import Image, ImageOps

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def check_health():
    health = pyautogui.screenshot(region=(930, 990, 60, 50))
    health.save("Screenshot.png")

    grayimg = Image.open('Screenshot.png').convert('RGB')
    grayimg = ImageOps.invert(grayimg)
    grayimg.save('gray.png')

    # Simple image to string
    text = pytesseract.image_to_string(grayimg)
    s_heath = re.sub('[^0-9]', '', text)

    if s_heath != "":
        i_health = int(s_heath)
        print(i_health)

        if i_health < 4000:
            do_mouse_click(1040, 1030)
            do_mouse_click(720, 1030)
            print('press key')

        return 1
    else:
        return -1


def do_mouse_click(x, y):

    # recalculate int for random click box
    x = randint(x - 20, x + 20)
    y = randint(y - 20, y + 20)

    xx, yy = pyautogui.position()
    pyautogui.click(x, y)
    pyautogui.moveTo(900, 500)
    pyautogui.moveTo(xx, yy)


try:
    i = 0
    modulus = 1
    while True:
        i = i+1
        rtnHealth = check_health()
        time.sleep(0.5)

        if i % modulus == 0 and rtnHealth == 1:
            do_mouse_click(660, 1030)
            modulus = randint(8, 20)
except KeyboardInterrupt:
    print("abort")


# logging.info('Start timer, shutdown after 3600 sec')
# time.sleep(3600)
# os.system("shutdown -s -f -t 60")
