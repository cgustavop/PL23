import json
import re
#def process_header(header):
# (?P<coluna>[a-zA-Z0-9éúíóÀà]+?,) normal
# (?P<lista>[a-zA-Z]+{(?P<elementos>(\d+,?)*)})
#    columns = header.split(',')

pattern = re.compile(r'(?P<coluna>[a-zA-Z0-9éúíóÀà]+?,)|(?P<lista>[a-zA-Z]+{(?P<elementos>(\d+,?)*)})')
# dá-nos as categorias e elementos de uma eventual categoria especial

filepath = input("CSV file path: ")
outpath = filepath.split('.')[0] + ".json"
data = []

with open(filepath, 'r', encoding="utf-8") as file:
    header = file.readline().strip()
    process_header(header)

    for line in file:
        entry_list = line.strip().split(',')
        data.append(dict(zip(columns,entry_list)))


json_object = json.dumps(data, indent=2, ensure_ascii=False)

with open(outpath, "w", encoding="utf-8") as outfile:
    outfile.write(json_object)