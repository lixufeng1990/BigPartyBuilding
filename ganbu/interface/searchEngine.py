#-*- coding:utf-8 -*-

import codecs
import json
import ganbu.bin.getData as getData

jiguan_people = getData.get_jiguan_people()
shiye_people = getData.get_shiye_people()
project_people = getData.get_project_people()
task_people = getData.get_task_people()


def search_people_by_department(department_name):
    result = {}
    all_people_count = 0 #部门总人数
    party_count = 0 #党员数
    all_chushi = set() #处室数
    all_xueli = {} #学历数
    all_age = {'m29':0, 'm3039':0, 'm4049':0, 'm5059':0, 'm60':0,
               'f29': 0, 'f3039': 0, 'f4049': 0, 'f5059': 0, 'f60': 0} #年龄分布
    all_politicalOutlook = {} #政治面貌

    for jiguan_person in jiguan_people:
        if (len(jiguan_person['department'].strip()) != 0) and (jiguan_person['department'] == department_name):
            #总人数
            all_people_count += 1
            #政治面貌
            political_outlook = jiguan_person['political_outlook'].strip()
            if  len(political_outlook) != 0:
                if political_outlook not in all_politicalOutlook.keys():
                    all_politicalOutlook[political_outlook] = 1
                else:
                    all_politicalOutlook[political_outlook] += 1
            else:
                all_politicalOutlook[u'其他'] += 1
            #处室
            chushi = jiguan_person['chushi'].strip()
            if len(chushi) != 0:
                all_chushi.add(chushi)
            #学历
            xueli = jiguan_person['xueli'].strip()
            if len(xueli) != 0:
                if xueli not in all_xueli.keys():
                    all_xueli[xueli] = 1
                else:
                    all_xueli[xueli] += 1

            #年龄
            birthday = str(jiguan_person['birthDay']).strip()
            sex = jiguan_person['sex'].strip()
            if (len(birthday) != 0) and (len(sex)!=0):
                birth_year = birthday.split('.')[0]
                age = 2018 - int(birth_year)
                if sex == '男':
                    if age < 30:
                        all_age['m29'] += 1
                    elif 30 <= age < 40:
                        all_age['m3039'] += 1
                    elif 40 <= age < 49:
                        all_age['m4049'] += 1
                    elif 50 <= age < 59:
                        all_age['m5059'] += 1
                    else:
                        all_age['m60'] += 1
                else:
                    if age < 30:
                        all_age['f29'] += 1
                    elif 30 <= age < 40:
                        all_age['f3039'] += 1
                    elif 40 <= age < 49:
                        all_age['f4049'] += 1
                    elif 50 <= age < 59:
                        all_age['f5059'] += 1
                    else:
                        all_age['f60'] += 1

    for shiye_person in shiye_people:
        department = shiye_person['unit']
        if (len(department) != 0) and (department == department_name):
            #总人数
            all_people_count += 1
            #政治面貌
            political_outlook = shiye_person['political_outlook'].strip()
            if  len(political_outlook) != 0:
                if political_outlook not in all_politicalOutlook.keys():
                    all_politicalOutlook[political_outlook] = 1
                else:
                    all_politicalOutlook[political_outlook] += 1
            else:
                all_politicalOutlook[u'其他'] += 1
            #处室
            chushi = shiye_person['unit_department'].strip()
            if len(chushi) != 0:
                all_chushi.add(chushi)
            #学历
            xueli = shiye_person['xueli'].strip()
            if len(xueli) != 0:
                if xueli not in all_xueli.keys():
                    all_xueli[xueli] = 1
                else:
                    all_xueli[xueli] += 1

            #年龄
            birth_year = str(shiye_person['birth_year']).strip()
            sex = shiye_person['sex'].strip()
            if (len(birth_year) != 0) and (len(sex) != 0):
                birth_year = birth_year.split('.')[0]
                age = 2018 - int(birth_year)
                if sex == '男':
                    if age < 30:
                        all_age['m29'] += 1
                    elif 30 <= age < 40:
                        all_age['m3039'] += 1
                    elif 40 <= age < 49:
                        all_age['m4049'] += 1
                    elif 50 <= age < 59:
                        all_age['m5059'] += 1
                    else:
                        all_age['m60'] += 1
                else:
                    if age < 30:
                        all_age['f29'] += 1
                    elif 30 <= age < 40:
                        all_age['f3039'] += 1
                    elif 40 <= age < 49:
                        all_age['f4049'] += 1
                    elif 50 <= age < 59:
                        all_age['f5059'] += 1
                    else:
                        all_age['f60'] += 1
    party_count = 0
    if '中共党员' in all_politicalOutlook.keys():
        party_count = all_politicalOutlook[u'中共党员']
    elif '党员' in all_politicalOutlook.keys():
        party_count = all_politicalOutlook[u'党员']
    chushi_count = len(all_chushi)
    result['all_people_count'] = all_people_count
    result['party_count'] = party_count
    result['chushi_count'] = chushi_count
    result['all_xueli'] = all_xueli
    result['all_age'] = all_age
    result['all_politicalOutlook'] = all_politicalOutlook
    return result

