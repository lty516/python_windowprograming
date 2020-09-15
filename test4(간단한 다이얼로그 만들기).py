import wx
import os

"""
Dialog(대화 상자)
-----------------
1. Built in Dialog
    - Common Dialog(공통 대화상자), System Dialog

2. User Define Dialog

3. 실행 방식 //다이얼로그 방식에는 두가지 실행 방법이 있다. 윈도우처럼 show만 한다고 되는 것이 아님
    1) madal        // 현재 실행하는 다이얼로그(ex. 메시지 다이얼로그)에만 집중. 다른 다이얼로그는 병행할 수 없다.
    2) modaless         // 현재 다이얼로그를 종료하지 않아도 다른 작업과 병행할 수 있는 방식. ex)메모장- 내용 아무거나 입력 - 편집 - 찾기
"""

class LoginFrame(wx.Dialog):
    panel = None

    def __init__(self, parent, title=None, size=(200, 200)):
        super().__init__(parent, title=title, size=size)
        self.loginUI()

    def loginUI(self):
        self.panel = wx.Panel(self)

        wx.StaticText(self.panel, label="ID : ", pos=(5, 5))
        wx.StaticText(self.panel, label="PASS : ", pos=(5, 40))

        self.m_id = wx.TextCtrl(self.panel, pos=(50, 5), size=(200, -1))
        self.m_pw = wx.TextCtrl(self.panel, pos=(50, 40))

        btn1 = wx.Button(self.panel, label="일반 버튼", pos=(5, 100), size=(70, -1))
        btn2 = wx.ToggleButton(self.panel, label="토글 버튼", pos=(90, 100), size=(70, -1))
        btn3 = wx.Button(self.panel, label="종료", pos=(180, 100), size=(70, -1))

        btn1.id, btn2.id, btn3.id = 1, 2, 3
        btn1.Bind(wx.EVT_BUTTON, self.onBtnHandler)
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.onBtnHandler)
        btn3.Bind(wx.EVT_BUTTON, self.onBtnHandler)

    def onBtnHandler(self, e):
        # print(e.GetEventObject().id)
        if e.GetEventObject().id == 1:
            dlg = wx.MessageDialog(self, "로그인 되었습니다.", "로그인", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()

            self.m_id.SetLabelText("tiger")
            self.m_pw.SetLabelText("1111")
        elif e.GetEventObject().id == 2:
            if e.GetEventObject().GetValue():
                self.panel.SetBackgroundColour(wx.Colour(255, 0, 0))
                self.panel.Refresh()
            else:
                self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))
                self.panel.Refresh()
        else:
            self.Close(True)

class MainFrame(wx.Frame):
    def __init__(self, parent, title=None, size=(200, 200)):
        super().__init__(parent, title=title, size=size)
        self.memoUI()
        self.Show(True)

    def memoUI(self):
        self.CreateStatusBar()

        menuBar = wx.MenuBar()
        menu = wx.Menu()

        menu.Append(100, "Message Dialog", "메시지 대화상자 보이기")
        menu.Append(101, "Color Dialog", "색상 대화상자 보이기")
        menu.Append(102, "File Dialog", "파일 대화상자 보이기")
        menu.Append(200, "Login", "로그인 대화상자 보이기")

        menuBar.Append(menu, "다이얼로그")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.onMessage, id=100)
        self.Bind(wx.EVT_MENU, self.onColor, id=101)
        self.Bind(wx.EVT_MENU, self.onFile, id=102)
        self.Bind(wx.EVT_MENU, self.onLogin, id=200)

    def onMessage(self, e):
        self.SetStatusText("메시지 대화상자 선택")
        dlg = wx.MessageDialog(self, "오늘 하루도 열심히...", "메시지박스", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()

    def onColor(self, e):
        self.SetStatusText("색상 대화상자 선택")
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)     # 더 많은 색을 선택할 수 있게 해주는 옵션

        if dlg.ShowModal() == wx.ID_OK:
            color = dlg.GetColourData()             # print로 찍어보면 색깔이 하나의 객체(주소)를 가지는 것을 볼 수 있다
            print(color.GetColour().Get())
            self.SetStatusText("당신이 선택한 색상은 {} 입니다." .format(str(color.GetColour().Get())))

    def onFile(self, e):
        self.SetStatusText("파일 대화상자 선택")
        dlg = wx.FileDialog(self, "파일 선택", "C:\\", "", "*.*", style=wx.ID_OPEN)

        if dlg.ShowModal() == wx.ID_Ok:
            path = dlg.GetPaths()
            print(path)
            filename = os.path.basename(path)
            print(filename)
            self.SetStatusText("당신이 선택한 파일은 {} 입니다.".format(filename))

    def onLogin(self, e):
        self.SetStatusText("로그인 대화 상자 선택")

        dlg = LoginFrame(None, "로그인", (300, 180))
        dlg.ShowModal()
        dlg.Destroy()

if __name__ == "__main__":
    app = wx.App()
    MainFrame(None, "다이얼로그 연습", (600, 400))
    app.MainLoop()