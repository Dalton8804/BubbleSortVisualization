from tkinter import *
import time
import random
#class rectangle(self, height):


root = Tk()
root.geometry('500x560+600+200')
root.title('Bubble Sort')
canv = Canvas(root, height = 425, width = 500)
incr = 50
numoflines = 50
amt = 8
bottom = 500
rects = []
templi = []
Label(root, text='Bubble Sort Visualization', font=('Symbol', 30)).grid(row=0,column=0, columnspan=2)

def createlines(num):
	global incr
	bottom = 500
	for x in num:
	#	if x == Diff():
	#		canv.create_line(incr,bottom,incr,400-x*amt, fill='red')
	#	else:
		canv.create_line(incr,bottom,incr,400-x*amt)
		incr+=amt
		
	canv.grid(row=1,column=0, columnspan=2)

#def Diff():
#
#	global templi,rects
#	#print(templi)
#	for i in range(len(templi)):
#		if templi[i] != rects[i]:
#			num = rects[i]
#			#templi = rects[:]
#			return num
#
#	templi = rects[:]

def clearcanv():
	#rects.clear()
	global incr
	incr = 50
	canv.delete('all')

def randlines():
	global templi,rects
	templi = [None]*numoflines
	rects = [None]*numoflines
	clearcanv()
	for i in range(numoflines):
		rects[i] = i
	for i in range(numoflines):
		rand = random.randint(0,numoflines-1)
		rects[i], rects[rand] = rects[rand], rects[i]
	#print(rects)
	templi = rects[:]
	createlines(rects)

def bubblesort(list):
	for iter_num in range(len(list)-1,0,-1):
		for idx in range(iter_num):
			if list[idx]>list[idx+1]:
				templi = list.copy()
				temp = list[idx]
				list[idx] = list[idx+1]
				list[idx+1] = temp
				#print(list)
				#print(templi)
				clearcanv()
				createlines(list)
				canv.update()

	completed()
def drawgreen(num):
	global bottom, incr, amt
	clearcanv()
	for i in range(num):
		canv.create_line(incr, bottom, incr, 400-i*amt, fill='green')
		incr+=amt
	for i in range(num, len(rects)):
		canv.create_line(incr, bottom, incr, 400-i*amt)
		incr+=amt

def completed():
	for i in range(numoflines+1):
		drawgreen(i)
		canv.update()


def startbubblesort():
	bubblesort(rects)

def fiftyline():
	global amt, numoflines
	amt, numoflines = 8, 50
	randlines()
def hunline():
	global amt, numoflines
	amt, numoflines = 4, 100
	randlines()
def twohun():
	global amt, numoflines
	amt, numoflines = 2, 200
	randlines()
def fourhun():
	global amt, numoflines
	amt, numoflines =1, 400
	randlines()

randlines()
hundredlines = Button(root, command=fiftyline, text='50 Lines').grid(row=2,column=0)
hundredlines = Button(root, command=hunline, text='100 Lines').grid(row=2,column=1)
twohundredlines = Button(root, command=twohun, text='250 Lines').grid(row=3,column=0)
fourhundredlines = Button(root, command=fourhun, text='500 Lines').grid(row=3,column=1)
drawrand = Button(root, command=randlines, text='Rearrange', height=2, width=20).grid(row=4,column=0)
#clearbutton = Button(root, command=clearcanv, text='clear').pack()
bubblesortbutton = Button(root, command=startbubblesort, text='Sort', height=2, width=20).grid(row=4,column=1)

root.mainloop()