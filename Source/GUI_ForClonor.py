#################################################################################################

#For this to work we at least need wx, subprocess and os

import wx, subprocess, os

##################################################################################################
#	###################
#	GENERAL CLASS FORMATS RELATING TO WIDGETS FOR ALL PANELS AND WINDOWS

class Button1(wx.Button):
	'''Generic Button Class'''
	def __init__(self, parent2, label2, name2):
		
		wx.Button.__init__(self, parent=parent2, label=label2, name=name2,
				   id=wx.ID_ANY, size=(75, 22))

class TextCtrl1(wx.TextCtrl):

	def __init__(self, parent2, value2):
		
		wx.TextCtrl.__init__(self, parent=parent2, value=value2,
				   id=wx.ID_ANY, size=(300, 20))


class StaticText1(wx.StaticText):

	def __init__(self, parent2, label2, font):
	
		wx.StaticText.__init__(self, parent=parent2, label=label2,
					id=wx.ID_ANY)
		self.SetFont(font)

#################################################################################################
##################################################
#	SETTINGS PRIORS AND OTHER ATTRIBUTES PANEL

      
class SetPriorsPanel(wx.Panel):

	def __init__(self, parent2):

		wx.Panel.__init__(self, parent=parent2,
				id=wx.ID_ANY, size = (600,600))

		self.SetBackgroundColour('white')

		#################################################################

		TextFont1 = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)	
		TextFont1.SetPointSize(14)

		#################################################################

		vbox = wx.BoxSizer(wx.VERTICAL)
		
		hboxInit0 = wx.BoxSizer(wx.HORIZONTAL)
		hboxInit0.Add(StaticText1(self, 'a', TextFont1), proportion = 0, flag=wx.RIGHT, border=15)
		self.TCtrla = TextCtrl1(self, 'NULL')
		hboxInit0.Add(self.TCtrla, proportion = 0)
		vbox.Add(hboxInit0, proportion = 0, flag= wx.ALIGN_CENTER, border = 50)
		vbox.Add((-1,30))

		hboxInit1 = wx.BoxSizer(wx.HORIZONTAL)
		hboxInit1.Add(StaticText1(self, 'X', TextFont1), proportion = 0, flag=wx.RIGHT, border=15)
		self.TCtrlX = TextCtrl1(self, 'NULL')
		hboxInit1.Add(self.TCtrlX, proportion = 0)
		vbox.Add(hboxInit1, proportion = 0, flag= wx.ALIGN_CENTER, border = 50)
		vbox.Add((-1,30))

		hboxInit2 = wx.BoxSizer(wx.HORIZONTAL)
		hboxInit2.Add(StaticText1(self, 'Y', TextFont1), proportion = 0, flag=wx.RIGHT, border=15)
		self.TCtrlY = TextCtrl1(self, 'NULL')
		hboxInit2.Add(self.TCtrlY, proportion = 0)
		vbox.Add(hboxInit2, proportion = 0, flag= wx.ALIGN_CENTER, border = 50)
		vbox.Add((-1,30))

		hboxInit3 = wx.BoxSizer(wx.HORIZONTAL)
		hboxInit3.Add(StaticText1(self, 'Z', TextFont1), proportion = 0, flag=wx.RIGHT, border=15)
		self.TCtrlZ = TextCtrl1(self, 'NULL')
		hboxInit3.Add(self.TCtrlZ, proportion = 0)
		vbox.Add(hboxInit3, proportion = 0, flag= wx.ALIGN_CENTER, border = 50)
		vbox.Add((-1,30))
		
		hboxInit4 = wx.BoxSizer(wx.HORIZONTAL)
		hboxInit4.Add(StaticText1(self, 'D', TextFont1), proportion = 0, flag=wx.RIGHT, border=15)
		self.TCtrlD = TextCtrl1(self, 'NULLAGAIN')
		hboxInit4.Add(self.TCtrlD, proportion = 0)
		vbox.Add(hboxInit4, proportion = 0, flag= wx.ALIGN_CENTER, border = 50)
		vbox.Add((-1,30))

		hboxInit5 = wx.BoxSizer(wx.HORIZONTAL)
		hboxInit5.Add(StaticText1(self, 'T', TextFont1), proportion = 0, flag=wx.RIGHT, border=15)
		self.TCtrlT = TextCtrl1(self, 'NULL')
		hboxInit5.Add(self.TCtrlT, proportion = 0)
		vbox.Add(hboxInit5, proportion = 0, flag= wx.ALIGN_CENTER, border = 50)
		vbox.Add((-1,30))

		hboxInit6 = wx.BoxSizer(wx.HORIZONTAL)
		hboxInit6.Add(StaticText1(self, 'R', TextFont1), proportion = 0, flag=wx.RIGHT, border=15)
		self.TCtrlR = TextCtrl1(self, 'NULL')
		hboxInit6.Add(self.TCtrlR, proportion = 0)
		vbox.Add(hboxInit6, proportion = 0, flag= wx.ALIGN_CENTER, border = 50)
		vbox.Add((-1,30))

		self.SetSizer(vbox)

	def Givea(self):
		return(self.TCtrla.GetValue())

	def GiveX(self):
		return(self.TCtrlX.GetValue())

	def GiveY(self):
		return(self.TCtrlY.GetValue())
	
	def GiveZ(self):
		return(self.TCtrlZ.GetValue())

	def GiveD(self):
		return(self.TCtrlD.GetValue())

	def GiveT(self):
		return(self.TCtrlT.GetValue())

	def GiveR(self):
		return(self.TCtrlR.GetValue())

