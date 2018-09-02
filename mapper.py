#File to handle the mapping of data from the dataloader

from dataloader import Dataloader

class Mapper:
    
    def getCoords(data, source_coordinates):
        for i in data['Lat']:
            if (i == None):
                print("test")
                #set i to be latitude of source_coordinates[district in i]
        for j in data['Long']:
            if (j == None):
                print("test")
                #set j to be the longitude of source_coords[district in j]
        # refactor this?

# Example of use
# Mapper.getCoords(Dataloader.loadData("sampledata.xlsx"), Dataloader.loadCoordsFile("somecsvfile"))