def search_task_by_department(department_name):
    result = {}

    big_tasks = {}  #重大任务详情
    units = set() #参与单位数
    people_join_task_info = {} #个人参与任务详情
    unfinish_task_people = set()  #正在进行的任务参与人数


    for project_person in project_people:
        upper_department_name = project_person['upper_department_name'].strip()
        if upper_department_name == department_name:
            project_type = project_person['project_type']
            # if project_type == '重大任务':
            project_name = project_person['project_name']
            finish_degree = project_person['finish_degree']
            project_progress = project_person['project_progress']
            unit_name = project_person['department_name']

            units.add(unit_name)
            if project_name not in big_tasks.keys():
                big_tasks[project_name] = {'project_name':project_name, 'project_type':project_type, 'finish_degree':finish_degree, 'project_progress':project_progress,
                                           'join_people_num':1, 'one_level_tasks':set(), 'two_level_tasks':set()}
            else:
                big_tasks[project_name]['join_people_num'] += 1

    for task_person in task_people:
        upper_department_name = task_person['upper_department_name'].strip()
        if upper_department_name == department_name:
            name = task_person['name']
            finish_state = task_person['finish_state']
            task_type = task_person['task_type']

            if name not in people_join_task_info.keys():
                people_join_task_info[name] = {'name':name, 'one_level_finish':0, 'one_level_unfinish':0, 'two_level_finish':0, 'two_level_unfinish':0}
                if (task_type == '一级任务') and  (finish_state == '已完成'):
                    people_join_task_info[name]['one_level_finish'] += 1
                elif (task_type == '一级任务') and  (finish_state == '未完成'):
                    people_join_task_info[name]['one_level_unfinish'] += 1
                    unfinish_task_people.add(name)
                elif (task_type == '二级任务') and  (finish_state == '已完成'):
                    people_join_task_info[name]['two_level_finish'] += 1
                else:
                    people_join_task_info[name]['two_level_unfinish'] += 1
                    unfinish_task_people.add(name)
            else:
                if (task_type == '一级任务') and  (finish_state == '已完成'):
                    people_join_task_info[name]['one_level_finish'] += 1
                elif (task_type == '一级任务') and  (finish_state == '未完成'):
                    people_join_task_info[name]['one_level_unfinish'] += 1
                    unfinish_task_people.add(name)
                elif (task_type == '二级任务') and  (finish_state == '已完成'):
                    people_join_task_info[name]['two_level_finish'] += 1
                else:
                    people_join_task_info[name]['two_level_unfinish'] += 1
                    unfinish_task_people.add(name)

            project_name = task_person['project_name']
            task_name = task_person['task_name']
            if project_name in big_tasks.keys():
                if task_type == '一级任务':
                    big_tasks[project_name]['one_level_tasks'].add(task_name)
                elif task_type == '二级任务':
                    big_tasks[project_name]['two_level_tasks'].add(task_name)

    big_tasks_count = len(big_tasks)
    tasks_finish_info = {'finished':0, '7699':0, '5175':0, '50':0}
    one_level_task_count = 0  # 一级任务数
    two_level_task_count = 0  # 二级任务数
    for big_task in big_tasks:
        if big_tasks[big_task]['finish_degree'] == '已完成':
            tasks_finish_info['finished'] += 1
        elif big_tasks[big_task]['finish_degree'] == '76-%-99%':
            tasks_finish_info['7699'] += 1
        elif big_tasks[big_task]['finish_degree'] == '51%-75%':
            tasks_finish_info['5175'] += 1
        elif big_tasks[big_task]['finish_degree'] == '50%以下':
            tasks_finish_info['50'] += 1

        one_level_task_count += len(big_tasks[big_task]['one_level_tasks'])
        big_tasks[big_task]['one_level_tasks_count'] = one_level_task_count
        big_tasks[big_task].pop('one_level_tasks')
        two_level_task_count += len(big_tasks[big_task]['two_level_tasks'])
        big_tasks[big_task]['two_level_tasks_count'] = two_level_task_count
        big_tasks[big_task].pop('two_level_tasks')


    jion_task_people_count = len(people_join_task_info)
    join_one_level_people_count = 0
    join_two_level_people_count = 0
    join_one_level_finish_count = 0
    join_one_level_unfinish_count = 0
    join_two_level_finish_count = 0
    join_two_level_unfinish_count = 0

    for join_people_name in people_join_task_info:
        join_people = people_join_task_info[join_people_name]
        one_level_flag = False
        two_level_flag = False
        if join_people['one_level_finish'] != 0:
            join_one_level_finish_count +=1
            one_level_flag = True
        if join_people['one_level_unfinish'] != 0:
            join_one_level_unfinish_count +=1
            one_level_flag = True
        if join_people['two_level_finish'] != 0:
            join_two_level_finish_count +=1
            two_level_flag = True
        if join_people['two_level_unfinish'] != 0:
            join_two_level_unfinish_count +=1
            two_level_flag = True
        if one_level_flag:
            join_one_level_people_count += 1
        if two_level_flag:
            join_two_level_people_count += 1

    units_count = len(units)
    big_tasks = sorted(big_tasks.items(), key=lambda item: item[1]['join_people_num'], reverse=True)
    result['big_tasks_count'] = big_tasks_count
    result['units_count'] = units_count
    result['one_level_task_count'] = one_level_task_count
    result['two_level_task_count'] = two_level_task_count
    result['tasks_finish_info'] = tasks_finish_info
    result['big_tasks'] = big_tasks

    people_join_task_info = sorted(people_join_task_info.items(),
                                   key=lambda item: item[1]['one_level_finish'] + item[1]['one_level_unfinish'] + item[1]['two_level_finish'] + item[1]['two_level_unfinish'],
                                   reverse=True)
    result['jion_task_people_count'] = jion_task_people_count
    result['join_one_level_people_count'] = join_one_level_people_count
    result['join_two_level_people_count'] = join_two_level_people_count
    result['join_one_level_finish_count'] = join_one_level_finish_count
    result['join_one_level_unfinish_count'] = join_one_level_unfinish_count
    result['join_two_level_finish_count'] = join_two_level_finish_count
    result['join_two_level_unfinish_count'] = join_two_level_unfinish_count
    result['people_join_task_info'] = people_join_task_info

    unfinish_task_people_count = len(unfinish_task_people)
    result['unfinish_task_people_count'] = unfinish_task_people_count

    return result

