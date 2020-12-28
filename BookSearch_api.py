import json
import requests

ServerIP = '192.168.100.76'
Port = '8081'

def SearchBook(SearchMode, KeyWord):
    LinkAddress = f'http://{ServerIP}:{Port}/datasnap/rest/TInterFace/searchbook/{SearchMode}/{KeyWord}'
    SearchResult = requests.get(LinkAddress).json()['result']
    # print(SearchResult)

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

if __name__ == '__main__':
    BookListReturn = SearchTitleNumber('TITLE', '刑法')
    for item in BookListReturn:
        print(item)