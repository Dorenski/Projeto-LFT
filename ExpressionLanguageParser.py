# Gramática
# 
#
# exp -> exp + exp | exp - exp | exp * exp | exp / exp | exp % exp | exp -- |
#        exp ++ | ++ exp | -- exp |  exp ** exp | 
#        exp === exp | exp !== exp | exp & exp | 
#        exp ^ exp | ' exp | exp ' | exp == exp | exp != exp |  exp > exp | exp < exp | exp >= exp | 
#        exp <= exp | exp && exp | exp || exp | !exp | ~exp | (exp) | +exp | -exp | exp ? exp : exp | 
#        ID | call | params | assign | TRUE | FALSE | STRING_AD | STRING_A
#        
#     FALTA OS TOKENS: exp += exp | exp -= exp | exp *= exp | exp <<= exp | exp >>= exp | exp >>>= exp | exp &= exp | exp ^= exp |  ' exp |= exp ' | exp /= exp | exp %= exp | exp **= exp | num
# 
# call → ID (params) | ID ( )
# params → exp, params | exp
# assign → ID = exp



import ply.yacc as yacc
import ply.lex as lex
from ExpressionLanguageLex import tokens

# Genérico poxa, é só copiar essa parte e alterar 
def p_exp_algumacoisa(p):
    ''' exp :  '''
#================================================

def p_exp_SOMA(p):
    ''' exp : exp SOMA exp '''
    
def p_exp_SUBTRACAO(p):
    ''' exp : exp SUBTRACAO exp '''

def p_exp_MULTIPLICACAO(p):
    ''' exp : exp MULTIPLICACAO exp '''

def p_exp_DIVISAO(p):
    ''' exp : exp DIVISAO exp '''

def p_exp_RESTO(p):
    ''' exp : exp RESTO exp '''

def p_exp_DECREMENTO(p):
    ''' exp : exp DECREMENTO '''
    
def p_exp_INCREMENTO(p):
    ''' exp : exp INCREMENTO '''

def p_exp_expINCREMENTO(p):
    ''' exp : INCREMENTO exp  '''

def p_exp_expDECREMENTO(p):
    ''' exp : DECREMENTO exp  '''

def p_exp_EXPONENCIACAO(p):
    ''' exp : exp EXPONENCIACAO exp '''

def p_exp_IGUAL_ESTRITA(p):
    ''' exp : exp IGUAL_ESTRITA exp '''

def p_exp_DESIGUAL_ESTRITA(p):
    ''' exp : exp DESIGUAL_ESTRITA exp '''

def p_exp_AND_BITABIT(p):
    ''' exp : exp AND_BITABIT exp '''

def p_exp_XOR_BITABIT(p):
    ''' exp : exp XOR_BITABIT exp '''

def p_exp_OR_BITABIT(p):
    ''' exp : exp OR_BITABIT exp '''

def p_exp_IGUALDADE(p):
    ''' exp : exp IGUALDADE exp '''

def p_exp_DESIGUALDADE(p):
    ''' exp : exp DESIGUALDADE exp '''

def p_exp_MAIOR(p):
    ''' exp : exp MAIOR exp '''

def p_exp_MENOR(p):
    ''' exp : exp MENOR exp '''

def p_exp_MAIOR_IGUAL(p):
    ''' exp : exp MAIOR_IGUAL exp '''

def p_exp_MENOR_IGUAL(p):
    ''' exp : exp MENOR_IGUAL exp '''

def p_exp_AND_LOGICO(p):
    ''' exp : exp AND_LOGICO exp '''

def p_exp_OR_LOGICO(p):
    ''' exp : exp OR_LOGICO exp '''

def p_exp_NAO_LOGICO(p):
    ''' exp : NAO_LOGICO exp  '''

def p_exp_NAO_BITABIT(p):
    ''' exp : NAO_BITABIT exp  '''

def p_exp_AGRUPAMENTO(p):
    ''' exp : L_PARENTESIS exp R_PARENTESIS '''

def p_exp_POSITIVO_UNARIO(p):
    ''' exp : SOMA exp '''

def p_exp_NEGATIVO_UNARIO(p):
    ''' exp : SUBTRACAO exp '''

def p_exp_TERNARIO(p):
   ''' exp : exp INTERROGACAO exp DOIS_PONTOS exp '''

def p_exp_ID(p):
   ''' exp : ID '''

def p_exp_CALL(p):
   ''' exp : call '''

def p_exp_PARAMS(p):
   ''' exp : params '''

def p_exp_ASSIGN(p):
   ''' exp : assign '''

def p_exp_TRUE(p):
   ''' exp : TRUE '''

def p_exp_FALSE(p):
   ''' exp : FALSE '''
   
def p_exp_STRING_AD(p):
   ''' exp : STRING_AD '''

def p_exp_STRING_A(p):
   ''' exp : STRING_A '''

def p_programa(p):
    pass
