import wx

class MainFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,"Gitz \/ Repo",size=(600,340))
		panel = wx.Panel(self,-1)
		panel.SetBackgroundColour('WHITE')
		img_sut_logo = wx.Image("./images/sut_logo.png",wx.BITMAP_TYPE_PNG)
		wx.StaticBitmap(panel, -1, wx.BitmapFromImage(img_sut_logo),(20,20)) 
		
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MainFrame()

	frame.Centre()
	frame.Show(True)
	app.MainLoop()
