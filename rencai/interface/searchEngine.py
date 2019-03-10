#-*- coding:utf-8 -*-

import codecs
import json
import rencai.bin.getData as getDate

provinces = ["江苏", "浙江", "广东", "福建", "山东", "湖南", "安徽", "河北", "上海", "湖北", "河南", "四川", "江西", "辽宁", "北京", "陕西", "山西", "天津",
             "重庆", "吉林", "黑龙江", "云南", "广西", "内蒙古", "贵州", "甘肃", "海南", "新疆", "宁夏", "西藏"]

def search_by_15th_qingke():
    qingke_candidates = getDate.get_15th_qingke_candidate()
    result = {}
    all_age = {'m29': 0, 'm3039': 0, 'm4049': 0, 'm5059': 0, 'm60': 0,
               'f29': 0, 'f3039': 0, 'f4049': 0, 'f5059': 0, 'f60': 0}  # 年龄分布
    all_politicalOutlook = {}  # 政治面貌
    all_nation = {}
    all_unit_xingzhi = {}
    candidate_list = []
    all_major = {}
    province_distribution = {}
    for province in provinces:
        province_distribution[province] = 0

    for candidate in qingke_candidates:
        candidate_list.append((candidate['name'], candidate['department_and_job']))
        # 政治面貌
        political_outlook = str(candidate['political_outlook'])
        if len(political_outlook) != 0:
            if political_outlook not in all_politicalOutlook.keys():
                all_politicalOutlook[political_outlook] = 1
            else:
                all_politicalOutlook[political_outlook] += 1
        else:
            all_politicalOutlook[u'其他'] += 1
        # 年龄
        age = candidate['age']
        sex = candidate['sex'].strip()
        if (len(sex) != 0):
            if sex == '男':
                if age < 30:
                    all_age['m29'] += 1
                elif 30 <= age < 40:
                    all_age['m3039'] += 1
                elif 40 <= age < 49:
                    all_age['m4049'] += 1
                elif 50 <= age < 59:
                    all_age['m5059'] += 1
                else:
                    all_age['m60'] += 1
            else:
                if age < 30:
                    all_age['f29'] += 1
                elif 30 <= age < 40:
                    all_age['f3039'] += 1
                elif 40 <= age < 49:
                    all_age['f4049'] += 1
                elif 50 <= age < 59:
                    all_age['f5059'] += 1
                else:
                    all_age['f60'] += 1
        # 民族
        nation = candidate['nation'].strip()
        if len(nation) != 0:
            if nation not in all_nation.keys():
                all_nation[nation] = 1
            else:
                all_nation[nation] += 1
        else:
            all_nation[u'其他'] += 1
        # 单位性质
        unit_xingzhi = candidate['unit_xingzhi'].strip()
        if len(unit_xingzhi) != 0:
            if unit_xingzhi not in all_unit_xingzhi.keys():
                all_unit_xingzhi[unit_xingzhi] = 1
            else:
                all_unit_xingzhi[unit_xingzhi] += 1
        else:
            all_unit_xingzhi[u'其他'] += 1
        #专业专长
        maior_job = candidate['maior_job'].strip()
        if len(maior_job) != 0:
            if maior_job not in all_major.keys():
                all_major[maior_job] = 1
            else:
                all_major[maior_job] += 1
        else:
            all_major[u'其他'] += 1
        #各省份人数
        for province in province_distribution:
            if province in candidate['location']:
                province_distribution[province] += 1

    result['all_politicalOutlook'] = all_politicalOutlook
    result['all_nation'] = all_nation
    result['all_unit_xingzhi'] = all_unit_xingzhi
    result['all_age'] = all_age
    result['candidate_list'] = candidate_list[:18]
    result['count'] = len(qingke_candidates)
    result['all_major'] = all_major
    result['province_distribution'] = province_distribution
    return result

def search_by_9th_datbiao():
    all_9th_daibiao = getDate.get_9th_daibiao()
    all_politicalOutlook = {}

    for daibiao in all_9th_daibiao:
        political_outlook = str(daibiao['political_outlook'])
        if len(political_outlook) != 0:
            if political_outlook not in all_politicalOutlook.keys():
                all_politicalOutlook[political_outlook] = 1
            else:
                all_politicalOutlook[political_outlook] += 1
        else:
            all_politicalOutlook[u'其他'] += 1

    print(all_politicalOutlook)

