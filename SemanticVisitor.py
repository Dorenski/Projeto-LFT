from AbstractVisitor import AbstractVisitor
from Visitor import *
import SymbolTable as st
from ExpressionLanguageLex import *

def coercion(type1, type2):
    if type1 == 'any' or type2 == 'any':
        return 'any'
        
    if (type1 in st.Number and type2 in st.Number):
        if (type1 == st.FLOAT or type2 == st.FLOAT):
            return st.FLOAT
        else:
            return st.INT
    else:
        return None

class SemanticVisitor(AbstractVisitor):

    def __init__(self):
        self.printer = Visitor()
        self.n_errors = 0
        st.beginScope('global')

    def getnerros(self):
        return self.n_errors

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
        st.symbolTable[-1][concretoClassdecl.type] = {st.BINDABLE: st.CLASS, st.TYPE: concretoClassdecl.type}
        st.beginScope(concretoClassdecl.type)
        concretoClassdecl.classbody.accept(self)
        st.endScope()

    def visitconcretoClassbody(self, concretoClassbody):
        concretoClassbody.classmembers.accept(self)

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
        params = ParametroConstructordecl.sigparams.accept(self)
        st.addFunction('constructor', params, 'void')
        st.beginScope('constructor')
        for p in params:
            st.addVar(p, 'any')
        ParametroConstructordecl.body.accept(self)
        st.endScope()
        
    def visitSemParametroConstructordecl(self, SemParemetroConstructordecl):
        st.addFunction('constructor', [], 'void')
        st.beginScope('constructor')
        SemParemetroConstructordecl.body.accept(self)
        st.endScope()

    def visitParametroMethoddecl(self, ParametroMethoddecl):
        params = ParametroMethoddecl.sigparams.accept(self)
        st.addFunction(ParametroMethoddecl.type, params, 'any')
        st.beginScope(ParametroMethoddecl.type)
        for p in params:
            st.addVar(p, 'any')
        ParametroMethoddecl.body.accept(self)
        st.endScope()

    def visitSemParametroMethoddecl(self, SemParametroMethoddecl):
        st.addFunction(SemParametroMethoddecl.type, [], 'any')
        st.beginScope(SemParametroMethoddecl.type)
        SemParametroMethoddecl.body.accept(self)
        st.endScope()

    def visitSemValorAttrdecl(self, SemValorAttrdecl):
        st.addVar(SemValorAttrdecl.type, 'any')

    def visitComValorAttrdecl(self, ComValorAttrdecl):
        type_exp = ComValorAttrdecl.exp.accept(self)
        st.addVar(ComValorAttrdecl.type, type_exp)
    
    def visitconcretoFuncdecl(self, concretoFuncdecl):
        name, params = concretoFuncdecl.signature.accept(self)
        st.addFunction(name, params, 'any')
        st.beginScope(name)
        for p in params:
            st.addVar(p, 'any')
        concretoFuncdecl.body.accept(self)
        st.endScope()
        
    def visitParametroSignature(self, ParametroSignature):
        params = ParametroSignature.sigparams.accept(self)
        return ParametroSignature.type, params

    def visitSemParametroSignature(self, SemParametroSignature):
        return SemParametroSignature.type, []

    def visitUmsigparams(self, umsigparam):
        return [umsigparam.type]

    def visitMaisdeUmsigparams(self, MaisdeUmsigparams):
        return [MaisdeUmsigparams.type] + MaisdeUmsigparams.sigparams.accept(self)

    def visitconcretoBody(self, concretoBody):
        concretoBody.stms.accept(self)

    def visitExpSoma(self, ExpSoma):
        tipoExp1 = ExpSoma.exp1.accept(self)
        tipoExp2 = ExpSoma.exp2.accept(self)
        
        if tipoExp1 == 'string' or tipoExp2 == 'string':
            return 'string'
            
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            ExpSoma.accept(self.printer)
            self.n_errors += 1 
            print('\n\t[Erro] Soma invalida. A expressao ', end='')
            ExpSoma.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            ExpSoma.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c

    def visitExpSubtracao(self, ExpSubtracao):
        tipoExp1 = ExpSubtracao.exp1.accept(self)
        tipoExp2 = ExpSubtracao.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            ExpSubtracao.accept(self.printer)
            self.n_errors += 1 
            print('\n\t[Erro] Subtracao invalida. Tipos incompatíveis.\n')
        return c

    def visitExpMultiplicacao(self, ExpMultiplicacao):
        tipoExp1 = ExpMultiplicacao.exp1.accept(self)
        tipoExp2 = ExpMultiplicacao.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            ExpMultiplicacao.accept(self.printer)
            self.n_errors += 1 
            print('\n\t[Erro] Multiplicacao invalida. Tipos incompatíveis.\n')
        return c

    def visitExpDivisao(self, ExpDivisao):
        tipoExp1 = ExpDivisao.exp1.accept(self)
        tipoExp2 = ExpDivisao.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            ExpDivisao.accept(self.printer)
            self.n_errors += 1 
            print('\n\t[Erro] Divisao invalida. Tipos incompatíveis.\n')
        return c
    
    def visitExpResto(self, ExpResto):
        tipoExp1 = ExpResto.exp1.accept(self)
        tipoExp2 = ExpResto.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            self.n_errors += 1 
            print('\n\t[Erro] Operador Resto invalido. Tipos incompatíveis.\n')
        return c

    def visitExpDecremento(self, ExpDecremento):
        return ExpDecremento.exp.accept(self)

    def visitExpIncremento(self, ExpIncremento):
        return ExpIncremento.exp.accept(self)

    def visitExpIncrementoPrefixo(self, ExpIncrementoPrefixo):
        return ExpIncrementoPrefixo.exp.accept(self)

    def visitExpDecrementoPrefixo(self, ExpDecrementoPrefixo):
        return ExpDecrementoPrefixo.exp.accept(self)

    def visitExpPotencia(self, ExpPotencia):
        tipoExp1 = ExpPotencia.exp1.accept(self)
        tipoExp2 = ExpPotencia.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            ExpPotencia.accept(self.printer)
            self.n_errors += 1 
            print('\n\t[Erro] Potencia invalida. Tipos incompatíveis.\n')
        return c

    def visitExpIgualdadeEstrita(self, ExpIgualdadeEstrita):
        ExpIgualdadeEstrita.exp1.accept(self)
        ExpIgualdadeEstrita.exp2.accept(self)
        return st.BOOL

    def visitExpDiferencaEstrita(self, ExpDiferencaEstrita):
        ExpDiferencaEstrita.exp1.accept(self)
        ExpDiferencaEstrita.exp2.accept(self)
        return st.BOOL

    def visitExpEbit(self, ExpEbit):
        ExpEbit.exp1.accept(self)
        ExpEbit.exp2.accept(self)
        return st.INT

    def visitExpXorbit(self, ExpXorbit):
        ExpXorbit.exp1.accept(self)
        ExpXorbit.exp2.accept(self)
        return st.INT

    def visitExpOUbit(self, ExpOUbit):
        ExpOUbit.exp1.accept(self)
        ExpOUbit.exp2.accept(self)
        return st.INT

    def visitExpigualdade(self, Expigualdade):
        Expigualdade.exp1.accept(self)
        Expigualdade.exp2.accept(self)
        return st.BOOL

    def visitExpdiferenca(self, Expdiferenca):
        Expdiferenca.exp1.accept(self)
        Expdiferenca.exp2.accept(self)
        return st.BOOL

    def visitExpmaior(self, Expmaior):
        Expmaior.exp1.accept(self)
        Expmaior.exp2.accept(self)
        return st.BOOL

    def visitExpmenor(self, Expmenor):
        Expmenor.exp1.accept(self)
        Expmenor.exp2.accept(self)
        return st.BOOL

    def visitExpmaiorigual(self, Expmaiorigual):
        Expmaiorigual.exp1.accept(self)
        Expmaiorigual.exp2.accept(self)
        return st.BOOL

    def visitExpmenorigual(self, Expmenorigual):
        Expmenorigual.exp1.accept(self)
        Expmenorigual.exp2.accept(self)
        return st.BOOL
        
    def visitExpElogico(self, ExpElogico):
        ExpElogico.exp1.accept(self)
        ExpElogico.exp2.accept(self)
        return st.BOOL
        
    def visitExpOUlogico(self, ExpOUlogico):
        ExpOUlogico.exp1.accept(self)
        ExpOUlogico.exp2.accept(self)
        return st.BOOL
        
    def visitExpNegacao(self, ExpNegacao):
        ExpNegacao.exp.accept(self)
        return st.BOOL
        
    def visitExpNegacaoBit(self, ExpNegacaoBit):
        ExpNegacaoBit.exp.accept(self)
        return st.INT
        
    def visitExpParenteses(self, ExpParenteses):
        return ExpParenteses.exp.accept(self)
        
    def visitExpPositivo(self, ExpPositivo):
        return ExpPositivo.exp.accept(self)
        
    def visitExpNegativo(self, ExpNegativo):
        return ExpNegativo.exp.accept(self)
        
    def visitExpTernario(self, ExpTernario):
        tipoExp1 = ExpTernario.exp1.accept(self)
        if tipoExp1 != st.BOOL:
            self.n_errors += 1 
            print("\n\t[Erro] A condicao do ternario deve ser boolean.\n")
        return ExpTernario.exp2.accept(self)
        
    def visitExpMaisIgual(self, ExpMaisIgual):
        tipoExp1 = ExpMaisIgual.exp1.accept(self)
        tipoExp2 = ExpMaisIgual.exp2.accept(self)
        return coercion(tipoExp1, tipoExp2) or tipoExp1
        
    def visitExpMenosIgual(self, ExpMenosIgual):
        tipoExp1 = ExpMenosIgual.exp1.accept(self)
        tipoExp2 = ExpMenosIgual.exp2.accept(self)
        return coercion(tipoExp1, tipoExp2)
        
    def visitExpMultiplicacaoIgual(self, ExpMultiplicacaoIgual):
        tipoExp1 = ExpMultiplicacaoIgual.exp1.accept(self)
        tipoExp2 = ExpMultiplicacaoIgual.exp2.accept(self)
        return coercion(tipoExp1, tipoExp2)
        
    def visitExpPotenciaIgual(self, ExpPotenciaIgual):
        tipoExp1 = ExpPotenciaIgual.exp1.accept(self)
        tipoExp2 = ExpPotenciaIgual.exp2.accept(self)
        return coercion(tipoExp1, tipoExp2)
        
    def visitExpDivisaoIgual(self, ExpDivisaoIgual):
        tipoExp1 = ExpDivisaoIgual.exp1.accept(self)
        tipoExp2 = ExpDivisaoIgual.exp2.accept(self)
        return coercion(tipoExp1, tipoExp2)
        
    def visitExpRestoIgual(self, ExpRestoIgual):
        tipoExp1 = ExpRestoIgual.exp1.accept(self)
        tipoExp2 = ExpRestoIgual.exp2.accept(self)
        return coercion(tipoExp1, tipoExp2)
        
    def visitExpDeslocamentoEsquerdaIgual(self, ExpDeslocamentoEsquerdaIgual):
        ExpDeslocamentoEsquerdaIgual.exp1.accept(self)
        ExpDeslocamentoEsquerdaIgual.exp2.accept(self)
        return st.INT
        
    def visitExpDeslocamentoDireitaIgual(self, ExpDeslocamentoDireitaIgual):
        ExpDeslocamentoDireitaIgual.exp1.accept(self)
        ExpDeslocamentoDireitaIgual.exp2.accept(self)
        return st.INT
        
    def visitExpDeslocamentoDireitaSemSinalIgual(self, ExpDeslocamentoDireitaSemSinalIgual):
        ExpDeslocamentoDireitaSemSinalIgual.exp1.accept(self)
        ExpDeslocamentoDireitaSemSinalIgual.exp2.accept(self)
        return st.INT
        
    def visitExpEbitIgual(self, ExpEbitIgual):
        ExpEbitIgual.exp1.accept(self)
        ExpEbitIgual.exp2.accept(self)
        return st.INT
        
    def visitExpXorbitIgual(self, ExpXorbitIgual):
        ExpXorbitIgual.exp1.accept(self)
        ExpXorbitIgual.exp2.accept(self)
        return st.INT
        
    def visitExpOUbitIgual(self, ExpOUbitIgual):
        ExpOUbitIgual.exp1.accept(self)
        ExpOUbitIgual.exp2.accept(self)
        return st.INT
        
    def visitExpNewSemParametro(self, ExpNewSemParametro):
        class_name = ExpNewSemParametro.type
           
        simbolo = st.getBindable(class_name)
        if simbolo is None or simbolo.get(st.BINDABLE) != st.CLASS:
            self.n_errors += 1
            print(f"\n\t[Erro] '{class_name}' nao eh uma classe.\n")
        return class_name
        
    def visitExpNewComParametro(self, ExpNewComParametro):
        simbolo = st.getBindable(ExpNewComParametro.type)
        if simbolo is None or simbolo.get(st.BINDABLE) != st.CLASS:
            self.n_errors += 1
            print(f"\n\t[Erro] '{ExpNewComParametro.type}' nao eh uma classe.\n")
        ExpNewComParametro.params.accept(self)
        return ExpNewComParametro.type
        
    def visitExpAcessoAtributo(self, ExpAcessoAtributo):
        ExpAcessoAtributo.exp.accept(self)
        return 'any'

    def visitExpAcessoMetodo(self, ExpAcessoMetodo):
        ExpAcessoMetodo.exp.accept(self)
        ExpAcessoMetodo.call.accept(self)
        return 'any'
    
    def visitExpThis(self, ExpThis):
        return 'object'
        
    def visitExpNum(self, ExpNum):
        if (isinstance(ExpNum.num, int)):
            return st.INT
        elif (isinstance(ExpNum.num, float)):
            return st.FLOAT

    def visitExpId(self, ExpId):
        idName = st.getBindable(ExpId.id)
        if (idName != None):
            return idName[st.TYPE]
        else:
            self.n_errors += 1
            print(f"\n\t[Erro] A variavel '{ExpId.id}' nao foi declarada.\n")
        return None

    def visitExpCall(self, ExpCall):
        return ExpCall.call.accept(self)
    
    def visitExpAssign(self, ExpAssign):
        return ExpAssign.assign.accept(self)

    def visitExpTrue(self, ExpTrue):
        return st.BOOL

    def visitExpFalse(self, ExpFalse):
        return st.BOOL

    def visitExpStringAD(self, ExpStringAD):  
        return 'string'

    def visitExpStringA(self, ExpStringA):
        return 'string'
    
    def visitLetSemValorVardecl(self, LetSemValorVardecl):
        st.addVar(LetSemValorVardecl.type, 'undefined')

    def visitVarSemValorVardecl(self, VarSemValorVardecl):
        st.addVar(VarSemValorVardecl.type, 'undefined')

    def visitConstSemValorVardecl(self, ConstSemValorVardecl):
        st.addVar(ConstSemValorVardecl.type, 'undefined')

    def visitLetComValorVardecl(self, LetComValorVardecl):
        type_exp = LetComValorVardecl.exp.accept(self)
        st.addVar(LetComValorVardecl.type, type_exp)

    def visitVarComValorVardecl(self, VarComValorVardecl):
        type_exp = VarComValorVardecl.exp.accept(self)
        st.addVar(VarComValorVardecl.type, type_exp)

    def visitConstComValorVardecl(self, ConstComValorVardecl):
        type_exp = ConstComValorVardecl.exp.accept(self)
        st.addVar(ConstComValorVardecl.type, type_exp)

    def visitUmstms(self, Umstms):
        Umstms.stm.accept(self)

    def visitMaisdeUmstms(self, MaisdeUmstms):
        MaisdeUmstms.stm.accept(self)
        MaisdeUmstms.stms.accept(self)

    def visitForStm(self, ForStm):
        ForStm.exp1.accept(self)
        type_exp2 = ForStm.exp2.accept(self)
        if type_exp2 != st.BOOL:
            self.n_errors += 1 
            print("\n\t[Erro] A condicao do FOR deve ser boolean.\n")
        ForStm.exp3.accept(self)
        ForStm.body.accept(self)

    def visitAssignStm(self, AssignStm):
        AssignStm.assign.accept(self)

    def visitVardeclStm(self, VardeclStm):
        VardeclStm.vardecl.accept(self)
    
    def visitExpStm(self, ExpStm):
        ExpStm.exp.accept(self)

    def visitReturnStm(self, ReturnStm):
        ReturnStm.exp.accept(self)

    def visitWhileStm(self, WhileStm):
        type_exp = WhileStm.exp.accept(self)
        if (type_exp != st.BOOL):
            WhileStm.exp.accept(self.printer)
            self.n_errors += 1 
            print("\n\t[Erro] A expressao do while eh", type_exp, end='')
            print(". Deveria ser boolean\n")
        WhileStm.body.accept(self)

    def visitIfStm(self, IfStm):
        type_exp = IfStm.exp.accept(self)
        if (type_exp != st.BOOL):
            IfStm.exp.accept(self.printer)
            self.n_errors += 1 
            print("\n\t[Erro] A expressao do IF eh", type_exp, end='')
            print(". Deveria ser boolean\n")
        IfStm.body.accept(self)

    def visitIfElseStm(self, IfElseStm):
        type_exp = IfElseStm.exp.accept(self)
        if (type_exp != st.BOOL):
            IfElseStm.exp.accept(self.printer)
            self.n_errors += 1 
            print("\n\t[Erro] A expressao do IF/ELSE eh", type_exp, end='')
            print(". Deveria ser boolean\n")
        IfElseStm.body1.accept(self)
        IfElseStm.body2.accept(self)

    def visitAtribuicaoSimples(self, AtribuicaoSimples):
        simbolo = st.getBindable(AtribuicaoSimples.type)
        if simbolo is None:
            st.addVar(AtribuicaoSimples.type, 'any')
        return AtribuicaoSimples.exp.accept(self)

    def visitAtribuicaoAtributo(self, AtribuicaoAtributo):
        AtribuicaoAtributo.exp1.accept(self)
        return AtribuicaoAtributo.exp2.accept(self)

    def visitCallSemParametro(self, CallSemParametro):
        simbolo = st.getBindable(CallSemParametro.type)
        if simbolo is None:
            return 'any'
            
        if simbolo.get(st.BINDABLE) != st.FUNCTION:
            self.n_errors += 1
            print(f"\n\t[Erro] O identificador '{CallSemParametro.type}' nao eh uma funcao.\n")
            return None
            
        return simbolo.get(st.TYPE)

    def visitCallComParametro(self, CallComParametro):
        simbolo = st.getBindable(CallComParametro.type)
        if simbolo is None:
            CallComParametro.params.accept(self)
            return 'any'
            
        if simbolo.get(st.BINDABLE) != st.FUNCTION:
            self.n_errors += 1
            print(f"\n\t[Erro] O identificador '{CallComParametro.type}' nao eh uma funcao.\n")
            return None
            
        CallComParametro.params.accept(self)
        return simbolo.get(st.TYPE)

    def visitCallAtributoSemParametro(self, CallAtributoSemParametro):
        CallAtributoSemParametro.exp.accept(self)
        return 'any'

    def visitCallAtributoComParametro(self, CallAtributoComParametro):
        CallAtributoComParametro.exp.accept(self)
        CallAtributoComParametro.params.accept(self)
        return 'any'

    def visitUmparams(self, Umparams):
        return [Umparams.exp.accept(self)]

    def visitMaisdeUmparams(self, MaisdeUmparams):
        return [MaisdeUmparams.exp.accept(self)] + MaisdeUmparams.params.accept(self)
    

