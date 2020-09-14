import wx

class ChildFrame(wx.Frame):
    def __init__(self, parent, title = None, size=(200,200)):
        super().__init__(parent, title = title, size=size)
        self.gui()

    def gui(self):
        # 메뉴 디자인 : 고정식 메뉴(Pull Down), 이동식 메뉴(Popup Down)
        # MenuBar, Menu, MenuItem 을 조합해서 메뉴 생성
        menubar = wx.MenuBar()
        mnuFile = wx.Menu()
        mnuEdit = wx.Menu()

        mnuFile_new = wx.MenuItem(mnuFile, wx.ID_NEW, "New", "New Document")
        mnuFile_open = wx.MenuItem(mnuFile, wx.ID_OPEN, "Open", "파일 열기")
        mnuFile_exit = wx.MenuItem(mnuFile, wx.ID_EXIT, "EXIT", "프로그램 종료")

        mnuFile.Append(mnuFile_new)
        mnuFile.Append(mnuFile_open)
        mnuFile.AppendSeparator()                                     # 구분선 표기
        mnuFile.Append(mnuFile_exit)
        menubar.Append(mnuFile, "파일")
        menubar.Append(mnuEdit, "편집")
        self.SetMenuBar(menubar)

        self.txtA = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        self.Bind(wx.EVT_MENU, self.onNew, mnuFile_new)
        self.Bind(wx.EVT_MENU, self.onOpen, mnuFile_open)
        self.Bind(wx.EVT_MENU, self.onExit, mnuFile_exit)

        #self.Move(100,50) # 원하는 위치에서 프로그램 실행
        self.Center()  # 프로그램이 화면 정가운데에서 실행
        self.Show(True)

    def onNew(self, ev):  # 접두에 on이 추가되면 이벤트 코드
        self.txtA.SetLabelText("새 문서를 선택하였습니다.")
    def onOpen(self, ev):
        self.txtA.SetLabelText("파일 열기를 선택하였습니다.")
        f = open("C:\\Users\\song1\\acorn\\python_window\\사전작업.txt", "r", encoding="utf8")
        data = f.read()
        self.txtA.SetLabelText(data)
        f.close()

    def onExit(self, ev):
        self.txtA.SetLabelText("프로그램 종료를 선택하였습니다.")
        self.Close(True)     # close : 일반 종료 , exit : 강제종료


if __name__ == "__main__":
    app = wx.App()
    frame = ChildFrame(None, "간단한 메모장 프로그램", (400, 600))
    app.MainLoop()