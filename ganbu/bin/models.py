#-*- coding:utf-8 -*-

import xlrd
import codecs
import json

def load_jiguan_people():
    file_path = '../../data/jiguan_people.xlsx'

    sheetno = 0

    id_col = 0
    company_and_job_col = 1
    name_col = 2
    sex_col = 3
    political_outlook_col = 4 #政治面貌
    nation_col = 5
    province_col = 6
    birthDay_col = 7
    join_work_time_col = 8 #参加工作时间
    join_position_col = 9 #入职时间
    tongzhiji_time_col = 10 #任同职级时间
    xueli_col = 11  #学历
    xuewei_col = 12 #学位
    department_col = 13 #部门
    chushi_col = 14 #处室

    all_people = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(1, nrows):
        people = {}
        people['id'] = table.row_values(row)[id_col]
        people['icompany_and_job'] = table.row_values(row)[company_and_job_col]
        people['name'] = table.row_values(row)[name_col].replace('　', '')
        people['sex'] = table.row_values(row)[sex_col]
        people['political_outlook'] = table.row_values(row)[political_outlook_col]
        people['nation'] = table.row_values(row)[nation_col]
        people['province'] = table.row_values(row)[province_col]
        people['birthDay'] = table.row_values(row)[birthDay_col]
        people['join_work_time'] = table.row_values(row)[join_work_time_col]
        people['jion_position'] = table.row_values(row)[join_position_col]
        people['tongzhiji_time'] = table.row_values(row)[tongzhiji_time_col]
        people['xueli'] = table.row_values(row)[xueli_col]
        people['xuewei'] = table.row_values(row)[xuewei_col]
        people['department'] = table.row_values(row)[department_col]
        people['chushi'] = table.row_values(row)[chushi_col]

        all_people.append(people)

    return all_people

def load_shiye_people():
    file_path = '../../data/shiye_people.xls'

    sheetno = 2

    unit_col = 0 #单位
    unit_department_col = 1 #单位部门
    name_col = 2
    sex_col = 3
    nation_col = 4
    birth_col = 5
    birth_year_col = 6
    birth_month_col = 7
    birth_day_col = 8
    political_outlook_col = 9  # 政治面貌
    join_work_time_col = 11  # 参加工作时间
    join_work_year_col = 12
    join_position_time_col = 13  # 入职时间
    join_position_year_col = 14
    department_col = 15  # 部门
    job_col = 16 #职务
    job_degree_col = 17 #岗位等级
    #任现职时间
    #任同等级起始时间
    graduate_school_and_major_col = 20
    #旧学历
    xuewei_col = 22 #学位
    #备注
    xueli_col = 24 #学历
    type_col = 25 #类别

    shiye_people = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(1, nrows):
        people = {}
        people['unit'] = table.row_values(row)[unit_col]
        people['unit_department'] = table.row_values(row)[unit_department_col]
        people['name'] = table.row_values(row)[name_col]
        people['sex'] = table.row_values(row)[sex_col]
        people['nation'] = table.row_values(row)[nation_col]
        people['birth'] = table.row_values(row)[birth_col]
        people['birth_year'] = table.row_values(row)[birth_year_col]
        people['birth_month'] = table.row_values(row)[birth_month_col]
        people['birth_day'] = table.row_values(row)[birth_day_col]
        people['political_outlook'] = table.row_values(row)[political_outlook_col]
        people['join_work_time'] = table.row_values(row)[join_work_time_col]
        people['join_work_year'] = table.row_values(row)[join_work_year_col]
        people['join_position_time'] = table.row_values(row)[join_position_time_col]
        people['join_position_year'] = table.row_values(row)[join_position_year_col]
        people['department'] = table.row_values(row)[department_col]
        people['job'] = table.row_values(row)[job_col]
        people['job_degree'] = table.row_values(row)[job_degree_col]
        people['graduate_school_and_major'] = table.row_values(row)[graduate_school_and_major_col]
        people['xuewei'] = table.row_values(row)[xuewei_col]
        people['xueli'] = table.row_values(row)[xueli_col]
        people['type'] = table.row_values(row)[type_col]

        shiye_people.append(people)

    return shiye_people

