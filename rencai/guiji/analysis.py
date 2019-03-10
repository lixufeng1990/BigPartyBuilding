import json
import codecs

def all_yuanshi_analysis():
    return None

def data_cut():
    file1 = open(r'data/data[2]_merge_solve.json', "r")
    fileJson = json.load(file1)
    for item in fileJson:
        print (item['id'])
        exp = item[u'人物经历']
        birth = item[u'出生年月'][0:4]
        if item[u'人物经历'] == "":
            continue
        sens = re.split('。|：|；',str(exp))
        result = []
        for sen in sens:
            sen = sen.decode('utf-8')
            if sen.__len__() < 15:
                continue
            for i in range(sen.__len__() - 4):
                #print (sen[i])
                if sen[i] >= '0' and sen[i] <= '9' and sen[i+1] >= '0' and sen[i+1] <= '9' and sen[i+2] >= '0' and sen[i+2] <= '9' and sen[i+3] >= '0' and sen[i+3] <= '9':
                    se = {}
                    now_time = sen[i:i+4]
                    age = int(now_time) - int(birth)
                    if age < 0:
                        age = 0
                    se['age'] = age
                    se['event'] = sen[i:]
                    result.append(se)
                    break
        item[u'人物经历'] = result
    jsda = json.dumps(fileJson, indent=4, ensure_ascii=False)
    fw = codecs.open("data/data[2]_merge_solve_cut.json", "w", encoding="utf-8")
    fw.write(jsda)