import json
import codecs
'''
统计人才成果：论文、专利、项目、书籍、获奖的分布情况，绘制饼图
'''
in_file_path = '../data/expert_product_stat_result.json'
out_file_path = '../data/sorted_expert_product_stat_result.json'

products_stats = json.load(codecs.open(in_file_path, 'r', encoding="utf-8"))

result = {}

for products_key in products_stats:
    result[products_key] = sorted(products_stats[products_key].items(), key=lambda x:int(x[0]))

json.dump(result, codecs.open(out_file_path, 'w', encoding='utf-8'), ensure_ascii=False)



