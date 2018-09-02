import pandas as pd

class dataLoader:
    
    #function to load data from an excel/csv
    #path is a string filepath
    def loadData(path):
        file = pd.read_excel(path)

dl = dataLoader()
dl.loadData("sample.xlsx")