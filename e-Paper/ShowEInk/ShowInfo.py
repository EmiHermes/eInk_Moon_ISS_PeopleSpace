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

class ISS():
    positions = []


actualButton = 0                    # Last pressed Button
timeToRefesh = 0                    # Time between Button press
timeToRefeshBtn1 = 1800             # Time to refresh the Action of Button WeatherForecast
timeToRefeshBtn2 = 3600             # Time to refresh the Action of Button PeopleInSpace
timeToRefeshBtn3 = 60               # Time to refresh the Action of Button WhereIsIIS
timeToRefeshBtn4 = 3600             # Time to refresh the Action of Button MoonPhase

Button.buttonNumber = ButtonNumber()
Button.timePressed = TimePressed()
Button.ISS= ISS()


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
fontBan55 = ImageFont.truetype('/usr/share/fonts/truetype/google/Bangers-Regular.ttf', 55)
fontBan60 = ImageFont.truetype('/usr/share/fonts/truetype/google/Bangers-Regular.ttf', 60)

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
    draw.text((25, 50), stringToShow2, font = fontOswBol15, fill = 0)
    
    # Paint all on the screen
    epd.display(epd.getbuffer(HBlackImage))


    
    
def WhereIsIIS(ISS):
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
       
    ISS.positions.append((ISSlat, ISSlon))
    print(ISS.positions)
    
    #Output informationon screen
    print("\nLatitude: " + str(lat))
    print("Longitude: " +str(lon))
    print(str(actualDay) + ' - ' + str(actualTime) + '\n')
    
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
    
    print('[]: ' + str(len(ISS.positions)))
    if (len(ISS.positions) > 250): #250 is a good number to have almost one turn 
        del ISS.positions[1]
    
    
    for i,t in enumerate(ISS.positions):
        (ISSlat, ISSlon) = t
        (x, y) = TransformLatLongToXY(ISSlat, ISSlon)
        
        if (((i+1) % (15*60/30)) == 0):
            print('X ')
            #print()
            s = 2
            draw.rectangle((x-s, y-s, x+s, y+s), fill = 0)
        else:
            print('0 ', end = '')
            s = 1
            draw.ellipse((x-s, y-s, x+s, y+s), outline = 0)
        
    print()
    
    # Paint all on the screen
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
    #print(daysData)
    dayData = daysData[str(dayNumber)]
    print(dayData)
    phaseName = dayData['phaseName']
    phaseNameText = dayData['npWidget']
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
    print('Phase: ' + str(phaseNameText))
    print('PhaseText: ' + str(phaseName))
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
        if (lightRounded > 0) and (lightRounded < 50): 
            photoMoon = 'Moon/phase_C-25.bmp'
        else:
            photoMoon = 'Moon/phase_C-75.bmp'
    elif (phaseName=="First quarter"):
        photoMoon = 'Moon/phase_C_50.bmp'
    elif (phaseName=="Full moon"):
        photoMoon = 'Moon/phase_100.bmp'
    elif (phaseName=="Waning"):
        if (lightRounded > 50) and (lightRounded < 100): 
            photoMoon = 'Moon/phase_D-25.bmp'
        else:
            photoMoon = 'Moon/phase_D-75.bmp'
    elif (phaseName=="Last quarter"):
        photoMoon = 'Moon/phase_D-50.bmp'
    
        
    print('Photo: ' + photoMoon)
    
    
    HBlackImage = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255)  # 298*176
    bmpWorld = Image.open(photoMoon)
    #bmpWorld = Image.open('world_map.bmp')
    HBlackImage.paste(bmpWorld, (0,0))
    draw = ImageDraw.Draw(HBlackImage)

    draw.rectangle((176, 0, 298, 176), fill = 0)

    stringToShow1 = str(dayNumber) + ' ' + str(monthName)
    stringToShow2 = str(dayName)
    stringToShow3 = str(phaseName)
    stringToShow4 = str(distRounded) + ' Km'
    stringToShow5 = str("%.1f" % lighting) + '%'
  

    #draw.text((130, 10), stringToShow1, font = fontVastShad15, fill = 255)
    draw.text((150, 10), stringToShow1, font = fontBan20, fill = 255)
    draw.text((170, 30), stringToShow2, font = fontBan20, fill = 255)
    draw.text((165, 60), stringToShow3, font = fontBan20, fill = 255) 
    draw.text((170, 85), stringToShow4, font = fontBan20, fill = 255) 
    draw.text((135, 120), stringToShow5, font = fontBan50, fill = 255) 
    
    # Paint all on the screen
    epd.display(epd.getbuffer(HBlackImage))
    
    
    
    
