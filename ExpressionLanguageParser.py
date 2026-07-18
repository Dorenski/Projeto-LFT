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
# stm → FOR(exp;exp;exp) body | assign; | vardecl | exp ; | RETURN exp ; | WHILE ( exp ) body | IF ( exp ) body | IF ( exp ) body ELSE body
#
# assign → ID = exp | exp . ID = exp
#
# call → ID (params) | ID () | exp . ID (params) | exp . ID ()
#
# params → exp, params | exp


import ply.yacc as yacc
import ply.lex as lex
from ExpressionLanguageLex import *
import SintaxteAbstrata as sa

# ================== program =========================


def p_program_funcdecl(p):
    ''' program : funcdecl '''
    p[0] = sa.Umfuncdecl(p[1])


def p_program_funcdecl_program(p):
    ''' program : funcdecl program '''
    p[0] = sa.MaisdeUmfuncdecl(p[1], p[2])


def p_program_vardecl(p):
    ''' program : vardecl '''
    p[0] = sa.Umvardecl(p[1])


def p_program_vardecl_program(p):
    ''' program : vardecl program '''
    p[0] = sa.MaisdeUmvardecl(p[1], p[2])


def p_program_classdecl(p):
    '''program : classdecl '''
    p[0] = sa.Umclassdecl(p[1])


def p_program_classdecl_program(p):
    '''program : classdecl program '''
    p[0] = sa.MaisdeUmclassdecl(p[1], p[2])
# ================== classdecl =========================


def p_classdecl_CLASS_ID_classbody(p):
    '''classdecl : CLASS ID classbody '''
    p[0] = sa.concretoClassdecl(p[2], p[3])
# ================== classbody =========================


def p_classbody_classmembers(p):
    '''classbody : L_CHAVE classmembers R_CHAVE '''
    p[0] = sa.concretoClassbody(p[2])
# ================== classmembers =========================


def p_classmembers_classmember(p):
    '''classmembers : classmember '''
    p[0] = sa.Umclassmember(p[1])


def p_classmembers_classmembers(p):
    '''classmembers : classmember classmembers '''
    p[0] = sa.MaisdeUmclassmember(p[1], p[2])
# ================== classmember =========================


def p_classmember_methoddecl(p):
    '''classmember : methoddecl '''
    p[0] = sa.methodClassmember(p[1])


def p_classmember_constructordecl(p):
    '''classmember : constructordecl '''
    p[0] = sa.constructorClassmember(p[1])


def p_classmember_attrdecl(p):
    '''classmember : attrdecl '''
    p[0] = sa.attrClassmember(p[1])
# ================== constructordecl =========================


def p_constructordecl_sigparams(p):
    '''constructordecl : CONSTRUCTOR L_PARENTESIS sigparams R_PARENTESIS body '''
    p[0] = sa.ParametroConstrutordecl(p[3], p[5])


def p_constructordecl_NOsigparams(p):
    '''constructordecl : CONSTRUCTOR L_PARENTESIS  R_PARENTESIS body '''
    p[0] = sa.SemParametroConstructordecl(p[4])
# ================== methoddecl =========================


def p_methoddecl_sigparams(p):
    '''methoddecl : ID L_PARENTESIS sigparams R_PARENTESIS body '''
    p[0] = sa.ParametroMethoddecl(p[1], p[3], p[5])


def p_methoddecl_NOsigparams(p):
    '''methoddecl : ID L_PARENTESIS R_PARENTESIS body '''
    p[0] = sa.SemParametroMethoddecl(p[1], p[4])
# ================== attrdecl =========================


def p_attrdecl_ID(p):
    ''' attrdecl : ID PONTO_E_VIRGULA '''
    p[0] = sa.SemValorAttrdecl(p[1])


def p_attrdecl_exp(p):
    ''' attrdecl : ID ATRIBUICAO exp PONTO_E_VIRGULA '''
    p[0] = sa.ComValorAttrdecl(p[1], p[3])
# ================== funcdecl =========================


def p_funcdecl(p):
    ''' funcdecl : signature body '''
    p[0] = sa.concretoFuncdecl(p[1], p[2])
# ================== signature =========================


def p_signature_sigparams(p):
    ''' signature : FUNCTION ID L_PARENTESIS sigparams R_PARENTESIS '''
    p[0] = sa.ParametroSignature(p[2], p[4])


