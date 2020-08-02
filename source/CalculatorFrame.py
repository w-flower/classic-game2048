# -*- coding: utf-8 -*- 



import wx
import os

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"2048", pos = wx.DefaultPosition, size = wx.Size( 382,442 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.SetBackgroundColour( wx.Colour( 246, 246, 246 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"  2048开始菜单", wx.DefaultPosition, wx.Size( 160,25 ), 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 16, 70, 90, 90, False, "微软雅黑" ) )
		self.m_staticText7.SetMaxSize( wx.Size( 19,19 ) )
		
		bSizer1.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"选择" ), wx.VERTICAL )
		
		
		self.m_staticText10 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		sbSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		sbSizer1.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.m_button1 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"开始游戏", wx.DefaultPosition, wx.Size( 100,31 ), 0 )
		self.m_button1.SetFont( wx.Font( 9, 70, 90, 90, False, "微软雅黑" ) )
		
		sbSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button2 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"我的战绩", wx.DefaultPosition, wx.Size( 100,31 ), 0 )
		self.m_button2.SetFont( wx.Font( 9, 70, 90, 90, False, "微软雅黑" ) )
		
		sbSizer1.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button3 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"人机对战(未开放)", wx.DefaultPosition, wx.Size( 100,31 ), 0 )
		self.m_button3.SetFont( wx.Font( 9, 70, 90, 90, False, "微软雅黑" ) )
		
		sbSizer1.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button4 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"模式/难度调整", wx.DefaultPosition, wx.Size( 100,31 ), 0 )
		self.m_button4.SetFont( wx.Font( 9, 70, 90, 90, False, "微软雅黑" ) )
		
		sbSizer1.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button5 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"更新日志", wx.DefaultPosition, wx.Size( 100,31 ), 0 )
		self.m_button5.SetFont( wx.Font( 9, 70, 90, 90, False, "微软雅黑" ) )
		
		sbSizer1.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.game_start )
		self.m_button2.Bind( wx.EVT_BUTTON, self.record )
		self.m_button3.Bind( wx.EVT_BUTTON, self.robot )
		self.m_button4.Bind( wx.EVT_BUTTON, self.change_mode )
		self.m_button5.Bind( wx.EVT_BUTTON, self.update_log )
	def __del__(self):
		self.Close(True)
		

	
	# Virtual event handlers, overide them in your derived class
	def game_start( self, event ):
		event.Skip()
	
	def record( self, event ):
		event.Skip()
	
	def robot( self, event ):
		event.Skip()
	
	def update_log( self, event ):
		event.Skip()

	def change_mode(self, event):
		event.Skip()
		
		
	

