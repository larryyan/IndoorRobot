import tkinter as tk
import tkinter.messagebox
# from tkinter import *
# import time
import BookSearch_api
# import webbrowser




# version information
TitleName = 'TestDemo'
Version = '0.1.3'
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
# Message = None        貌似与函数参数重复，所以我给注释了
ERROR = 'ERROR'
PASS = 'PASS'


def Debug(DebugMode):
    print('=====================DEBUG INFORMATION=====================')

    if DebugMode == 'SelectedInfo':
        print('SearchResultSorted:\n', SearchResultSorted)
        return
    if DebugMode == 1:
        print('SelectedBooks:', SelectedBooks)
        print('SelectedBooksInfo:', SelectedBooksInfo)
        print('SearchResultSorted[Position]:', SearchResultSorted[Position])
        print('Position:', Position)
        print('CallNo:', CallNo)
        return
    if DebugMode == 2:
        print('SelectedBooks:', SelectedBooks)
        print('Position:', Position)
        return

    return



'''
# NOTE PADE
MapLink = f'http://192.168.100.133:8080/cgi-bin/BookLocation.exe?barcode={CallNo}'
CallNo_Sample：Z0192036

lb=>RawInfoBox
lb2=>SelectedBox
sb=>Scrollbar for lb
sb2=>Scrollbar for lb2


'''




def Search():
    global SearchMode
    global KeyWord
    global LinkAddress
    global SearchResultSorted
    SearchMode = 'TITLE'
    KeyWord = InputBox.get()
    try:
        SearchResultSorted = BookSearch_api.SearchTitleNumber(SearchMode, KeyWord)
    except Exception:
        print('!Exception_Value: SearchResultSorted!')
        print('ERROR:BookSearch_api.SearchTitleNumber')
        notification(ERROR, '未能找到您查找的数据')
        return
    for i in range(len(SearchResultSorted)):
        lb.insert('end', SearchResultSorted[i]['Title'])
    Debug('SelectedInfo')


def BookAdd():
    global SelectedBooks
    global CallNo
    global SelectedBooksInfo
    global Position

    try:
        Position = lb.get(lb.curselection())
    except Exception:
        return

    lb2.insert('end', str(Position))
    # SelectedBooks=list(set(SelectedBooks))
    SelectedBooks = lb2.get(0, tk.END)

    Position = lb.curselection()
    Position = Position[0]
    SelectedBooksInfo.append(SearchResultSorted[Position])

    Debug(1)     # Debug


def BookRemove():
    global Position
    global SelectedBooks
    try:
        Position = lb2.curselection()
    except Exception:
        return
    lb2.delete(Position)
    SelectedBooks = lb2.get(0, tk.END)

    Debug(2)


# This Function is still testing
def notification(Status, Message):
    if Status == ERROR:
        tkinter.messagebox.showwarning(title='ERROR', message=Message)
        return
    if Status == PASS:
        tkinter.messagebox.showinfo(title='Message', message=Message)
        return
    else:
        tkinter.messagebox.askokcancel(title='ERROR', message=(Message, '谁整的垃圾玩意出BUG了'))
    return


''' 
# Another version of text processing   
for i in SearchResultSorted:
    lb.insert(tk.END,i)
'''


# 主程序 main function
if __name__ == '__main__':

    SearchFrame = tk.Frame(window)
    ButtonFrame = tk.Frame(window)
    ListFrame = tk.Frame(window)
    SearchFrame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
    ButtonFrame.pack(expand=True, fill=tk.BOTH)
    ListFrame.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

    SearchButton = tk.Button(window, text='Search',
                             font=('Arial', 20), relief=tk.GROOVE, bg='azure',
                             command=Search)
    SearchButton.pack(in_=SearchFrame,
                      side=tk.RIGHT,
                      expand=tk.NO,
                      ipadx=30, ipady=10,
                      anchor=tk.NE)

    InputBox = tk.Entry(window, width=20, font=('Arial', 20))
    InputBox.pack(in_=SearchFrame,
                  side=tk.TOP,
                  expand=tk.NO,
                  ipady=20,
                  fill=tk.X,
                  anchor=tk.N)

    BookAddButton = tk.Button(window, text='Add Select To BookList',
                              font=('Arial', 20), bg='azure', command=BookAdd)

    BookAddButton.pack(in_=ButtonFrame,
                       side=tk.LEFT,
                       expand=tk.YES, fill=tk.Y,
                       ipadx=20, ipady=5,
                       # anchor=tk.W
                       )

    BookDeclineButton = tk.Button(window, text='Remove from BookList',
                                  font=('Arial', 20), bg='azure', command=BookRemove)

    BookDeclineButton.pack(in_=ButtonFrame,
                           side=tk.RIGHT,
                           expand=tk.YES, fill=tk.Y,
                           ipadx=20, ipady=5,
                           # anchor=tk.E
                           )

    sb2 = tk.Scrollbar(window)
    sb2.pack(in_=ListFrame, side=tk.RIGHT, fill=tk.Y)
    sb = tk.Scrollbar(window)
    sb.pack(in_=ListFrame, side=tk.LEFT, fill=tk.Y)

    # TEST INFO
    # SearchResultSorted=[{'Title':"TEST1",'Number':'CHI'},{'Title':"TEST2",'Number':'CHI'},{'Title':"WASD",'Number':'CHI'}]

    lb = tk.Listbox(window, listvariable=SearchResultSorted,
                    width=40, relief=tk.GROOVE, yscrollcommand=sb.set)
    lb.pack(in_=ListFrame,
            side=tk.LEFT,
            expand=tk.YES,
            # anchor=tk.NW,
            fill=tk.Y,
            ipady=160
            )

    lb2 = tk.Listbox(window, listvariable=SelectedBooks,
                     width=40, relief=tk.GROOVE, yscrollcommand=sb2.set)
    lb2.pack(in_=ListFrame,
             side=tk.RIGHT,
             expand=tk.YES,
             # anchor=tk.NE,
             fill=tk.Y,
             ipady=160
             )

    sb.config(command=lb.yview)
    sb2.config(command=lb2.yview)

    window.mainloop()
