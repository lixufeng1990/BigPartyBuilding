#coding=utf-8
#python3
import jieba.posseg as pseg
import json
import codecs
import time
import requests
from bs4 import BeautifulSoup
def spbaike(url):
    headers = {
        'Host': 'baike.baidu.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    }
    time.sleep(0.1)
    info = {}
    wb_data = requests.get(url,headers=headers).content
    soup = BeautifulSoup(wb_data,'lxml')
    name_ = soup.select('.lemmaWgt-lemmaTitle-title > h1')
    if len(name_) != 0:
        name = name_[0].get_text()
    else:
        return False
    info['name'] = name
    description = soup.select('body > div.body-wrapper > div.content-wrapper > div > div.main-content > div.lemma-summary > div ')
    if len(description) != 0:
            description_ = ''
            for des in description:
                description_ += des.get_text()
            info['description'] = description_.replace('\n','').replace('\xa0','')
    else:
        description = soup.select('body > div.body-wrapper > div.content-wrapper > div > div.main-content > div.para')
        if len(description) != 0:
            description_ = ''
            for des in description:
                description_ += des.get_text()
            info['description'] = description_.replace('\n', '').replace('\xa0', '')
    taglist_ = soup.select('.taglist')
    if len(taglist_) > 0:  # taglist
        taglist = ''
        for tag in taglist_:
            taglist += tag.get_text().replace('\n','')+','
        taglist = taglist[:-1]
        info['taglist'] = taglist
    datalist1 = soup.select('div.basic-info.cmn-clearfix > dl > dt')  # infoboxAttributes
    datalist2 = soup.select('div.basic-info.cmn-clearfix > dl > dd')  # infoboxAttributesValue
    if len(datalist1) != 0 and len(datalist2) != 0:
        for i in range(len(datalist1)):
            info[datalist1[i].get_text().replace('\xa0','')] = datalist2[i].get_text().strip()
    datalist3 = soup.select('.title-text')  # 详细信息
    if len(datalist3) != 0:
        detail_header = []
        detail_content = ''
        for data in datalist3:
            detail_header.append(data.get_text())
        detail_header.append('词条标签')
        datalist4 = soup.select('body > div.body-wrapper > div.content-wrapper > div > div.main-content > div ')
        for data in datalist4:
            detail_content += data.get_text()
        detail_content = detail_content.replace('\n','').replace('\xa0','').replace('编辑','')
        length = len(detail_header)
        for i in range(0,length-1):
            begin = detail_content.find(detail_header[i])
            end = detail_content.find(detail_header[i+1])
            info[detail_header[i].replace(name,'')] = detail_content[begin+len(detail_header[i]):end]
    if len(info) == 0:
        print('姓名为:'+name+' 节点不存在！')
        return False
    else:
        return info

if __name__=="__main__":
    # info = spbaike('https://baike.baidu.com/item/%E5%90%B4%E6%9D%B0/12699479')
    # print(info)
    qingke_file = '../rencai/data/15th_qingke_candidate.json'
    qingke_people = json.load(codecs.open(qingke_file, 'r', encoding='utf-8'))
    qingke_names = set()
    for qingke_person in qingke_people:
        qingke_names.add(qingke_person['name'])
    count = 0
    nodes = []
    urls = json.load(codecs.open('qingke_nameAndDepart_url.json', 'r', encoding='utf-8'))
    for url in urls:
        info = spbaike(url['url'])
        try:
            if info['name'] in qingke_names:
                count += 1
                print("processing :"+str(count)+" url info...")
                nodes.append(info)
        except:
            print(info)
    json.dump(nodes, codecs.open('scholar_detail.json','w',encoding='utf-8'), ensure_ascii=False)
    # json_data = json.dumps({'nodes':nodes}, ensure_ascii=False)
    # with codecs.open('scholar_detail.json','w',encoding='utf-8') as foo:
    #     foo.write(json_data)