import json
import os
import jieba.analyse
import jieba
import numpy as np
yuanshi = json.load(open('yuanshi_experiences.json',encoding = 'utf-8'))
yuanshis = sorted(yuanshi,key = lambda item:len(item['人物经历']),reverse = True)
features = [['留学'],['进步奖','成就奖'],['总工程师'],['自然科学基金','杰出青年基金']]
#
'''
sample50 = []
schools = {}
for index,ele in enumerate(yuanshis):
	tem = []
	s = ele['organization']
	if s not in schools:
		schools[s] = 0
	schools[s] += 1
	#tem.append(0)
	#sentence = ele['人物经历']
	#tem.append(0)
	#for feature in features:
	#	flag = 0
	#	for ele in feature:
	#		if sentence.find(ele) > 0:
	#			flag = 1
	#			break
	#	tem.append(flag)
	#sample50.append(tem)
	#if index >= 100:
		#break

schools = sorted(schools.items(),key = lambda item:item[1],reverse = True)
for index,ele in enumerate(schools):
	print(ele[0])
	if index > 10:
		break
exit(0)
'''
def train_class(features,datas,tot):
	prob = []
	prob.append(len(datas) / tot)
	fea = [0] * len(features)
	for data in datas:
		sentence = data['description']
		for i,feature in enumerate(features):
			flag = 0
			for ele in feature:
				if sentence.find(ele) > 0:
					flag = 1
			fea[i] += flag
	for x in fea:
		x = (x + 1) / (len(datas) + 2)
		prob.append([1-x,x])
	return prob

def train(features,posdatas,negdatas):
	tot = len(posdatas) + len(negdatas)
	prob = {}
	prob['pos'] = train_class(features,posdatas,tot)
	prob['neg'] = train_class(features,negdatas,tot)
	return prob


posdatas = []
for index,ele in enumerate(yuanshis):
	tem = {}
	#s = ele['organization']
	#tem.append(0)
	tem['description'] = ele['人物经历']
	posdatas.append(tem)
	if index >= 50:
		break
negdatas = []
Neg1 = json.load(open('scholar_dict_2.json',encoding = 'utf-8'))['nodes']
Neg2 = json.load(open('scholar_dict_26.json',encoding = 'utf-8'))['nodes']
for ele in Neg1:
	if 'description' in ele:
		negdatas.append(ele)
for ele in Neg2:
	if 'description' in ele:
		negdatas.append(ele)
print(len(negdatas))
prob = train(features,posdatas,negdatas)

def preidct(prob,x):
	po = np.log(prob['pos'][0])
	pn = np.log(prob['neg'][0])
	for i,ele in enumerate(x):
		po += np.log(prob['pos'][i + 1][ele])
		pn += np.log(prob['neg'][i + 1][ele])
	#print('po',po)
	#print('pn',pn)
	return 1 if po > pn else 0


#print(prob)
#x = [0,0,0,0,0,0,0,0,0,0]

#[0, 0, 28, 24, 20, 19, 26, 19, 26, 18, 37, 20]
def exact_features(x,keyname):
	sentence = x[keyname]
	tem = []
	for feature in features:
		flag = 0
		for ele in feature:
			if sentence.find(ele) > 0:
				flag = 1
				break
		tem.append(flag)
	return tem
acc = 0
for ele in yuanshis[100:200]:
	if preidct(prob,exact_features(ele,'人物经历')) == 1:
		acc += 1
print(acc / 100)
pro1 = []
pro2 = []
for i in range(len(prob['pos'])):
	if i == 0:
		continue
	pro1.append((i,prob['pos'][i][1]))
	pro2.append((i,prob['pos'][i][1] - prob['neg'][i][1]))
	#print('pos',prob['pos'][i])
	#print('neg',prob['neg'][i])
pro1 = sorted(pro1,key = lambda item:item[1],reverse = True)
pro2 = sorted(pro2,key = lambda item:item[1],reverse = True)
for i in pro1:
	print(features[i[0] - 1],i[1])
print('pro2')
for i in pro2:
	#print(i[0])
	print(features[i[0] - 1],i[1])
