import wx

"""
Dialog(대화 상자)
-----------------
1. Built in Dialog
    - Common Dialog(공통 대화상자), System Dialog

2. User Define Dialog

3. 실행 방식
    1) modal
    2) modaless
"""


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

        menuBar.Append(menu, "다이얼로그")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.onMessage, id=100)
        self.Bind(wx.EVT_MENU, self.onColor, id=101)
        self.Bind(wx.EVT_MENU, self.onFile, id=102)

    def onMessage(self, e):
        self.SetStatusText("메시지 대화상자 선택")
        dlg = wx.MessageDialog(self, "오늘 하루도 열심히...", "메시지박스", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()

    def onColor(self, e):
        self.SetStatusText("색상 대화상자 선택")
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)
        dlg.ShowModal()

    def onFile(self, e):
        self.SetStatusText("파일 대화상자 선택")
        dlg = wx.FileDialog(self, "파일 선택", style=wx.ID_OPEN)
        dlg.ShowModal()


if __name__ == "__main__":
    app = wx.App()
    MainFrame(None, "다이얼로그 연습", (600, 400))
    app.MainLoop()