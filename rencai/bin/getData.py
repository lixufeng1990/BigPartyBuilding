#-*- coding:utf-8 -*-

import codecs
import json

def get_9th_daibiao():
    file = '../data/9th_daibiao.json'
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_people = json.load(rf)
    return all_people

def get_15th_qingke_candidate():
    file = '../data/15th_qingke_candidate.json'
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_people = json.load(rf)
    return all_people

def get_all_qingke():
    file = '../data/all_qingke.json'
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_people = json.load(rf)
    return all_people

def get_2017_yuanshi_candidate():
    file = '../data/2017_yuanshi_candidate.json'
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_people = json.load(rf)
    return all_people

def get_all_yuanshi():
    file = '../data/all_yuanshi.json'
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_people = json.load(rf)
    return all_people

def get_1st_chuangxin_candidate():
    file = '../data/1st_chuangxin_candidate.json'
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_people = json.load(rf)
    return all_people

def get_all_female_scientists():
    file = '../data/all_female_scientists.json'
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_people = json.load(rf)
    return all_people

def get_5_wei_analysis():
    file = '../data/5_wei_analysis.json'
    result = {'data1':[], 'data2':[], 'data3':[], 'data4':[], 'data5':[]}
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_province = json.load(rf)
        for province in all_province:
            result['data1'].append([province['edu'], province['gdp'], province['name'], '教育水平'])
            result['data2'].append([province['scholar'], province['gdp'], province['name'], '学者数量'])
            result['data3'].append([province['rd'], province['gdp'], province['name'], 'R&D经费投入'])
            result['data4'].append([round(province['science']/0.689, 3), province['gdp'], province['name'], '科技创新水平'])
            result['data5'].append([round(province['quality']/18.71, 3), province['gdp'], province['name'], '公民科学素质'])


    return result


if __name__ == "__main__":
    json.dump(get_5_wei_analysis(), codecs.open('../data/get_5_wei_analysis.json', 'w', encoding='utf-8'), ensure_ascii=False)