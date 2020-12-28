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


if __name__ == '__main__':
    (SearchBookNumber, SearchBookInfo) = SearchBook('TITLE', '刑法')
    print(SearchBookNumber)
    for item in SearchBookInfo:
        print(item)