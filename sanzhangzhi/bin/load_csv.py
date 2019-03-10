#-*- coding:utf-8 -*-

import xlrd
import json
import codecs
from datetime import datetime
from xlrd import xldate_as_tuple

def load_sanzhang():
    file_path = '../data/sanzhang.xlsx'

    sheetno = 0

    name_col = 0
    all_total_col = 1
    province_col = 2
    city_col = 3
    area_col = 4
    street_col = 5

    all_province = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(1, nrows):
        province = {}
        province['name'] = table.row_values(row)[name_col]
        province['all_total'] = table.row_values(row)[all_total_col]
        province['province'] = table.row_values(row)[province_col]
        province['city'] = table.row_values(row)[city_col]
        province['area'] = table.row_values(row)[area_col]
        province['street'] = table.row_values(row)[street_col]
        all_province.append(province)

    return all_province



if __name__ == '__main__':
    json.dump(load_sanzhang(), codecs.open('../data/sanzhang.json', 'w', encoding='utf-8'), ensure_ascii=False)