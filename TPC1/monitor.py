readings = []

def read_data(file):
    '''Lê a informação do ficheiro para um modelo, previamente pensado em memória.
    '''

    data = open(file, "r", encoding="UTF-8")
    
    for entry in data:
        if entry.startswith('idade'):
            keys = entry.strip('\n').split(',')
        else:
            values = entry.strip('\n').split(',')
            # Mapeia os valores indicando a idade, sexo, tensão, colesterol, batimento e temDoença para cada leitura
            readings.append(dict(zip(keys,values)))

def disease_by_gender():
    '''Calcula a distribuição da doença por sexo.

       Retorna um dicionário onde cada chave corresponde a um sexo possuindo um
       tuplo onde indica o número de infetados e o número total de entradas
       para esse sexo, respetivamente.
    '''
    distr = dict()

    male_total = female_total = 0
    male_ill = female_ill = 0

    for reading in readings:
        
        if reading['sexo'] == 'M':
            male_total += 1
            
            if reading['temDoença'] == '1':
                male_ill += 1

        elif reading['sexo'] == 'F':
            female_total += 1
            
            if reading['temDoença'] == '1':
                female_ill += 1

    distr['M'] = (male_ill, male_total)
    distr['F'] = (female_ill, female_total)

    return distr

def disease_by_age():
    '''Calcula a distribuição da doença por escalões etários.
    '''
    distr = dict()
    
    count_disease = 0
    count_total = 0
    
    init = 30
    end = 34
    
    entries = sorted([(int(entry['idade']), int(entry['temDoença'])) for entry in readings])

    for age,disease in entries:  

        if age <= end:
            count_disease += disease
            count_total += 1 
       
        else:
            distr[(init,end)] = (count_disease,count_total)
            init += 5
            end += 5
            count_disease = 0 
            count_total = 0
    
    distr[(init,end)] = (count_disease,count_total)
        
    return distr

def disease_by_cholesterol_level():
    '''Calcula a distribuição da doença por níveis de colesterol.
    '''
    distr = dict()
    
    count_disease = 0
    count_total = 0
    
    entries = sorted([(int(entry['colesterol']), int(entry['temDoença'])) for entry in readings])

    init = entries[1][0]
    end = init + 10

    for cholesterol,disease in entries:

        if cholesterol <= end:
            count_disease += disease
            count_total += 1 
       
        else:
            distr[(init,end)] = (count_disease,count_total)
            init += 10
            end += 10
            count_disease = 0 
            count_total = 0
    
    distr[(init,end)] = (count_disease,count_total)
        
    return distr

def print_table(distr):
    '''Imprime uma distribuição na forma de uma tabela.
    '''
    total = len(readings)
    table = ""

    table += '   Valor   | Quantidade | Amostra (%) | Total (%) \n'
    
    for key, (disease,ref_total) in distr.items():
        if ref_total > 0:
            aux_ref = (disease / ref_total) * 100
            ref_str = f'{aux_ref:.2f}'
            aux_total = (disease / total) * 100
            total_str = f'{aux_total:.2f}'

            table += f'{str(key):^10} | {disease:^10} | {ref_str:^11} | {total_str:^10} \n'

    print(table)


read_data("myheart.csv")

print("Disease by gender\n")
print_table(disease_by_gender())

print("Disease by age\n")
print_table(disease_by_age())

print("Disease by cholesterol levels\n")
print_table(disease_by_cholesterol_level())