def p_signature_NOsigparams(p):
    ''' signature : FUNCTION ID L_PARENTESIS R_PARENTESIS '''
    p[0] = sa.SemParametroSignature(p[2])
# ================== sigparams =========================


def p_sigparams_id(p):
    ''' sigparams : ID '''
    p[0] = sa.Umsigparams(p[1])


def p_sigparams_id_sigparams(p):
    ''' sigparams : ID VIRGULA sigparams '''
    p[0] = sa.MaisdeUmsigparams(p[1], p[3])
# ================== body =========================


def p_body(p):
    ''' body : L_CHAVE stms R_CHAVE '''
    p[0] = sa.concretoBody(p[2])
# ================== EXP =========================


def p_exp_TERNARIO(p):
    ''' exp : exp1 INTERROGACAO exp DOIS_PONTOS exp'''
    p[0] = sa.ExpTernario(p[1], p[3], p[5])


def p_exp_MAIS_IGUAL(p):
    ''' exp : exp1 MAIS_IGUAL exp'''
    p[0] = sa.ExpMaisIgual(p[1], p[3])


def p_exp_MENOS_IGUAL(p):
    ''' exp : exp1 MENOS_IGUAL exp'''
    p[0] = sa.ExpMenosIgual(p[1], p[3])


def p_exp_MULTIPLICACAO_IGUAL(p):
    ''' exp : exp1 MULTIPLICACAO_IGUAL exp'''
    p[0] = sa.ExpMultiplicacaoIgual(p[1], p[3])


def p_exp_EXPONENCIACAO_IGUAL(p):
    ''' exp : exp1 EXPONENCIACAO_IGUAL exp'''
    p[0] = sa.ExpPotencia(p[1], p[3])


def p_exp_DIVISAO_IGUAL(p):
    ''' exp : exp1 DIVISAO_IGUAL exp'''
    p[0] = sa.ExpDivisaoIgual(p[1], p[3])


def p_exp_RESTO_IGUAL(p):
    ''' exp : exp1 RESTO_IGUAL exp'''
    p[0] = sa.ExpRestoIgual(p[1], p[3])


def p_exp_DESLOC_E_IGUAL(p):
    ''' exp : exp1 DESLOC_E_IGUAL exp'''
    p[0] = sa.ExpDeslocamentoEsquerdaIgual(p[1], p[3])


def p_exp_DESLOC_D_IGUAL(p):
    ''' exp : exp1 DESLOC_D_IGUAL exp'''
    p[0] = sa.ExpDeslocamentoDireitaIgual(p[1], p[3])


def p_exp_DESLOC_D_S_IGUAL(p):
    ''' exp : exp1 DESLOC_D_S_IGUAL exp'''
    p[0] = sa.ExpDeslocamentoDireitaSemSinalIgual(p[1], p[3])


def p_exp_AND_BIT_IGUAL(p):
    ''' exp : exp1 AND_BIT_IGUAL exp'''
    p[0] = sa.ExpEbitIgual(p[1], p[3])


def p_exp_XOR_BIT_IGUAL(p):
    ''' exp : exp1 XOR_BIT_IGUAL exp'''
    p[0] = sa.ExpXorbitIgual(p[1], p[3])


def p_exp1_OR_BIT_IGUAL(p):
    ''' exp : exp1 OR_BIT_IGUAL exp'''
    p[0] = sa.ExpOUbitIgual(p[1], p[3])


def p_exp_exp1(p):
    ''' exp : exp1'''
    p[0] = p[1]
# ------------------------------------


def p_exp1_OR_LOGICO(p):
    ''' exp1 : exp1 OR_LOGICO exp2'''
    p[0] = sa.ExpOUlogico(p[1], p[3])


def p_exp1_exp2(p):
    ''' exp1 : exp2'''
    p[0] = p[1]
# ------------------------------------


def p_exp2_AND_LOGICO(p):
    ''' exp2 : exp2 AND_LOGICO exp3'''
    p[0] = sa.ExpElogico(p[1], p[3])


def p_exp2_exp3(p):
    ''' exp2 : exp3'''
    p[0] = p[1]
# ------------------------------------


def p_exp3_OR_BITABIT(p):
    ''' exp3 : exp3 OR_BITABIT exp4 '''
    p[0] = sa.ExpOUbit(p[1], p[3])


def p_exp3_exp4(p):
    ''' exp3 : exp4 '''
    p[0] = p[1]
