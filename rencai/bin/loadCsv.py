#-*- coding:utf-8 -*-

import xlrd
import json
import codecs
from datetime import datetime
from xlrd import xldate_as_tuple


def get_9th_daibiao():
    file_path = '../data/9th_daibiao.xls'

    sheetno = 0

    suggest_unit_col = 0
    name_col = 3
    sex_col = 4
    nation_col = 5
    birthDay_col = 6
    political_outlook_col = 7  # 政治面貌
    hometown_col = 9
    xueli_col = 12  # 学历
    graduate_school_col = 13  # 毕业院校
    major_col = 14 #专业
    speciality_col = 16  #专长
    maior_job_col = 17  #专业技术职务
    is_zhongkeyuan_col = 35
    is_gongchengyuan_col = 36
    department_and_job_col = 20 #工作单位及职务

    all_people = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(1, nrows):
        people = {}
        people['suggest_unit'] = table.row_values(row)[suggest_unit_col]
        people['name'] = table.row_values(row)[name_col]
        people['sex'] = table.row_values(row)[sex_col]
        people['nation'] = table.row_values(row)[nation_col]
        people['birthDay'] = table.row_values(row)[birthDay_col]
        people['age'] = 2018 - int(table.row_values(row)[birthDay_col].split('-')[0])
        people['political_outlook'] = table.row_values(row)[political_outlook_col]
        people['hometown'] = table.row_values(row)[hometown_col]
        people['xueli'] = table.row_values(row)[xueli_col]
        people['graduate_school'] = table.row_values(row)[graduate_school_col]
        people['major'] = table.row_values(row)[major_col]
        people['speciality'] = table.row_values(row)[speciality_col]
        people['maior_job'] = table.row_values(row)[maior_job_col]
        people['is_zhongkeyuan'] = table.row_values(row)[is_zhongkeyuan_col]
        people['is_gongchengyuan'] = table.row_values(row)[is_gongchengyuan_col]
        people['department_and_job'] = table.row_values(row)[department_and_job_col]
        all_people.append(people)

    return all_people

def get_15th_qingke_candidate():
    file_path = '../data/15th_qingke.xls'

    sheetno = 0

    speciality_col = 3  # 专长
    name_col = 4
    sex_col = 5
    nation_col = 7
    birthDay_col = 6
    political_outlook_col = 8  # 政治面貌
    recommend_unit_col = 9  #推荐单位
    unit_xingzhi_col = 11   #单位性质
    maior_job_col = 13  # 专业技术职务
    location_col = 12  #单位所在地
    department_and_job_col = 14  # 工作单位及职务

    all_people = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(1, nrows):
        people = {}
        people['name'] = table.row_values(row)[name_col]
        people['sex'] = table.row_values(row)[sex_col]
        people['nation'] = table.row_values(row)[nation_col]
        # people['birthDay'] = table.row_values(row)[birthDay_col]
        date = datetime(*xldate_as_tuple(table.row_values(row)[birthDay_col], 0))
        people['birthDay'] = str(date.year) + '年' + str(date.month) + '月' + str(date.day) + '日'
        people['age'] = 2018 - int(date.year)
        people['political_outlook'] = table.row_values(row)[political_outlook_col]
        people['speciality'] = table.row_values(row)[speciality_col]
        people['recommend_unit'] = table.row_values(row)[recommend_unit_col]
        people['unit_xingzhi'] = table.row_values(row)[unit_xingzhi_col]
        people['maior_job'] = table.row_values(row)[maior_job_col]
        people['location'] = table.row_values(row)[location_col]
        people['department_and_job'] = table.row_values(row)[department_and_job_col]
        all_people.append(people)

    return all_people

def all_qingke():
    file_path = '../data/all_qingke.xlsx'

    sheetno = 0

    name_col = 1
    sex_col = 3
    birthDay_col = 4
    nation_col = 5
    political_outlook_col = 6  # 政治面貌
    speciality_col = 11  # 专长
    work_department_col = 2
    job_col = 7
    session_col = 14

    all_people = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(1, nrows):
        people = {}
        people['name'] = table.row_values(row)[name_col]
        people['sex'] = table.row_values(row)[sex_col]
        people['nation'] = table.row_values(row)[nation_col]
        people['birthDay'] = table.row_values(row)[birthDay_col]
        if table.row_values(row)[birthDay_col] and  table.row_values(row)[birthDay_col]!=1.0:
            date = datetime(*xldate_as_tuple(table.row_values(row)[birthDay_col], 0))
            people['birthDay'] = str(date.year)+'年'+str(date.month)+'月'+str(date.day)+'日'
            people['age'] = 2018 - int(date.year)
        else:
            people['birthDay'] = ''
            people['age'] = ''
        people['political_outlook'] = table.row_values(row)[political_outlook_col]
        people['speciality'] = table.row_values(row)[speciality_col]
        people['work_department'] = table.row_values(row)[work_department_col]
        people['job'] = table.row_values(row)[job_col]
        people['session'] = table.row_values(row)[session_col]
        all_people.append(people)

    return all_people

