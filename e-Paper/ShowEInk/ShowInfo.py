import sys
import os
import time
from datetime import datetime
from gpiozero import Button         # import the Button control from gpiozero

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
    
from waveshare_epd import epd2in7
from PIL import Image, ImageDraw, ImageFont
import json, urllib.request


if sys.version_info[0] <3:
    raise Exception("Python 3 is the correct version that you NEED!!")

btn1 = Button(5)                    # Button 1 of HAT
btn2 = Button(6)                    # Button 2 of HAT                  
btn3 = Button(13)                   # Button 3 of HAT
btn4 = Button(19)                   # Button 4 of HAT


class ButtonNumber():
    value = 0
    
class TimePressed():
    value = 0


actualButton = 0                    # Last pressed Button
timeToRefesh = 0                    # Time between Button press
timeToRefeshBtn1 = 0                # Time to refresh the Action of Button 1
timeToRefeshBtn2 = 25 #3600             # Time to refresh the Action of Button PeopleInSpace
timeToRefeshBtn3 = 25 #300              # Time to refresh the Action of Button WhereIsIIS
timeToRefeshBtn4 = 3600             # Time to refresh the Action of Button 4

Button.buttonNumber = ButtonNumber()
Button.timePressed = TimePressed()

epd = epd2in7.EPD()
epd.init()
print("Clear---")
epd.Clear(0xFF)

fontBan10 = ImageFont.truetype('/usr/share/fonts/truetype/google/Bangers-Regular.ttf', 10)
fontBan15 = ImageFont.truetype('/usr/share/fonts/truetype/google/Bangers-Regular.ttf', 15)
fontBan20 = ImageFont.truetype('/usr/share/fonts/truetype/google/Bangers-Regular.ttf', 20)
fontBan25 = ImageFont.truetype('/usr/share/fonts/truetype/google/Bangers-Regular.ttf', 25)
fontBan30 = ImageFont.truetype('/usr/share/fonts/truetype/google/Bangers-Regular.ttf', 30)
fontBan50 = ImageFont.truetype('/usr/share/fonts/truetype/google/Bangers-Regular.ttf', 50)

fontIndie10 = ImageFont.truetype('/usr/share/fonts/truetype/google/IndieFlower-Regular.ttf', 10)
fontIndie15 = ImageFont.truetype('/usr/share/fonts/truetype/google/IndieFlower-Regular.ttf', 15)
fontIndie20 = ImageFont.truetype('/usr/share/fonts/truetype/google/IndieFlower-Regular.ttf', 20)
fontIndie25 = ImageFont.truetype('/usr/share/fonts/truetype/google/IndieFlower-Regular.ttf', 25)
fontIndie30 = ImageFont.truetype('/usr/share/fonts/truetype/google/IndieFlower-Regular.ttf', 30)


