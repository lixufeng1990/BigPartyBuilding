import json
import codecs
'''
生成构建schema所需的字典文件
'''
tags = ["expert_award", "expert_book", "expert_project_by_ceet", "expert_project_by_jjw", "expert_paper_by_ceet", "expert_paper_by_wf_paper",
        "expert_patent_by_ceet", "expert_patent_by_wf_patent"]

input_file_path = './data/expert_tj.json'
schema_file_path = './data/rencai_properties.json'


schema = {"award":[], 'book':[], 'project':[], 'paper':[], 'patent':[]}

source = json.load(codecs.open(input_file_path, 'r', encoding='utf-8'))

schema["award"] = list(source['expert_award'].keys())

schema["book"] = list(source['expert_book'].keys())

schema["project"] = list(set(list(source['expert_project_by_ceet'].keys())+list(source['expert_project_by_jjw'].keys())))

schema["paper"] = list(set(list(source['expert_paper_by_ceet'].keys())+list(source['expert_paper_by_wf_paper'].keys())))

schema["patent"] = list(set(list(source['expert_patent_by_ceet'].keys())+list(source['expert_patent_by_wf_patent'].keys())))

json.dump(schema, codecs.open(schema_file_path, 'w', encoding='utf-8'), ensure_ascii=False)



