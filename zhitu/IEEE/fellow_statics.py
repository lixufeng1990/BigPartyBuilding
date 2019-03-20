import json
import codecs

# ieee_file = 'ieee_tongji_data.json'
ieee_file = './data/ieee_tongji_data_v2.json'
acm_file = 'acm_tongji_data.json'

def get_ieee_tongji():
    all_fellows = json.load(codecs.open(ieee_file, 'r', encoding='utf-8'))
    wait_years = {}
    avg_pubs = {}
    avg_cite = {}
    sim_ranka = {}

    for fellow_key in all_fellows:
        fellow = all_fellows[fellow_key]
        if fellow['wait_year'] in wait_years:
            wait_years[fellow['wait_year']] += 1
        else:
            wait_years[fellow['wait_year']] = 1

        if fellow['avg_pub_num'] in avg_pubs:
            avg_pubs[fellow['avg_pub_num']] += 1
        else:
            avg_pubs[fellow['avg_pub_num']] = 1

        if fellow['avg_cite_num'] in avg_cite:
            avg_cite[fellow['avg_cite_num']] += 1
        else:
            avg_cite[fellow['avg_cite_num']] = 1

        if fellow['sim_rank'] in sim_ranka:
            sim_ranka[fellow['sim_rank']] += 1
        else:
            sim_ranka[fellow['sim_rank']] = 1

        sourted_wait_years = sorted(wait_years)
        wait_years_values = [wait_years[year] for year in sourted_wait_years]
        sourted_avg_pubs = sorted(avg_pubs)
        avg_pubs_values = [avg_pubs[pub] for pub in sourted_avg_pubs]
        sourted_avg_cite = sorted(avg_cite)
        avg_cite_values = [avg_cite[cite] for cite in sourted_avg_cite]
        sourted_sim_ranka = sorted(sim_ranka)
        sim_ranka_values = [round(sim_ranka[sim]/4440.354, 3) for sim in sourted_sim_ranka]

    return {'wait_years_kyes':sourted_wait_years,
            'wait_years_values':wait_years_values,
            'avg_pubs_keys':sourted_avg_pubs,
            'avg_pubs_values':avg_pubs_values,
            'avg_cite_keys':sourted_avg_cite,
            'avg_cite_values':avg_cite_values,
            'sim_ranka_keys':sourted_sim_ranka,
            'sim_ranka_values':sim_ranka_values,
            }


if __name__ == '__main__':
    json.dump(get_ieee_tongji(), codecs.open('ieee_statistics.json', 'w', encoding='utf-8'), ensure_ascii=False)