##################################################################################################
#	##################
#	INITIATION PANEL

class InitiateCOPanel(wx.Panel):

	def __init__(self, parent2):

		wx.Panel.__init__(self, parent=parent2,
				id=wx.ID_ANY, size = (600,600))

		self.SetBackgroundColour('white')

		#################################################################
	
		TextFont1 = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)	
		TextFont1.SetPointSize(14)


		self.CurrentDir = os.getcwd()
		ImportBrowse = Button1(self, 'Import', 'Import the data')
		NewickBrowse = Button1(self, 'Newick', 'Import Newick')
		OutputBrowse = Button1(self, 'Export', 'Choose Export file')
		

		##################################################################

		vbox = wx.BoxSizer(wx.VERTICAL)
		
		hboxInit1 = wx.BoxSizer(wx.HORIZONTAL)
		hboxInit1.Add(StaticText1(self, 'Insert Newick File', TextFont1), proportion = 0, flag=wx.RIGHT, border=15)
		self.TCtrlNewick = TextCtrl1(self, '*.nwk')
		hboxInit1.Add(self.TCtrlNewick, proportion = 0)
		hboxInit1.Add(NewickBrowse, proportion = 0)
		vbox.Add(hboxInit1, proportion = 0, flag= wx.ALIGN_CENTER, border = 50)
		vbox.Add((-1,50))

		hboxInit2 = wx.BoxSizer(wx.HORIZONTAL)
		hboxInit2.Add(StaticText1(self, 'Insert Fasta File', TextFont1), proportion = 0, flag=wx.RIGHT, border=15)
		self.TCtrlFasta = TextCtrl1(self, '*.xmfa')
		hboxInit2.Add(self.TCtrlFasta, proportion = 0)
		hboxInit2.Add(ImportBrowse, proportion = 0)
		vbox.Add(hboxInit2, proportion = 0, flag= wx.ALIGN_CENTER, border = 50)
		vbox.Add((-1,50))

		hboxInit3 = wx.BoxSizer(wx.HORIZONTAL)
		hboxInit3.Add(StaticText1(self, 'Insert Output File', TextFont1), proportion = 0, flag=wx.RIGHT, border=15)
		self.TCtrlOutput = TextCtrl1(self, '*.out')
		hboxInit3.Add(self.TCtrlOutput, proportion = 0)
		hboxInit3.Add(OutputBrowse, proportion = 0)
		vbox.Add(hboxInit3, proportion = 0, flag= wx.ALIGN_CENTER, border = 50)
		vbox.Add((-1,50))

		self.SetSizer(vbox)