# ------------------------------------


def p_exp4_XOR_BITABIT(p):
    ''' exp4 : exp4 XOR_BITABIT exp5 '''
    p[0] = sa.ExpXorbit(p[1], p[3])


def p_exp4_exp5(p):
    ''' exp4 : exp5 '''
    p[0] = p[1]
# ------------------------------------


def p_exp5_AND_BITABIT(p):
    ''' exp5 : exp5 AND_BITABIT exp6 '''
    p[0] = sa.ExpEbit(p[1], p[3])


def p_exp5_exp6(p):
    ''' exp5 : exp6 '''
    p[0] = p[1]
# ------------------------------------


def p_exp6_IGUALDADE(p):
    ''' exp6 : exp6 IGUALDADE exp7 '''
    p[0] = sa.Expigualdade(p[1], p[3])


def p_exp6_DESIGUALDADE(p):
    ''' exp6 : exp6 DESIGUALDADE exp7 '''
    p[0] = sa.ExpDiferenca(p[1], p[3])


def p_exp6_IGUAL_ESTRITA(p):
    ''' exp6 : exp6 IGUAL_ESTRITA exp7 '''
    p[0] = sa.ExpIgualdadeEstrita(p[1], p[3])


def p_exp6_DESIGUAL_ESTRITA(p):
    ''' exp6 : exp6 DESIGUAL_ESTRITA exp7 '''
    p[0] = sa.ExpDiferencaEstrita(p[1], p[3])


def p_exp6_exp7(p):
    ''' exp6 : exp7 '''
    p[0] = p[1]
# ------------------------------------


def p_exp7_MAIOR(p):
    ''' exp7 : exp7 MAIOR exp8 '''
    p[0] = sa.Expmaior(p[1], p[3])


def p_exp7_MENOR(p):
    ''' exp7 : exp7 MENOR exp8 '''
    p[0] = sa.Expmenor(p[1], p[3])


def p_exp7_MAIOR_IGUAL(p):
    ''' exp7 : exp7 MAIOR_IGUAL exp8 '''
    p[0] = sa.Expmaiorigual(p[1], p[3])


def p_exp7_MENOR_IGUAL(p):
    ''' exp7 : exp7 MENOR_IGUAL exp8 '''
    p[0] = sa.Expmenorigual(p[1], p[3])


def p_exp7_exp8(p):
    ''' exp7 : exp8 '''
    p[0] = p[1]
# ------------------------------------


def p_exp8_SOMA(p):
    ''' exp8 : exp8 SOMA exp9 '''
    p[0] = sa.ExpSoma(p[1], p[3])


def p_exp8_SUBTRACAO(p):
    ''' exp8 : exp8 SUBTRACAO exp9 '''
    p[0] = sa.ExpSubtracao(p[1], p[3])


def p_exp8_exp9(p):
    ''' exp8 : exp9 '''
    p[0] = p[1]
# ------------------------------------


def p_exp9_MULTIPLICACAO(p):
    ''' exp9 : exp9 MULTIPLICACAO exp10 '''
    p[0] = sa.ExpMultiplicacao(p[1], p[3])


def p_exp9_DIVISAO(p):
    ''' exp9 : exp9 DIVISAO exp10 '''
    p[0] = sa.ExpDivisao(p[1], p[3])


def p_exp9_RESTO(p):
    ''' exp9 : exp9 RESTO exp10 '''
    p[0] = sa.ExpResto(p[1], p[3])


def p_exp9_exp10(p):
    ''' exp9 : exp10 '''
    p[0] = p[1]
# ------------------------------------


def p_exp10_EXPONENCIACAO(p):
    ''' exp10 : exp11 EXPONENCIACAO exp10 '''
    p[0] = sa.ExpPotencia(p[1], p[3])


def p_exp10_exp11(p):
    ''' exp10 : exp11 '''
    p[0] = p[1]
# ------------------------------------


def p_exp11_INCREMENTO_PREFIXO(p):
    ''' exp11 : INCREMENTO exp11 '''
    p[0] = sa.ExpIncrementoPrefixo(p[2])


def p_exp11_DECREMENTO_PREFIXO(p):
    ''' exp11 : DECREMENTO exp11 '''
    p[0] = sa.ExpDecrementoPrefixo(p[2])


def p_exp11_NAO_LOGICO(p):
    ''' exp11 : NAO_LOGICO exp11 '''
    p[0] = sa.ExpNegacao(p[2])


