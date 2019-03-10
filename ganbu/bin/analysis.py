import ganbu.bin.getData as getData
import json
import codecs

# jiguan_people = getData.get_jiguan_people()
# shiye_people = getData.get_shiye_people()
# project_people = getData.get_project_people()
# task_people = getData.get_task_people()
# all_people = getData.get_all_people()

def find_different_people_in_two_source():
    jiguan_people = getData.get_jiguan_people()
    shiye_people = getData.get_shiye_people()
    project_people = getData.get_project_people()
    task_people = getData.get_task_people()
    has_people = []
    miss_people = {}
    miss_people_names = []
    for jiguan_person in jiguan_people:
        has_people.append(jiguan_person['name'])
    for shiye_person in shiye_people:
        has_people.append(shiye_person['name'])

    for project_person in project_people:
        if (project_person['name'] not in has_people) and (project_person['name'] not in miss_people.keys()):
            miss_people_names.append(project_person['name'])
            miss_people[project_person['name']] = ({'name':project_person['name'], 'upper_department_name':project_person['upper_department_name'],
                                'project_name':project_person['project_name'], 'department_name':project_person['department_name'], 'project_role':project_person['project_role']})
    for task_person in task_people:
        if (task_person['name'] not in has_people) and (task_person['name'] not in miss_people.keys()):
            miss_people_names.append(task_person['name'])
            miss_people[task_person['name']] = ({'name': project_person['name'], 'upper_department_name': project_person['upper_department_name'],
                 'project_name': project_person['project_name'], 'department_name': project_person['department_name'], 'task_name':task_person['task_name']})


    return miss_people_names

def get_department_for_people_in_xueshi():
    peopel_with_department = {}
    all_xueshi_people = getData.get_shiye_people()
    all_people = getData.get_all_people()
    for xueshi_person in all_xueshi_people:
        if xueshi_person['name'] not in peopel_with_department.keys():
            flag = True
            for ganbu in all_people:
                if xueshi_person['name'] == ganbu['name']:
                    peopel_with_department[xueshi_person['name']] = ganbu['department']
                    flag = False
                    break
            if flag:
                peopel_with_department[xueshi_person['name']] = '未知'

    return peopel_with_department







if __name__ == '__main__':
    # miss_people = find_different_people_in_two_source()
    # json.dump(miss_people, codecs.open('./miss_people.txt', 'w', encoding='utf-8'), ensure_ascii=False)

    xueshi_people = get_department_for_people_in_xueshi()
    json.dump(xueshi_people, codecs.open('./xueshi_people.json', 'w', encoding='utf-8'), ensure_ascii=False)