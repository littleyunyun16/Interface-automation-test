import os
import getpathinfo
import xlrd

path=getpathinfo.get_path()



class readExcel():
    def get_xls(self,xls_name,sheet_name):
        cls=[]
        xlsPath=os.path.join(path,'case',xls_name)  # 得到
        file=xlrd.open_workbook(xlsPath)
        sheet=file.sheet_by_name(sheet_name)
        case_nrows=sheet.nrows
        for i in range(case_nrows):
            if sheet.row_values(i)[0]!=u'module':
                cls.append(sheet.row_values(i))
        return cls


if __name__ == '__main__':
    # print(readExcel().get_xls('ReturnOrder.xlsx','Sheet1'))
    print(readExcel().get_xls('ReturnOrder.xlsx', 'Sheet1')[0][5])