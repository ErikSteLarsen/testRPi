import datetime
import time
import pygsheets
from garo_gm3d import Garo

#authorization
gc = pygsheets.authorize(service_file='/Users/ErikS/Desktop/Garo-GM3D/test123-337418-2f66f46a491c.json')
#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('test')
#select the first sheet 
wks = sh[0]

current_watt_hours = wks.get_value((1,2))
current_watt_hours = int(current_watt_hours)
print('Current energy meter standing (as read from the spreadsheet in column B1) is {}Wh'.format(current_watt_hours))

# Initialize the Garo GM3D
garo = Garo(17, current_watt_hours)
garo.listen()

counter = 2


while True:
    
    current_watt_hours = garo.get_watt_hours()
    
    wks.update_value((counter,1), str(datetime.datetime.now()))
    wks.update_value((counter,2), "test")
    counter += 1
    time.sleep(30)