import json
import requests


# 实际应用场景
ServerIP = '192.168.100.76'
Port = '8081'


# 内部搜索函数，建议不要外部调用
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


'''
 SearchMode是搜索方式，如：AUTHOR、TITLE
 KeyWord是搜索关键词，用户输入
 返回值：Booklist字典：{'Title':书名, 'Number':索书号}
'''


def SearchTitleNumber(SearchMode, KeyWord):
    (SearchBookNumber, SearchBookInfo) = SearchBook(SearchMode, KeyWord)
    BookList = []
    for item in SearchBookInfo:
        BookList.append({'Title': item['fields']['BTitle'], 'Number': item['fields']['BCallNo']})
    return BookList


# 以下内容为内部测试
if __name__ == '__main__':
    BookListReturn = SearchTitleNumber('TITLE', '红楼梦')
    for item in BookListReturn:
        print(item)
