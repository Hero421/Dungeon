from tkinter import Tk, BOTH, Listbox, StringVar, END, W, E
from tkinter.ttk import Frame, Label, Button, Entry, Style
from sys import exit
from time import sleep

import Dungeon

global_index = 0

class RootFrame(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)   
		self.parent = parent
		self.initUI()

	def initUI(self):

		global global_index

		#Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

		self.input = StringVar()
		self.map = StringVar()

		self.parent.title('Dungeon')
		self.pack(fill=BOTH, expand=1)

		frame1 = Frame(self)
		frame1.grid(row=0, column=0)

		from module_links import ses_area

		map_ = Label(frame1, text=self.map)
		map_['text'] = self.map
		map_.grid(row=0, column=0)

		frame2 = Frame(self)
		frame2.grid(row=1, column=0)

		for column in range(5):
			frame2.columnconfigure(column, pad=10)

		for row in range(3):
			frame2.rowconfigure(row, pad=3)

		Input_area = Label(frame2, textvariable=self.input)
		Input_area.grid(row=0, columnspan=5)
		
		Up_button = Button(frame2, text='^')
		Up_button.grid(row=1, column=3)

		Right_button = Button(frame2, text='>')
		Right_button.grid(row=2, column=4)

		Down_button = Button(frame2, text='v')
		Down_button.grid(row=2, column=3)

		Left_button = Button(frame2, text='<')
		Left_button.grid(row=2, column=2)

		Turn_button = Button(frame2, text='End turn', command=self.onTapOnTurnButton)
		Turn_button.grid(row=4, columnspan=5)
		
		Quit_button = Button(self, text='Quit', command= lambda: exit(self)).grid(row=3, column=0)

	#def onSelect(self, val):
		#sender = val.widget
		#idx = sender.curselection()
		#value = sender.get(idx)   

		#self.var.set(value)

	def onTapOnTurnButton(self):
		
		from module_links import ses_area
		
		self.map = ses_area.create_map()

def main():
	root = Tk()
	Rf = RootFrame(root)
	#root.overrideredirect(1)
	#root.state('zoomed')
	root.mainloop()

if __name__ == '__main__':
	main()