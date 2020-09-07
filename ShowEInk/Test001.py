import sys
import os
import time
from gpiozero import Button         # import the Button control from gpiozero

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
    
from waveshare_epd import epd2in7
from PIL import Image, ImageDraw, ImageFont


btn1 = Button(5)                    # Button 1 of HAT
btn2 = Button(6)                    # Button 2 of HAT                  
btn3 = Button(13)                   # Button 3 of HAT
btn4 = Button(19)                   # Button 4 of HAT


epd = epd2in7.EPD()
epd.init()
print("Clear---")
epd.Clear(0xFF)


# Print a message on the screen
# @param :  string = text to be shown
def printToDisplay(string):
    HBlackImage = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255)  # 298*126
    print('*****1')
    # Create a draw object and the font object we will use for the display
    draw = ImageDraw.Draw(HBlackImage)
    font1 = ImageFont.truetype('/usr/share/fonts/truetype/google/Bangers-Regular.ttf', 30)
    font2 = ImageFont.truetype('/usr/share/fonts/truetype/google/IndieFlower-Regular.ttf', 30)
    print('*****2')
    # Draw the text to the display. First argument is starting location of the text in pixels
    draw.text((25, 65), string, font = font1, fill = 0)
    print('*****3')
    # Add the images to the display. Both the black and red layers need to be passed in, even
    # if we did not add anything to one of them
    epd.display(epd.getbuffer(HBlackImage))
    print('*****4')
    
# Select a pressed button
def handleBtnPress(btn):
    # Get the button pin number
    pinNum = btn.pin.number
    
    # python hack for a switch statement. The number represents the pin number and
    # the value is the message we will print
    switcher = {
        5: "Hello, World!",
        6: "This is my first \nRPi project.",
        13: "Hope you liked it.",
        19: "Goodbye"
    }

    # Get the string based on the passed in button and send it to printToDisplay()
    msg = switcher.get(btn.pin.number, "Error")
    print('Displaying... ' + msg)
    printToDisplay(msg)
    print('Displayed!')
    
    
while True:
    try:
        # Tell the button what to do when pressed
        btn1.when_pressed = handleBtnPress
        btn2.when_pressed = handleBtnPress
        btn3.when_pressed = handleBtnPress
        btn4.when_pressed = handleBtnPress

        print('waiting...')
        time.sleep(0.5)
    
    except KeyboardInterrupt:    
        #logging.info("ctrl + c:")
        epd2in7.epdconfig.module_exit()
        exit()
