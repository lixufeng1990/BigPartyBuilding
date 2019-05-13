import json
import codecs
'''
加入知兔的数据重新进行估计：全体28%加入19篇论文，10个项目和8个专利
'''
in_file_path = '../data/sorted_expert_product_stat_result.json'
out_file_path = '../data/zhitu_sorted_expert_product_stat.json'

products_stats = json.load(codecs.open(in_file_path, 'r', encoding="utf-8"))

result = {}

for products_key in products_stats:
    result[products_key] = sorted(products_stats[products_key].items(), key=lambda x:int(x[0]))

json.dump(result, codecs.open(out_file_path, 'w', encoding='utf-8'), ensure_ascii=False)



