import ply.lex as lex

states = (
   ('comment','exclusive'),
)

reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'for' : 'FOR',
   'function' : 'FUNCTION',
   'program' : 'PROGRAM'
}

# List of token names.   This is always required
tokens = [
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'LBRCKT',
   'RBRCKT',
   'LSPAREN',
   'RSPAREN',
   'EQUAL',
   'LESS',
   'MORE',
   'COMMA',
   'STRING',
   'COMMENT',
   'RANGE',
   'FLOAT'
 ] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRCKT  = r'\{'
t_RBRCKT  = r'\}'
t_LSPAREN  = r'\['
t_RSPAREN  = r'\]'
t_EQUAL = r'='
t_LESS = r'<'
t_MORE = r'>'
t_RANGE = r'\.\.'
t_FLOAT = r'\d+\.\d+'
t_COMMA = r';|,'
t_STRING = r'[_a-zA-Z0-9:çáéíóúàãõẽâôê]+'

def t_begin_comment(t):
    r'/\*'
    t.lexer.begin('comment')

def t_comment_COMMENT(t):
    r'[\._\-\sa-zA-Z0-9:çáéíóúàãõẽâôê]+'   
    return t

def t_COMMENT(t):
    r'//[\._\-\sa-zA-Z0-9:çáéíóúàãõẽâôê]+\n'
    return t

def t_comment_end(t):
    r'\*/'
    t.lexer.begin('INITIAL') 

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
t_comment_ignore = ' \t'

# Error handling rule
def t_INITIAL_comment_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = open("max.p", "r")

# Give the lexer some input
lexer.input(data.read())

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)