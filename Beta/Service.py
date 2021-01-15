import tkinter as tk
import tkinter.messagebox
import json
import requests
from Beta.data import *

'''
import sys
sys.path.append('../')
from GUI import *
'''

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

def SearchBook(SearchMode, KeyWord):
    SearchResult = []
    try:
        LinkAddress = f'http://{ServerIP}:{Port}/datasnap/rest/TInterFace/searchbook/{SearchMode}/{KeyWord}'
        SearchResult = requests.get(LinkAddress).json()['result']
    except:
        LinkAddress = f'http://d1808bfb-7b8e-4f9a-936b-75c19663032f.mock.pstmn.io/datasnap/rest/TInterFace/searchbook/{SearchMode}/{KeyWord}'
        SearchResult = requests.get(LinkAddress).json()['result']

    item = SearchResult[0]
    try:
        item['fields']['Msg'] == "检索完毕"
    except:
        print(item['fields']['Msg'])
        return
    itemFields = item['fields']['Data']['fields']
    BookNumber = itemFields['FCount']
    BookItems = itemFields['FItems']
    return BookNumber, BookItems

def SearchTitleNumber(SearchMode, KeyWord):
    (SearchBookNumber, SearchBookInfo) = SearchBook(SearchMode, KeyWord)
    BookList = []
    for item in SearchBookInfo:
        BookList.append({'Title': item['fields']['BTitle'], 'Number': item['fields']['BCallNo']})
    return BookList


def Search():
    global SearchMode
    global KeyWord
    global LinkAddress
    global SearchResultSorted
    SearchMode = 'TITLE'
    KeyWord = InputBox.get()
    try:
        SearchResultSorted = SearchTitleNumber(SearchMode, KeyWord)
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





#Under this is GUI service


# version information
TitleName = 'TestDemo'
Version = '0.1.4'
# 谢邀，本人代码是逆练出来的，请谅解

# define Window
window = tk.Tk()
window.title(f'{TitleName}  {Version}')
window.geometry('800x600')


SearchFrame = tk.Frame(window)
ButtonFrame = tk.Frame(window)
ListFrame = tk.Frame(window)

InputBox = tk.Entry(window, width=20, font=('Arial', 20))

SearchButton = tk.Button(window, text='Search',
                         font=('Arial', 20), relief=tk.GROOVE, bg='azure',
                         command=Search)

BookAddButton = tk.Button(window, text='Add Select To BookList',
                          font=('Arial', 20), bg='azure', command=BookAdd)

BookDeclineButton = tk.Button(window, text='Remove from BookList',
                              font=('Arial', 20), bg='azure', command=BookRemove)

sb2 = tk.Scrollbar(window)
sb2.pack(in_=ListFrame, side=tk.RIGHT, fill=tk.Y)
sb = tk.Scrollbar(window)
sb.pack(in_=ListFrame, side=tk.LEFT, fill=tk.Y)

lb = tk.Listbox(window, listvariable=SearchResultSorted,
                width=40, relief=tk.GROOVE, yscrollcommand=sb.set)

lb2 = tk.Listbox(window, listvariable=SelectedBooks,
                 width=40, relief=tk.GROOVE, yscrollcommand=sb2.set)