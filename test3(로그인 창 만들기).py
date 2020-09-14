import wx

class LoginFrame(wx.Frame):
    panel = None

    def __init__(self, parent, title=None, size=(200, 200)):
        super().__init__(parent, title=title, size=size)
        self.loginUI()
        self.Show(True)

    def loginUI(self):
        self.panel = wx.Panel(self)

        wx.StaticText(self.panel, label="ID : ", pos=(5, 5))
        wx.StaticText(self.panel, label="PASS : ", pos=(5, 40))

        self.m_id = wx.TextCtrl(self.panel, pos=(50, 5), size=(200, -1))
        self.m_pw = wx.TextCtrl(self.panel, pos=(50, 40))

        btn1 = wx.Button(self.panel, label="일반 버튼", pos=(5, 100), size=(70, -1))
        btn2 = wx.ToggleButton(self.panel, label="토글 버튼", pos=(90, 100), size=(70, -1))
        btn3 = wx.Button(self.panel, label="종료", pos=(180, 100), size=(70, -1))

        #btn1.Bind(wx.EVT_BUTTON, self.onBtn1)
        #btn2.Bind(wx.EVT_TOGGLEBUTTON, self.onBtn2)
        #btn3.Bind(wx.EVT_BUTTON, self.onBtn3)

        btn1.id, btn2.id, btn3.id = 1, 2, 3
        btn1.Bind(wx.EVT_BUTTON, self.onBtnHandler)
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.onBtnHandler)
        btn3.Bind(wx.EVT_BUTTON, self.onBtnHandler)

    """
    def onBtn1(self, e):
        dlg = wx.MessageDialog(self, "로그인 되었습니다.", "로그인", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

        self.m_id.SetLabelText("tiger")
        self.m_pw.SetLabelText("1111")

    def onBtn2(self, e):
        # print(e.GetEventObject())
        # print(e.GetEventObject().GetValue())
        if e.GetEventObject().GetValue():
            self.panel.SetBackgroundColour(wx.Colour(255, 0, 0))
            self.panel.Refresh()
        else:
            self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))
            self.panel.Refresh()

    def onBtn3(self, e):
        self.Close(True)
    """

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

if __name__ == "__main__":
    app = wx.App()
    LoginFrame(None, "로그인", (300, 180))
    app.MainLoop()