#		###################################################################
#		ALL EVENTS RELATING TO SPECIFIC PANEL

		ImportBrowse.Bind(wx.EVT_BUTTON, self.ImportFile)
		NewickBrowse.Bind(wx.EVT_BUTTON, self.NewickFile)
		OutputBrowse.Bind(wx.EVT_BUTTON, self.OutputFile)

#		###################################################################
#		ALL FUNCTIONS RELATING TO SPECIFIC PANEL

	def ImportFile(self, event):

		wildcard1 = "eXtended Multi-FastA File (*.xmfa)|*.xmfa|" \
            	"All files (*.*)|*.*"

		dlg = wx.FileDialog(self, message="Choose a file:",
		defaultDir=self.CurrentDir,
		defaultFile="", wildcard=wildcard1,
		style= wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR 
		)
		
		if dlg.ShowModal() == wx.ID_OK:
			paths = dlg.GetPaths()
#			print("You chose the following file(s):")
#			for path in paths:
#				print(path)
			self.TCtrlFasta.SetValue(paths[0])			
			dlg.Destroy()

	def NewickFile(self, event):

		wildcard3 = "Newick/Nexus File (*.nwk)|*.nwk|" \
            	"All files (*.*)|*.*"
		
		dlg = wx.FileDialog(self, message="Choose a file:",
		defaultDir=self.CurrentDir,
		defaultFile="", wildcard=wildcard3,
		style= wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR 
		)
		
		if dlg.ShowModal() == wx.ID_OK:
			paths = dlg.GetPaths()
#			print("You chose the following file(s):")
#			for path in paths:
#				print(path)
			self.TCtrlNewick.SetValue(paths[0])
			dlg.Destroy()

	def OnQuit(self, event):
		self.Close()

	def OutputFile(self, event):

		wildcard2 = "Out-File (*.out)|*.out|" \
		"Extensible Markup Language File (*.xml)|*.xml|" \
            	"All files (*.*)|*.*"

		dlg = wx.FileDialog(self, message="Choose a file:",
		defaultDir=self.CurrentDir,
		defaultFile="", wildcard=wildcard2,
		style= wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR 
		)
		
		if dlg.ShowModal() == wx.ID_OK:
			paths = dlg.GetPaths()
#			print("You chose the following file(s):")
#			for path in paths:
#				print(path)
			self.TCtrlOutput.SetValue(paths[0])
			dlg.Destroy()


	def GiveNewick(self):
		return(self.TCtrlNewick.GetValue())

	def GiveFasta(self):
		return(self.TCtrlFasta.GetValue())
	
	def GiveOutput(self):
		return(self.TCtrlOutput.GetValue())


##################################################################################################
#################################################
#	MAIN APPLICATION AND GENERAL 

class GenFrame(wx.Frame): 
	
	def __init__(self, parent2, title2): 

		wx.Frame.__init__(self, parent=parent2, title=title2, id=wx.ID_ANY, size=(600, 650))
		self.Centre()
		
		self.MyUI()

	def MyUI(self):
	
#		###################
#		ALL SET VARIABLES AND CONSTANTS, SUCH AS FONTS AND DIRECTORIES

		TextFont1 = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)	
		TextFont1.SetPointSize(14)

#		###################
#		MENUS, STATUSBARS AND SIDEBARS

		menubar=wx.MenuBar()

		fileMenu = wx.Menu()
		switchItem = fileMenu.Append(wx.ID_ANY, 'Switch Panels', 'Switch to a different panel')
		fileMenu.AppendSeparator()
		exitItem = fileMenu.Append(wx.ID_ANY, 'Quit', 'Quit application (ctrl+Q)')
		
		viewMenu=wx.Menu()
		self.StatusItem = viewMenu.Append(wx.ID_ANY, 'Show Statusbar', 
		'Show Statusbar', kind=wx.ITEM_CHECK)
		viewMenu.Check(self.StatusItem.GetId(), True)
		
		menubar.Append(fileMenu, '&File')
		menubar.Append(viewMenu, '&View')
		self.SetMenuBar(menubar)

