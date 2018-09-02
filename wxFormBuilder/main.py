import wx
import gui

class mainFrame(gui.GUIFrameMain):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        gui.GUIFrameMain.__init__(self,parent)

    #directory picker
    def directoryPicker(self, event):
        
        #open a file
        with wx.FileDialog(self, "Import data file", wildcard="Microsoft Excel or CSV files (*.xls;*.xlsx;*.csv)|*.xls;*.xlsx;*.csv", style=wx.FD_OPEN) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            
            #print file path, todo pass path to DataLoader
            print(fileDialog.GetPath())


app = wx.App(False)

frame = mainFrame(None)
frame.Show(True)
app.MainLoop()