def search_by_department(department_name):
    out_result = {}
    people_info = search_people_by_department(department_name)
    task_info = search_task_by_department(department_name)
    for key in task_info:
        people_info[key] = task_info[key]
    out_result[department_name] = people_info

    return out_result

def search_by_name(person_name):
    return None

def search_ganbu_info(department_name=None, task_type=None, age_area=None, sex=None, person_name=None):
    # if person_name:
    #     return search_by_name(person_name)
    # if department_name:
    #
    # else:
    return None


if __name__ == '__main__':
    # people_info = search_people_by_department(u'办公厅')
    # out_file = './search_people_by_department.json'
    # json.dump(people_info, codecs.open(out_file, 'w', encoding='utf-8'), ensure_ascii=False)

    # people_info = search_task_by_department(u'办公厅')
    # out_file = './search_task_by_department.json'
    # json.dump(people_info, codecs.open(out_file, 'w', encoding='utf-8'), ensure_ascii=False)

    department_file = './departments'
    out_result = {}
    with codecs.open(department_file, 'r', encoding='utf-8')  as rf:
        for department in rf.readlines():
            department_name = department.strip()
            result = search_people_by_department(department_name)
            task_info = search_task_by_department(department_name)
            for key in task_info:
                result[key] = task_info[key]
            out_result[department_name] = result
    json.dump(out_result, codecs.open('./search_result_by_department.json', 'w',  encoding='utf-8'), ensure_ascii=False)