fontBunIn10 = ImageFont.truetype('/usr/share/fonts/truetype/google/BungeeInline-Regular.ttf', 10)
fontBunIn15 = ImageFont.truetype('/usr/share/fonts/truetype/google/BungeeInline-Regular.ttf', 15)
fontBunIn20 = ImageFont.truetype('/usr/share/fonts/truetype/google/BungeeInline-Regular.ttf', 20)
fontBunIn25 = ImageFont.truetype('/usr/share/fonts/truetype/google/BungeeInline-Regular.ttf', 25)
fontBunIn30 = ImageFont.truetype('/usr/share/fonts/truetype/google/BungeeInline-Regular.ttf', 30)
fontBunOut10 = ImageFont.truetype('/usr/share/fonts/truetype/google/BungeeOutline-Regular.ttf', 10)
fontBunOut15 = ImageFont.truetype('/usr/share/fonts/truetype/google/BungeeOutline-Regular.ttf', 15)
fontBunOut20 = ImageFont.truetype('/usr/share/fonts/truetype/google/BungeeOutline-Regular.ttf', 20)
fontBunOut25 = ImageFont.truetype('/usr/share/fonts/truetype/google/BungeeOutline-Regular.ttf', 25)
fontBunOut30 = ImageFont.truetype('/usr/share/fonts/truetype/google/BungeeOutline-Regular.ttf', 30)
fontBunShad10 = ImageFont.truetype('/usr/share/fonts/truetype/google/BungeeShade-Regular.ttf', 10)
fontBunShad15 = ImageFont.truetype('/usr/share/fonts/truetype/google/BungeeShade-Regular.ttf', 15)
fontBunShad20 = ImageFont.truetype('/usr/share/fonts/truetype/google/BungeeShade-Regular.ttf', 20)
fontBunShad25 = ImageFont.truetype('/usr/share/fonts/truetype/google/BungeeShade-Regular.ttf', 25)
fontBunShad30 = ImageFont.truetype('/usr/share/fonts/truetype/google/BungeeShade-Regular.ttf', 30)
fontJacq10 = ImageFont.truetype('/usr/share/fonts/truetype/google/JacquesFrancoisShadow-Regular.ttf', 10)
fontJacq15 = ImageFont.truetype('/usr/share/fonts/truetype/google/JacquesFrancoisShadow-Regular.ttf', 15)
fontJacq20 = ImageFont.truetype('/usr/share/fonts/truetype/google/JacquesFrancoisShadow-Regular.ttf', 20)
fontJacq25 = ImageFont.truetype('/usr/share/fonts/truetype/google/JacquesFrancoisShadow-Regular.ttf', 25)
fontJacq30 = ImageFont.truetype('/usr/share/fonts/truetype/google/JacquesFrancoisShadow-Regular.ttf', 30)
fontLonOut10 = ImageFont.truetype('/usr/share/fonts/truetype/google/LondrinaOutline-Regular.ttf', 10)
fontLonOut15 = ImageFont.truetype('/usr/share/fonts/truetype/google/LondrinaOutline-Regular.ttf', 15)
fontLonOut20 = ImageFont.truetype('/usr/share/fonts/truetype/google/LondrinaOutline-Regular.ttf', 20)
fontLonOut25 = ImageFont.truetype('/usr/share/fonts/truetype/google/LondrinaOutline-Regular.ttf', 25)
fontLonOut30 = ImageFont.truetype('/usr/share/fonts/truetype/google/LondrinaOutline-Regular.ttf', 30)
fontLonShad10 = ImageFont.truetype('/usr/share/fonts/truetype/google/LondrinaShadow-Regular.ttf', 10)
fontLonShad15 = ImageFont.truetype('/usr/share/fonts/truetype/google/LondrinaShadow-Regular.ttf', 15)
fontLonShad20 = ImageFont.truetype('/usr/share/fonts/truetype/google/LondrinaShadow-Regular.ttf', 20)
fontLonShad25 = ImageFont.truetype('/usr/share/fonts/truetype/google/LondrinaShadow-Regular.ttf', 25)
fontLonShad30 = ImageFont.truetype('/usr/share/fonts/truetype/google/LondrinaShadow-Regular.ttf', 30)
fontLonSke10 = ImageFont.truetype('/usr/share/fonts/truetype/google/LondrinaSketch-Regular.ttf', 10)
fontLonSke15 = ImageFont.truetype('/usr/share/fonts/truetype/google/LondrinaSketch-Regular.ttf', 15)
fontLonSke20 = ImageFont.truetype('/usr/share/fonts/truetype/google/LondrinaSketch-Regular.ttf', 20)
fontLonSke25 = ImageFont.truetype('/usr/share/fonts/truetype/google/LondrinaSketch-Regular.ttf', 25)
fontLonSke30 = ImageFont.truetype('/usr/share/fonts/truetype/google/LondrinaSketch-Regular.ttf', 30)

fontOswReg10 = ImageFont.truetype('/usr/share/fonts/truetype/google/Oswald-Regular.ttf', 10)
fontOswReg15 = ImageFont.truetype('/usr/share/fonts/truetype/google/Oswald-Regular.ttf', 15)
fontOswReg20 = ImageFont.truetype('/usr/share/fonts/truetype/google/Oswald-Regular.ttf', 20)
fontOswReg25 = ImageFont.truetype('/usr/share/fonts/truetype/google/Oswald-Regular.ttf', 25)
fontOswReg30 = ImageFont.truetype('/usr/share/fonts/truetype/google/Oswald-Regular.ttf', 30)
fontOswBol10 = ImageFont.truetype('/usr/share/fonts/truetype/google/Oswald-Bold.ttf', 10)
fontOswBol15 = ImageFont.truetype('/usr/share/fonts/truetype/google/Oswald-Bold.ttf', 15)
fontOswBol20 = ImageFont.truetype('/usr/share/fonts/truetype/google/Oswald-Bold.ttf', 20)
fontOswBol25 = ImageFont.truetype('/usr/share/fonts/truetype/google/Oswald-Bold.ttf', 25)
fontOswBol30 = ImageFont.truetype('/usr/share/fonts/truetype/google/Oswald-Bold.ttf', 30)

fontVastShad10 = ImageFont.truetype('/usr/share/fonts/truetype/google/VastShadow-Regular.ttf', 10)
fontVastShad15 = ImageFont.truetype('/usr/share/fonts/truetype/google/VastShadow-Regular.ttf', 15)
fontVastShad20 = ImageFont.truetype('/usr/share/fonts/truetype/google/VastShadow-Regular.ttf', 20)
fontVastShad25 = ImageFont.truetype('/usr/share/fonts/truetype/google/VastShadow-Regular.ttf', 25)
fontVastShad30 = ImageFont.truetype('/usr/share/fonts/truetype/google/VastShadow-Regular.ttf', 30)


