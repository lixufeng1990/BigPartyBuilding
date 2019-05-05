import json
import codecs
'''
将原始schema字典文件转换为前端所需的形式
'''
schema_in_file_path = './data/rencai_properties.json'
schema_out_file_path = './data/rencai_schema.json'

shema_properties = json.load(codecs.open(schema_in_file_path, 'r', encoding="utf-8"))

result = {
  "name": "学科",
  "children": []
}

for out_key in shema_properties.keys():
    result['children'].append({'name':out_key, 'children':[{'name':property, 'children':[]} for property in shema_properties[out_key]]})

json.dump(result, codecs.open(schema_out_file_path, 'w', encoding='utf-8'), ensure_ascii=False)