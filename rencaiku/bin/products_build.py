import json
import codecs
'''
绘制人才成果饼图：论文、专利、项目
'''
in_file_path = '../data/sorted_expert_product_stat_result.json'
out_file_path = '../data/expert_product_stat_build.json'

products_stats = json.load(codecs.open(in_file_path, 'r', encoding="utf-8"))

result = {'paper':{'x_name':[],'y_value':[]},'patent':{'x_name':[],'y_value':[]},'project':{'x_name':[],'y_value':[]}}

'''
分的很细：到30
count_15 = 0
count_20 = 0
count_25 = 0
count_30 = 0
count_other = 0
for paper_stats in products_stats['paper_stats']:
    if int(paper_stats[0]) <= 10:
        result['paper']['x_name'].append(paper_stats[0])
        result['paper']['y_value'].append({'value':paper_stats[1], 'name':paper_stats[0]})
    elif int(paper_stats[0]) > 10 and int(paper_stats[0]) < 15:
        count_15 += paper_stats[1]
    elif int(paper_stats[0]) == 15:
        count_15 += paper_stats[1]
        result['paper']['x_name'].append('10-15')
        result['paper']['y_value'].append({'value': count_15, 'name': '10-15'})
    elif int(paper_stats[0]) > 15 and int(paper_stats[0]) < 20:
        count_20 += paper_stats[1]
    elif int(paper_stats[0]) == 20:
        count_20 += paper_stats[1]
        result['paper']['x_name'].append('15-20')
        result['paper']['y_value'].append({'value': count_20, 'name': '15-20'})
    elif int(paper_stats[0]) > 20 and int(paper_stats[0]) < 25:
        count_25 += paper_stats[1]
    elif int(paper_stats[0]) == 25:
        count_25 += paper_stats[1]
        result['paper']['x_name'].append('20-25')
        result['paper']['y_value'].append({'value': count_25, 'name': '20-25'})
    elif int(paper_stats[0]) > 25 and int(paper_stats[0]) < 30:
        count_30 += paper_stats[1]
    elif int(paper_stats[0]) == 30:
        count_30 += paper_stats[1]
        result['paper']['x_name'].append('25-30')
        result['paper']['y_value'].append({'value': count_30, 'name': '25-30'})
    else:
        count_other += paper_stats[1]
result['paper']['x_name'].append('大于30')
result['paper']['y_value'].append({'value': count_other, 'name': '大于30'})
for patent_stats in products_stats['patent_stats']:
    if int(patent_stats[0]) <= 10:
        result['patent']['x_name'].append(patent_stats[0])
        result['patent']['y_value'].append({'value':patent_stats[1], 'name':patent_stats[0]})
    elif int(patent_stats[0]) > 10 and int(patent_stats[0]) < 15:
        count_15 += patent_stats[1]
    elif int(patent_stats[0]) == 15:
        count_15 += patent_stats[1]
        result['patent']['x_name'].append('10-15')
        result['patent']['y_value'].append({'value': count_15, 'name': '10-15'})
    elif int(patent_stats[0]) > 15 and int(patent_stats[0]) < 20:
        count_20 += patent_stats[1]
    elif int(patent_stats[0]) == 20:
        count_20 += patent_stats[1]
        result['patent']['x_name'].append('15-20')
        result['patent']['y_value'].append({'value': count_20, 'name': '15-20'})
    elif int(patent_stats[0]) > 20 and int(patent_stats[0]) < 25:
        count_25 += patent_stats[1]
    elif int(patent_stats[0]) == 25:
        count_25 += patent_stats[1]
        result['patent']['x_name'].append('20-25')
        result['patent']['y_value'].append({'value': count_25, 'name': '20-25'})
    elif int(patent_stats[0]) > 25 and int(patent_stats[0]) < 30:
        count_30 += patent_stats[1]
    elif int(patent_stats[0]) == 30:
        count_30 += patent_stats[1]
        result['patent']['x_name'].append('25-30')
        result['patent']['y_value'].append({'value': count_30, 'name': '25-30'})
    else:
        count_other += patent_stats[1]
result['patent']['x_name'].append('大于30')
result['patent']['y_value'].append({'value': count_other, 'name': '大于30'})

for project_stats in products_stats['project_stats']:
    if int(project_stats[0]) <= 10:
        result['project']['x_name'].append(project_stats[0])
        result['project']['y_value'].append({'value':project_stats[1], 'name':project_stats[0]})
    elif int(project_stats[0]) > 10 and int(project_stats[0]) < 15:
        count_15 += project_stats[1]
    elif int(project_stats[0]) == 15:
        count_15 += project_stats[1]
        result['project']['x_name'].append('10-15')
        result['project']['y_value'].append({'value': count_15, 'name': '10-15'})
    elif int(project_stats[0]) > 15 and int(project_stats[0]) < 20:
        count_20 += project_stats[1]
    elif int(project_stats[0]) == 20:
        count_20 += project_stats[1]
        result['project']['x_name'].append('15-20')
        result['project']['y_value'].append({'value': count_20, 'name': '15-20'})
    elif int(project_stats[0]) > 20 and int(project_stats[0]) < 25:
        count_25 += project_stats[1]
    elif int(project_stats[0]) == 25:
        count_25 += project_stats[1]
        result['project']['x_name'].append('20-25')
        result['project']['y_value'].append({'value': count_25, 'name': '20-25'})
    elif int(project_stats[0]) > 25 and int(project_stats[0]) < 30:
        count_30 += project_stats[1]
    elif int(project_stats[0]) == 30:
        count_30 += project_stats[1]
        result['project']['x_name'].append('25-30')
        result['project']['y_value'].append({'value': count_30, 'name': '25-30'})
    else:
        count_other += project_stats[1]
result['project']['x_name'].append('大于30')
result['project']['y_value'].append({'value': count_other, 'name': '大于30'})
'''

count_other = 0
for paper_stats in products_stats['paper_stats']:
    if int(paper_stats[0]) <= 5:
        result['paper']['x_name'].append(paper_stats[0])
        result['paper']['y_value'].append({'value':paper_stats[1], 'name':paper_stats[0]})
    else:
        count_other += paper_stats[1]
result['paper']['x_name'].append('大于5')
result['paper']['y_value'].append({'value': count_other, 'name': '大于5'})

count_other = 0
for patent_stats in products_stats['patent_stats']:
    if int(patent_stats[0]) <= 5:
        result['patent']['x_name'].append(patent_stats[0])
        result['patent']['y_value'].append({'value':patent_stats[1], 'name':patent_stats[0]})
    else:
        count_other += patent_stats[1]
result['patent']['x_name'].append('大于5')
result['patent']['y_value'].append({'value': count_other, 'name': '大于5'})

count_other = 0
for project_stats in products_stats['project_stats']:
    if int(project_stats[0]) <= 5:
        result['project']['x_name'].append(project_stats[0])
        result['project']['y_value'].append({'value':project_stats[1], 'name':project_stats[0]})
    else:
        count_other += project_stats[1]
result['project']['x_name'].append('大于5')
result['project']['y_value'].append({'value': count_other, 'name': '大于5'})

json.dump(result, codecs.open(out_file_path, 'w', encoding='utf-8'), ensure_ascii=False)



