import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file='/Users/ErikS/Desktop/Garo-GM3D/test123-337418-2f66f46a491c.json')

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['John', 'Steve', 'Sarah']

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('test')

#select the first sheet 
wks = sh[0]

#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(df,(1,1))