def main():
    codigo_teste = """
class Motor {
        potencia;

        constructor() {
            this.potencia = 100;
        }

        aumentar(extra) {
            this.potencia += extra;
            return this.potencia;
        }
    }

    function testarLogica(valor, flag) {
        let x = valor;
        let y = 5;
        let z = 0;

        // Testando condicional e operadores bit-a-bit
        if (flag === true) {
            z = (x & y) | 1;
            z <<= 1;
        } else {
            z = ~x ^ y;
        }

        // ERRO INTENCIONAL 1: 
        // O while exige uma expressão booleana (verdadeiro/falso).
        // Aqui estamos passando uma operação matemática (z + 10), que resulta em um número.
        while (z + 10) {
            z--;
        }

        // Testando FOR (a variável 'k' será inferida no Visitor por causa da nossa adaptação)
        for (k = 0; k < 3; k++) {
            z *= 2;
        }

        // ERRO INTENCIONAL 2: 
        // Tentativa de fazer uma conta matemática de subtração com uma string.
        // Nossa função 'coercion' só permite matemática entre números.
        let erroSubtracao = 50 - "texto";

        return z;
    }

    function main() {
        let m = new Motor();
        m.aumentar(50);
        
        let teste = testarLogica(10, false);
        
        return teste;
    }
    """
    
    lexer = lex.lex()
    lexer.input(codigo_teste)
    parser = yacc.yacc()
    result = parser.parse(input=codigo_teste, debug=False)
    print("#imprime erros semanticos encontrados")
    svisitor = SemanticVisitor()
    result.accept(svisitor)
    print(f"Foram encontrados {svisitor.getnerros()} erros")


if __name__ == "__main__":
    main()