def load_project_people():
    file_path = '../../data/project_people.xlsx'

    sheetno = 0

    project_name_col = 0
    plan_finish_time_col = 1
    type_col = 2
    project_progress_col = 3
    project_role_col = 4
    name_col = 5
    department_name_col = 6
    upper_department_name_col = 7
    # _col = 8 #没啥用
    project_type_col = 9 #项目类别
    finish_degree_col = 10 #完成情况

    project_people = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(1, nrows):
        people = {}
        people['project_name'] = table.row_values(row)[project_name_col]
        people['plan_finish_time'] = table.row_values(row)[plan_finish_time_col]
        people['type'] = table.row_values(row)[type_col]
        people['project_progress'] = table.row_values(row)[project_progress_col]
        people['project_role'] = table.row_values(row)[project_role_col]
        people['name'] = table.row_values(row)[name_col]
        people['department_name'] = table.row_values(row)[department_name_col]
        people['upper_department_name'] = table.row_values(row)[upper_department_name_col]
        people['project_type'] = table.row_values(row)[project_type_col]
        people['finish_degree'] = table.row_values(row)[finish_degree_col]

        project_people.append(people)

    return project_people

def load_task_people():
    file_path = '../../data/task_people.xlsx'

    sheetno = 0

    upper_department_name_col = 0
    task_name_col = 1
    task_description_col = 2
    task_state_col = 3
    task_role_col = 4
    task_sequence_col = 5
    priority_col = 6
    finish_time_col = 7
    finish_state_col = 8
    name_col = 9
    type_col = 10
    department_name_col = 11
    project_name_col = 12
    project_finish_degree_col = 13
    task_type_col = 14  #任务重大类型


    task_people = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(1, nrows):
        people = {}
        people['upper_department_name'] = table.row_values(row)[upper_department_name_col]
        people['task_name'] = table.row_values(row)[task_name_col]
        people['task_description'] = table.row_values(row)[task_description_col]
        people['task_state'] = table.row_values(row)[task_state_col]
        people['task_role'] = table.row_values(row)[task_role_col]
        people['task_sequence'] = table.row_values(row)[task_sequence_col]
        people['priority'] = table.row_values(row)[priority_col]
        people['finish_time'] = table.row_values(row)[finish_time_col]
        people['finish_state'] = table.row_values(row)[finish_state_col]
        people['name'] = table.row_values(row)[name_col]
        people['type'] = table.row_values(row)[type_col]
        people['department_name'] = table.row_values(row)[department_name_col]
        people['project_name'] = table.row_values(row)[project_name_col]
        people['project_finish_degree'] = table.row_values(row)[project_finish_degree_col]
        people['task_type'] = table.row_values(row)[task_type_col]

        task_people.append(people)

    return task_people

def load_xueshi():
    file_path = '../../data/xueshi.xlsx'

    sheetno = 4

    name_col = 0
    date_col = 1
    xueshi_col = 2

    task_people = []
    excel_data = xlrd.open_workbook(file_path)
    table = excel_data.sheets()[sheetno]
    nrows = table.nrows
    for row in range(1, nrows):
        people = {}
        people['name'] = table.row_values(row)[name_col]
        people['date'] = table.row_values(row)[date_col]
        people['xueshi'] = table.row_values(row)[xueshi_col]

        task_people.append(people)

    return task_people


if __name__ == '__main__':
    # all_people = load_jiguan_people()
    # out_people_file = '../../data/all_jiguan_people.json'
    # json.dump(all_people, codecs.open(out_people_file, 'w', encoding='utf-8'), ensure_ascii=False)

    # all_people = load_project_people()
    # out_people_file = '../../data/all_project_people.json'
    # json.dump(all_people, codecs.open(out_people_file, 'w', encoding='utf-8'), ensure_ascii=False)

    # all_people = load_task_people()
    # out_people_file = '../../data/all_task_people.json'
    # json.dump(all_people, codecs.open(out_people_file, 'w', encoding='utf-8'), ensure_ascii=False)

    # all_people = load_shiye_people()
    # out_people_file = '../../data/all_shiye_people.json'
    # json.dump(all_people, codecs.open(out_people_file, 'w', encoding='utf-8'), ensure_ascii=False)

    all_xueshi = load_xueshi()
    out_xueshi_file = '../../data/all_xueshi.json'
    json.dump(all_xueshi, codecs.open(out_xueshi_file, 'w', encoding='utf-8'), ensure_ascii=False)