def search_by_selected_yuanshi(selected_yuanshi):
    result = {}
    all_age = {'m29': 0, 'm3039': 0, 'm4049': 0, 'm5059': 0, 'm60': 0,
               'f29': 0, 'f3039': 0, 'f4049': 0, 'f5059': 0, 'f60': 0}  # 年龄分布
    all_yuanshi_type = {}
    all_department = {}
    all_xueke = {}
    all_city = {}
    for yuanshi in selected_yuanshi:
        # 年龄
        age = yuanshi['age']
        sex = yuanshi['sex'].strip()
        if sex and age:
            if sex == '男':
                if age < 30:
                    all_age['m29'] += 1
                elif 30 <= age < 40:
                    all_age['m3039'] += 1
                elif 40 <= age < 49:
                    all_age['m4049'] += 1
                elif 50 <= age < 59:
                    all_age['m5059'] += 1
                else:
                    all_age['m60'] += 1
            else:
                if age < 30:
                    all_age['f29'] += 1
                elif 30 <= age < 40:
                    all_age['f3039'] += 1
                elif 40 <= age < 49:
                    all_age['f4049'] += 1
                elif 50 <= age < 59:
                    all_age['f5059'] += 1
                else:
                    all_age['f60'] += 1
        # 院士类别
        yuanshi_type = yuanshi['yuanshi_type']
        if len(yuanshi_type) != 0:
            if yuanshi_type not in all_yuanshi_type.keys():
                all_yuanshi_type[yuanshi_type] = 1
            else:
                all_yuanshi_type[yuanshi_type] += 1
        # 两院部门
        yuanshi_department = yuanshi['yuanshi_department'].strip()
        if len(yuanshi_department) != 0:
            if yuanshi_department not in all_department.keys():
                all_department[yuanshi_department] = 1
            else:
                all_department[yuanshi_department] += 1
        # 专业
        xueke = yuanshi['xueke'].strip()
        if len(xueke) != 0:
            if xueke not in all_xueke.keys():
                all_xueke[xueke] = 1
            else:
                all_xueke[xueke] += 1
        #所在的排行
        city = yuanshi['city'].strip()
        if len(city) != 0:
            if city not in all_city.keys():
                all_city[city] = 1
            else:
                all_city[city] += 1

    all_department = sorted(all_department.items(), key=lambda item:item[1], reverse=True)
    all_xueke = sorted(all_xueke.items(), key=lambda item:item[1], reverse=True)
    all_city = sorted(all_city.items(), key=lambda item:item[1], reverse=True)
    result['all_age'] = all_age
    result['all_yuanshi_type'] = all_yuanshi_type
    result['all_department'] = all_department[:8]
    result['all_xueke'] = all_xueke[:8]
    result['all_city'] = all_city
    result['province_num'] = len(all_city)
    return result

def search_yuanshi(sex=None, age_area=None, type=None, department=None):
    all_yuanshi = getDate.get_all_yuanshi()
    selected_yuanshi = []
    #思路：一层层的按照搜索条件，进行过滤
    for yuanshi in all_yuanshi:
        yuanshi_sex = yuanshi['sex']
        if sex:
            if yuanshi_sex != sex: continue
        yuanshi_age = yuanshi['age']
        if age_area:
            if (age_area == '29岁以下') and (yuanshi_age>29): continue
            elif (age_area=='30岁-39岁') and (yuanshi_age<30 or yuanshi_age>39): continue
            elif (age_area=='40岁-49岁') and (yuanshi_age<40 or yuanshi_age>49): continue
            elif (age_area=='50岁-59岁') and (yuanshi_age<50 or yuanshi_age>59): continue
            elif (age_area=='60岁以上') and (yuanshi_age<60): continue
        yuanshi_type = yuanshi['yuanshi_type']
        if type:
            if (type=='中国科学院') and (yuanshi_type=='工程院'): continue
            elif (type=='中国工程院') and (yuanshi_type=='科学院'): continue
        yuanshi_department = yuanshi['yuanshi_department']
        if department:
            if department != yuanshi_department: continue
        selected_yuanshi.append(yuanshi)

    return selected_yuanshi

def search_1st_chuangxin_candidate():
    all_1st_chuangxin_candidate = getDate.get_1st_chuangxin_candidate()
    result = {}
    #按省份的人数统计
    all_province = {}
    # 所在的排行
    for chuangxin_candidate in all_1st_chuangxin_candidate:
        province = chuangxin_candidate['province'].strip()
        if len(province) != 0:
            if province not in all_province.keys():
                all_province[province] = 1
            else:
                all_province[province] += 1
    all_province = sorted(all_province.items(), key=lambda item: item[1], reverse=True)
    result['all_province_num'] = len(all_province)
    result['all_province'] = all_province
    return result

def search_all_female_scientists():
    all_female_scientists = getDate.get_all_female_scientists()
    result = {}
    #按省份的人数统计
    all_province = {}
    # 所在的排行
    for female_scientist in all_female_scientists:
        province = female_scientist['province'].strip()
        if len(province) != 0:
            if province not in all_province.keys():
                all_province[province] = 1
            else:
                all_province[province] += 1
    all_province = sorted(all_province.items(), key=lambda item: item[1], reverse=True)
    result['all_province_num'] = len(all_province)
    result['all_province'] = all_province
    return result

if __name__ == '__main__':
    result = search_by_15th_qingke()
    json.dump(result, codecs.open('./search_by_15th_qingke.json', 'w', encoding='utf-8'), ensure_ascii=False)
    # search_by_9th_datbiao()
    # all_yuanshi_info = search_by_selected_yuanshi(all_yuanshi)
    # json.dump(all_yuanshi_info, codecs.open('./search_by_all_yuanshi.json', 'w', encoding='utf-8'), ensure_ascii=False)

    # selected_yuanshi_info = search_by_selected_yuanshi(search_yuanshi())
    # json.dump(selected_yuanshi_info, codecs.open('./selected_yuanshi_info_all_province_distribution.json', 'w', encoding='utf-8'), ensure_ascii=False)


    # json.dump(search_1st_chuangxin_candidate(), codecs.open('./search_1st_chuangxin_candidate.json', 'w', encoding='utf-8'), ensure_ascii=False)
    # json.dump(search_all_female_scientists(), codecs.open('./search_all_female_scientists.json', 'w', encoding='utf-8'), ensure_ascii=False)