def WeatherForecast():
    url = "http://api.openweathermap.org/data/2.5/forecast?"
    #url = url + "q={city_name}" 
    #url = url + "q=Düsseldorf"        # ASCII problems  !!!
    url = url + "id=2934246"
    #url = url + "&appid={your_API_key}" 
    url = url + "&units=metric"        # In Metric 
    url = url + "&cnt=6"               # Only 6 results
    
    print(url)
    print('/// Calling ///')
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    data = result['list']
    cityData = result['city']
    
    print('***** RESULT *****')    
    print(cityData)
    print('******************')
    print(data)
    print('******************')
    
    # City information
    cityName = cityData['name']
    citySunrise = datetime.utcfromtimestamp(cityData['sunrise'])
    citySunset = datetime.utcfromtimestamp(cityData['sunset'])
    citySunriseTime = citySunrise.strftime('%H:%M:%S')
    citySunsetTime = citySunset.strftime('%H:%M:%S')
    
    # Weather 0
    fore0DT = datetime.utcfromtimestamp(data[0]['dt'])
    fore0DTDay = fore0DT.strftime('%d/%m')
    fore0DTTime = fore0DT.strftime('%H:%M')
    fore0DTText = data[0]['dt_txt']
    # Temperature
    fore0MainTemp = round(data[0]['main']['temp'], 1)
    fore0MainTempMin = data[0]['main']['temp_min']
    fore0MainTempMax = data[0]['main']['temp_max']
    fore0MainTempLike = round(data[0]['main']['feels_like'], 1)
    fore0MainHumidity = data[0]['main']['humidity']
    fore0MainPress = data[0]['main']['pressure']
    # Sky
    fore0SkyDes = data[0]['weather'][0]['description']
    fore0SkyIcon = data[0]['weather'][0]['icon']
    fore0SkyIconFile = 'Weather/' + str(fore0SkyIcon) + '@4x.bmp'
    fore0SkyCloud = str(data[0]['clouds']['all']) + '%'
    fore0SkyRain = str(data[0]['pop']) + '%'
    fore0WindSpeed = data[0]['wind']['speed']
    fore0WindDirec = data[0]['wind']['deg']
    # Rain
    if 'rain' not in data[0]:
        fore0Rain = '0%'
        fore0RainIs = False
    else:
        fore0Rain = str(data[0]['rain']['3h']) + '%'
        fore0RainIs = True
    # Snow
    if 'snow' not in data[0]:
        fore0Snow = '0%'
        fore0SnowIs = False
    else:
        fore0Snow = str(data[0]['snow']['3h']) + '%'
        fore0SnowIs = True    
    
    # Wind direction
    if (fore0WindDirec >= 348.75) and (fore0WindDirec < 11.24):
        fore0Wind = str(fore0WindSpeed) + 'N'
    if (fore0WindDirec >= 11.25) and (fore0WindDirec < 33.74):
        fore0Wind = str(fore0WindSpeed) + 'NNE'
    if (fore0WindDirec >= 33.75) and (fore0WindDirec < 56.24):
        fore0Wind = str(fore0WindSpeed) + 'NE'
    if (fore0WindDirec >= 56.25) and (fore0WindDirec < 78.74):
        fore0Wind = str(fore0WindSpeed) + 'ENE'
    if (fore0WindDirec >= 78.75) and (fore0WindDirec < 101.24):
        fore0Wind = str(fore0WindSpeed) + 'E'
    if (fore0WindDirec >= 101.25) and (fore0WindDirec < 123.44):
        fore0Wind = str(fore0WindSpeed) + 'ESE'
    if (fore0WindDirec >= 123.75) and (fore0WindDirec < 146.24):
        fore0Wind = str(fore0WindSpeed) + 'SE'
    if (fore0WindDirec >= 146.25) and (fore0WindDirec < 168.74):
        fore0Wind = str(fore0WindSpeed) + 'SSE'
    if (fore0WindDirec >= 168.75) and (fore0WindDirec < 191.24):
        fore0Wind = str(fore0WindSpeed) + 'S'
    if (fore0WindDirec >= 191.25) and (fore0WindDirec < 213.74):
        fore0Wind = str(fore0WindSpeed) + 'SSW'
    if (fore0WindDirec >= 213.75) and (fore0WindDirec < 236.24):
        fore0Wind = str(fore0WindSpeed) + 'SW'
    if (fore0WindDirec >= 236.25) and (fore0WindDirec < 258.74):
        fore0Wind = str(fore0WindSpeed) + 'WSW'
    if (fore0WindDirec >= 258.75) and (fore0WindDirec < 281.24):
        fore0Wind = str(fore0WindSpeed) + 'W'
    if (fore0WindDirec >= 281.25) and (fore0WindDirec < 303.74):
        fore0Wind = str(fore0WindSpeed) + 'WNW'
    if (fore0WindDirec >= 303.75) and (fore0WindDirec < 326.24):
        fore0Wind = str(fore0WindSpeed) + 'NW'
    if (fore0WindDirec >= 326.25) and (fore0WindDirec < 348.74):
        fore0Wind = str(fore0WindSpeed) + 'NNW'
    
    
    # Weather 1
    fore1DT = datetime.utcfromtimestamp(data[1]['dt'])
    fore1DTDay = fore1DT.strftime('%d/%m')
    fore1DTTime = fore1DT.strftime('%H:%M')
    fore1DTText = data[1]['dt_txt']
    # Temperature
    fore1MainTemp = round(data[1]['main']['temp'], 1)
    fore1MainTempMin = data[1]['main']['temp_min']
    fore1MainTempMax = data[1]['main']['temp_max']
    fore1MainTempLike = round(data[1]['main']['feels_like'], 1)
    fore1MainHumidity = data[1]['main']['humidity']
    fore1MainPress = data[1]['main']['pressure']
    # Sky
    fore1SkyDes = data[1]['weather'][0]['description']
    fore1SkyIcon = data[1]['weather'][0]['icon']
    fore1SkyIconFile = 'Weather/' + str(fore0SkyIcon) + '@2x.bmp'
    fore1SkyCloud = str(data[1]['clouds']['all']) + '%'
    fore1SkyRain = str(data[1]['pop']) + '%'
    # Rain
    if 'rain' not in data[1]:
        fore1Rain = '0%'
        fore1RainIs = False
    else:
        fore1Rain = str(data[1]['rain']['3h']) + '%'
        fore1RainIs = True
    # Snow
    if 'snow' not in data[1]:
        fore1Snow = '0%'
        fore1SnowIs = False
    else:
        fore1Snow = str(data[1]['snow']['3h']) + '%'
        fore1SnowIs = True
    
    
    # Weather 2
    fore2MainTempMin = data[2]['main']['temp_min']
    fore2MainTempMax = data[2]['main']['temp_max']
    # Weather 3
    fore3MainTempMin = data[3]['main']['temp_min']
    fore3MainTempMax = data[3]['main']['temp_max']
    # Weather 4
    fore4MainTempMin = data[4]['main']['temp_min']
    fore4MainTempMax = data[4]['main']['temp_max']
    # Weather 5
    fore5MainTempMin = data[5]['main']['temp_min']
    fore5MainTempMax = data[5]['main']['temp_max']
    # MinTemperature in the next hours 
    foreMainTempMin = fore0MainTempMin
    if (fore1MainTempMin < foreMainTempMin):
        foreMainTempMin = fore1MainTempMin
    if (fore2MainTempMin < foreMainTempMin):
        foreMainTempMin = fore2MainTempMin
    if (fore3MainTempMin < foreMainTempMin):
        foreMainTempMin = fore3MainTempMin
    if (fore4MainTempMin < foreMainTempMin):
        foreMainTempMin = fore4MainTempMin
    if (fore5MainTempMin < foreMainTempMin):
        foreMainTempMin = fore5MainTempMin
    foreMainTempMin = round(foreMainTempMin, 1)
    # MaxTemperature in the next hours  
    foreMainTempMax = fore0MainTempMax
    if (fore1MainTempMax > foreMainTempMax):
        foreMainTempMax = fore1MainTempMax
    if (fore2MainTempMax > foreMainTempMax):
        foreMainTempMax = fore2MainTempMax
    if (fore3MainTempMax > foreMainTempMax):
        foreMainTempMax = fore3MainTempMax
    if (fore4MainTempMax > foreMainTempMax):
        foreMainTempMax = fore4MainTempMax
    if (fore5MainTempMax > foreMainTempMax):
        foreMainTempMax = fore5MainTempMax
    foreMainTempMax = round(foreMainTempMax, 1) 
        
    # Traces of Information...
    print('City: ' + str(cityName))
    print('Sunrise: ' + str(citySunriseTime))
    print('Sunset: ' + str(citySunsetTime))
    print()
    print('Time: ' + str(fore0DTTime))
    print('Day: ' + str(fore0DTDay))
    print('DayText: ' + str(fore0DTText))
    print('Temp: ' + str(fore0MainTemp))
    print('TempMin: ' + str(fore0MainTempMin))
    print('TempMax: ' + str(fore0MainTempMax))
    print('TempLike: ' + str(fore0MainTempLike))
    print('Humidity: ' + str(fore0MainHumidity))
    print('Pression: ' + str(fore0MainPress))
    print('Min: ' + str(foreMainTempMin))
    print('Max: ' + str(foreMainTempMax))  
    print('Descr: ' + str(fore0SkyDes))
    print('Icon: ' + str(fore0SkyIcon))
    print('IconFile: ' + str(fore0SkyIconFile))
    print('Clouds: ' + str(fore0SkyCloud))
    print('Rain: ' + str(fore0SkyRain))
    print('WindSpeed: ' + str(fore0WindSpeed))
    print('WindDirec: ' + str(fore0WindDirec))
    print('Wind: ' + str(fore0Wind))
    print('IsRain: ' + str(fore0Rain))
    print('ISSnow: ' + str(fore0Snow))
    print()
    print('-- After --')
    print('Time: ' + str(fore1DTTime))
    print('Day: ' + str(fore1DTDay))
    print('DayText: ' + str(fore1DTText))
    print('Icon: ' + str(fore1SkyIcon))
    print('IconFile: ' + str(fore1SkyIconFile))
    print('Descr: ' + str(fore1SkyDes))    
    print('Clouds: ' + str(fore1SkyCloud))
    print('Rain: ' + str(fore1SkyRain))
            
    
    HBlackImage = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255)  # 298*176
    imgForecastToday = Image.open(fore0SkyIconFile)
    HBlackImage.paste(imgForecastToday, (0, -20))
    draw = ImageDraw.Draw(HBlackImage)
    imgForecastAfter = Image.open(fore1SkyIconFile)
    HBlackImage.paste(imgForecastAfter, (180, 86))
    

    # Now...
    draw.text((2, 1), str(cityName), font = fontBan20, fill = 0)
    draw.text((2, 20), str(citySunriseTime) + ' -> ' + str(citySunsetTime), font = fontBan20, fill = 0)
    draw.text((100, 1), str(fore0DTDay) + ' ' + str(fore0DTTime), font = fontBan20, fill = 0) 
    draw.text((2, 40), str(fore0SkyDes), font = fontBan25, fill = 0)
    draw.text((2, 65), 'Clouds: ' + str(fore0SkyCloud), font = fontBan15, fill = 0) 
    draw.text((2, 80), 'Rain:  ' + str(fore0SkyRain), font = fontBan15, fill = 0)
    draw.text((2, 95), 'Wind:  ' + str(fore0Wind), font = fontBan20, fill = 0)
    draw.text((2, 120), str(fore0MainTemp), font = fontBan60, fill = 0)  
    draw.text((100, 155), str(foreMainTempMax) + 'C ' + str(foreMainTempMin) + 'C', font = fontBan20, fill = 0)
    
    # After...
    draw.text((210, 20), str(fore1DTDay), font = fontBan20, fill = 0) 
    draw.text((220, 40), str(fore1DTTime), font = fontBan20, fill = 0)    
    if (fore1RainIs == True):
        draw.text((190, 65), 'Rain:   ' + str(fore1Rain), font = fontBan15, fill = 0)
    if (fore1SnowIs == True):
        draw.text((190, 80), 'Snow: ' + str(fore1Snow), font = fontBan15, fill = 0)   
    draw.text((215, 145), str(fore1MainTemp), font = fontBan30, fill = 0)
    
    
    # Paint all on the screen
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
        #printToDisplay('This is my first \nRPi eInk project.')
        btn.timePressed.value = 0
        WeatherForecast()
        btn.timePressed.value = 0
    elif (pinNum==6):
        btn.timePressed.value = 0
        PeopleInSpace()
        btn.timePressed.value = 0
        time.sleep(2)
        btn.timePressed.value = 0        
    elif (pinNum==13):
        btn.timePressed.value = 0
        WhereIsIIS(btn.ISS)
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

        time.sleep(0.5)
        
        if (Button.buttonNumber.value == 0):
            print('-- (' + str(Button.buttonNumber.value) + ') - ' + str(Button.timePressed.value))
        
        if (Button.buttonNumber.value == 5):
            print('5........' + str(Button.timePressed.value) + ' / ' + str(timeToRefeshBtn1))
            if (Button.timePressed.value >= timeToRefeshBtn1):
                Button.timePressed.value = 0
                WeatherForecast()
                
        if (Button.buttonNumber.value == 6):
            print('6........' + str(Button.timePressed.value) + ' / ' + str(timeToRefeshBtn2))
            if (Button.timePressed.value >= timeToRefeshBtn2):
                Button.timePressed.value = 0
                PeopleInSpace()
        
        if (Button.buttonNumber.value == 13):
            print('13.......' + str(Button.timePressed.value) + ' / ' + str(timeToRefeshBtn3))
            if (Button.timePressed.value >= timeToRefeshBtn3):
                Button.timePressed.value = 0
                WhereIsIIS(Button.ISS)
        
        if (Button.buttonNumber.value == 19):
            print('19.......' + str(Button.timePressed.value) + ' / ' + str(timeToRefeshBtn4))
            if (Button.timePressed.value >= timeToRefeshBtn4):
                Button.timePressed.value = 0
                MoonPhase()
    
    
    except KeyboardInterrupt: 
        epd2in7.epdconfig.module_exit()
        exit()
