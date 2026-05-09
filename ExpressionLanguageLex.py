import ply.lex as lex

reservadas = {
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'true': 'TRUE',
    'false': 'FALSE'
    


}
tokens = [
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
] 
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
    
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def

def main():
    lexer = lex.lex()
    while True:
        try:
            s = input('Enter expression: ')
            if s.lower() == 'exit':
                break
            lexer.input(s)
            for tok in lexer:
                print(tok)
        except EOFError:
            break

if __name__ == '__main__':
    main()
