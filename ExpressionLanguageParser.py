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
# signature → FUNCTION ID ( sigparams ) | FUNCTION ID ()
#
# sigparams → ID |  ID , sigparams
#
# body → { stms }
#
# exp -> exp + exp | exp - exp | exp * exp | exp / exp | exp % exp | exp -- |
#        exp ++ | ++ exp | -- exp |  exp ** exp | exp === exp | exp !== exp | exp & exp | 
#        exp ^ exp | ' exp | exp ' | exp == exp | exp != exp |  exp > exp | exp < exp | exp >= exp | 
#        exp <= exp | exp && exp | exp || exp | !exp | ~exp | (exp) | olhar +exp | olhar -exp | exp ? exp : exp | 
#        exp += exp | exp -= exp | exp *= exp | exp **= exp | exp /= exp | exp %= exp |
#        exp <<= exp | exp >>= exp | exp >>>= exp | exp &= exp | exp ^= exp |  ' exp |= exp ' | 
#        NEW ID () | NEW ID ( params ) | exp . ID | exp . call | THIS |
#        num | ID | call  | assign | TRUE | FALSE | STRING_AD | STRING_A 
#
# vardecl → LET ID ; | VAR ID ; | CONST ID ; | LET ID = exp ; | CONST ID = exp ; | VAR ID = exp ;
#
# stms → stm | stm stms
#
# stm → FOR(exp;exp;exp) body | assign; | vardecl | exp ; | RETURN exp ; | WHILE ( exp ) body | IF ( exp ) body | IF ( exp ) body ELSE body
#
# assign → ID = exp | exp . ID = exp
#
# call → ID (params) | ID () | exp . ID (params) | exp . ID ()
#
# params → exp, params | exp



import ply.yacc as yacc
import ply.lex as lex
from ExpressionLanguageLex import tokens
import SintaxeAbstrata as sa

#================== program =========================
def p_program_funcdecl(p):
    ''' program : funcdecl '''

def p_program_funcdecl_program(p):
    ''' program : funcdecl program '''

def p_program_vardecl(p):
    ''' program : vardecl '''

def p_program_vardecl_program(p):
    ''' program : vardecl program '''

def p_program_classdecl(p):
    '''program : classdecl '''
    
def p_program_classdecl_program(p):
    '''program : classdecl program '''

#================== classdecl =========================
def p_classdecl_CLASS_ID_classbody(p):
    '''classdecl : CLASS ID classbody '''
    
#================== classbody =========================
def p_classbody_classmembers(p):
    '''classbody : L_CHAVE classmembers R_CHAVE '''

#================== classmembers =========================
def p_classmembers_classmember(p):
    '''classmembers : classmember '''

def p_classmembers_classmembers(p):
    '''classmembers : classmember classmembers '''

#================== classmember =========================
def p_classmember_methoddecl(p):
    '''classmember : methoddecl '''

def p_classmember_constructordecl(p):
    '''classmember : constructordecl '''

def p_classmember_attrdecl(p):
    '''classmember : attrdecl '''

#================== constructordecl =========================   
def p_constructordecl_sigparams(p):
    '''constructordecl : CONSTRUCTOR L_PARENTESIS sigparams R_PARENTESIS body '''
    
def p_constructordecl_NOsigparams(p):
    '''constructordecl : CONSTRUCTOR L_PARENTESIS  R_PARENTESIS body '''
    
#================== methoddecl =========================
def p_methoddecl_sigparams(p):
    '''methoddecl : ID L_PARENTESIS sigparams R_PARENTESIS body '''
    
def p_methoddecl_NOsigparams(p):
    '''methoddecl : ID L_PARENTESIS R_PARENTESIS body '''

#================== attrdecl =========================
def p_attrdecl_ID(p):
    ''' attrdecl : ID PONTO_E_VIRGULA '''
    
def p_attrdecl_exp(p):
    ''' attrdecl : ID ATRIBUICAO exp PONTO_E_VIRGULA '''

#================== funcdecl =========================
def p_funcdecl(p):
    ''' funcdecl : signature body '''

#================== signature =========================
def p_signature_sigparams(p):
    ''' signature : FUNCTION ID L_PARENTESIS sigparams R_PARENTESIS '''

def p_signature_NOsigparams(p):
    ''' signature : FUNCTION ID L_PARENTESIS R_PARENTESIS '''
    
#================== sigparams =========================
def p_sigparams_id(p):
    ''' sigparams : ID '''  
    
def p_sigparams_id_sigparams(p):
    ''' sigparams : ID VIRGULA sigparams '''

#================== body =========================
def p_body(p):
    ''' body : L_CHAVE stms R_CHAVE '''

#================== EXP =========================
def p_exp_SOMA(p):
    ''' exp : exp SOMA exp '''
    p[0] = sa.ExpSoma(p[1], p[3])
    
def p_exp_SUBTRACAO(p):
    ''' exp : exp SUBTRACAO exp '''
    p[0] = sa.ExpSubtracao(p[1], p[3])

def p_exp_MULTIPLICACAO(p):
    ''' exp : exp MULTIPLICACAO exp '''
    p[0] = sa.ExpMultiplicacao(p[1], p[3])