def p_exp11_NAO_BITABIT(p):
    ''' exp11 : NAO_BITABIT exp11 '''
    p[0] = sa.ExpNegacaoBit(p[2])


def p_exp11_MAIS_UNARIO(p):
    ''' exp11 : SOMA exp11 '''
    p[0] = sa.ExpPositivo(p[2])


def p_exp11_MENOS_UNARIO(p):
    ''' exp11 : SUBTRACAO exp11 '''
    p[0] = sa.ExpNegativo(p[2])


def p_exp11_exp12(p):
    ''' exp11 : exp12 '''
    p[0] = p[1]
# ------------------------------------


def p_exp12_INCREMENTO_SUFIXO(p):
    ''' exp12 : exp12 INCREMENTO '''
    p[0] = sa.ExpIncremento(p[1])


def p_exp12_DECREMENTO_SUFIXO(p):
    ''' exp12 : exp12 DECREMENTO '''
    p[0] = sa.ExpDecremento(p[1])


def p_exp12_exp13(p):
    ''' exp12 : exp13 '''
    p[0] = p[1]
# ------------------------------------


def p_exp13_ACESSO_ID(p):
    ''' exp13 : exp13 ACESSO_MEMBRO ID '''
    p[0] = sa.ExpAcessoAtributo(p[1], p[3])


def p_exp13_ACESSO_CALL(p):
    ''' exp13 : exp13 ACESSO_MEMBRO call '''
    p[0] = sa.ExpAcessoMetodo(p[1], p[3])


def p_exp13_exp14(p):
    ''' exp13 : exp14 '''
    p[0] = p[1]
# ------------------------------------


def p_exp14_NEW_VAZIO(p):
    ''' exp14 : NEW ID L_PARENTESIS R_PARENTESIS '''
    p[0] = sa.ExpNewSemParametro(p[2])


def p_exp14_NEW_PARAMS(p):
    ''' exp14 : NEW ID L_PARENTESIS params R_PARENTESIS '''
    p[0] = sa.ExpNewComParametro(p[2], p[4])


def p_exp14_THIS(p):
    ''' exp14 : THIS '''
    p[0] = sa.ExpThis()


def p_exp14_NUM(p):
    ''' exp14 : INT_LITERAL '''
    p[0] = sa.ExpNum(p[1])


def p_exp14_ID(p):
    ''' exp14 : ID '''
    p[0] = sa.ExpId(p[1])


def p_exp14_CALL(p):
    ''' exp14 : call '''
    p[0] = sa.ExpCall(p[1])


def p_exp14_ASSIGN(p):
    ''' exp14 : assign '''
    p[0] = sa.ExpAssign(p[1])


def p_exp14_TRUE(p):
    ''' exp14 : TRUE '''
    p[0] = sa.ExpTrue()


def p_exp14_FALSE(p):
    ''' exp14 : FALSE '''
    p[0] = sa.ExpFalse()


def p_exp14_STRING_AD(p):
    ''' exp14 : STRING_AD '''
    p[0] = sa.ExpStringAD(p[1])


def p_exp14_STRING_A(p):
    ''' exp14 : STRING_A '''
    p[0] = sa.ExpStringA(p[1])


def p_exp14_AGRUPAMENTO(p):
    ''' exp14 : L_PARENTESIS exp R_PARENTESIS '''
    p[0] = sa.ExpParenteses(p[2])
# ================== vardecl =========================


def p_vardecl(p):
    ''' vardecl : LET ID PONTO_E_VIRGULA'''
    p[0] = sa.LetSemValorVardecl(p[2])


def p_vardecl_let(p):
    ''' vardecl : LET ID ATRIBUICAO exp PONTO_E_VIRGULA'''
    p[0] = sa.LetComValorVardecl(p[2], p[4])


def p_vardecl_const(p):
    ''' vardecl : CONST ID PONTO_E_VIRGULA'''
    p[0] = sa.ConstSemValorVardecl(p[2])


def p_vardecl_const_exp(p):
    ''' vardecl : CONST ID ATRIBUICAO exp PONTO_E_VIRGULA'''
    p[0] = sa.ConstComValorVardecl(p[2], p[4])


def p_vardecl_var(p):
    ''' vardecl : VAR ID PONTO_E_VIRGULA'''
    p[0] = sa.VarSemValorVardecl(p[2])


