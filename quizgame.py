import utime
from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 16

start_button = Pin(20, Pin.IN, Pin.PULL_UP)
true_button = Pin(19, Pin.IN, Pin.PULL_UP)
false_button = Pin(18, Pin.IN, Pin.PULL_UP)

i2c = I2C(0, sda=machine.Pin(16), scl=machine.Pin(17), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.hide_cursor()

# Read questions into a list
with open("quizfile.txt", 'r') as file:
    questions = file.readlines()

while True:
    lcd.clear()
    lcd.putstr("True or False")
    lcd.move_to(0,1)
    lcd.putstr("Press Start ...")
    
    while True:
        if (start_button.value() == 0):
            break
    # Quiz start
    score = 0
    for question in questions:
        lcd.clear()
        # strip off any whitespace
        # then split the entries into line1, 2 and answer
        (text, text2, answer) = question.strip().split(";", 3)
        lcd.putstr(text)
        lcd.move_to(0,1)
        lcd.putstr(text2)
        while True:
            if (true_button.value() == 0):
                if (answer == "T"):
                    score += 1
                break
            if (false_button.value() == 0):
                if (answer == "F"):
                    score += 1
                break
    lcd.clear()
    lcd.putstr("Game over")
    lcd.move_to(0,1)
    lcd.putstr("Score {} of {}".format(score, len(questions)))
    utime.sleep(5)