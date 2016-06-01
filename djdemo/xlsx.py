#-*-coding:utf-8-*-

import sys
import xlrd

def read(path):
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(u'办公用品')
    for row in table.get_rows():
        if row[0].value == u'项目':
            deps = [item.value for item in row[4:-2]]
        if row[0].value == u"人数":
            nums = [item.value for item in row[4:-2]]
        if row[0].value == u"标准":
            stans = [item.value for item in row[4:-2]]
        if isinstance(row[3].value, (int, float)):
            print u"物品：%s单价：%g" % (row[0].value, row[3].value )
    # while True:
        #row = table.row_values(i)
        #i = i + 1
        #import pdb;pdb.set_trace()
        # if ''.join(row[3].split('.')).isdigit():
        #    print u"物品：%s单价：%g" % (row[0].value, row[3].value )

    deps = [(deps[i], nums[i], stans[i]) for i in range(len(deps)-1)]
    print deps

if __name__=='__main__':
    read(sys.argv[1])