import json
import codecs

all_data = json.load(codecs.open('../data/first_field_all_province_tj_data.json', 'r', encoding='utf-8'))
second_level_all_data = json.load(codecs.open('../data/second_field_all_province_tj_data.json', 'r', encoding='utf-8'))

def get_map_data():
    map_data = {'project':[], 'patent':[], 'paper':[]}
    for province_name in all_data:
        province_data = all_data[province_name]
        map_data['project'].append({'name':province_name, 'people':province_data['people_count'], 'project':province_data['project_num']['project_count']})
        map_data['patent'].append({'name':province_name, 'people':province_data['people_count'], 'patent':province_data['patent_num']['patent_count']})
        map_data['paper'].append({'name':province_name, 'people':province_data['people_count'], 'paper':province_data['paper_num']['paper_count']})

    return map_data

def get_second_level_map_data():
    result = {}
    for second_level_name in second_level_all_data:
        second_level_data = second_level_all_data[second_level_name]
        meta_map_data = {'project': [], 'patent': [], 'paper': []}
        for province_name in second_level_data:
            province_data = second_level_data[province_name]
            meta_map_data['project'].append({'name':province_name, 'people':province_data['people_count'], 'project':province_data['project_num']['project_count']})
            meta_map_data['patent'].append({'name':province_name, 'people':province_data['people_count'], 'patent':province_data['patent_num']['patent_count']})
            meta_map_data['paper'].append({'name':province_name, 'people':province_data['people_count'], 'paper':province_data['paper_num']['paper_count']})
            result[second_level_name] = meta_map_data

    return result

if __name__ == '__main__':
    # print(get_map_data())
    # print([x['name'] for x in get_map_data()['project']])
    json.dump(get_second_level_map_data(), codecs.open('../data/rczy_second_level_map_data.json', 'w', encoding='utf-8'), ensure_ascii=False)
    # json.dump(get_map_data(), codecs.open('../data/rczy_map_data.json', 'w', encoding='utf-8'), ensure_ascii=False)
