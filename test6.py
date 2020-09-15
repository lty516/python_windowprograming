import wx

class MainFrame(wx.Frame):
    def __init__(self, parent, title=None, size=(200, 200)):
        super().__init__(parent, title=title, size=size)

        panel1 = wx.Panel(self, style=wx.SUNKEN_BORDER)
        panel1.SetBackgroundColour("RED")

        panel2 = wx.Panel(self, style=wx.SUNKEN_BORDER)
        panel2.SetBackgroundColour("BLUE")

        box = wx.BoxSizer(wx.VERTICAL)    # VERTICAL: 수평 , HORIZONTAL : 수직
        box.Add(panel1, 1, wx.EXPAND)
        box.Add(panel2, 1, wx.EXPAND)

        self.SetSizer(box)

        self.Show(True)

if __name__ == "__main__":
    app = wx.App()
    MainFrame(None, "Layout Manager", (600, 600))
    app.MainLoop()