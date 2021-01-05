import tkinter as tk
# from tkinter import *
import BookSearch_api
# import webbrowser

# version information
TitleName = 'TestDemo'
Version = '0.1.2'
# 谢邀，本人代码是逆练出来的，请谅解

# define Window
window = tk.Tk()
window.title(f'{TitleName}  {Version}')
window.geometry('800x600')
var = tk.StringVar()


# define variables
'''
ServerIP = '192.168.100.76'
Port = 8081
'''

LinkAddress = None
KeyWord = None
SearchMode = None
SearchResult = None
SearchResultNo = None

MapLink = None
CallNo = None
SearchResultSorted = []
SelectedBooks = None
SelectedBooksInfo = []

Position = 0


def Debug():
    print('=====================DEBUG INFORMATION=====================')
    print('SelectedBooks:', SelectedBooks)
    print('SelectedBooksInfo:', SelectedBooksInfo)
    print('SearchResultSorted[Position]:', SearchResultSorted[Position])
    print('Position:', Position)
    print('CallNo:', CallNo)


'''
# NOTE PADE
MapLink = f'http://192.168.100.133:8080/cgi-bin/BookLocation.exe?barcode={CallNo}'
CallNo_Sample：Z0192036

lb=>RawInfoBox
lb2=>SelectedBox
sb=>Scorllbar for lb
sb2=>Scorllbar for lb2


'''


'''
#the older version of the independent Search function
def Search():
    global SearchMode
    global KeyWord
    global LinkAddress
    SearchMode = 'TITLE'
    KeyWord = InputBox.get()
    LinkAddress = f'http://{ServerIP}:{Port}/datasnap/rest/TInterFace/searchbook/{SearchMode}/{KeyWord}'
    SearchResult = requests.get(LinkAddress).json()
    print(SearchResult)
'''


# This Function is still testing
def Search():
    global SearchMode
    global KeyWord
    global LinkAddress
    global SearchResultSorted
    SearchMode = 'TITLE'
    KeyWord = InputBox.get()
    SearchResultSorted = BookSearch_api.SearchTitleNumber(SearchMode, KeyWord)
    print(SearchResultSorted)   # Debug

    for i in range(len(SearchResultSorted)):
        lb.insert('end', SearchResultSorted[i]['Title'])


''' 
# Another version of text processing   
for i in SearchResultSorted:
    lb.insert(tk.END,i)
'''


SearchButton = tk.Button(window, text='Search',
                         font=('Arial', 20), relief=tk.GROOVE, bg='azure',
                         command=Search)
SearchButton.pack(side=tk.RIGHT,
                  expand=tk.NO,
                  ipadx=30, ipady=10,
                  anchor=tk.NE)


InputBox = tk.Entry(window, width=20, font=('Arial', 20))
InputBox.pack(side=tk.TOP,
              expand=tk.NO,
              ipady=20,
              fill=tk.X,
              anchor=tk.N)


def BookAdd():
    global SelectedBooks
    global CallNo
    global SelectedBooksInfo
    global Position

    try:
        value = lb.get(lb.curselection())
    except Exception:
        return

    lb2.insert('end', str(value))
    # SelectedBooks=list(set(SelectedBooks))
    SelectedBooks = lb2.get(0, tk.END)

    Position = lb.curselection()
    Position = Position[0]
    SelectedBooksInfo.append(SearchResultSorted[Position])

    Debug()     # Debug


def BookRemove():
    global Position, SelectedBooks
    Position = lb2.curselection()
    lb2.delete(Position)
    SelectedBooks = lb2.get(0, tk.END)
    print(SelectedBooks)


BookAddButton = tk.Button(window, text='Add Select To BookList',
                          font=('Arial', 20), bg='azure', command=BookAdd)

BookAddButton.pack(side=tk.TOP,
                   expand=tk.NO,
                   ipadx=20, ipady=5,
                   anchor=tk.W,)


BookDeclineButton = tk.Button(window, text='Remove from BookList',
                              font=('Arial', 20), bg='azure', command=BookRemove)
BookDeclineButton.pack(side=tk.TOP,
                       expand=tk.YES,
                       ipadx=20, ipady=5,
                       anchor=tk.E)


sb2 = tk.Scrollbar(window)
sb2.pack(side=tk.RIGHT, fill=tk.Y)
sb = tk.Scrollbar(window)
sb.pack(side=tk.LEFT, fill=tk.Y)

# TEST INFO
# SearchResultSorted=[{'Title':"TEST1",'Number':'CHI'},{'Title':"TEST2",'Number':'CHI'},{'Title':"WASD",'Number':'CHI'}]


lb = tk.Listbox(window, listvariable=SearchResultSorted,
                width=40, relief=tk.GROOVE, yscrollcommand=sb.set)
lb.pack(side=tk.LEFT,
        expand=tk.YES,
        # anchor=tk.NW,
        fill=tk.Y,
        ipady=160
        )


lb2 = tk.Listbox(window, listvariable=SelectedBooks,
                 width=40, relief=tk.GROOVE, yscrollcommand=sb2.set)
lb2.pack(side=tk.RIGHT,
         expand=tk.YES,
         # anchor=tk.NE,
         fill=tk.Y,
         ipady=160
         )

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
