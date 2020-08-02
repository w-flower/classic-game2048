# -*- coding: UTF-8 -*-

import os
import random
import time

import wx

from source import CalculatorFrame
from source.record import Record
from source.think import add, think

aim = 2048


class Calculator(CalculatorFrame.MyFrame1):
    def run(self):
        self.game_side_length = 4
        self.game_add = 1
        #获取战绩
        global myrecord
        myrecord = Record()

    def game_start(self, event):
        class Game_start(wx.Frame):
            def __init__(self, parent, side_length=4, add=1):
                wx.Frame.__init__(self,
                                  parent,
                                  id=wx.ID_ANY,
                                  title=u"2048",
                                  pos=wx.DefaultPosition,
                                  size=wx.Size(415, 438),
                                  style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
                
                self.aim = aim #难度存储在对象中
                
                self.colors = { #每个方格的颜色
                0: (204, 192, 179),
                2: (238, 228, 218),
                4: (237, 224, 200),
                8: (242, 177, 121),
                16: (245, 149, 99),
                32: (246, 124, 95),
                64: (246, 94, 59),
                128: (237, 207, 114),
                256: (237, 207, 114),
                512: (237, 207, 114),
                1024: (237, 207, 114),
                2048: (237, 207, 114),
                }
                #grid1~16: 每个方块
                self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

                gSizer1 = wx.GridSizer(0, 2, 0, 0)

                gSizer2 = wx.GridSizer(0, 2, 0, 0)

                self.grid1 = wx.StaticText(self, wx.ID_ANY,
                                           u"2048", wx.DefaultPosition,
                                           wx.Size(100, 100), 0)
                self.grid1.Wrap(-1)
                self.grid1.SetFont(wx.Font(30, 70, 90, 90, False, "微软雅黑"))
                self.grid1.SetBackgroundColour(wx.Colour(4, 157, 207))
                self.SetBackgroundColour( wx.Colour( 246, 246, 246 ) )

                gSizer2.Add(self.grid1, 0, wx.ALL, 5)

                self.grid2 = wx.StaticText(self, wx.ID_ANY,
                                           u"2048", wx.DefaultPosition,
                                           wx.Size(100, 100), 0)
                self.grid2.Wrap(-1)
                self.grid2.SetFont(wx.Font(30, 70, 90, 90, False, "微软雅黑"))
                self.grid2.SetBackgroundColour(wx.Colour(0, 255, 128))

                gSizer2.Add(self.grid2, 0, wx.ALL, 5)

                self.grid5 = wx.StaticText(self, wx.ID_ANY,
                                           u"2048", wx.DefaultPosition,
                                           wx.Size(100, 100), 0)
                self.grid5.Wrap(-1)
                self.grid5.SetFont(wx.Font(30, 70, 90, 90, False, "微软雅黑"))
                self.grid5.SetBackgroundColour(wx.Colour(0, 128, 255))

                gSizer2.Add(self.grid5, 0, wx.ALL, 5)

                self.grid6 = wx.StaticText(self, wx.ID_ANY,
                                           u"2048", wx.DefaultPosition,
                                           wx.Size(100, 100), 0)
                self.grid6.Wrap(-1)
                self.grid6.SetFont(wx.Font(30, 70, 90, 90, False, "微软雅黑"))
                self.grid6.SetBackgroundColour(wx.Colour(255, 128, 192))

                gSizer2.Add(self.grid6, 0, wx.ALL, 5)

                self.grid9 = wx.StaticText(self, wx.ID_ANY,
                                           u"2048", wx.DefaultPosition,
                                           wx.Size(100, 100), 0)
                self.grid9.Wrap(-1)
                self.grid9.SetFont(wx.Font(30, 70, 90, 90, False, "微软雅黑"))
                self.grid9.SetBackgroundColour(wx.Colour(255, 128, 255))

                gSizer2.Add(self.grid9, 0, wx.ALL, 5)

                self.grid10 = wx.StaticText(self, wx.ID_ANY, u"2048",
                                            wx.DefaultPosition,
                                            wx.Size(100, 100), 0)
                self.grid10.Wrap(-1)
                self.grid10.SetFont(wx.Font(30, 70, 90, 90, False, "微软雅黑"))
                self.grid10.SetBackgroundColour(wx.Colour(254, 224, 130))

                gSizer2.Add(self.grid10, 0, wx.ALL, 5)

                self.grid13 = wx.StaticText(self, wx.ID_ANY, u"2048",
                                            wx.DefaultPosition,
                                            wx.Size(100, 100), 0)
                self.grid13.Wrap(-1)
                self.grid13.SetFont(wx.Font(30, 70, 90, 90, False, "微软雅黑"))
                self.grid13.SetBackgroundColour(wx.Colour(0, 128, 192))

                gSizer2.Add(self.grid13, 0, wx.ALL, 5)

                self.grid14 = wx.StaticText(self, wx.ID_ANY, u"2048",
                                            wx.DefaultPosition,
                                            wx.Size(100, 100), 0)
                self.grid14.Wrap(-1)
                self.grid14.SetFont(wx.Font(30, 70, 90, 90, False, "微软雅黑"))
                self.grid14.SetBackgroundColour(wx.Colour(128, 128, 192))

                gSizer2.Add(self.grid14, 0, wx.ALL, 5)

                gSizer1.Add(gSizer2, 1, wx.EXPAND, 5)

                gSizer3 = wx.GridSizer(0, 2, 0, 0)

                self.grid3 = wx.StaticText(self, wx.ID_ANY,
                                           u"2048", wx.DefaultPosition,
                                           wx.Size(100, 100), 0)
                self.grid3.Wrap(-1)
                self.grid3.SetFont(wx.Font(30, 70, 90, 90, False, "微软雅黑"))
                self.grid3.SetBackgroundColour(wx.Colour(0, 64, 128))

                gSizer3.Add(self.grid3, 0, wx.ALL, 5)

                self.grid4 = wx.StaticText(self, wx.ID_ANY,
                                           u"2048", wx.DefaultPosition,
                                           wx.Size(100, 100), 0)
                self.grid4.Wrap(-1)
                self.grid4.SetFont(wx.Font(30, 70, 90, 90, False, "微软雅黑"))
                self.grid4.SetBackgroundColour(wx.Colour(255, 0, 128))

                gSizer3.Add(self.grid4, 0, wx.ALL, 5)

                self.grid7 = wx.StaticText(self, wx.ID_ANY,
                                           u"2048", wx.DefaultPosition,
                                           wx.Size(100, 100), 0)
                self.grid7.Wrap(-1)
                self.grid7.SetFont(wx.Font(30, 70, 90, 90, False, "微软雅黑"))
                self.grid7.SetBackgroundColour(wx.Colour(128, 0, 0))

                gSizer3.Add(self.grid7, 0, wx.ALL, 5)

                self.grid8 = wx.StaticText(self, wx.ID_ANY,
                                           u"2048", wx.DefaultPosition,
                                           wx.Size(100, 100), 0)
                self.grid8.Wrap(-1)
                self.grid8.SetFont(wx.Font(30, 70, 90, 90, False, "微软雅黑"))
                self.grid8.SetBackgroundColour(wx.Colour(255, 128, 0))

                gSizer3.Add(self.grid8, 0, wx.ALL, 5)
                

                self.grid11 = wx.StaticText(self, wx.ID_ANY, u"2048",
                                            wx.DefaultPosition,
                                            wx.Size(100, 100), 0)
                self.grid11.Wrap(-1)
                self.grid11.SetFont(wx.Font(30, 70, 90, 90, False, "微软雅黑"))
                self.grid11.SetBackgroundColour(wx.Colour(0, 128, 64))

                gSizer3.Add(self.grid11, 0, wx.ALL, 5)

                self.grid12 = wx.StaticText(self, wx.ID_ANY, u"2048",
                                            wx.DefaultPosition,
                                            wx.Size(100, 100), 0)
                self.grid12.Wrap(-1)
                self.grid12.SetFont(wx.Font(30, 70, 90, 90, False, "微软雅黑"))
                self.grid12.SetBackgroundColour(wx.Colour(221, 147, 230))

                gSizer3.Add(self.grid12, 0, wx.ALL, 5)

                self.grid15 = wx.StaticText(self, wx.ID_ANY, u"2048",
                                            wx.DefaultPosition,
                                            wx.Size(100, 100), 0)
                self.grid15.Wrap(-1)
                self.grid15.SetFont(wx.Font(30, 70, 90, 90, False, "微软雅黑"))
                self.grid15.SetBackgroundColour(
                    wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

                gSizer3.Add(self.grid15, 0, wx.ALL, 5)

                self.grid16 = wx.StaticText(self, wx.ID_ANY, u"2048",
                                            wx.DefaultPosition,
                                            wx.Size(100, 100), 0)
                self.grid16.Wrap(-1)
                self.grid16.SetFont(wx.Font(30, 70, 90, 90, False, "微软雅黑"))
                self.grid16.SetBackgroundColour(
                    wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

                gSizer3.Add(self.grid16, 0, wx.ALL, 5)

                gSizer1.Add(gSizer3, 1, wx.EXPAND, 5)

                self.SetSizer(gSizer1)
                self.Layout()

                self.Centre(wx.BOTH)

                # Connect Events
                self.Bind(wx.EVT_KEY_DOWN, self.run)
                #初始化数据
                self.game_start_n = side_length
                self.game_start_lst = [[0 for _ in range(self.game_start_n)]
                                       for i in range(self.game_start_n)]
                self.game_start_randomLst = [2, 2, 4, 2, 2, 2, 2]
                self.game_start_add = add
                self.huihe = 0
                
                #初始化列表
                for i in range(random.randint(2, 3)):
                    self.game_start_lst[random.randint(
                        0, self.game_start_n - 1)][random.randint(
                            0, self.game_start_n -
                            1)] = self.game_start_randomLst[random.randint(
                                0, 1)]
                #判断目标是什么并显示

                dia = wx.MessageDialog(None, u"游戏说明: wasd上下左右控制, 获得{}方块QWQ".format(self.aim), u"说明",
                                           wx.YES_NO | wx.ICON_QUESTION) if self.aim != "forever" else wx.MessageDialog(None, u"游戏说明: wasd上下左右控制, 直到游戏结束为止QWQ", u"说明",
                                           wx.YES_NO | wx.ICON_QUESTION)
                dia.ShowModal()
                

            # Virtual event handlers, overide them in your derived class
            def run(self, event):
                self.huihe += 1
                self.start = time.time() if self.huihe == 1 else self.start
                '''
                差不多相当于__init__吧
                流程:
                1, 判断游戏是否胜利or结束
                2, 接收键盘信息
                3, 判断是什么键按下
                4, 根据键, 方块上下左右移动
                5, 增加方块 , 如果增加失败则游戏结束
                6, 输出
                '''
                print(self.game_start_lst)
                self.write()
                
                keycode = event.GetKeyCode() 

                
                
                if keycode == 87:
                    self.think(None, "w")
                    
                    if not self.add_new():
                        game = 'over'
                                  
                    self.write()
                    
                elif keycode == 65:
                    
                    self.think(None, "a")
                    
                    if not self.add_new():
                        game = 'over' 

                    self.write()                  
                elif keycode == 83:
                    
                    self.think(None, "s")
                    
                    if not self.add_new():
                        game = 'over'  

                    self.write()
              
                elif keycode == 68:
                    
                    self.think(None, "d")
                    
                    if not self.add_new():
                        game = 'over'

                    self.write()
                    
                else:
                    print("pass")
                try:
                    tp = self.is_game_over()
                    game = "win" if tp else game
                    self.game_is_over_win(game)
                except:
                    pass
            def game_is_over_win(self, game):
                '''
                如果游戏输了或者赢了的话
                '''
                try:
                    if game == 'over':
                        finish = time.time()
                        dia = wx.MessageDialog(None, u"game over~", u"游戏结束",
                                            wx.YES_NO)
                        dia.ShowModal()
                        self.__record_down()
                        print('game over')
                        self.Close(True)
                    if game == 'win':
                        self.finish = time.time()
                        dia = wx.MessageDialog(None, u"你赢了~", u"游戏结束",
                                            wx.YES_NO )
                        dia.ShowModal()
                        print("game over")
                        self.__record_win()
                        self.__record_time(self.finish-self.start)
                        self.Close(True)
                        
                except:
                    pass

            def is_game_over(self):
                '''胜利返回true, 失败返回false, 继续返回none'''

                for i in self.game_start_lst:
                    for j in i:
                        if j == self.aim:
                            return True
                

            def think(self, event, get):
                '''思考列表并改变'''
                tp = think(get, self.game_start_lst)
                if tp == False:
                    return False
                self.game_start_lst = tp
                return True

            def add_new(self):
                '''
                新增格子
                return: 失败返回Flase, 成功返回True
                '''
                tp = add(self.game_start_lst, self.game_start_add)
                if tp == False:
                    return False
                self.game_start_lst = tp
                return True

            def write(self):
                '''打印输出'''
                self.grid1.Label = str(self.game_start_lst[0][0])
                self.grid1.Show(False) if self.grid1.Label == "0" else self.grid1.Show(True)
                self.grid1.SetBackgroundColour(wx.Colour(self.colors[int(self.grid1.Label)]))

                self.grid2.Label = str(self.game_start_lst[0][1])
                self.grid2.Show(False) if self.grid2.Label == "0" else self.grid2.Show(True)
                self.grid2.SetBackgroundColour(wx.Colour(self.colors[int(self.grid2.Label)]))

                self.grid3.Label = str(self.game_start_lst[0][2])
                self.grid3.Show(False) if self.grid3.Label == "0" else self.grid3.Show(True)
                self.grid3.SetBackgroundColour(wx.Colour(self.colors[int(self.grid3.Label)]))

                self.grid4.Label = str(self.game_start_lst[0][3])
                self.grid4.Show(False) if self.grid4.Label == "0" else self.grid4.Show(True)
                self.grid4.SetBackgroundColour(wx.Colour(self.colors[int(self.grid4.Label)]))

                self.grid5.Label = str(self.game_start_lst[1][0])
                self.grid5.Show(False) if self.grid5.Label == "0" else self.grid5.Show(True)
                self.grid5.SetBackgroundColour(wx.Colour(self.colors[int(self.grid5.Label)]))

                self.grid6.Label = str(self.game_start_lst[1][1])
                self.grid6.Show(False) if self.grid6.Label == "0" else self.grid6.Show(True)
                self.grid6.SetBackgroundColour(wx.Colour(self.colors[int(self.grid6.Label)]))

                self.grid7.Label = str(self.game_start_lst[1][2])
                self.grid7.Show(False) if self.grid7.Label == "0" else self.grid7.Show(True)
                self.grid7.SetBackgroundColour(wx.Colour(self.colors[int(self.grid7.Label)]))

                self.grid8.Label = str(self.game_start_lst[1][3])
                self.grid8.Show(False) if self.grid8.Label == "0" else self.grid8.Show(True)
                self.grid8.SetBackgroundColour(wx.Colour(self.colors[int(self.grid8.Label)]))

                self.grid9.Label = str(self.game_start_lst[2][0])
                self.grid9.Show(False) if self.grid9.Label == "0" else self.grid9.Show(True)
                self.grid9.SetBackgroundColour(wx.Colour(self.colors[int(self.grid9.Label)]))

                self.grid10.Label = str(self.game_start_lst[2][1])
                self.grid10.Show(False) if self.grid10.Label == "0" else self.grid10.Show(True)
                self.grid10.SetBackgroundColour(wx.Colour(self.colors[int(self.grid10.Label)]))

                self.grid11.Label = str(self.game_start_lst[2][2])
                self.grid11.Show(False) if self.grid11.Label == "0" else self.grid11.Show(True)
                self.grid11.SetBackgroundColour(wx.Colour(self.colors[int(self.grid11.Label)]))

                self.grid12.Label = str(self.game_start_lst[2][3])
                self.grid12.Show(False) if self.grid12.Label == "0" else self.grid12.Show(True)
                self.grid12.SetBackgroundColour(wx.Colour(self.colors[int(self.grid12.Label)]))

                self.grid13.Label = str(self.game_start_lst[3][0])
                self.grid13.Show(False) if self.grid13.Label == "0" else self.grid13.Show(True)
                self.grid13.SetBackgroundColour(wx.Colour(self.colors[int(self.grid13.Label)]))

                self.grid14.Label = str(self.game_start_lst[3][1])
                self.grid14.Show(False) if self.grid14.Label == "0" else self.grid14.Show(True)
                self.grid14.SetBackgroundColour(wx.Colour(self.colors[int(self.grid14.Label)]))

                self.grid15.Label = str(self.game_start_lst[3][2])
                self.grid15.Show(False) if self.grid15.Label == "0" else self.grid15.Show(True)
                self.grid15.SetBackgroundColour(wx.Colour(self.colors[int(self.grid15.Label)]))

                self.grid16.Label = str(self.game_start_lst[3][3])
                self.grid16.Show(False) if self.grid16.Label == "0" else self.grid16.Show(True)
                self.grid16.SetBackgroundColour(wx.Colour(self.colors[int(self.grid16.Label)]))
                

            def __record_win(self):
                '''胜利局数加一'''
                myrecord.record_win()

            def __record_down(self):
                '''失败局数加一'''
                myrecord.record_down()

            def __record_time(self, time):
                '''增加胜利时间'''
                myrecord.record_time(time)
            
            

        start_game_win = Game_start(self)
        start_game_win.Show()

    def record(self, event):
        '''我的战绩'''
        class Record_win(wx.Frame):
            def __init__(self, parent):
                wx.Frame.__init__(self,
                                  parent,
                                  id=wx.ID_ANY,
                                  title=u"战绩",
                                  pos=wx.DefaultPosition,
                                  size=wx.Size(392, 256),
                                  style=wx.DEFAULT_FRAME_STYLE
                                  | wx.TAB_TRAVERSAL)
                self.SetBackgroundColour( wx.Colour( 246, 246, 246 ) )

                sbSizer1 = wx.StaticBoxSizer(
                    wx.StaticBox(self, wx.ID_ANY, u"你的战绩"), wx.VERTICAL)

                self.m_staticText1 = wx.StaticText(sbSizer1.GetStaticBox(),
                                                   wx.ID_ANY, u"普通局",
                                                   wx.DefaultPosition,
                                                   wx.DefaultSize, 0)
                self.m_staticText1.Wrap(-1)
                sbSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

                self.m_staticText2 = wx.StaticText(
                    sbSizer1.GetStaticBox(), wx.ID_ANY,
                    u"     胜利:{}局".format(myrecord.win), wx.DefaultPosition,
                    wx.DefaultSize, 0)
                self.m_staticText2.Wrap(-1)
                sbSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)

                self.m_staticText21 = wx.StaticText(
                    sbSizer1.GetStaticBox(), wx.ID_ANY,
                    u"     失败:{}局".format(myrecord.down), wx.DefaultPosition,
                    wx.DefaultSize, 0)
                self.m_staticText21.Wrap(-1)
                sbSizer1.Add(self.m_staticText21, 0, wx.ALL, 5)

                self.m_staticText2112 = wx.StaticText(
                    sbSizer1.GetStaticBox(), wx.ID_ANY,
                    u"     最高纪录:{}".format(myrecord.max_time() if myrecord.max_time() != False else "暂无"), wx.DefaultPosition,
                    wx.DefaultSize, 0)
                self.m_staticText21.Wrap(-1)
                sbSizer1.Add(self.m_staticText2112, 0, wx.ALL, 5)

                self.m_staticText6 = wx.StaticText(sbSizer1.GetStaticBox(),
                                                   wx.ID_ANY, u"人机对战局",
                                                   wx.DefaultPosition,
                                                   wx.DefaultSize, 0)
                self.m_staticText6.Wrap(-1)
                sbSizer1.Add(self.m_staticText6, 0, wx.ALL, 5)

                self.m_staticText22 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY,
                u"     胜利:{}局".format(myrecord.robot_win),
                    wx.DefaultPosition, wx.DefaultSize, 0)
                self.m_staticText22.Wrap(-1)
                sbSizer1.Add(self.m_staticText22, 0, wx.ALL, 5)

                self.m_staticText221 = wx.StaticText(
                    sbSizer1.GetStaticBox(), wx.ID_ANY,
                    u"     失败:{}局".format(myrecord.robot_down),
                    wx.DefaultPosition, wx.DefaultSize, 0)
                self.m_staticText221.Wrap(-1)
                sbSizer1.Add(self.m_staticText221, 0, wx.ALL, 5)

                self.SetSizer(sbSizer1)
                self.Layout()

                self.Centre(wx.BOTH)

        record_win_root = Record_win(self)
        record_win_root.Show(True)
        

    def robot(self, event):
        pass
        

    def update_log(self, event): #更新日志
        '''更新日志'''
        class UpdateLog ( wx.Frame ):
	
            def __init__( self, parent ):
                wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 580,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
                
                

                self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
                self.SetBackgroundColour( wx.Colour( 246, 246, 246 ) )
                
                fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
                fgSizer1.SetFlexibleDirection( wx.BOTH )
                fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

                
                
                self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"2020.x.xx~2020.07.1x\n2048非ui版成立\n\n2020.07.2x\n2048ui版成立                                         ", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText9.Wrap( -1 )
                fgSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )
                
                self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"2020.07.24\n新增功能:\n新增日志功能, 偷偷的记录你的行为\n新增更新日志, 查找作者的动态~\n\n修复bug:\n方块重叠问题", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText21.Wrap( -1 )
                fgSizer1.Add( self.m_staticText21, 0, wx.ALL, 5 )
                
                self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"2020.07.25\n美化界面, 更符合美观的配色", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText23.Wrap( -1 )
                fgSizer1.Add( self.m_staticText23, 0, wx.ALL, 5 )
                
                self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"2020.07.27\n新增功能:调整难度[by 梦久别、提出]\n修改:\n1, 日志显示\n2, 方块显示的颜色QWQ[by 梦久别、提出]\n3, 删除了记录日志(因为测试中太废了)", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText24.Wrap( -1 )
                fgSizer1.Add( self.m_staticText24, 0, wx.ALL, 5 )

                self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"2020.07.28\n细节优化\n(其中 提示修改 为梦久别、提出\n在此特别感谢大佬♪(･ω･)ﾉ)\n代码整理优化, 添加注释, 准备开源\n正在开发:人机对战, 时间系统\n(时间系统总是出bug啊啊啊)", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText2.Wrap( -1 )
                fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

                self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"2020.07.29\n细节优化\n修复时间系统和战绩系统的bug, 成功发行版本alpha", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText3.Wrap( -1 )
                fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
                
                self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
                self.m_scrolledWindow1.SetScrollRate( 5, 5 )
                fgSizer1.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )
                
                
                self.SetSizer( fgSizer1 )
                self.Layout()
                
                self.Centre( wx.BOTH )
        tp = UpdateLog(self)
        tp.Show()

    def change_mode(self, event): 
        '''难度模式调整'''
        class ChangeMdoe ( wx.Frame ):
	
            def __init__( self, parent ):
                wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"难度/模式调整", pos = wx.DefaultPosition, size = wx.Size( 376,392 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
                
                self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
                self.SetBackgroundColour( wx.Colour( 246, 246, 246 ) )
                
                bSizer1 = wx.BoxSizer( wx.VERTICAL )
                
                sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"难度调整" ), wx.VERTICAL )
                
                self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"目标方块:", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText2.Wrap( -1 )
                self.m_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "微软雅黑" ) )
                
                sbSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
                
                m_choice1Choices = [ u"2048", u"1024", u"512", u"256", u"128", u"64", u"无限模式", wx.EmptyString ]
                self.m_choice1 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
                self.m_choice1.SetSelection( 0 )
                sbSizer1.Add( self.m_choice1, 0, wx.ALL, 5 )

                bSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )
                
                self.m_button1 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
                bSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
                
                
                self.SetSizer( bSizer1 )
                self.Layout()
                
                self.Centre( wx.BOTH )
                # Connect Events
                self.m_button1.Bind( wx.EVT_BUTTON, self.change_mode_yes )
            
            # Virtual event handlers, overide them in your derived class
            def change_mode_yes( self, event ):
                event.Skip()
                aim_index = int(self.m_choice1.GetCurrentSelection())
                lst = [2048, 1024, 512, 256, 128, 64, "forever"] #forever 无限模式
                global aim
                aim = lst[aim_index]
                print(aim)
                self.Close(True)

        tp = ChangeMdoe(self)
        tp.Show(True)

    def __record_robor_win(self, event):
        '''人机对战局胜利场数加一'''
        myrecord.record_robot_win()

    def __record_robor_down(self, event):
        '''人机对战局失败场数加一'''
        myrecord.record_robot_down()


if __name__ == "__main__":
    app = wx.App()
    # None表示的是此窗口没有上级父窗体。如果有，就直接在父窗体代码调用的时候填入‘self’就好了。
    main_win = Calculator(None)
    main_win.run()
    main_win.Show()
    app.MainLoop()
