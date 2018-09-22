#file to handle importing of data and resolution of coordinates

import pandas as pd

#import data sheet
try:
    df = pd.read_excel("sampledata.xlsx")
    #mark empty fields with a 0
    df.fillna(0, inplace=True)
    data = df
    #handler for failures
except:
    print("File Read Error - Check Path")
    exit()

try:
    df = pd.read_csv("worldcities.csv")
    coordfile = df.to_dict()
    #handler for failures
except:
    print("File Read Error - Check Path")
    exit()

def getd(district, coords):
        try:
            for i in range(len(coords['lat'])):
                if (coords['city_ascii'][i] == district):
                    #get the index for the coords
                    return i
        except:
            print('Invalid District: ' + district)
            exit()

rindex = 0
for row in data.itertuples(index=True):
    if (row.Lat == 0.0):
        indx = getd(row.District, coordfile)
        
        #if index is valid then set coords
        if (indx != None):
            data.set_value(rindex, 'Lat', coordfile['lat'][indx])
            data.set_value(rindex, 'Long', coordfile['lng'][indx])
    rindex+=1

#here we will need to convert and output the dataframe -> ?