#		###################
#		WINDOWS/PANELS/SIZERS/BUTTONS/
		
		self.SetPriors = SetPriorsPanel(self)
		self.InitiateCO = InitiateCOPanel(self)
		self.InitiateCO.Hide()

		CreatePanel = wx.Panel(self, id=wx.ID_ANY, size=(600,50))
		CreatePanel.SetBackgroundColour('white')
		
		CreateSizer = wx.BoxSizer(wx.HORIZONTAL)
		self.Click = Button1(CreatePanel, 'Click', 'Click the button')
		CreateSizer.Add(self.Click, proportion = 0, flag = wx.ALIGN_RIGHT)
		Terminate = Button1(CreatePanel, 'Terminate', 'Terminate the process')
		CreateSizer.Add(Terminate, proportion = 0, flag = wx.ALIGN_RIGHT)
		CreatePanel.SetSizer(CreateSizer)

		self.MainSizer = wx.BoxSizer(wx.VERTICAL)
		self.MainSizer.Add(self.SetPriors, 1, wx.EXPAND)
		self.MainSizer.Add(self.InitiateCO, 1, wx.EXPAND)
		self.MainSizer.Add(CreatePanel, 0, wx.EXPAND)
		self.SetSizer(self.MainSizer) 

#		###################
#		SCROLLBARS/STATUSBARS

		self.Statusbar = self.CreateStatusBar()
#		self.Statusbar = wx.StatusBar()
		self.Statusbar.SetBackgroundColour('white')

#		###################
#		ALL EVENTS REGARDING MAIN MENU

		self.Bind(wx.EVT_MENU, self.OnQuit, exitItem)
		self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

		self.Bind(wx.EVT_MENU, self.OnSwitchPanels, switchItem)
		self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.StatusItem)

		self.Click.Bind(wx.EVT_BUTTON, self.InitiateClonor)
		Terminate.Bind(wx.EVT_BUTTON, self.TerminateProcess)
#		################################
#		ALL FUNCTIONS LEADING TO EVENTS WITHIN MENU(in alphapetical order)

	def InitiateClonor(self, event):
	
		self.Click.Disable()		

		IP = self.InitiateCO.GiveFasta()
		NP = self.InitiateCO.GiveNewick()
		OP = self.InitiateCO.GiveOutput()
		aP = self.SetPriors.Givea()
		XP = self.SetPriors.GiveX()
		YP = self.SetPriors.GiveY()
		ZP = self.SetPriors.GiveZ()
		DP = self.SetPriors.GiveD()
		TP = self.SetPriors.GiveT()
		RP = self.SetPriors.GiveR()
		self.proc = subprocess.call(['Clonor', '-a', aP, '-x', XP, '-y', YP, '-z', ZP, 
				'-D', DP, '-T', TP, '-R', RP, NP, IP, OP])

#		poll = self.proc.poll()
#		if poll != None:
#			self.Click.Enable()

	def OnCloseWindow(self, event):

		dial = wx.MessageDialog(None, 'Are you sure you want to quit', 'Question',
		wx.YES_NO |wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = dial.ShowModal()

		if ret == wx.ID_YES:
			self.Destroy()
		else:
			event.Veto()
	
	def OnQuit(self, event):
		self.Close()

	def OnSwitchPanels(self, event):
		if self.SetPriors.IsShown():
			self.SetTitle("Panel 2 is showing")
			self.SetPriors.Hide()
			self.InitiateCO.Show()
		else:
			self.SetTitle("Panel 1 is showing")
			self.SetPriors.Show()
			self.InitiateCO.Hide()
		self.Layout()

	def TerminateProcess(self, event):
		self.proc.terminate()
		self.Click.Enable()

	def ToggleStatusBar(self, event):
		if self.StatusItem.IsChecked():
			self.Statusbar.Show()
		else:
			self.Statusbar.Hide()
		self.Layout()
		
##################################################################################################
##################################################################################################

app = wx.App()
frame = GenFrame(None, 'Loading onto of Clonal Origin')
frame.Show()
app.MainLoop()

#################################################################################################
