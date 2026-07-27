from AbstractVisitor import AbstractVisitor
from ExpressionLanguageParser import *
import AssemblyST as st

def getAssemblyType(type_val=None):
    return ".word" 

class AssemblyVisitor(AbstractVisitor):

    def __init__(self):
        st.beginScope('global_scope')
        self.funcs = []  
        self.text = []  
        self.text.append(".text")
        self.text.append("    move $fp, $sp")
        self.data = set()  
        self.rotulos = {}

    def novo_rotulo(self, string):
        if not string in self.rotulos:
            self.rotulos[string] = 0
        rotulo = f"{string}_{self.rotulos[string]}"
        self.rotulos[string] += 1
        return rotulo
    
    def getList(self):
        return self.text if st.getScope() == 'global_scope' else self.funcs   

    # ================== program =========================
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
        code = self.getList()
        code.append("constructor:")
        code.append("    move $fp, $sp")
        st.beginScope('constructor')
        ParametroConstructordecl.sigparams.accept(self)
        ParametroConstructordecl.body.accept(self)
        st.endScope()
        
    def visitSemParametroConstructordecl(self, SemParemetroConstructordecl):
        code = self.getList()
        code.append("constructor:")
        code.append("    move $fp, $sp")
        st.beginScope('constructor')
        SemParemetroConstructordecl.body.accept(self)
        st.endScope()

    def visitParametroMethoddecl(self, ParametroMethoddecl):
        code = self.getList()
        code.append(f"{ParametroMethoddecl.type}:")
        code.append("    move $fp, $sp")
        st.beginScope(ParametroMethoddecl.type)
        ParametroMethoddecl.sigparams.accept(self)
        ParametroMethoddecl.body.accept(self)
        st.endScope()

    def visitSemParametroMethoddecl(self, SemParametroMethoddecl):
        code = self.getList()
        code.append(f"{SemParametroMethoddecl.type}:")
        code.append("    move $fp, $sp")
        st.beginScope(SemParametroMethoddecl.type)
        SemParametroMethoddecl.body.accept(self)
        st.endScope()

    def visitSemValorAttrdecl(self, SemValorAttrdecl):
        pass

    def visitComValorAttrdecl(self, ComValorAttrdecl):
        ComValorAttrdecl.exp.accept(self)
    
    def visitconcretoFuncdecl(self, concretoFuncdecl):
        concretoFuncdecl.signature.accept(self)
        concretoFuncdecl.body.accept(self)

        code = self.getList()
        code.append("    move $sp, $fp")  
        code.append("    jr $ra")
        st.endScope()
        
    def visitParametroSignature(self, ParametroSignature):
        st.beginScope(ParametroSignature.type)
        code = self.getList()
        code.append(f"{ParametroSignature.type}:")
        code.append("    move $fp, $sp")
        ParametroSignature.sigparams.accept(self)

    def visitSemParametroSignature(self, SemParametroSignature):
        st.beginScope(SemParametroSignature.type)
        code = self.getList()
        code.append(f"{SemParametroSignature.type}:")
        code.append("    move $fp, $sp")

    def visitUmsigparams(self, umsigparam):
        st.addVar(umsigparam.type, getAssemblyType())

    def visitMaisdeUmsigparams(self, MaisdeUmsigparams):
        st.addVar(MaisdeUmsigparams.type, getAssemblyType())
        MaisdeUmsigparams.sigparams.accept(self)

    def visitconcretoBody(self, concretoBody):
        if concretoBody.stms:
            concretoBody.stms.accept(self)

    def _visitBinaryExp(self, exp1, exp2, mips_instruction):
        code = self.getList()
        exp1.accept(self)
        code.append("    addi $sp, $sp, -4")
        st.addSP(-4)
        code.append("    sw $v0, 0($sp)")
        exp2.accept(self)
        code.append("    lw $t0, 0($sp)")
        code.append("    addi $sp, $sp, 4")
        st.addSP(4)
        
        if mips_instruction in ["div", "rem"]:
            code.append(f"    div $t0, $v0")
            if mips_instruction == "div":
                code.append("    mflo $v0")
            else:
                code.append("    mfhi $v0")
        else:
            code.append(f"    {mips_instruction} $v0, $t0, $v0")

    def visitExpSoma(self, ExpSoma):
        self._visitBinaryExp(ExpSoma.exp1, ExpSoma.exp2, "add")

    def visitExpSubtracao(self, ExpSubtracao):
        self._visitBinaryExp(ExpSubtracao.exp1, ExpSubtracao.exp2, "sub")

    def visitExpMultiplicacao(self, ExpMultiplicacao):
        self._visitBinaryExp(ExpMultiplicacao.exp1, ExpMultiplicacao.exp2, "mul")

    def visitExpDivisao(self, ExpDivisao):
        self._visitBinaryExp(ExpDivisao.exp1, ExpDivisao.exp2, "div")
    
    def visitExpResto(self, ExpResto):
        self._visitBinaryExp(ExpResto.exp1, ExpResto.exp2, "rem")

    def visitExpDecremento(self, ExpDecremento):
        code = self.getList()
        ExpDecremento.exp.accept(self)
        code.append("    sub $v0, $v0, 1")


    def visitExpIncremento(self, ExpIncremento):
        code = self.getList()
        ExpIncremento.exp.accept(self)
        code.append("    add $v0, $v0, 1")

    def visitExpIncrementoPrefixo(self, ExpIncrementoPrefixo):
        self.visitExpIncremento(ExpIncrementoPrefixo)

    def visitExpDecrementoPrefixo(self, ExpDecrementoPrefixo):
        self.visitExpDecremento(ExpDecrementoPrefixo)

    def visitExpPotencia(self, ExpPotencia):
        code = self.getList()
        ExpPotencia.exp1.accept(self)
        code.append("    addi $sp, $sp, -4")
        st.addSP(-4)
        code.append("    sw $v0, 0($sp)")
        ExpPotencia.exp2.accept(self)
        code.append("    lw $t0, 0($sp)")
        code.append("    addi $sp, $sp, 4")
        st.addSP(4) 
        code.append("    move $t1, $v0")
        code.append("    li $v0, 1")  
        rotulo_laco = self.novo_rotulo("pot")
        rotulo_final = self.novo_rotulo("fim_pot")
        code.append(f"{rotulo_laco}:")
        code.append(f"    beq $t1, $zero, {rotulo_final}")
        code.append("    mul $v0, $v0, $t0")
        code.append("    sub $t1, $t1, 1")
        code.append(f"    j {rotulo_laco}")
        code.append(f"{rotulo_final}:")

    def visitExpIgualdadeEstrita(self, ExpIgualdadeEstrita):
        self._visitBinaryExp(ExpIgualdadeEstrita.exp1, ExpIgualdadeEstrita.exp2, "seq")

    def visitExpDiferencaEstrita(self, ExpDiferencaEstrita):
        self._visitBinaryExp(ExpDiferencaEstrita.exp1, ExpDiferencaEstrita.exp2, "sne")

    def visitExpEbit(self, ExpEbit):
        self._visitBinaryExp(ExpEbit.exp1, ExpEbit.exp2, "and")

    def visitExpXorbit(self, ExpXorbit):
        self._visitBinaryExp(ExpXorbit.exp1, ExpXorbit.exp2, "xor")

    def visitExpOUbit(self, ExpOUbit):
        self._visitBinaryExp(ExpOUbit.exp1, ExpOUbit.exp2, "or")

    def visitExpigualdade(self, Expigualdade):
        self._visitBinaryExp(Expigualdade.exp1, Expigualdade.exp2, "seq")

    def visitExpdiferenca(self, Expdiferenca):
        self._visitBinaryExp(Expdiferenca.exp1, Expdiferenca.exp2, "sne")

    def visitExpmaior(self, Expmaior):
        self._visitBinaryExp(Expmaior.exp1, Expmaior.exp2, "sgt")

    def visitExpmenor(self, Expmenor):
        self._visitBinaryExp(Expmenor.exp1, Expmenor.exp2, "slt")

    def visitExpmaiorigual(self, Expmaiorigual):
        self._visitBinaryExp(Expmaiorigual.exp1, Expmaiorigual.exp2, "sge")

    def visitExpmenorigual(self, Expmenorigual):
        self._visitBinaryExp(Expmenorigual.exp1, Expmenorigual.exp2, "sle")
        
    def visitExpElogico(self, ExpElogico):
        self._visitBinaryExp(ExpElogico.exp1, ExpElogico.exp2, "and")
        
    def visitExpOUlogico(self, ExpOUlogico):
        self._visitBinaryExp(ExpOUlogico.exp1, ExpOUlogico.exp2, "or")
        
    def visitExpNegacao(self, ExpNegacao):
        code = self.getList()
        ExpNegacao.exp.accept(self)
        code.append("    seq $v0, $v0, 0") 
        
    def visitExpNegacaoBit(self, ExpNegacaoBit):
        code = self.getList()
        ExpNegacaoBit.exp.accept(self)
        code.append("    not $v0, $v0")
        
    def visitExpParenteses(self, ExpParenteses):
        ExpParenteses.exp.accept(self)
        
    def visitExpPositivo(self, ExpPositivo):
        ExpPositivo.exp.accept(self) 
        
    def visitExpNegativo(self, ExpNegativo):
        code = self.getList()
        ExpNegativo.exp.accept(self)
        code.append("    neg $v0, $v0")
        
    def visitExpTernario(self, ExpTernario):
        code = self.getList()
        rotulo_falso = self.novo_rotulo("ternario_falso")
        rotulo_fim = self.novo_rotulo("ternario_fim")
        ExpTernario.exp1.accept(self)
        code.append(f"    beq $v0, $zero, {rotulo_falso}")
        ExpTernario.exp2.accept(self)
        code.append(f"    j {rotulo_fim}")
        code.append(f"{rotulo_falso}:")
        ExpTernario.exp3.accept(self)
        code.append(f"{rotulo_fim}:")
        
    def visitExpMaisIgual(self, ExpMaisIgual):
        self.visitExpSoma(ExpMaisIgual)
        
    def visitExpMenosIgual(self, ExpMenosIgual):
        self.visitExpSubtracao(ExpMenosIgual)
        
    def visitExpMultiplicacaoIgual(self, ExpMultiplicacaoIgual):
        self.visitExpMultiplicacao(ExpMultiplicacaoIgual)
        
    def visitExpPotenciaIgual(self, ExpPotenciaIgual):
        self.visitExpPotencia(ExpPotenciaIgual)
        
    def visitExpDivisaoIgual(self, ExpDivisaoIgual):
        self.visitExpDivisao(ExpDivisaoIgual)
        
    def visitExpRestoIgual(self, ExpRestoIgual):
        self.visitExpResto(ExpRestoIgual)
        
    def visitExpDeslocamentoEsquerdaIgual(self, ExpDeslocamentoEsquerdaIgual):
        self._visitBinaryExp(ExpDeslocamentoEsquerdaIgual.exp1, ExpDeslocamentoEsquerdaIgual.exp2, "sllv")
        
    def visitExpDeslocamentoDireitaIgual(self, ExpDeslocamentoDireitaIgual):
        self._visitBinaryExp(ExpDeslocamentoDireitaIgual.exp1, ExpDeslocamentoDireitaIgual.exp2, "srav")
        
    def visitExpDeslocamentoDireitaSemSinalIgual(self, ExpDeslocamentoDireitaSemSinalIgual):
        self._visitBinaryExp(ExpDeslocamentoDireitaSemSinalIgual.exp1, ExpDeslocamentoDireitaSemSinalIgual.exp2, "srlv")
        
    def visitExpEbitIgual(self, ExpEbitIgual):
        self._visitBinaryExp(ExpEbitIgual.exp1, ExpEbitIgual.exp2, "and")
        
    def visitExpXorbitIgual(self, ExpXorbitIgual):
        self._visitBinaryExp(ExpXorbitIgual.exp1, ExpXorbitIgual.exp2, "xor")
        
    def visitExpOUbitIgual(self, ExpOUbitIgual):
        self._visitBinaryExp(ExpOUbitIgual.exp1, ExpOUbitIgual.exp2, "or")
        
    def visitExpNewSemParametro(self, ExpNewSemParametro):
        pass
        
    def visitExpNewComParametro(self, ExpNewComParametro):
        ExpNewComParametro.params.accept(self)
        
    def visitExpAcessoAtributo(self, ExpAcessoAtributo):
        pass

    def visitExpAcessoMetodo(self, ExpAcessoMetodo):
        pass
    
    def visitExpThis(self, ExpThis):
        code = self.getList()
        code.append("    move $v0, $a0")
        
    def visitExpNum(self, ExpNum):
        code = self.getList() 
        code.append(f"    li $v0, {ExpNum.num}")

    def visitExpId(self, ExpId):
        code = self.getList() 
        bind = st.getBindable(ExpId.id)
        if bind != None:
            if st.getScope(ExpId.id) == 'global_scope':
                code.append(f"    lw $v0, {ExpId.id}($zero)")
            else:
                code.append(f"    lw $v0, {bind[st.OFFSET]}($fp)")

    def visitExpCall(self, ExpCall):
        ExpCall.call.accept(self)
    
    def visitExpAssign(self, ExpAssign):
        ExpAssign.assign.accept(self)

    def visitExpTrue(self, ExpTrue):
        self.getList().append(f"    li $v0, 1")

    def visitExpFalse(self, ExpFalse):
        self.getList().append(f"    li $v0, 0")

    def visitExpStringAD(self, ExpStringAD):  
        pass

    def visitExpStringA(self, ExpStringA):
        pass
    
    def visitLetSemValorVardecl(self, LetSemValorVardecl):
        st.addVar(LetSemValorVardecl.type, getAssemblyType())

    def visitVarSemValorVardecl(self, VarSemValorVardecl):
        st.addVar(VarSemValorVardecl.type, getAssemblyType())

    def visitConstSemValorVardecl(self, ConstSemValorVardecl):
        st.addVar(ConstSemValorVardecl.type, getAssemblyType())

    def visitLetComValorVardecl(self, LetComValorVardecl):
        LetComValorVardecl.exp.accept(self)
        st.addVar(LetComValorVardecl.type, getAssemblyType())
        bind = st.getBindable(LetComValorVardecl.type)
        self.getList().append(f"    sw $v0, {bind[st.OFFSET]}($fp)")

    def visitVarComValorVardecl(self, VarComValorVardecl):
        VarComValorVardecl.exp.accept(self)
        st.addVar(VarComValorVardecl.type, getAssemblyType())
        bind = st.getBindable(VarComValorVardecl.type)
        self.getList().append(f"    sw $v0, {bind[st.OFFSET]}($fp)")

    def visitConstComValorVardecl(self, ConstComValorVardecl):
        ConstComValorVardecl.exp.accept(self)
        st.addVar(ConstComValorVardecl.type, getAssemblyType())
        bind = st.getBindable(ConstComValorVardecl.type)
        self.getList().append(f"    sw $v0, {bind[st.OFFSET]}($fp)")

    def visitUmstms(self, Umstms):
        Umstms.stm.accept(self)

    def visitMaisdeUmstms(self, MaisdeUmstms):
        MaisdeUmstms.stm.accept(self)
        MaisdeUmstms.stms.accept(self)

    def visitForStm(self, ForStm):
        code = self.getList()
        rotulo_inicial = self.novo_rotulo("for_inicio")
        rotulo_final = self.novo_rotulo("for_fim")
        
        ForStm.exp1.accept(self)
        code.append(f"{rotulo_inicial}:")
        ForStm.exp2.accept(self)
        code.append(f"    beq $v0, $zero, {rotulo_final}")
        ForStm.body.accept(self)
        ForStm.exp3.accept(self)
        code.append(f"    j {rotulo_inicial}")
        code.append(f"{rotulo_final}:")

    def visitAssignStm(self, AssignStm):
        AssignStm.assign.accept(self)

    def visitVardeclStm(self, VardeclStm):
        VardeclStm.vardecl.accept(self)
    
    def visitExpStm(self, ExpStm):
        ExpStm.exp.accept(self)

    def visitReturnStm(self, ReturnStm):
        code = self.getList()
        ReturnStm.exp.accept(self)
        code.append("    move $sp, $fp")  
        code.append("    jr $ra")

    def visitWhileStm(self, WhileStm):
        code = self.getList()
        rotulo_inicial = self.novo_rotulo("whilestm")
        rotulo_final = self.novo_rotulo("fim_whilestm")      
        code.append(f"{rotulo_inicial}:")
        WhileStm.exp.accept(self)
        code.append(f"    beq $v0, $zero, {rotulo_final}")
        WhileStm.body.accept(self)
        code.append(f"    j {rotulo_inicial}")
        code.append(f"{rotulo_final}:")

    def visitIfStm(self, IfStm):
        code = self.getList()
        rotulo_final = self.novo_rotulo("if_fim")
        IfStm.exp.accept(self)
        code.append(f"    beq $v0, $zero, {rotulo_final}")
        IfStm.body.accept(self)
        code.append(f"{rotulo_final}:")

    def visitIfElseStm(self, IfElseStm):
        code = self.getList()
        rotulo_else = self.novo_rotulo("ifelse_else")
        rotulo_final = self.novo_rotulo("ifelse_fim")
        IfElseStm.exp.accept(self)
        code.append(f"    beq $v0, $zero, {rotulo_else}")
        IfElseStm.body1.accept(self)
        code.append(f"    j {rotulo_final}")
        code.append(f"{rotulo_else}:")
        IfElseStm.body2.accept(self)
        code.append(f"{rotulo_final}:")

    def visitAtribuicaoSimples(self, AtribuicaoSimples):
        code = self.getList()
        AtribuicaoSimples.exp.accept(self)
        bind = st.getBindable(AtribuicaoSimples.type)
        if bind == None:
            st.addVar(AtribuicaoSimples.type, getAssemblyType())
            bind = st.getBindable(AtribuicaoSimples.type)

        if st.getScope(AtribuicaoSimples.type) == 'global_scope':
            code.append(f"    sw $v0, {AtribuicaoSimples.type}($zero)")
        else:
            code.append(f"    sw $v0, {bind[st.OFFSET]}($fp)")

    def visitAtribuicaoAtributo(self, AtribuicaoAtributo):
        AtribuicaoAtributo.exp1.accept(self)
        AtribuicaoAtributo.exp2.accept(self)

    def visitCallSemParametro(self, CallSemParametro):
        code = self.getList()
        code.append("    addi $sp, $sp, -8")
        st.addSP(-8)
        oldSP = st.getSP()
        code.append("    sw $ra, 0($sp)")
        code.append("    sw $fp, 4($sp)")
        
        code.append(f"    jal {CallSemParametro.type}")
        
        code.append("    lw $fp, 4($sp)")
        code.append("    lw $ra, 0($sp)")
        code.append("    addi $sp, $sp, 8")
        st.addSP(oldSP - st.getSP())
        st.addSP(8)

    def visitCallComParametro(self, CallComParametro):
        code = self.getList()
        code.append("    addi $sp, $sp, -8")
        st.addSP(-8)
        oldSP = st.getSP()
        code.append("    sw $ra, 0($sp)")
        code.append("    sw $fp, 4($sp)")
        
        CallComParametro.params.accept(self)
        code.append(f"    jal {CallComParametro.type}")
        
        code.append("    lw $fp, 4($sp)")
        code.append("    lw $ra, 0($sp)")
        code.append("    addi $sp, $sp, 8")
        st.addSP(oldSP - st.getSP())
        st.addSP(8)

    def visitCallAtributoSemParametro(self, CallAtributoSemParametro):
        pass

    def visitCallAtributoComParametro(self, CallAtributoComParametro):
        pass

    def visitUmparams(self, Umparams):
        code = self.getList()
        Umparams.exp.accept(self)
        code.append("    addi $sp, $sp, -4")
        st.addSP(-4)
        code.append(f"    sw $v0, {st.getSP()}($fp)")

    def visitMaisdeUmparams(self, MaisdeUmparams):
        code = self.getList()
        MaisdeUmparams.exp.accept(self)
        code.append("    addi $sp, $sp, -4")
        st.addSP(-4)
        code.append(f"    sw $v0, {st.getSP()}($fp)")
        MaisdeUmparams.params.accept(self)

    def get_code(self):
        finalcode = []
        if self.data:
            for globalVar in self.data:
                finalcode.insert(0, f"    {globalVar[0]}: {globalVar[1]} 0")
            finalcode.insert(0, ".data")
        finalcode = finalcode + self.text
        finalcode.append("    j end")
        finalcode = finalcode + self.funcs
        finalcode.append("\nend:\n    li $v0, 10\n    syscall")
        return "\n".join(finalcode)
    
def main():
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
    print("#Gera Assembly")
    assemblyvisitor = AssemblyVisitor()
    result.accept(assemblyvisitor)
    print(assemblyvisitor.get_code())
    
if __name__ == "__main__":
    main()