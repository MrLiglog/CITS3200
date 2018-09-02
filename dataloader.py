#File to handles the importing of data

import pandas as pd

#Abstract class to be called by other files
class Dataloader:
    
    #function to load data from an excel/csv
    #path is a string filepath
    def loadData(path):
        #attempt to read
        try:
            df = pd.read_excel(path)
            return df.to_dict()
        #handler for failures
        except:
            print("File Read Error - Check Path")
            exit()

    #function to load a coordinates file from a CSV
    def loadCoordsFile(path):
        try:
            df = pd.read_csv(path)
            return df.to_dict()
        #handler for failures
        except:
            print("File Read Error - Check Path")
            exit()

#Example of Usage
#dict = Dataloader.loadData("sampledata.xlsx")