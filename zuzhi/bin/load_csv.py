#-*- coding:utf-8 -*-

import xlrd
import json
import codecs
from datetime import datetime
from xlrd import xldate_as_tuple

def load_gaoxiao():
    file_path = '../data/gaoxiaokexie.xlsx'

    sheetno = 0

    name_col = 1
    province_col = 2

    all_province = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(2, nrows):
        province = {}
        province['name'] = table.row_values(row)[name_col]
        province['province'] = table.row_values(row)[province_col]
        all_province.append(province)

    return all_province

def load_nongjixie():
    file_path = '../data/nongjixie.xlsx'

    sheetno = 0

    province_col = 1
    total_col = 12

    all_province = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(2, nrows):
        province = {}
        province['province'] = table.row_values(row)[province_col]
        province['total'] = table.row_values(row)[total_col]
        all_province.append(province)

    return all_province

def load_qiyekexie():
    file_path = '../data/qiyekexie.xls'

    sheetno = 0

    name_col = 0
    province_col = 17

    all_province = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(1, nrows):
        province = {}
        province['name'] = table.row_values(row)[name_col]
        province['province'] = table.row_values(row)[province_col]
        all_province.append(province)

    return all_province

def load_yuanqukexie():
    file_path = '../data/yuanqukexie.xls'

    sheetno = 0

    name_col = 0
    province_col = 16

    all_province = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(1, nrows):
        province = {}
        province['name'] = table.row_values(row)[name_col]
        province['province'] = table.row_values(row)[province_col]
        all_province.append(province)

    return all_province


if __name__ == '__main__':
    # json.dump(load_gaoxiao(), codecs.open('../data/load_gaoxiaokexie.json', 'w', encoding='utf-8'), ensure_ascii=False)
    # json.dump(load_nongjixie(), codecs.open('../data/load_nongjixie.json', 'w', encoding='utf-8'), ensure_ascii=False)
    # json.dump(load_qiyekexie(), codecs.open('../data/load_qiyekexie.json', 'w', encoding='utf-8'), ensure_ascii=False)
    json.dump(load_yuanqukexie(), codecs.open('../data/load_yuanqukexie.json', 'w', encoding='utf-8'), ensure_ascii=False)