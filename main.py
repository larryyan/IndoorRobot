import tkinter as tk
#from tkinter import *
import requests
#import api
import webbrowser

#version information
TitleName = 'TestDemo'
Version = '0.1.0'


#define Window
window = tk.Tk()
window.title(f'{TitleName}  {Version}')
window.geometry('800x600')
var=tk.StringVar()


#define variables
ServerIP = '192.168.100.76'
Port = 8081
LinkAddress = None
KeyWord = None
SearchMode = None
SearchResult = None

MapLink = None
CallNo = None
SearchResultSorted = None
SelectedBooks = None


'''
MapLink = f'http://192.168.100.133:8080/cgi-bin/BookLocation.exe?barcode={CallNo}'

CallNo_Sample：Z0192036
'''

def Search():
    global SearchMode
    global KeyWord
    global LinkAddress
    SearchMode = 'TITLE'
    KeyWord = InputBox.get()
    LinkAddress = f'http://{ServerIP}:{Port}/datasnap/rest/TInterFace/searchbook/{SearchMode}/{KeyWord}'
    SearchResult = requests.get(LinkAddress).json()
    print(SearchResult)





SearchButton=tk.Button(window,text='Search',
                       font=('Arial',20),relief=tk.GROOVE,bg='azure',
                       command=Search)
SearchButton.pack(side=tk.RIGHT,
                  expand=tk.NO,
                  ipadx=30,ipady=10,
                  anchor=tk.NE)


InputBox=tk.Entry(window,width=20,font=('Arial',20))
InputBox.pack(side=tk.TOP,
              expand=tk.NO,
              ipady=20,
              fill=tk.X,
              anchor=tk.N)

def BookAdd():
    global SelectedBooks
    value=lb.get(lb.curselection())
    lb2.insert('end',str(value))
    #SelectedBooks=list(set(SelectedBooks))
    


def BookRemove():
    
    #value=lb2.get(lb.curselection())
    #缺少删除指定内容的函数
    lb2.delete(0,tk.END)


BookAddButton=tk.Button(window,text='Add Select To BookList',
                        font=('Arial',20),bg='azure',command=BookAdd)

BookAddButton.pack(side=tk.TOP,
                   expand=tk.NO,
                   ipadx=20,ipady=5,
                   anchor=tk.W,)



BookdeclineButton=tk.Button(window,text='Remove from BookList',
                            font=('Arial',20),bg='azure',command=BookRemove)
BookdeclineButton.pack(side=tk.TOP,
                   expand=tk.YES,
                   ipadx=20,ipady=5,

                   anchor=tk.E)



sb2=tk.Scrollbar(window)
sb2.pack(side=tk.RIGHT,fill=tk.Y)
sb=tk.Scrollbar(window)
sb.pack(side=tk.LEFT,fill=tk.Y)




lb=tk.Listbox(window,listvariable=SearchResultSorted,
              width=40, relief=tk.GROOVE,yscrollcommand=sb.set)
lb.pack(side=tk.LEFT,
              expand=tk.YES,
              #anchor=tk.NW,
              fill=tk.Y,
              ipady=160,

              )


lb2=tk.Listbox(window,listvariable=SelectedBooks,
               width=40, relief=tk.GROOVE,yscrollcommand=sb2.set)
lb2.pack(side=tk.RIGHT,
              expand=tk.YES,
              #anchor=tk.NE,
              fill=tk.Y,
              ipady=160,

              )




for i in range(1000):
    lb.insert('end',str(i))
    #lb2.insert('end',str(i))

sb.config(command=lb.yview)
sb2.config(command=lb2.yview)






'''
lb2=tk.Listbox(window,listvariable=SelectedBooks)
lb2.pack(side=tk.RIGHT,
              #anchor=tk.NE,
              expand=tk.YES,
              fill=tk.Y,
              ipadx=60)


lb=tk.Listbox(window,listvariable=SearchResultSorted)
lb.pack(side=tk.LEFT,
              #anchor=tk.NW,
              expand=tk.YES,
              fill=tk.Y,
              ipadx=90)


l=tk.Label(window,textvariable=var,
           bg='azure',font=('Arial',12),
           width=20,height=2)
l.pack(side=tk.LEFT,expand=tk.NO)

'''

window.mainloop()