def get_2017_yuanshi_candidate():
    file_path = '../data/2017_recommend_liangyuan.xls'

    sheetno = 0

    recommend_unit_col = 2
    name_col = 3
    sex_col = 4
    nation_col = 6
    age_col = 5
    xueli_col = 7
    unit_xingzhi_col = 10
    recommend_type_col = 12
    recommend_department_col = 13
    speciality_col = 14  # 专长
    department_and_job_col = 9  # 工作单位及职务

    all_people = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(1, nrows):
        people = {}
        people['name'] = table.row_values(row)[name_col]
        people['sex'] = table.row_values(row)[sex_col]
        people['nation'] = table.row_values(row)[nation_col]
        people['age'] = table.row_values(row)[age_col]
        people['recommend_unit'] = table.row_values(row)[recommend_unit_col]
        people['speciality'] = table.row_values(row)[speciality_col]
        people['xueli'] = table.row_values(row)[xueli_col]
        people['unit_xingzhi'] = table.row_values(row)[unit_xingzhi_col]
        people['recommend'] = table.row_values(row)[recommend_type_col]
        people['recommend_department'] = table.row_values(row)[recommend_department_col]
        people['department_and_job'] = table.row_values(row)[department_and_job_col]
        all_people.append(people)

    return all_people

def get_all_yuanshi():
    file_path = '../data/all_liangyuan.xlsx'

    sheetno = 0

    name_col = 2
    sex_col = 3
    nation_col = 4
    birthDay_col = 6
    yuanshi_type_col = 8
    xueke_col = 9
    major_col = 10
    yuanshi_department_col = 11
    department_and_job_col = 7
    city_col = 12

    all_people = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(1, nrows):
        people = {}
        people['name'] = table.row_values(row)[name_col]
        people['sex'] = table.row_values(row)[sex_col]
        people['nation'] = table.row_values(row)[nation_col]
        people['birthDay'] = table.row_values(row)[birthDay_col]
        if table.row_values(row)[birthDay_col]:
            try:
                date = datetime(*xldate_as_tuple(table.row_values(row)[birthDay_col], 0))
                people['age'] = 2018 - int(date.year)
            except:
                print(table.row_values(row))
        else:
            people['age'] = None
        people['yuanshi_type'] = table.row_values(row)[yuanshi_type_col]
        people['xueke'] = table.row_values(row)[xueke_col]
        people['major'] = table.row_values(row)[major_col]
        people['yuanshi_department'] = table.row_values(row)[yuanshi_department_col]
        people['department_and_job'] = table.row_values(row)[department_and_job_col]
        people['city'] = table.row_values(row)[city_col]
        all_people.append(people)

    return all_people


def get_1st_chuangxin_candidate():
    file_path = '../data/2017_chuangxin_candidate.xlsx'

    sheetno = 0

    name_col = 1
    sex_col = 2
    nation_col = 3
    birthDay_col = 4
    political_outlook_col = 5  # 政治面貌
    xueli_col = 6
    job_col = 8 #职务
    unit_xingzhi_col = 9
    province_col = 10
    xueke_col = 12
    xingzheng_degree_col = 15 #行政级别
    department_and_job_col = 7

    all_people = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(1, nrows):
        people = {}
        people['name'] = table.row_values(row)[name_col]
        people['sex'] = table.row_values(row)[sex_col]
        people['nation'] = table.row_values(row)[nation_col]
        people['birthDay'] = str(table.row_values(row)[birthDay_col])
        people['age'] = 2018 - int(str(table.row_values(row)[birthDay_col]).split('-')[0])
        people['political_outlook'] = table.row_values(row)[political_outlook_col]
        people['xueke'] = table.row_values(row)[xueke_col]
        people['xueli'] = table.row_values(row)[xueli_col]
        people['job'] = table.row_values(row)[job_col]
        people['unit_xingzhi'] = table.row_values(row)[unit_xingzhi_col]
        province = table.row_values(row)[province_col]
        province = province.replace('市', '')
        province = province.replace('省', '')
        people['province'] = province
        people['xingzheng_degree'] = table.row_values(row)[xingzheng_degree_col]
        people['department_and_job'] = table.row_values(row)[department_and_job_col]
        all_people.append(people)

    return all_people

