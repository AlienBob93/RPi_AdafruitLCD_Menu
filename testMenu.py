#Prashant Rao 

#import pywapi as weather
import string 
from time import sleep
import Adafruit_CharLCD as LCD
from Menu import Menu

lcd = LCD.Adafruit_CharLCDPlate()
menu = Menu()

#loc_ID = pywapi.get_location_ids('mckees rock, pa')
#print(loc_ID)

#The menu can show strings, bash and python expressions
#		     topElement(      Name , Type of content , Lower row content)

top1 = menu.topElement("< Weather      >", "STRING", "        v")
top2 = menu.topElement("< Network     >", "STRING", "        v")
top3 = menu.topElement("< System       >", "STRING", "        v")
top4 = menu.topElement("< Radio        >", "STRING", "        v")


sub11 = menu.subElement("Weather>Cond.", "PYTHON", 'str(Weather.currCond())')
sub12 = menu.subElement("Weather>Temp.", "PYTHON", 'str(str(Weather.currTemp()) +chr(223)+ "F")')
sub13 = menu.subElement("Weather>Loc.", "PYTHON", 'str(Weather.currLoc())')

sub21 = menu.subElement("Netw.>Signal", "BASH", "iwconfig wlan0 | awk -F'[ =]+' '/Signal level/ {print $7}' | cut -d/ -f1")
sub22 = menu.subElement("Netw.>SSID", "BASH", "iwconfig wlan0 | grep 'ESSID:' | awk '{print $4}' | sed 's/ESSID://g'")
sub23 = menu.subElement("Netw>IP", "BASH", "ifconfig wlan0 | grep 'inet addr:' | awk '{print $2}' | sed 's/addr://g'")

sub31 = menu.subElement("System>CPU", "PYTHON", 'str(str(psutil.cpu_percent()) + "%")')

sub41 = menu.subElement("Radio>", "RADIO", 'str(radioINFO.station())')

#Adding elements to the menu
menu.addTopElement(top1)
menu.addTopElement(top2)
menu.addTopElement(top3)
menu.addTopElement(top4)

menu.addSubElement(top1, sub11)
menu.addSubElement(top1, sub12)
menu.addSubElement(top1, sub13)
menu.addSubElement(top2, sub21)
menu.addSubElement(top2, sub22)
menu.addSubElement(top2, sub23)
menu.addSubElement(top3, sub31)
menu.addSubElement(top4, sub41)

#initializing display
lcd.clear()
lcd.set_color(1.0, 0, 0)

#little loading animation
i = 0
lcd.message("LOADING\n")
while(i < 16):
    lcd.message(chr(219))
    sleep(.1)
    i += 1

#starting the menu
menu.startMenu(lcd, LCD)
