import json
import codecs

fellow_file = 'ieee_fellow_new.json'
accumulation_file = 'fellow_paper_year_count_2.json'
fellows = json.load(codecs.open(fellow_file, 'r', encoding='utf-8'))['RECORDS']

def basic_info_static():
    sex = {'male':0, "female":0}
    countries = {}
    regions = {}
    orgs = {}
    phd_schools = {}

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

        if fellow['final_phd_school']:
            if fellow['final_phd_school'] in phd_schools:
                phd_schools[fellow['final_phd_school']] += 1
            else:
                phd_schools[fellow['final_phd_school']] = 1

    sourted_countries = sorted(countries.items(), key=lambda x: x[1], reverse=True)
    sourted_regions = sorted(regions.items(), key=lambda x: x[1], reverse=True)
    sourted_orgs = sorted(orgs.items(), key=lambda x: x[1], reverse=True)
    sourted_phd_schools = sorted(phd_schools.items(), key=lambda x: x[1], reverse=True)

    json.dump({'sex':sex, 'countries':sourted_countries, 'regions':sourted_regions, "orgs":sourted_orgs, "phd_schools":sourted_phd_schools}, codecs.open('tongji.json', 'w', encoding='utf-8'), ensure_ascii=False)

def years_static():
    accumulation_people = json.load(codecs.open(accumulation_file, 'r', encoding='utf-8'))
    years_people = {}
    for accumulation_person in accumulation_people:
        year = accumulation_people[accumulation_person]
        if year not in years_people:
            years_people[year] = 1
        else:
            years_people[year] += 1
    # years_people = sorted(years_people.items(), key=lambda x: x[0], reverse=False)

    years = sorted(years_people)
    nums = [years_people[year]+14 for year in years]

    print(years)
    print(nums)

if __name__ == "__main__":
    # years_static()
    basic_info_static()