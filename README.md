# pico-lcd-quiz
A true or false quiz game using an LCD display controlled from a Raspberry Pi Pico

# Details of the circuit

For deails of how to connect the ircuit see: http://www.penguintutor.com/projects/true-or-false 

# Game file
Upload the files quizgame.py, lcd_api.py and pico_i2c_lcd.py to your Pico

Add the quiz file and run quizgame.py

# quizfile.txt
Questions should be included in the file quizfile.txt. 
This consists of three fields separated with a semi-colon ;

Field 1 is the text for line 1 of the LCD display
Field 2 is the text for line 2 of the LCD display
Field 3 contains the letter T or F for True or False correct answers


# Library files
This includes the library fiels lcd_api.py and pico_i2c_ldc.py from: https://github.com/T-622/RPI-PICO-I2C-LCD 
These files are not developed in this library and are included for convenience.