def p_exp_DIVISAO(p):
    ''' exp : exp DIVISAO exp '''
    p[0] = sa.ExpDivisao(p[1], p[3])

def p_exp_RESTO(p):
    ''' exp : exp RESTO exp '''
    p[0] = sa.ExpResto(p[1], p[3])

def p_exp_DECREMENTO(p):
    ''' exp : exp DECREMENTO '''
    p[0] = sa.ExpDecremento(p[1])
    
def p_exp_INCREMENTO(p):
    ''' exp : exp INCREMENTO '''
    p[0] = sa.ExpIncremento(p[1])

def p_exp_expINCREMENTO(p):
    ''' exp : INCREMENTO exp  '''
    p[0] = sa.ExpIncrementoPrefixo(p[1])

def p_exp_expDECREMENTO(p):
    ''' exp : DECREMENTO exp  '''
    p[0] = sa.ExpDecrementoPrefixo(p[1])

def p_exp_EXPONENCIACAO(p):
    ''' exp : exp EXPONENCIACAO exp '''
    p[0] = sa.ExpPotencia(p[1], p[3])

def p_exp_IGUAL_ESTRITA(p):
    ''' exp : exp IGUAL_ESTRITA exp '''
    p[0] = sa.ExpIgualdadeEstrita(p[1], p[3])

def p_exp_DESIGUAL_ESTRITA(p):
    ''' exp : exp DESIGUAL_ESTRITA exp '''
    p[0] = sa.ExpDiferencaEstrita(p[1], p[3])

def p_exp_AND_BITABIT(p):
    ''' exp : exp AND_BITABIT exp '''
    p[0] = sa.ExpEbit(p[1], p[3])

def p_exp_XOR_BITABIT(p):
    ''' exp : exp XOR_BITABIT exp '''
    p[0] = sa.ExpXorbit(p[1], p[3])

def p_exp_OR_BITABIT(p):
    ''' exp : exp OR_BITABIT exp '''
    p[0] = sa.ExpOUbit(p[1], p[3])

def p_exp_IGUALDADE(p):
    ''' exp : exp IGUALDADE exp '''
    p[0] = sa.Expigualdade(p[1], p[3])

def p_exp_DESIGUALDADE(p):
    ''' exp : exp DESIGUALDADE exp '''
    p[0] = sa.Expdiferenca(p[1], p[3])

def p_exp_MAIOR(p):
    ''' exp : exp MAIOR exp '''
    p[0] = sa.Expmaior(p[1], p[3])

def p_exp_MENOR(p):
    ''' exp : exp MENOR exp '''
    p[0] = sa.Expmenor(p[1], p[3])

def p_exp_MAIOR_IGUAL(p):
    ''' exp : exp MAIOR_IGUAL exp '''
    p[0] = sa.Expmaiorigual(p[1], p[3])
    
def p_exp_MENOR_IGUAL(p):
    ''' exp : exp MENOR_IGUAL exp '''
    p[0] = sa.Expmenorigual(p[1], p[3])

def p_exp_AND_LOGICO(p):
    ''' exp : exp AND_LOGICO exp '''
    p[0] = sa.ExpElogico(p[1], p[3])

def p_exp_OR_LOGICO(p):
    ''' exp : exp OR_LOGICO exp '''
    p[0] = sa.ExpOUlogico(p[1], p[3])

def p_exp_NAO_LOGICO(p):
    ''' exp : NAO_LOGICO exp  '''
    p[0] = sa.ExpNegacao(p[1])

def p_exp_NAO_BITABIT(p):
    ''' exp : NAO_BITABIT exp  '''
    p[0] = sa.ExpNegacaoBit(p[1])

def p_exp_AGRUPAMENTO(p):
    ''' exp : L_PARENTESIS exp R_PARENTESIS '''
    p[0] = sa.ExpParenteses(p[1])

def p_exp_POSITIVO_UNARIO(p):
    ''' exp : SOMA exp '''
    p[0] = sa.ExpPositivo(p[1])

def p_exp_NEGATIVO_UNARIO(p):
    ''' exp : SUBTRACAO exp '''
    p[0] = sa.ExpNegativo(p[1])

def p_exp_TERNARIO(p):
   ''' exp : exp INTERROGACAO exp DOIS_PONTOS exp '''
   p[0] = sa.ExpTernario(p[1], p[3], p[5])

def p_exp_MAIS_IGUAL_exp(p):
    ''' exp : exp MAIS_IGUAL exp'''
    p[0] = sa.ExpMaisIgual(p[1], p[3])

def p_exp_MENOS_IGUAL_exp(p):
    ''' exp : exp MENOS_IGUAL exp'''
    p[0] = sa.ExpMenosIgual(p[1], p[3])

def p_exp_MULTIPLICACAO_IGUAL_exp(p):
    ''' exp : exp MULTIPLICACAO_IGUAL exp'''
    p[0] = sa.ExpMultiplicacaoIgual(p[1], p[3])

def p_exp_EXPONENCIACAO_IGUAL_exp(p):
    ''' exp : exp EXPONENCIACAO_IGUAL exp'''
    p[0] = sa.ExpPotenciaIgual(p[1], p[3])