def TransformLatLongToXY(lat, lon):
    x = (int)(0.733 * lon + 132)
    y = (int)(-1.006 * lat + 90.5)
    return x, y


def PeopleInSpace():
    url = 'http://api.open-notify.org/astros.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    
    print("There are currently " + str(result["number"]) + " astronauts in space:")
    print("")

    people = result["people"]

    listPeople = ''
    for p in people:
        listPeople = listPeople + p["name"] + "  ( " + p["craft"] + " )\n"
        
    print(listPeople)
    
    stringToShow1 = "People in Space:"
    stringToShow2 = listPeople
    
    HBlackImage = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255)  # 298*176
    bmpSpace = Image.open('space.bmp')
    HBlackImage.paste(bmpSpace, (0,0))
    draw = ImageDraw.Draw(HBlackImage)
    draw.text((25, 10), stringToShow1, font = fontBunIn20, fill = 254)
    #draw.text((25, 60), stringToShow2, font = fontVastShad10, fill = 0)
    draw.text((25, 60), stringToShow2, font = fontOswBol15, fill = 0)
    
    
    epd.display(epd.getbuffer(HBlackImage))

    # Reset timeToRefresh
    #global timeToRefesh = 0
    
    
    
def WhereIsIIS():
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    
    #Let's extract the required information
    location =result["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]
    rightNow = result["timestamp"]
    actualDay = time.strftime('%A, %Y-%m-%d', time.localtime(rightNow))
    actualTime = time.strftime('%H:%M:%S', time.localtime(rightNow))
  
    ISSlat = float(result['iss_position']['latitude'])
    ISSlon = float(result['iss_position']['longitude'])
        
    #Output informationon screen
    print("\nLatitude: " + str(lat))
    print("Longitude: " +str(lon))
    print(str(actualDay))
    print(str(actualTime))
    
    stringToShow1 = actualDay #+ "\n  " + actualTime
    stringToShow2 = actualTime
    stringToShow3 =  str(lat) + " : " +str(lon)
    
    HBlackImage = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255)  # 298*176
    bmpWorld = Image.open('WorldMap.bmp')
    #bmpWorld = Image.open('world_map.bmp')
    HBlackImage.paste(bmpWorld, (0,0))
    draw = ImageDraw.Draw(HBlackImage)
    issLogo = Image.open('iss.bmp').convert('L')
           
    draw.text((10, 1), stringToShow1, font = fontVastShad15, fill = 0)
    draw.text((90, 15), stringToShow2, font = fontBan20, fill = 0) 
    draw.text((5, 155), stringToShow3, font = fontLonShad20, fill = 0)
    
    print('LAT: '+ str(ISSlat))
    print('LON: '+ str(ISSlon))
    (x,y) = TransformLatLongToXY(ISSlat, ISSlon)
    print('***** LAT: '+ str(x) + ' - ' + str(ISSlat))
    print('***** LON: '+ str(y) + ' - ' + str(ISSlon))
    
    HBlackImage.paste(issLogo, ((int)(x-10), (int)(y-10)))
    
    
    epd.display(epd.getbuffer(HBlackImage))

    
