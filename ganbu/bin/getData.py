#-*- coding:utf-8 -*-

import codecs
import json

def get_jiguan_people():
    file = '../../data/all_jiguan_people.json'
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_people = json.load(rf)
    return all_people

def get_shiye_people():
    file = '../../data/all_shiye_people.json'
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_people = json.load(rf)
    return all_people

def get_project_people():
    file = '../../data/all_project_people.json'
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_people = json.load(rf)
    return all_people

def get_task_people():
    file = '../../data/all_task_people.json'
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_people = json.load(rf)
    return all_people

def fusion_all_people():
    jiguan_people = get_jiguan_people()
    shiye_people = get_shiye_people()
    all_people = []
    for jiguan_person in jiguan_people:
        unify_person = {}
        unify_person['name'] = jiguan_person['name']
        unify_person['sex'] = jiguan_person['sex']
        unify_person['political_outlook'] = jiguan_person['political_outlook']
        unify_person['birthDay'] = jiguan_person['birthDay']
        if jiguan_person['birthDay']:
            unify_person['age'] = 2018 - int(str(jiguan_person['birthDay']).split('.')[0])
        else:
            unify_person['age'] = None
        unify_person['xueli'] = jiguan_person['xueli']
        unify_person['department'] = jiguan_person['department']
        unify_person['chushi'] = jiguan_person['chushi']
        unify_person['company_and_job'] = jiguan_person['icompany_and_job']
        unify_person['type'] = '机关'
        all_people.append(unify_person)
    for shiye_person in shiye_people:
        unify_person = {}
        unify_person['name'] = shiye_person['name']
        unify_person['sex'] = shiye_person['sex']
        unify_person['political_outlook'] = shiye_person['political_outlook']
        unify_person['birthDay'] = shiye_person['birth']
        birth_year = str(shiye_person['birth_year']).strip()
        if birth_year:
            birth_year = birth_year.split('.')[0]
            age = 2018 - int(birth_year)
            unify_person['age'] = age
        else:
            unify_person['age'] = None
        unify_person['xueli'] = shiye_person['xueli']
        unify_person['department'] = shiye_person['unit']
        unify_person['chushi'] = shiye_person['unit_department']
        unify_person['company_and_job'] = shiye_person['department']+shiye_person['job']
        unify_person['type'] = '事业'
        all_people.append(unify_person)

    return all_people

def get_all_people():
    file = '../../data/all_ganbu.json'
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_people = json.load(rf)
    return all_people

def get_xueshi_people():
    file = '../../data/all_xueshi.json'
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_people = json.load(rf)
    return all_people


if __name__ == '__main__':
    all_people = fusion_all_people()
    json.dump(all_people, codecs.open('../../data/all_ganbu.json', 'w', encoding='utf-8'), ensure_ascii=False)