def p_exp_DIVISAO_IGUAL_exp(p):
    ''' exp : exp DIVISAO_IGUAL exp'''
    p[0] = sa.ExpDivisaoIgual(p[1], p[3])

def p_exp_RESTO_IGUAL_exp(p):
    ''' exp : exp RESTO_IGUAL exp'''
    p[0] = sa.ExpRestoIgual(p[1], p[3])

def p_exp_DESLOC_E_IGUAL_exp(p):
    ''' exp : exp DESLOC_E_IGUAL exp'''
    p[0] = sa.ExpDeslocamentoEsquerdaIgual(p[1], p[3])

def p_exp_DESLOC_D_IGUAL_exp(p):
    ''' exp : exp DESLOC_D_IGUAL exp'''
    p[0] = sa.ExpDeslocamentoDireitaIgual(p[1], p[3])

def p_exp_DESLOC_D_S_IGUAL_exp(p):
    ''' exp : exp DESLOC_D_S_IGUAL exp'''
    p[0] = sa.ExpDeslocamentoDireitaSemSinalIgual(p[1], p[3])

def p_exp_AND_BIT_IGUAL_exp(p):
    ''' exp : exp AND_BIT_IGUAL exp'''
    p[0] = sa.ExpEbitIgual(p[1], p[3])

def p_exp_XOR_BIT_IGUAL_exp(p):
    ''' exp : exp XOR_BIT_IGUAL exp'''  
    p[0] = sa.ExpXorbitIgual(p[1], p[3])

def p_exp_OR_BIT_IGUAL_exp(p):
    ''' exp : exp OR_BIT_IGUAL exp'''  
#COMEÇAR DAQUI
# exp . ID | exp . call | THIS |
def p_exp_NEW_ID_NOparams(p):
    ''' exp : NEW ID L_PARENTESIS R_PARENTESIS'''

def p_exp_NEW_ID_params(p):
    ''' exp : NEW ID L_PARENTESIS params R_PARENTESIS'''
    
def p_exp_exp_ID(p):
    ''' exp : exp ACESSO_MEMBRO ID'''

def p_exp_exp_call(p):
    ''' exp : exp ACESSO_MEMBRO call'''

def p_exp_THIS(p):
    ''' exp : THIS'''
#FINALIZA AQUI
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
    ''' vardecl : LET ID PONTO_E_VIRGULA'''
    
def p_vardecl_let(p):
    ''' vardecl : LET ID ATRIBUICAO exp PONTO_E_VIRGULA'''
    
def p_vardecl_const(p):
    ''' vardecl : CONST ID PONTO_E_VIRGULA'''
    
def p_vardecl_const_exp(p):
    ''' vardecl : CONST ID ATRIBUICAO exp PONTO_E_VIRGULA'''
    
def p_vardecl_var(p):
    ''' vardecl : VAR ID PONTO_E_VIRGULA'''
    
def p_vardecl_var_exp(p):
    ''' vardecl : VAR ID ATRIBUICAO exp PONTO_E_VIRGULA'''

#================== stms =========================

def p_stms_stm(p):
    ''' stms : stm '''
def p_stms_stm_stms(p):
    ''' stms : stm stms '''
    
#================== stm =========================
def p_stm_for(p):
    ''' stm : FOR L_PARENTESIS exp PONTO_E_VIRGULA exp PONTO_E_VIRGULA exp R_PARENTESIS body '''
def p_stm_assign(p):
    ''' stm : assign PONTO_E_VIRGULA '''
def p_stm_vardecl(p):
    ''' stm : vardecl '''
def p_stm_exp(p):
    ''' stm : exp PONTO_E_VIRGULA '''
def p_stm_return(p):
    ''' stm : RETURN exp PONTO_E_VIRGULA '''
def p_stm_while(p):
    ''' stm : WHILE L_PARENTESIS exp R_PARENTESIS body '''
def p_stm_if(p):
    ''' stm : IF L_PARENTESIS exp R_PARENTESIS body '''
def p_stm_if_else(p):
    ''' stm : IF L_PARENTESIS exp R_PARENTESIS body ELSE body '''



#================== assign =========================
def p_assign_ID(p):
    ''' assign : ID ATRIBUICAO exp '''
    
def p_assign_exp_ID(p):
    ''' assign : exp ACESSO_MEMBRO ID ATRIBUICAO exp '''
#================== call =========================
def p_call_ID_Params(p):
    ''' call : ID L_PARENTESIS params R_PARENTESIS '''

def p_call_ID(p):
    ''' call : ID L_PARENTESIS R_PARENTESIS '''

def p_call_exp_ID_Params(p):
    ''' call : exp ACESSO_MEMBRO ID L_PARENTESIS params R_PARENTESIS '''

def p_call_exp_ID_NOParams(p):
    ''' call : exp ACESSO_MEMBRO ID L_PARENTESIS R_PARENTESIS '''
    
#================== params =========================
def p_params_exp_params(p):
    ''' params : exp VIRGULA param'''
def p_params_exp(p):
    ''' params : exp '''
