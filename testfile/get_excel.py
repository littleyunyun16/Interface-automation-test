import os
import getpathinfo
import xlrd

path=getpathinfo.get_path()

def datacel(xls_name,sheet_name):
    xlsPath = os.path.join(path, 'case', xls_name)
    file = xlrd.open_workbook(xlsPath)
    sheet = file.sheet_by_name(sheet_name)
    case_nrows = sheet.nrows
    listid=[]
    listname = []
    listurl = []
    listmethod = []
    listparams = []
    listexpect = []
    listresponse = []
    listresult = []
    listpassed = []
    case_data = []
    for i in range(1,case_nrows):
        listid.append(sheet.cell(i, 0).value)
        listname.append(sheet.cell(i,1).value)
        listurl.append(sheet.cell(i,2).value)
        listmethod.append(sheet.cell(i,3).value)
        listparams.append(sheet.cell(i,4).value)
        listexpect.append(sheet.cell(i,5).value)
        listresponse.append(sheet.cell(i,6).value)
        listresult.append(sheet.cell(i,7).value)
        listpassed.append(sheet.cell(i,8).value)

    return listid, listname, listurl, listurl, listmethod, listparams, listexpect,listresponse,listresult,listpassed


def makedata():
    path = os.getcwd() + '//test_case_data//case.xlsx'
    listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname = datacel(path)
    i = 0
    make_data = []
    for i in range(len(listid)):
        make_data.append({'url': listurl[i], 'key': listkey[i], 'coneent': listconeent[i], 'fangshi': listfangshi[i],
                          'qiwang': listqiwang[i]})
        i += 1
    return make_data

if