def load_all_female_scientists():
    file_path = '../data/all_female_scientists.xlsx'

    sheetno = 0

    name_col = 1
    birthDay_col = 2
    major_col = 3
    province_col = 5
    session_col = 6 #第几届
    unit_xingzhi_col = 7
    department_and_job_col = 4

    all_people = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(1, nrows):
        people = {}
        people['name'] = table.row_values(row)[name_col]
        people['sex'] = '女'
        people['birthDay'] = str(table.row_values(row)[birthDay_col])
        people['age'] = 2018 - int(str(table.row_values(row)[birthDay_col]).split('.')[0])
        people['major'] = table.row_values(row)[major_col]
        people['unit_xingzhi'] = table.row_values(row)[unit_xingzhi_col]
        province = table.row_values(row)[province_col]
        province = province.replace('市', '')
        province = province.replace('省', '')
        province = province.replace('自治区', '')
        province = province.replace('大学', '')
        people['province'] = province
        people['session'] = table.row_values(row)[session_col]
        people['department_and_job'] = table.row_values(row)[department_and_job_col]
        all_people.append(people)

    return all_people

def load_all_qianren():
    file_path = '../data/all_qianren.xls'

    sheetno = 0

    name_col = 1
    department_col = 2
    job_col = 3
    major_col = 4
    sub_major_col = 5

    all_people = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(1, nrows):
        people = {}
        people['name'] = table.row_values(row)[name_col]
        people['department'] = table.row_values(row)[department_col]
        people['job'] = table.row_values(row)[job_col]
        people['major'] = table.row_values(row)[major_col]
        people['sub_major'] = table.row_values(row)[sub_major_col]
        all_people.append(people)

    return all_people

def load_5_wei():
    file_path = '../data/5_wei_analysis.xlsx'

    sheetno = 0

    name_col = 0
    year_col = 1
    gdp_col = 2
    science_col = 3
    rd_col = 4
    scholar_col = 5
    edu_col = 6
    paper_col = 7
    patent_col = 8
    quality_col = 9 #公民科学素质

    all_province = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(1, nrows):
        province = {}
        province['name'] = table.row_values(row)[name_col]
        province['year'] = table.row_values(row)[year_col]
        province['gdp'] = table.row_values(row)[gdp_col]
        province['science'] = table.row_values(row)[science_col]
        province['rd'] = table.row_values(row)[rd_col]
        province['scholar'] = table.row_values(row)[scholar_col]
        province['edu'] = table.row_values(row)[edu_col]
        province['paper'] = table.row_values(row)[paper_col]
        province['patent'] = table.row_values(row)[patent_col]
        province['quality'] = table.row_values(row)[quality_col]
        all_province.append(province)

    return all_province



if __name__ == '__main__':
    json.dump(get_9th_daibiao(), codecs.open('../data/9th_daibiao.json', 'w', encoding='utf-8'), ensure_ascii=False)
    # json.dump(get_15th_qingke_candidate(), codecs.open('../data/15th_qingke_candidate.json', 'w', encoding='utf-8'), ensure_ascii=False)
    # json.dump(all_qingke(), codecs.open('../data/all_qingke.json', 'w', encoding='utf-8'), ensure_ascii=False)
    # json.dump(get_2017_yuanshi_candidate(), codecs.open('../data/2017_yuanshi_candidate.json', 'w', encoding='utf-8'), ensure_ascii=False)
    # json.dump(get_all_yuanshi(), codecs.open('../data/all_yuanshi.json', 'w', encoding='utf-8'), ensure_ascii=False)
    # json.dump(get_1st_chuangxin_candidate(), codecs.open('../data/1st_chuangxin_candidate.json', 'w', encoding='utf-8'), ensure_ascii=False)
    # json.dump(load_all_female_scientists(), codecs.open('../data/all_female_scientists.json', 'w', encoding='utf-8'), ensure_ascii=False)
    # json.dump(load_all_qianren(), codecs.open('../data/all_qianren.json', 'w', encoding='utf-8'), ensure_ascii=False)
    # json.dump(load_5_wei(), codecs.open('../data/5_wei_analysis.json', 'w', encoding='utf-8'), ensure_ascii=False)