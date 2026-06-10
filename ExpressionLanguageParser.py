# program → funcdecl | funcdecl program | vardecl | vardecl program | classdecl | classdecl program
#
# classdecl → CLASS ID classbody
#
# classbody → { classmembers }
#
# classmembers → classmember | classmember classmembers
#
# classmember → methoddecl | constructordecl | attrdecl
#
# constructordecl → CONSTRUCTOR ( sigparams ) body | CONSTRUCTOR ( ) body
#
# methoddecl → ID ( sigparams ) body | ID ( ) body
#
# attrdecl → ID ; | ID = exp ;
#
# funcdecl → signature body
#
# signature → FUNCTION ID ( sigparams )
#
# sigparams → ID |  ID , sigparams | ε
#
# body → { stms }
#
# exp -> exp + exp | exp - exp | exp * exp | exp / exp | exp % exp | exp -- |
#        exp ++ | ++ exp | -- exp |  exp ** exp | exp === exp | exp !== exp | exp & exp | 
#        exp ^ exp | ' exp | exp ' | exp == exp | exp != exp |  exp > exp | exp < exp | exp >= exp | 
#        exp <= exp | exp && exp | exp || exp | !exp | ~exp | (exp) | +exp | -exp | exp ? exp : exp | 
#        exp += exp | exp -= exp | exp *= exp | exp **= exp | exp /= exp | exp %= exp |
#        exp <<= exp | exp >>= exp | exp >>>= exp | exp &= exp | exp ^= exp |  ' exp |= exp ' | 
#        NEW ID () | NEW ID ( params ) | exp . ID | exp . call | THIS |
#        num | ID | call  | assign | TRUE | FALSE | STRING_AD | STRING_A 
#
# vardecl → LET ID ; | VAR ID ; | CONST ID ; | LET ID = exp ; | CONST ID = exp ; | VAR ID = exp ;
#
# stms → stm | stm stms
#
# stm → #IMPLEMENTAR O FOR# | assign; | vardecl | exp ; | RETURN exp ; | WHILE ( exp ) body | IF ( exp ) body | IF ( exp ) body ELSE body
#
# assign → ID = exp | exp . ID = exp
#
# call → ID (params) | ID () | exp . ID (params) | exp . ID ()
#
# params → exp, params | exp | ε



import ply.yacc as yacc
import ply.lex as lex
from ExpressionLanguageLex import tokens

#================== program =========================
def p_program_funcdecl(p):
    ''' program : funcdecl '''

def p_program_funcdecl_program(p):
    ''' program : funcdecl program '''

def p_program_vardecl(p):
    ''' program : vardecl '''

def p_program_vardecl_program(p):
    ''' program : vardecl program '''
    
#================== funcdecl =========================
def p_funcdecl(p):
    ''' funcdecl : signature body '''

#================== signature =========================
def p_signature(p):
    ''' signature : FUNCTION ID L_PARENTESIS sigparams R_PARENTESIS '''
    
#================== sigparams =========================
def p_sigparams_id(p):
    ''' sigparams : ID '''  
    
def p_sigparams_id_sigparams(p):
    ''' sigparams : ID VIRGULA sigparams '''

#================== body =========================
def p_body(p):
    ''' body : L_CHAVES stms R_CHAVES '''

#================== EXP =========================
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

def p_exp_MAIS_IGUAL_exp(p):
    ''' exp : exp MAIS_IGUAL exp'''

def p_exp_MENOS_IGUAL_exp(p):
    ''' exp : exp MENOS_IGUAL exp'''

def p_exp_MULTIPLICACAO_IGUAL_exp(p):
    ''' exp : exp MULTIPLICACAO_IGUAL exp'''

def p_exp_EXPONENCIACAO_IGUAL_exp(p):
    ''' exp : exp EXPONENCIACAO_IGUAL exp'''

def p_exp_DIVISAO_IGUAL_exp(p):
    ''' exp : exp DIVISAO_IGUAL exp'''

def p_exp_RESTO_IGUAL_exp(p):
    ''' exp : exp RESTO_IGUAL exp'''

def p_exp_DESLOC_E_IGUAL_exp(p):
    ''' exp : exp DESLOC_E_IGUAL exp'''

def p_exp_DESLOC_D_IGUAL_exp(p):
    ''' exp : exp DESLOC_D_IGUAL exp'''

def p_exp_DESLOC_D_S_IGUAL_exp(p):
    ''' exp : exp DESLOC_D_S_IGUAL exp'''

def p_exp_AND_BIT_IGUAL_exp(p):
    ''' exp : exp AND_BIT_IGUAL exp'''

def p_exp_XOR_BIT_IGUAL_exp(p):
    ''' exp : exp XOR_BIT_IGUAL exp'''  

def p_exp_OR_BIT_IGUAL_exp(p):
    ''' exp : exp OR_BIT_IGUAL exp'''  

def p_exp_INT_LITERAL(p):
    ''' exp : INT_LITERAL'''

def p_exp_ID(p):
   ''' exp : ID '''

def p_exp_CALL(p):
   ''' exp : call '''

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

#================== vardecl =========================

def p_vardecl(p):
    ''' vardecl : LET ID PONTO_VIRGULA'''
def p_vardecl_let(p):
    ''' vardecl : LET ID ATRIBUICAO exp PONTO_VIRGULA'''
def p_vardecl_const(p):
    ''' vardecl : CONST ID PONTO_VIRGULA'''
def p_vardecl_const_exp(p):
    ''' vardecl : CONST ID ATRIBUICAO exp PONTO_VIRGULA'''
def p_vardecl_var(p):
    ''' vardecl : VAR ID PONTO_VIRGULA'''
def p_vardecl_var_exp(p):
    ''' vardecl : VAR ID ATRIBUICAO exp PONTO_VIRGULA'''

#================== stms =========================

def p_stms_stm(p):
    ''' stms : stm '''
def p_stms_stm_stms(p):
    ''' stms : stm stms '''
    
#================== stm =========================

def p_stm_assign(p):
    ''' stm : assign PONTO_VIRGULA '''
def p_stm_vardecl(p):
    ''' stm : vardecl '''
def p_stm_exp(p):
    ''' stm : exp PONTO_VIRGULA '''
def p_stm_return(p):
    ''' stm : RETURN exp PONTO_VIRGULA '''
def p_stm_while(p):
    ''' stm : WHILE L_PARENTESIS exp R_PARENTESIS body '''
def p_stm_if(p):
    ''' stm : IF L_PARENTESIS exp R_PARENTESIS body '''
def p_stm_if_else(p):
    ''' stm : IF L_PARENTESIS exp R_PARENTESIS body ELSE body '''



#================== assign =========================
def p_assign_ID(p):
    ''' assign : ID ATRIBUICAO exp '''
    
#================== call =========================
def p_call_ID_Params(p):
    ''' call : ID L_PARENTESIS params R_PARENTESIS '''

def p_call_ID(p):
    ''' call : ID L_PARENTESIS R_PARENTESIS '''

#================== params =========================
def p_params_exp_params(p):
    ''' params : exp VIRGULA param'''
def p_params_exp(p):
    ''' params : exp '''
