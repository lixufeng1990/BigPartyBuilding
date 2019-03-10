#-*- coding:utf-8 -*-

import codecs
import json

def get_sanzhang():
    file = '../data/sanzhang.json'
    result = []
    with codecs.open(file, 'r', encoding='utf-8') as rf:
        all_province = json.load(rf)
        for province in all_province:
            result.append({'name':province['name'], 'value':province['all_total'], 'province':province['province'], 'city':province['city'],
                           'area':province['area'], 'street':province['street']})

    return result


if __name__ == "__main__":
    json.dump(get_sanzhang(), codecs.open('../data/get_sanzhang.json', 'w', encoding='utf-8'), ensure_ascii=False)