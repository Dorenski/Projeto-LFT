from AbstractVisitor import AbstractVisitor
from ExpressionLanguageParser import *
# global tab
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor(AbstractVisitor):

    def visitUmfuncdecl(self, Umfuncdecl):
        Umfuncdecl.funcdecl.accept(self)

    def visitMaisdeUmfuncdecl(self, MaisdeUmfuncdecl):
        MaisdeUmfuncdecl.funcDecl.accept(self)
        MaisdeUmfuncdecl.program.accept(self)

    def visitUmvardecl(self, Umvardecl):
        Umvardecl.vardecl.accept(self)

    def visitMaisdeUmvardecl(self, MaisdeUmvardecl):
        MaisdeUmvardecl.vardecl.accept(self)
        MaisdeUmvardecl.program.accept(self)

    def visitUmclassdecl(self, Umclassdecl):
        Umclassdecl.classdecl.accept(self)

    def visitMaisdeUmclassdecl(self, MaisdeUmclassdecl):
        MaisdeUmclassdecl.classdecl.accept(self)
        MaisdeUmclassdecl.program.accept(self)

    def visitconcretoClassdecl(self, concretoClassdecl):
        print("Class")
        print(concretoClassdecl.type, end='')
        concretoClassdecl.classbody.accept(self)

    def visitconcretoClassbody(self, concretoClassbody):
        print("{")
        concretoClassbody.classmembers.accept(self)
        print("}")

    def visitUmclassmember(self, Umclassmember):
        Umclassmember.classmember.accept(self)

    def visitMaisdeUmclassmember(self, MaisdeUmclassmember):
        MaisdeUmclassmember.classmember.accept(self)
        MaisdeUmclassmember.classmembers.accept(self)

    def visitmethodClassmember(self, methodClassmember):
        methodClassmember.methoddecl.accept(self)

    def visitconstructorClassmember(self, constructorClassmember):
        constructorClassmember.constructordecl.accept(self)

    def visitattrClassmember(self, attrClassmember):
        attrClassmember.attrdecl.accept(self)

    def visitParametroConstructordecl(self, ParametroConstructordecl):
        print("Constructor (", end='', sep='')
        ParametroConstructordecl.sigparams.accept(self)
        print(")", end='', sep='')
        ParametroConstructordecl.body.accept(self)
        
    def visitSemParametroConstructordecl(self, SemParemetroConstructordecl):
        print("Constructor ( )", end='', sep='')
        SemParemetroConstructordecl.body.accept(self)

    def visitParametroMethoddecl(self, ParametroMethoddecl):
        print(ParametroMethoddecl.type,"(", end='', sep='')
        ParametroMethoddecl.sigparams.accept(self)
        print(")", end='', sep='')
        ParametroMethoddecl.body.accept(self)

    def visitSemParametroMethoddecl(self, SemParametroMethoddecl):
        print(SemParametroMethoddecl.type,"( )", end='', sep='')
        SemParametroMethoddecl.body.accept(self)

    def visitSemValorAttrdecl(self, SemValorAttrdecl):
        print(SemValorAttrdecl.type, ",", end='', sep='')

    def visitComValorAttrdecl(self, ComValorAttrdecl):
        print(ComValorAttrdecl.type, " = ", end='', sep='')
        ComValorAttrdecl.exp.accept(self)
        print(";")

    def visitconcretoFuncdecl(self, concretoFuncdecl):
        concretoFuncdecl.signature.accept(self)
        concretoFuncdecl.body.accept(self)
        print()
        
    def visitParametroSignature(self, ParametroSignature):
        print("Function ", ParametroSignature.type, "(", end='', sep='')
        ParametroSignature.sigparams.accept(self)
        print(")", end='', sep='')

    def visitSemParametroSignature(self, SemParametroSignature):
        print("Function ", SemParametroSignature.type, "( )", end='', sep='')

    def visitUmsigparams(self, umsigparam):
        print(umsigparam.type, end='', sep='')

    def visitMaisdeUmsigparams(self, MaisdeUmsigparams):
        print(MaisdeUmsigparams.type, ",", end='', sep='')
        MaisdeUmsigparams.sigparams.accept(self)

    def visitconcretoBody(self, concretoBody):
        print("{")
        concretoBody.stms.accept(self)
        print("}")

    def visitExpSoma(self, ExpSoma):
        ExpSoma.exp1.accept(self)
        print(" + ", end='', sep='')
        ExpSoma.exp2.accept(self)

    def visitExpSubtracao(self, ExpSubtracao):
        ExpSubtracao.exp1.accept(self)
        print(" - ", end='', sep='')
        ExpSubtracao.exp2.accept(self)

    def visitExpMultiplicacao(self, ExpMultiplicacao):
        ExpMultiplicacao.exp1.accept(self)
        print(" * ", end='', sep='')
        ExpMultiplicacao.exp2.accept(self)

    def visitExpDivisao(self, ExpDivisao):
        ExpDivisao.exp1.accept(self)
        print(" / ", end='', sep='')
        ExpDivisao.exp2.accept(self)
    
    def visitExpResto(self, ExpResto):
        ExpResto.exp1.accept(self)
        print(" % ", end='', sep='')
        ExpResto.exp2.accept(self)

    def visitExpDecremento(self, ExpDecremento):
        ExpDecremento.exp.accept(self)
        print(" -- ", end='', sep='')

    def visitExpIncremento(self, ExpIncremento):
        ExpIncremento.exp.accept(self)
        print(" ++ ", end='', sep='')

    def visitExpIncrementoPrefixo(self, ExpIncrementoPrefixo):
        print(" ++ ", end='', sep='')
        ExpIncrementoPrefixo.exp.accept(self)

    def visitExpDecrementoPrefixo(self, ExpDecrementoPrefixo):
        print(" -- ", end='', sep='')
        ExpDecrementoPrefixo.exp.accept(self)

    def visitExpPotencia(self, ExpPotencia):
        ExpPotencia.exp1.accept(self)
        print(" ** ", end='', sep='')
        ExpPotencia.exp2.accept(self)

    def visitExpIgualdadeEstrita(self, ExpIgualdadeEstrita):
        ExpIgualdadeEstrita.exp1.accept(self)
        print(" === ", end='', sep='')
        ExpIgualdadeEstrita.exp2.accept(self)

    def visitExpDiferencaEstrita(self, ExpDiferencaEstrita):
        ExpDiferencaEstrita.exp1.accept(self)
        print(" !== ", end='', sep='')
        ExpDiferencaEstrita.exp2.accept(self)

    def visitExpEbit(self, ExpEbit):
        ExpEbit.exp1.accept(self)
        print(" & ", end='', sep='')
        ExpEbit.exp2.accept(self)

    def visitExpXorbit(self, ExpXorbit):
        ExpXorbit.exp1.accept(self)
        print(" ^ ", end='', sep='')
        ExpXorbit.exp2.accept(self)

    def visitExpOUbit(self, ExpOUbit):
        ExpOUbit.exp1.accept(self)
        print(" | ", end='', sep='')
        ExpOUbit.exp2.accept(self)

    def visitExpigualdade(self, Expigualdade):
        Expigualdade.exp1.accept(self)
        print(" == ", end='', sep='')
        Expigualdade.exp2.accept(self)

    def visitExpdiferenca(self, Expdiferenca):
        Expdiferenca.exp1.accept(self)
        print(" != ", end='', sep='')
        Expdiferenca.exp2.accept(self)

    def visitExpmaior(self, Expmaior):
        Expmaior.exp1.accept(self)
        print(" > ", end='', sep='')
        Expmaior.exp2.accept(self)

    def visitExpmenor(self, Expmenor):
        Expmenor.exp1.accept(self)
        print(" < ", end='', sep='')
        Expmenor.exp2.accept(self)

    def visitExpmaiorigual(self, Expmaiorigual):
        Expmaiorigual.exp1.accept(self)
        print(" >= ", end='', sep='')
        Expmaiorigual.exp2.accept(self)

    def visitExpmenorigual(self, Expmenorigual):
        Expmenorigual.exp1.accept(self)
        print(" <= ", end='', sep='')
        Expmenorigual.exp2.accept(self)

    def visitExpElogico(self, ExpElogico):
        ExpElogico.exp1.accept(self)
        print(" && ", end='', sep='')
        ExpElogico.exp2.accept(self)

    def visitExpOUlogico(self, ExpOUlogico):
        ExpOUlogico.exp1.accept(self)
        print(" || ", end='', sep='')
        ExpOUlogico.exp2.accept(self)

    def visitExpNegacao(self, ExpNegacao):
        print(" ! ", end='', sep='')
        ExpNegacao.exp.accept(self)

    def visitExpNegacaoBit(self, ExpNegacaoBit):
        print(" ~ ", end='', sep='')
        ExpNegacaoBit.exp.accept(self)
    
    def visitExpParenteses(self, ExpParenteses):
        print("(", end='', sep='')
        ExpParenteses.exp.accept(self)
        print(")", end='', sep='')

    def visitExpPositivo(self, ExpPositivo):
        print(" + ", end='', sep='')
        ExpPositivo.exp.accept(self)

    def visitExpNegativo(self, ExpNegativo):
        print(" - ", end='', sep='')
        ExpNegativo.exp.accept(self)
    
    def visitExpTernario(self, ExpTernario):
        ExpTernario.exp1.accept(self)
        print(" ? ", end='', sep='')
        ExpTernario.exp2.accept(self)
        print(" : ", end='', sep='')
        ExpTernario.exp3.accept(self)

    def visitExpMaisIgual(self, ExpMaisIgual):
        ExpMaisIgual.exp1.accept(self)
        print(" += ", end='', sep='')
        ExpMaisIgual.exp2.accept(self)

    def visitExpMenosIgual(self, ExpMenosIgual):
        ExpMenosIgual.exp1.accept(self)
        print(" -= ", end='', sep='')
        ExpMenosIgual.exp2.accept(self)
    
    def visitExpMultiplicacaoIgual(self, ExpMultiplicacaoIgual):
        ExpMultiplicacaoIgual.exp1.accept(self)
        print(" *= ", end='', sep='')
        ExpMultiplicacaoIgual.exp2.accept(self)

    def visitExpPotenciaIgual(self, ExpPotenciaIgual):
        ExpPotenciaIgual.exp1.accept(self)
        print(" **= ", end='', sep='')
        ExpPotenciaIgual.exp2.accept(self)

    def visitExpDivisaoIgual(self, ExpDivisaoIgual):
        ExpDivisaoIgual.exp1.accept(self)
        print(" /= ", end='', sep='')
        ExpDivisaoIgual.exp2.accept(self)

    def visitExpRestoIgual(self, ExpRestoIgual):
        ExpRestoIgual.exp1.accept(self)
        print(" %= ", end='', sep='')
        ExpRestoIgual.exp2.accept(self)

    def visitExpDeslocamentoEsquerdaIgual(self, ExpDeslocamentoEsquerdaIgual):
        ExpDeslocamentoEsquerdaIgual.exp1.accept(self)
        print(" <<= ", end='', sep='')
        ExpDeslocamentoEsquerdaIgual.exp2.accept(self)

    def visitExpDeslocamentoDireitaIgual(self, ExpDeslocamentoDireitaIgual):
        ExpDeslocamentoDireitaIgual.exp1.accept(self)
        print(" >>= ", end='', sep='')
        ExpDeslocamentoDireitaIgual.exp2.accept(self)

    def visitExpDeslocamentoDireitaSemSinalIgual(self, ExpDeslocamentoDireitaSemSinalIgual):
        ExpDeslocamentoDireitaSemSinalIgual.exp1.accept(self)
        print(" >>>= ", end='', sep='')
        ExpDeslocamentoDireitaSemSinalIgual.exp2.accept(self)

    def visitExpEbitIgual(self, ExpEbitIgual):
        ExpEbitIgual.exp1.accept(self)
        print(" &= ", end='', sep='')
        ExpEbitIgual.exp2.accept(self)

    def visitExpXorbitIgual(self, ExpXorbitIgual):
        ExpXorbitIgual.exp1.accept(self)
        print(" ^= ", end='', sep='')
        ExpXorbitIgual.exp2.accept(self)

    def visitExpOUbitIgual(self, ExpOUbitIgual):
        ExpOUbitIgual.exp1.accept(self)
        print(" |= ", end='', sep='')
        ExpOUbitIgual.exp2.accept(self)
    
    def visitExpNewSemParametro(self, ExpNewSemParametro):
        print("new ", end='', sep='')
        print(ExpNewSemParametro.type)
        print("( )", end='', sep='')

    def visitExpNewComParametro(self, ExpNewComParametro):
        print("new ", end='', sep='')
        ExpNewComParametro.type.accept(self)
        print("(", end='', sep='')
        ExpNewComParametro.params.accept(self)
        print(")", end='', sep='')

    def visitExpAcessoAtributo(self, ExpAcessoAtributo):
        ExpAcessoAtributo.exp.accept(self)
        print(".", end='', sep='')
        print(ExpAcessoAtributo.type)

    def visitExpAcessoMetodo(self, ExpAcessoMetodo):
        ExpAcessoMetodo.exp.accept(self)
        print(".", end='', sep='')
        ExpAcessoMetodo.call.accept(self)
    
    def visitExpThis(self, ExpThis):
        print("this", end='', sep='')
        
    def visitExpNum(self, ExpNum):
        print(ExpNum.num, end='', sep='')

    def visitExpId(self, ExpId):
        print(ExpId.id, end='', sep='')

    def visitExpCall(self, ExpCall):
        ExpCall.call.accept(self)
    
    def visitExpAssign(self, ExpAssign):
        ExpAssign.assign.accept(self)

    def visitExpTrue(self, ExpTrue):
        print("true", end='', sep='')

    def visitExpFalse(self, ExpFalse):
        print("false", end='', sep='')

    def visitExpStringAD(self, ExpStringAD):
        print(ExpStringAD.val, end='', sep='')    

    def visitExpStringA(self, ExpStringA):
        print(ExpStringA.val, end='', sep='')
    
    def visitLetSemValorVardecl(self, LetSemValorVardecl):
        print("let ", LetSemValorVardecl.type, ";", end='', sep='')

    def visitVarSemValorVardecl(self, VarSemValorVardecl):
        print("var ", VarSemValorVardecl.type, ";", end='', sep='')

    def visitConstSemValorVardecl(self, ConstSemValorVardecl):
        print("const ", ConstSemValorVardecl.type, ";", end='', sep='')

    def visitLetComValorVardecl(self, LetComValorVardecl):
        print("let ", LetComValorVardecl.type, " = ", end='', sep='')
        LetComValorVardecl.exp.accept(self)
        print(";")

    def visitVarComValorVardecl(self, VarComValorVardecl):
        print("var ", VarComValorVardecl.type, " = ", end='', sep='')
        VarComValorVardecl.exp.accept(self)
        print(";")

    def visitConstComValorVardecl(self, ConstComValorVardecl):
        print("const ", ConstComValorVardecl.type, " = ", end='', sep='')
        ConstComValorVardecl.exp.accept(self)
        print(";")

    def visitUmstms(self, Umstms):
        Umstms.stm.accept(self)

    def visitMaisdeUmstms(self, MaisdeUmstms):
        MaisdeUmstms.stm.accept(self)
        MaisdeUmstms.stms.accept(self)

    def visitForStm(self, ForStm):
        print("for (", end='', sep='')
        ForStm.exp1.accept(self)
        print(" ; ", end='', sep='')
        ForStm.exp2.accept(self)
        print(" ; ", end='', sep='')
        ForStm.exp3.accept(self)
        print(" )", end='', sep='')
        ForStm.body.accept(self)

    def visitAssignStm(self, AssignStm):
        AssignStm.assign.accept(self)
        print(";")

    def visitVardeclStm(self, VardeclStm):
        VardeclStm.vardecl.accept(self)
    
    def visitExpStm(self, ExpStm):
        ExpStm.exp.accept(self)
        print(";")

    def visitReturnStm(self, ReturnStm):
        print("return ", end='', sep='')
        ReturnStm.exp.accept(self)
        print(";")

    def visitWhileStm(self, WhileStm):
        print("while (", end='', sep='')
        WhileStm.exp.accept(self)
        print(")", end='', sep='')
        WhileStm.body.accept(self)

    def visitIfStm(self, IfStm):
        print("if (", end='', sep='')
        IfStm.exp.accept(self)
        print(" )", end='', sep='')
        IfStm.body.accept(self)


    def visitIfElseStm(self, IfElseStm):
        print("if (", end='', sep='')
        IfElseStm.exp.accept(self)
        print(" )", end='', sep='')
        IfElseStm.body1.accept(self)
        print(" else ", end='', sep='')
        IfElseStm.body2.accept(self)

    def visitAtribuicaoSimples(self, AtribuicaoSimples):
        print(AtribuicaoSimples.type, end='', sep='')
        print(" = ", end='', sep='')
        AtribuicaoSimples.exp.accept(self)

    def visitAtribuicaoAtributo(self, AtribuicaoAtributo):
        AtribuicaoAtributo.exp1.accept(self)
        print(".", end='', sep='')
        print(AtribuicaoAtributo.type, end='', sep='') 
        print(" = ", end='', sep='')
        AtribuicaoAtributo.exp2.accept(self)

    def visitCallSemParametro(self, CallSemParametro):
        print(CallSemParametro.type, "( )", end='', sep='')

    def visitCallComParametro(self, CallComParametro):
        print(CallComParametro.type, "(", end='', sep='')
        CallComParametro.params.accept(self)
        print(")", end='', sep='')

    def visitCallAtributoSemParametro(self, CallAtributoSemParametro):
        CallAtributoSemParametro.exp.accept(self)
        print(".", CallAtributoSemParametro.type, "( )", end='', sep='')

    def visitCallAtributoComParametro(self, CallAtributoComParametro):
        CallAtributoComParametro.exp.accept(self)
        print(".", CallAtributoComParametro.type, "(", end='', sep='')
        CallAtributoComParametro.params.accept(self)
        print(")", end='', sep='')

    def visitUmparams(self, Umparams):
        Umparams.exp.accept(self)

    def visitMaisdeUmparams(self, MaisdeUmparams):
        MaisdeUmparams.exp.accept(self)
        print(", ", end='', sep='')
        MaisdeUmparams.params.accept(self)


if __name__ == "__main__":

    codigo_teste = """
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
    """
    lexer = lex.lex()
    lexer.input(codigo_teste)
    parser = yacc.yacc()
    result = parser.parse(input=codigo_teste, debug=False)
    print("# imprime o programa que foi passado como entrada")
    visitor = Visitor()

    if result:
        result.accept(visitor)