#File to handle the mapping of data from the dataloader

from dataloader import Dataloader

class Mapper:

    def getd(district, coords):
        try:
            for i in range(len(coords['lat'])):
                if (coords['city_ascii'][i] == district):
                    #get the index for the coords
                    return i
        except:
            print('Invalid District: ' + district)
            exit()
    
    def getCoords(data, source_coordinates):
        for i in range(len(data['District'])):
            if (data['Lat'][i] == 0):
                indx = Mapper.getd(data['District'][i], source_coordinates)
                data['Lat'][i] = source_coordinates['lat'][indx]
            if (data['Long'][i] == 0):
                data['Long'][i] = source_coordinates['lng'][indx]
        #SOME INDEX RELATED BUG IN HERE SETTING INDEX FAILS TO NONE
                

# Example of use
Mapper.getCoords(Dataloader.loadData("sampledata.xlsx"), Dataloader.loadCoordsFile("worldcities.csv"))