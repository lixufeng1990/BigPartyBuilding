import json
import codecs

fellow_file = 'ieee_fellow_new.json'

fellows = json.load(codecs.open(fellow_file, 'r', encoding='utf-8'))['RECORDS']

sex = {'male':0, "female":0}
countries = {}
regions = {}
orgs = {}

for fellow in fellows:
    if fellow['gender'] and fellow['gender'] == 'male':
        sex['male'] += 1
    elif fellow['gender'] and fellow['gender'] == 'female':
        sex['female'] += 1


    if fellow['final_org_country']:
        if fellow['final_org_country'] in countries:
            countries[fellow['final_org_country']] += 1
        else:
            countries[fellow['final_org_country']] = 1

    if fellow['region']:
        if fellow['region'] in regions:
            regions[fellow['region']] += 1
        else:
            regions[fellow['region']] = 1

    if fellow['final_org']:
        if fellow['final_org'] in orgs:
            orgs[fellow['final_org']] += 1
        else:
            orgs[fellow['final_org']] = 1

sourted_countries = sorted(countries.items(), key=lambda x: x[1], reverse=True)
sourted_regions = sorted(regions.items(), key=lambda x: x[1], reverse=True)
sourted_orgs = sorted(orgs.items(), key=lambda x: x[1], reverse=True)


json.dump({'sex':sex, 'countries':sourted_countries, 'regions':sourted_regions, "orgs":sourted_orgs}, codecs.open('tongji.json', 'w', encoding='utf-8'), ensure_ascii=False)