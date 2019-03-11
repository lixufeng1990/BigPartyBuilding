#-*- coding:utf-8 -*-

import codecs
import json

def get_gaoxiaokexie():
    file = '../data/load_gaoxiaokexie.json'
    result = {}
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_province = json.load(rf)
        for province in all_province:
            if province['province'] in result:
                result[province['province']] += 1
            else:
                result[province['province']] = 1

    return result

def get_qiyekexie():
    file = '../data/load_qiyekexie.json'
    result = {}
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_province = json.load(rf)
        for province in all_province:
            if province['province'] in result:
                result[province['province']] += 1
            else:
                result[province['province']] = 1

    return result

def get_yuanqukexie():
    file = '../data/load_yuanqukexie.json'
    result = {}
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_province = json.load(rf)
        for province in all_province:
            if province['province'] in result:
                result[province['province']] += 1
            else:
                result[province['province']] = 1

    return result

def get_nongjixie():
    file = '../data/nongjixie.json'
    result = {}
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_province = json.load(rf)
        for province in all_province:
            result[province['province']] = province['total']

    return result

def get_all_info():
    all_province_total = json.load(codecs.open('../data/all_province_total.json', 'r', encoding='utf-8'))
    gaoxiaokexie = json.load(codecs.open('../data/gaoxiaokexie.json', 'r', encoding='utf-8'))
    nongjixie = json.load(codecs.open('../data/nongjixie_dict.json', 'r', encoding='utf-8'))
    qiyekexie = json.load(codecs.open('../data/qiyekexie.json', 'r', encoding='utf-8'))
    yuanqukexie = json.load(codecs.open('../data/yuanqukexie.json', 'r', encoding='utf-8'))

    for province in all_province_total:
        if province['name'] in gaoxiaokexie:
            province['gaoxiao'] = gaoxiaokexie[province['name']]
        else:
            province['gaoxiao'] = 0

        if province['name'] in nongjixie:
            province['nongji'] = nongjixie[province['name']]
        else:
            province['nongji'] = 0

        if province['name'] in qiyekexie:
            province['qiye'] = qiyekexie[province['name']]
        else:
            province['qiye'] = 0

        if province['name'] in yuanqukexie:
            province['yuanqu'] = yuanqukexie[province['name']]
        else:
            province['yuanqu'] = 0

    return all_province_total


if __name__ == "__main__":
    # json.dump(get_gaoxiaokexie(), codecs.open('../data/gaoxiaokexie.json', 'w', encoding='utf-8'), ensure_ascii=False)
    # json.dump(get_qiyekexie(), codecs.open('../data/qiyekexie.json', 'w', encoding='utf-8'), ensure_ascii=False)
    # json.dump(get_yuanqukexie(), codecs.open('../data/yuanqukexie.json', 'w', encoding='utf-8'), ensure_ascii=False)
    # json.dump(get_nongjixie(), codecs.open('../data/nongjixie_dict.json', 'w', encoding='utf-8'), ensure_ascii=False)
    json.dump(get_all_info(), codecs.open('../data/all_info.json', 'w', encoding='utf-8'), ensure_ascii=False)