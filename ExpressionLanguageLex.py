import ply.lex as lex

reservadas = {
	'break' : 'BREAK',
	'case' : 'CASE',
	'catch' : 'CATCH',
	'class' : 'CLASS',
	'const' : 'CONST',
	'continue' : 'CONTINUE',
	'debugger' : 'DEBUGGER',
	'default' :  'DEFAULT',
	'delete' : 'DELETE',
	'do' : 'DO',
	'else' : 'ELSE',
	'export' : 'EXPORT',
	'extends' : 'EXTENDS',
	'finally' : 'FINALLY',
	'for' : 'FOR',
	'function' : 'FUNCTION',
	'if' : 'IF',
	'import' : 'IMPORT',
	'in' : 'IN',
	'instanceof' : 'INSTANCEOF',
	'new' : 'NEW',
	'return' : 'RETURN',
	'super' : 'SUPER',
	'switch' : 'SWITCH',
	'this' : 'THIS',
	'throw' : 'THROW',
	'try' : 'TRY',
	'typeof' : 'TYPEOF',
	'var' : 'VAR',
	'void' : 'VOID',
	'while' : 'WHILE',
	'with' : 'WITH',
	'yield' : 'YIELD',
	'await' : 'AWAIT',
	'protected' : 'PROTECTED',
	'static' : 'STATIC',
	'private' : 'PRIVATE',
	'public' : 'PUBLIC',
	'let' : 'LET',
	'abstract' : 'ABSTRACT',
	'boolean' : 'BOOLEAN',
	'byte' : 'BYTE',
	'char' : 'CHAR',
	'double' : 'DOUBLE',
	'final' : 'FINAL',
	'float' : 'FLOAT', 
	'int' : 'INT',
	'long' : 'LONG',
	'short' : 'SHORT',
	'true' : 'TRUE',
	'false' : 'FALSE',
	'null' : 'NULL',
	'undefined' : 'UNDEFINED'
    
}

tokens = [
	'L_PARENTESIS',
	'R_PARENTESIS',
	'ACESSO_MEMBRO',
	'L_COLCHETE',
	'R_COLCHETE',
	'L_CHAVE',
	'R_CHAVE',
	'INCREMENTO_POS',
	'DECREMENTO_POS',
	'NAO_LOGICO',
	'NAO_BITABIT',
	'POSITIVO_U',
	'NEGATIVO_U',
	'INCREMENTO_PRE',
	'DECREMENTO_PRE',
	'EXPONENCIACAO',
	'MULTIPLICACAO',
	'RESTO',
	'DIVISAO',
	'SOMA',
	'SUBTRACAO',
	'MENOR',
	'MENOR_IGUAL',
	'MAIOR',
	'MAIOR_IGUAL',
	'IGUALDADE',
	'DESIGUALDADE',
	'IGUAL_ESTRITA',
	'DESIGUAL_ESTRITA',
	'AND_BITABIT',
	'XOR_BITABIT',
	'OR_BITABIT',
	'AND_LOGICO',
	'OR_LOGICO',
	'TERNARIO',
	'ATRIBUICAO',
	'PROPAGACAO',
	'VIRGULA',
	
	'PONTO_E_VIRGULA',
	'ASPAS_DUPLAS',
	'ASPAS',
	'ID',
	'STRING_AD',
	'STRING_A',
	'OCTAL',
	'HEXADECIMAL',
	'BOOLEAN',
	'OBJECT',
	'COMENTARIO',
	'L_COMENTARIO_MULTILINHA'
	'R_COMENTARIO_MULTILINHA'
] + list(reservadas.values())

t_L_PARENTESIS = r'\('
t_R_PARENTESIS = r'\)'
t_ACESSO_MEMBRO = r'\.'
t_L_COLCHETE = r'\['
t_R_COLCHETE = r'\]'
t_L_CHAVE = r'\{'
t_R_CHAVE = r'\}'

t_INCREMENTO_POS = r'\+\+'
t_DECREMENTO_POS = r'\-\-'

t_NAO_LOGICO = r'\!'
t_NAO_BITABIT = r'\~'
t_POSITIVO_U = r'\+'
t_NEGATIVO_U = r'\-'

t_INCREMENTO_PRE = r'\+\+'
t_DECREMENTO_PRE = r'\-\-'

t_EXPONENCIACAO = r'\**'
t_MULTIPLICACAO = r'\*'
t_RESTO = r'\%'
t_DIVISAO = r'\/'
t_SOMA = r'\+'
t_SUBTRACAO = r'\-'

t_MENOR = r'\<'
t_MENOR_IGUAL = r'\<\='
t_MAIOR = r'\>'
t_MAIOR_IGUAL = r'\>\='
t_IGUALDADE = r'\=\='
t_DESIGUALDADE = r'\!\='
t_IGUAL_ESTRITA = r'\=\=\='
t_DESIGUAL_ESTRITA = r'\!\=\='
t_AND_BITABIT = r'\&'
t_XOR_BITABIT = r'\^'
t_OR_BITABIT = r'\|'
t_AND_LOGICO = r'\&\&'
t_OR_LOGICO = r'\|\|'
t_TERNARIO = r'\?\:'
t_ATRIBUICAO = r'\.'
t_PROPAGACAO = r'\.\.\.'
t_VIRGULA = r'\,'
t_PONTO_E_VIRGULA = r'\;'
t_ASPAS_DUPLAS = r'\"'
t_ASPAS = r'\''
t_COMENTARIO = r'\/\/'

t_ignore = ' \t\r'

def t_ID(t):
	r'[a-zA-Z_$][a-zA-Z_0-9$]*'
	t.type = reservadas.get(t.value, 'ID')
	return t

def t_STRING_AD(t):
    r'"[^"\n]*"'

    return t

def t_STRING_A(t):
    r"'[^'\n]*'"
    return t
	

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_OCTAL(t): 
    r'0[oO][0-7]+'
    return t
	
def t_HEXADECIMAL(t):
    r'0[xX][0-9a-fA-F]+'
    return t

def t_BOOLEAN(t):
    r'\b(true|false)\b'
    return t

def t_OBJECT(t):
    r'\b(null|undefined)\b'
    return t

def t_L_COMENTARIO_MULTILINHA(t):
    r'\/\*'
    return t

def t_R_COMENTARIO_MULTILINHA(t):
    r'\*\/'
    return t    

def main():
	pass

main()