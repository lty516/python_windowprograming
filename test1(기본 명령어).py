import wx

app = wx.App()      # window 프로그램을 만들때 필수적으로 생성하는 객체
frame = wx.Frame(None, title ="test1 입니다. ")  # window를 만들어 주는 기본적인 객체
frame.Show(True)        # 만들어진 window를 화면에 보여주는 명령어
app.MainLoop()      # 반복적으로 화면에 띄우는 명령어