def MoonPhase():
    now = datetime.now()    
    url = "https://www.icalendar37.net/lunar/api/?"
    url = url + "lang=en&year=" + str(now.year)
    url = url + "&month=" + str(now.month)
    
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
            
    monthName = result['monthName']    
    daysData = result['phase']
    dayNumber = now.day
    print(daysData)
    dayData = daysData[str(dayNumber)]
    phaseName = dayData['phaseName']    
    lighting = dayData['lighting']
    lightRounded = round(lighting, 1)
    distance = dayData['dis']
    distRounded = int(distance)
    dayWeek = dayData['dayWeek']    
    timeEvent = dayData['timeEvent']    
    isPhaseLimit = str(dayData['isPhaseLimit'])    
    if (isPhaseLimit.isdigit()):
        phaseNumber = isPhaseLimit 
    
    if (dayWeek == 0):
        dayName = 'Monday'
    if (dayWeek == 1):
        dayName = 'Tuesday'
    if (dayWeek == 2):
        dayName = 'Wednesday'
    if (dayWeek == 3):
        dayName = 'Thursday'
    if (dayWeek == 4):
        dayName = 'Friday'
    if (dayWeek == 5):
        dayName = 'Saturday'
    if (dayWeek == 6):
        dayName = 'Sunday'
    
    print('** ** ** ** ** ** ** **')
    print('Month: ' + str(monthName))
    print('Day: ' + str(dayNumber))
    print('Phase: ' + str(phaseName))
    print('Lighting: ' + str(lighting) + '%')    
    print('Lighting: ' + str(lightRounded) + '%')
    print('Distance: ' + str(distance) + 'Km')
    print('Distance: ' + str(distRounded) + 'Km')
    print('DayWeek: ' + str(dayWeek) + ' ' + dayName)
    print('IsPhaseLimit: ' + str(isPhaseLimit))
    print('TimeEvent: ' + str(timeEvent))
    print('** ** ** ** ** ** ** **')
    
    
        
    if (phaseName=="New Moon"):
        photoMoon = 'Moon/phase_0.bmp'
    elif (phaseName=="Waxing"):
        photoMoon = 'Moon/phase_C-25.bmp'
    elif (phaseName=="First quarter"):
        photoMoon = 'Moon/phase_C_50.bmp'
    elif (phaseName=="Waxing"):
        photoMoon = 'Moon/phase_C-75.bmp'
    elif (phaseName=="Full moon"):
        photoMoon = 'Moon/phase_100.bmp'
    elif (phaseName=="Waning"):
        photoMoon = 'Moon/phase_D-25.bmp'
    elif (phaseName=="Last quarter"):
        photoMoon = 'Moon/phase_D-50.bmp'
    elif (phaseName=="Waning"):
        photoMoon = 'Moon/phase_D-75.bmp'
    
    
    
    HBlackImage = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255)  # 298*176
    bmpWorld = Image.open(photoMoon)
    #bmpWorld = Image.open('world_map.bmp')
    HBlackImage.paste(bmpWorld, (0,0))
    draw = ImageDraw.Draw(HBlackImage)

    draw.rectangle((176, 0, 298, 176), fill = 0)

    stringToShow1 = str(dayNumber) + ' ' + str(monthName)
    stringToShow2 = 'Sunday'
    stringToShow3 = str(phaseName)
    stringToShow4 = str(distRounded) + ' Km'
    stringToShow5 = str("%.1f" % lighting) + '%'
  

    #draw.text((130, 10), stringToShow1, font = fontVastShad15, fill = 255)
    draw.text((150, 10), stringToShow1, font = fontBan20, fill = 255)
    draw.text((170, 30), stringToShow2, font = fontBan20, fill = 255)
    draw.text((165, 60), stringToShow3, font = fontBan20, fill = 255) 
    draw.text((170, 85), stringToShow4, font = fontBan20, fill = 255) 
    draw.text((135, 120), stringToShow5, font = fontBan50, fill = 255) 
    
    epd.display(epd.getbuffer(HBlackImage))
    
    
    
    
    
    
    
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
    actualButton = pinNum
    print('>>>> ' + str(actualButton))
   
    btn.buttonNumber.value = pinNum
    
    
    if (pinNum==5):        
        printToDisplay('This is my first \nRPi project.')
    elif (pinNum==6):
        btn.timePressed.value = 0
        PeopleInSpace()
        btn.timePressed.value = 0
        time.sleep(2)
        btn.timePressed.value = 0        
    elif (pinNum==13):
        btn.timePressed.value = 0
        WhereIsIIS()
        btn.timePressed.value = 0
        time.sleep(2)
        btn.timePressed.value = 0
    elif (pinNum==19):
        MoonPhase()        
        time.sleep(2)
        btn.timePressed.value = 0
    else:
        print('Wrong Button!')  
    
    

timePressed = TimePressed()
while True:
    try:        
        Button.timePressed.value +=  .5

        # Tell the button what to do when pressed
        btn1.when_pressed = handleBtnPress
        btn2.when_pressed = handleBtnPress
        btn3.when_pressed = handleBtnPress
        btn4.when_pressed = handleBtnPress

        #print('waiting... ' + str(timeToRefesh) + '  -> ' + str(actualButton))
        #print('waiting..... ' + str(timePressed.value) + '  -> ' + str(actualButton))
        time.sleep(0.5)
        
        print('-- (' + str(Button.buttonNumber.value) + ') - ' + str(Button.timePressed.value))
        
        if (Button.buttonNumber.value == 6):
            print('6........' + str(Button.timePressed.value) + ' / ' + str(timeToRefeshBtn2))
            if (Button.timePressed.value >= timeToRefeshBtn2):
                Button.timePressed.value = 0
                PeopleInSpace()
        
        if (Button.buttonNumber.value == 13):
            print('13.......' + str(Button.timePressed.value) + ' / ' + str(timeToRefeshBtn3))
            if (Button.timePressed.value >= timeToRefeshBtn3):
                Button.timePressed.value = 0
                WhereIsIIS()
        
        if (Button.buttonNumber.value == 19):
            print('19.......' + str(Button.timePressed.value) + ' / ' + str(timeToRefeshBtn4))
            if (Button.timePressed.value >= timeToRefeshBtn4):
                Button.timePressed.value = 0
                MoonPhase()
    
    except KeyboardInterrupt:    
        #logging.info("ctrl + c:")
        epd2in7.epdconfig.module_exit()
        exit()