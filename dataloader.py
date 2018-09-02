#File to handles the importing of data

import pandas as pd

class dataLoader:
    
    #function to load data from an excel/csv
    #path is a string filepath
    def loadData(path):
        try:
            file = pd.read_excel(path)
        except:
            print("File Read Error - Check Path")
            exit(1)

dl = dataLoader()
dl.loadData("sample.xlsx")