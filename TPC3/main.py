import re
import json

# alínea A
def freq_processos():

    data = dict();
        
    file = open("processos.txt", "r")

    for line in file:
        pattern = re.compile(r'(?P<proc_num>\d+)\s*::(?P<date>(\d+-*)+)')
        search = pattern.search(line)

        if (search != None):
            proc_num = search.group('proc_num')
            date = pattern.search(line).group('date').split('-')
            year = date[0]
            count = data.get(year,0)
            data[year] = count + 1
    
    return data
        
# alínea B
def freq_nomes():

    # dict {SEC : {NOME : FREQ}}
    nomes = dict()
    apelidos = dict()

    pattern = re.compile(r'(([a-zA-Z]+\s*)+)')
    pattern_date = re.compile(r'(?P<proc_num>\d+)\s*::(?P<date>(\d+-*)+)')


    file = open("processos.txt", "r")

    for line in file:

        if date := pattern_date.search(line):
            year = date.group('date').split('-')[0]
            sec = int(int(year) / 100) - 1

        for m in re.finditer(pattern, line):
            nome = m.group(1).split()
            proprio = nome[0]
            apelido = nome[len(nome)-1]
            
            if(not sec in nomes and not sec in apelidos):
                nomes[sec] = dict()
                apelidos[sec] = dict()
            
            nomes[sec][proprio] = nomes[sec].get(proprio,0) + 1
            apelidos[sec][apelido] = apelidos[sec].get(apelido,0) + 1
            

    return (nomes, apelidos)

# alinea C
def parentesco():
    file = open("processos.txt", "r")

    graus = dict()

    for line in file:
        
        if re.search(',Pai|Mae\s', line):
            count = graus.get('Filhos',0)
            graus['Filhos'] = count + 1
        elif re.search(',Irma(o)?\s', line):
            count = graus.get('Irmaos',0)
            graus['Irmaos'] = count + 1
        elif re.search(',Avo\s', line):
            count = graus.get('Netos',0)
            graus['Netos'] = count + 1
        elif re.search(',Ti(a|o)\s', line):
            count = graus.get('Sobrinhos',0)
            graus['Sobrinhos'] = count + 1

    return graus

def main():
    print('''
    a - Calcula a frequência de processos por ano (primeiro elemento da data);

    b - Calcula a frequência de nomes próprios (o primeiro em cada nome) e apelidos (o ultimo em cada nome) por séculos e apresenta os 5 mais usados;

    c - Calcula a frequência dos vários tipos de relação: irmão, sobrinho, etc.;

    d - Converta os 20 primeiros registos num novo ficheiro de output mas em formato Json.
    '''
    )

    option = input("Alínea: ")

    match option.lower():
        case "a":
            print("Processos por anos:")
            print(freq_processos())
        case "b":
            (nomes,apelidos) = freq_nomes()
            print("Nomes próprios por séculos")
            print(nomes)
            print("Apelidos por séculos")
            print(apelidos)
        case "c":
            print("Graus de parentesco")
            print(parentesco())
        case "d":
            convert()

if __name__ == "__main__":
    main()