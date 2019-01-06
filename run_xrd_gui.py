from tkinter import *
import xrd_graphs

root=Tk()
root.title('xrd数据可视化')
root.geometry('300x200')

def func():
	dirpath=entry.get()
	xrd_graphs.main(dirpath)
e=StringVar()
entry=Entry(root,textvariable=e)
e.set('输入文件地址...')
entry.pack()
button=Button(root,text='run',command=func)
button.pack()
root.mainloop()
