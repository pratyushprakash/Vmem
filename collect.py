from math import log10, floor
from collections import defaultdict

system_call_list = []
data_dict = defaultdict(lambda: 0)
features = []


def get_data(filepath):
    global system_call_list, data_dict, features
    min, max = 100000, 0
    with open(filepath, 'r+') as f:
        prev_call = -1
        read_data = False
        for line in f:
            if line.split()[0] == 'SysCall':
                read_data = True
                if prev_call != -1:
                    system_call_list.append([prev_call, dict(data_dict)])
                prev_call = int(line.split()[1])
                data_dict = defaultdict(lambda: 0)
            elif read_data:
                try:
                    '''
                    if int(line.split()[3]) > max:
                        max = int(line.split()[3])
                    if int(line.split()[3]) < min:
                        min = int(line.split()[3])
'''
                    # print(line.split())
                    if floor(log10(int(line.split()[3], 16))) not in features:
                        features.append(floor(log10(int(line.split()[3], 16))))

                    data_dict[floor(log10(int(line.split()[3], 16)))] += 1
                except:
                    # print(line.split())
                    pass
    print('min: {}, max: {}'.format(min, max))
    return system_call_list, features