def p_vardecl_var_exp(p):
    ''' vardecl : VAR ID ATRIBUICAO exp PONTO_E_VIRGULA'''
    p[0] = sa.VarComValorVardecl(p[2], p[4])
# ================== stms =========================


def p_stms_stm(p):
    ''' stms : stm '''
    p[0] = sa.Umstms(p[1])


def p_stms_stm_stms(p):
    ''' stms : stm stms '''
    p[0] = sa.MaisdeUmstms(p[1], p[2])
# ================== stm =========================


def p_stm_for(p):
    ''' stm : FOR L_PARENTESIS exp PONTO_E_VIRGULA exp PONTO_E_VIRGULA exp R_PARENTESIS body '''
    p[0] = sa.ForStm(p[3], p[5], p[7], p[9])


def p_stm_assign(p):
    ''' stm : assign PONTO_E_VIRGULA '''
    p[0] = sa.AssignStm(p[1])


def p_stm_vardecl(p):
    ''' stm : vardecl '''
    p[0] = sa.VardeclStm(p[1])


def p_stm_exp(p):
    ''' stm : exp PONTO_E_VIRGULA '''
    p[0] = sa.ExpStm(p[1])


def p_stm_return(p):
    ''' stm : RETURN exp PONTO_E_VIRGULA '''
    p[0] = sa.ReturnStm(p[2])


def p_stm_while(p):
    ''' stm : WHILE L_PARENTESIS exp R_PARENTESIS body '''
    p[0] = sa.WhileStm(p[3], p[5])


def p_stm_if(p):
    ''' stm : IF L_PARENTESIS exp R_PARENTESIS body '''
    p[0] = sa.IfStm(p[3], p[5])


def p_stm_if_else(p):
    ''' stm : IF L_PARENTESIS exp R_PARENTESIS body ELSE body '''
    p[0] = sa.IfElseStm(p[3], p[5], p[7])
# ================== assign =========================


def p_assign_ID(p):
    ''' assign : ID ATRIBUICAO exp '''
    p[0] = sa.AtribuicaoSimples(p[1], p[3])


def p_assign_exp_ID(p):
    ''' assign : exp13 ACESSO_MEMBRO ID ATRIBUICAO exp '''
    p[0] = sa.AtribuicaoAtributo(p[1], p[3], p[5])
# ================== call =========================


def p_call_ID_Params(p):
    ''' call : ID L_PARENTESIS params R_PARENTESIS '''
    p[0] = sa.CallComParametro(p[1], p[3])


def p_call_ID(p):
    ''' call : ID L_PARENTESIS R_PARENTESIS '''
    p[0] = sa.CallSemParametro(p[1])


def p_call_exp_ID_Params(p):
    ''' call : exp13 ACESSO_MEMBRO ID L_PARENTESIS params R_PARENTESIS '''
    p[0] = sa.CallAtributoComParametro(p[1], p[3], p[5])


def p_call_exp_ID_NOParams(p):
    ''' call : exp13 ACESSO_MEMBRO ID L_PARENTESIS R_PARENTESIS '''
    p[0] = sa.CallAtributoSemParametro(p[1], p[3])
# ================== params =========================


def p_params_exp_params(p):
    ''' params : exp VIRGULA params'''
    p[0] = sa.MaisdeUmparams(p[1], p[3])


def p_params_exp(p):
    ''' params : exp '''
    p[0] = sa.Umparams(p[1])


data2 = '''
class Calculadora {
    resultado;

    constructor() {
        this.resultado = 0;
    }

    somar(a, b) {
        let res = a + b;
        this.resultado += res;
        return this.resultado;
    }
}

function operacoes(x, y) {
    const msg = "Iniciando processamento";
    var status = 'ativo';
    let z = x ** y;
    
    if (z >= 100) {
        z %= 10;
    } else {
        z <<= 2;
    }

    while (status == 'ativo') {
        if (z === 0) {
            status = 'inativo';
        }
        z--;
    }

    for (i = 0; i < 5; i++) {
        z = z | 1;
        z = (z > 0) ? z : ~z;
    }

    return true;
}

function main() {
    let calc = new Calculadora();
    calc.somar(10, 20);
    operacoes(2, 8);
    return false;
}
'''
if __name__ == '__main__':
    lexer.input(data2)
    parser = yacc.yacc()
    parser.parse(debug=True)
