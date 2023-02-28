import sys

soma = 0
ligado = 1

for line in sys.stdin:
    tokens = line.split(" ")
    
    for token in tokens:
        if 'off' == token.rstrip().lower():
            ligado = 0
        elif 'on' == token.rstrip().lower():
            ligado = 1
        elif '=' == token.rstrip().lower():
            print(soma)
        elif token.isnumeric():
            soma += int(token.rstrip()) * ligado
        else:
            print(f"Input inválido: {token}")