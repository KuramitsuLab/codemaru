import sys
import json
import random
random.seed(0)

def read_file(file_path):
    dataset = {}
    with open(file_path) as f:
        for line in f.readlines():
            data = json.loads(line)
            IN = data['in']
            OUT = data['out']
            if OUT in dataset.keys():
                dataset[OUT].append(IN)
            else:
                dataset[OUT] = [IN]
    return dataset


def write_files(dataset, MAX_data=1):
    MAX_data=int(MAX_data)
    with open(sys.argv[1].strip('.josnl')+'_IN'+sys.argv[2]+'.jsonl', 'w') as f:

        for code, japanese_list  in dataset.items():
            try:
                japanese = random.sample(japanese_list, k=MAX_data)
            except ValueError:
                japanese = random.sample(japanese_list, k=len(japanese_list))
                
            COUNT = 0
            for japan in japanese:
                COUNT += 1
                if COUNT <= MAX_data:
                    dict = {'in':japan,'out':code}
                    json.dump(dict, f, separators=(',',':'),ensure_ascii=False)
                    f.write('\n')
                else:
                    break

#python3 make_abci.py read.jsonl new_file.jsonl

def main():
    file_path = sys.argv[1]
    dataset = read_file(file_path)
    write_files(dataset, sys.argv[2])

main()