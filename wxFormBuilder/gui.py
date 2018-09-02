# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Aug 29 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class GUIFrameMain
###########################################################################

class GUIFrameMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.menuFile = wx.Menu()
		self.menuImport = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Import", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFile.Append( self.menuImport )

		self.m_menubar1.Append( self.menuFile, u"File" )

		self.menuAnalyse = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.menuAnalyse, wx.ID_ANY, u"Analysis_1", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuAnalyse.Append( self.m_menuItem3 )

		self.m_menubar1.Append( self.menuAnalyse, u"Analyse" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_menubar1.Bind( wx.EVT_LEFT_DOWN, self.directoryPicker )
		self.Bind( wx.EVT_MENU, self.directoryPicker, id = self.menuImport.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def directoryPicker( self, event ):
		event.Skip()



###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_dirPicker4 = wx.DirPickerCtrl( self, wx.ID_ANY, u"hnb", u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		fgSizer1.Add( self.m_dirPicker4, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


