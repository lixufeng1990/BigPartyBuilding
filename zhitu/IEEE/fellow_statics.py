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
    sim_ranks = {}

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

        if fellow['sim_rank'] in sim_ranks:
            sim_ranks[fellow['sim_rank']] += 1
        else:
            sim_ranks[fellow['sim_rank']] = 1

        sourted_wait_years = sorted(wait_years)
        wait_years_values = [wait_years[year] for year in sourted_wait_years]
        sourted_avg_pubs = sorted(avg_pubs)
        avg_pubs_values = [avg_pubs[pub] for pub in sourted_avg_pubs]
        sourted_avg_cite = sorted(avg_cite)
        avg_cite_values = [avg_cite[cite] for cite in sourted_avg_cite]
        sourted_sim_ranks = sorted(sim_ranks)
        max_sim = sourted_sim_ranks[-1]
        min_sim = sourted_sim_ranks[0]
        sourted_sim_ranka_guiyue = [round((x-min_sim)/(max_sim-min_sim+1)-0.4, 3) for x in sourted_sim_ranks]
        sim_ranka_values = [sim_ranks[sim] for sim in sourted_sim_ranks]

    return {
            'wait_years_kyes':sourted_wait_years,
            'wait_years_values':wait_years_values,
            'avg_pubs_keys':sourted_avg_pubs,
            'avg_pubs_values':avg_pubs_values,
            'avg_cite_keys':sourted_avg_cite,
            'avg_cite_values':avg_cite_values,
            'sim_ranka_keys':sourted_sim_ranka_guiyue,
            'sim_ranka_values':sim_ranka_values
            }

def get_avg_pub_plot_data(tongji_data):
    # tongji_data = get_ieee_tongji()
    avg_pubs_keys = tongji_data['avg_pubs_keys']
    avg_pubs_values = tongji_data['avg_pubs_values']

    avg_pub_top_range = 20
    avg_pub_size = 2
    avg_pub_plot_x = []
    avg_pub_plot_y = []
    pointer = 0
    for i in [avg_pub_size*x for x in range(int(avg_pub_top_range/avg_pub_size))]:
        x_name = str(i)+'-'+str(i+avg_pub_size)
        avg_pub_plot_x.append(x_name)
        bottom = i
        top = i+avg_pub_size
        count = 0
        while avg_pubs_keys[pointer] < top:
            count +=  avg_pubs_values[pointer]
            pointer += 1
        avg_pub_plot_y.append(count)
    avg_pub_plot_x.append('>=20')
    count = 0
    while pointer < len(avg_pubs_keys):
        count += avg_pubs_values[pointer]
        pointer += 1
    avg_pub_plot_y.append(count)

    return {'avg_pub_plot_x':avg_pub_plot_x, 'avg_pub_plot_y':avg_pub_plot_y}


def get_plot_data(tongji_data, keys_name, values_name, top_range, size):
    keys = tongji_data[keys_name]
    values = tongji_data[values_name]

    avg_plot_x = []
    avg_plot_y = []
    pointer = 0
    for i in [size*x for x in range(int(top_range/size))]:
        x_name = str(i)+'-'+str(i+size)
        avg_plot_x.append(x_name)
        bottom = i
        top = i+size
        count = 0
        while keys[pointer] < top:
            count +=  values[pointer]
            pointer += 1
        avg_plot_y.append(count)
    avg_plot_x.append('>='+str(top_range))
    count = 0
    while pointer < len(keys):
        count += values[pointer]
        pointer += 1
    avg_plot_y.append(count)

    return {'avg_plot_x':avg_plot_x, 'avg_plot_y':avg_plot_y}

def get_sim_rank_plot_data(tongji_data):
    # tongji_data = get_ieee_tongji()
    avg_pubs_keys = tongji_data['sim_ranka_keys']
    avg_pubs_values = tongji_data['sim_ranka_values']

    avg_pub_top_range = 0.6
    avg_pub_size = 0.02
    avg_pub_plot_x = []
    avg_pub_plot_y = []
    pointer = 2
    i = 0.4
    while i < avg_pub_top_range:
        x_name = round(str(i), 3)+'-'+str(round(i+avg_pub_size, 3))
        avg_pub_plot_x.append(x_name)
        bottom = i
        top = i+avg_pub_size
        count = 0
        try:
            while avg_pubs_keys[pointer] < top:
                count += avg_pubs_values[pointer]
                pointer += 1
            avg_pub_plot_y.append(count)
            i += avg_pub_size
        except Exception:
            avg_pub_plot_y.append(count)
            i += avg_pub_size

    return {'avg_sim_plot_x':avg_pub_plot_x, 'avg_sim_plot_y':avg_pub_plot_y}



if __name__ == '__main__':
    # json.dump(get_ieee_tongji(), codecs.open('ieee_statistics.json', 'w', encoding='utf-8'), ensure_ascii=False)
    get_ieee_tongji = get_ieee_tongji()
    ploat_data = {}
    #统计平均论文数
    avg_pub_plot = get_avg_pub_plot_data(get_ieee_tongji)
    ploat_data['avg_pub_plot_x'] = avg_pub_plot['avg_pub_plot_x']
    ploat_data['avg_pub_plot_y'] = avg_pub_plot['avg_pub_plot_y']
    #统计平均引用数
    avg_cite_plot = get_plot_data(get_ieee_tongji, "avg_cite_keys", "avg_cite_values", 1000, 100)
    ploat_data['avg_cite_plot_x'] = avg_cite_plot['avg_plot_x']
    ploat_data['avg_cite_plot_y'] = avg_cite_plot['avg_plot_y']
    # 统计相似数
    avg_sim_plot = get_sim_rank_plot_data(get_ieee_tongji)
    ploat_data['avg_sim_plot_x'] = avg_sim_plot['avg_sim_plot_x']
    ploat_data['avg_sim_plot_y'] = avg_sim_plot['avg_sim_plot_y']

    json.dump(ploat_data, codecs.open('ieee_plot_data.json', 'w', encoding='utf-8'), ensure_ascii=False)

