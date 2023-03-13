import json

#def process_header(header):

#    columns = header.split(',')


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