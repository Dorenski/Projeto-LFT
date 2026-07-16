from abc import abstractmethod, ABCMeta

# Padrão =============================================
@abstractmethod
def visit(self, ): pass

class AbstractVisitor(metaclass=ABCMeta):

# ================== program =========================  
    @abstractmethod
    def visitUmfuncdecl(self, Umfuncdecl): pass

    @abstractmethod
    def visitMaisdeUmfuncdecl(self, MaisdeUmfuncdecl): pass

    @abstractmethod
    def visitUmvardecl(self, Umvardecl): pass

    @abstractmethod
    def visitMaisdeUmvardecl(self, MaisdeUmvardecl): pass
    
    @abstractmethod
    def visitUmclassdecl(self, Umclassdecl): pass

    @abstractmethod
    def visitMaisdeUmclassdecl(self, MaisdeUmclassdecl): pass

# ================== classdecl =========================

    @abstractmethod
    def visitconcretoClassdecl(self, concretoClassdecl): pass

# ================== classbody =========================

    @abstractmethod
    def visitconcretoClassbody(self, concretoClassbody): pass

# ================== classmembers =========================

    @abstractmethod
    def visitUmclassmember(self, Umclassmember): pass

    @abstractmethod
    def visitMaisdeUmclassmember(self, MaisdeUmclassmember): pass

# ================== classmember =========================

    @abstractmethod
    def visitmethodClassmember(self, methodClassmember): pass

    @abstractmethod
    def visitconstructorClassmember(self, constructorClassmember): pass

    @abstractmethod
    def visitattrClassmember(self, attrClassmember): pass

# ================== constructordecl =========================

    @abstractmethod
    def visitParametroConstructordecl(self, ParametroConstructordecl): pass

    @abstractmethod
    def visitSemParametroConstructordecl(self, SemParemetroConstructordecl): pass

# ================== methoddecl =========================

    @abstractmethod
    def visitParametroMethoddecl(self, ParametroMethoddecl): pass

    @abstractmethod
    def visitSemParametroMethoddecl(self, SemParametroMethoddecl): pass

# ================== attrdecl =========================

    @abstractmethod
    def visitSemValorAttrdecl(self, SemValorAttrdecl): pass

    @abstractmethod
    def visitComValorAttrdecl(self, ComValorAttrdecl): pass

# ================== funcdecl =========================

    @abstractmethod
    def visitconcretoFuncdecl(self, concretoFuncdecl): pass

# ================== signature =========================

    @abstractmethod
    def visitParametroSignature(self, ParametroSignature): pass

    @abstractmethod
    def visitSemParametroSignature(self, SemParametroSignature): pass

# ================== sigparams =========================

    @abstractmethod
    def visitUmsigparams(self, Umsigparams): pass

    @abstractmethod
    def visitMaisdeUmsigparams(self, MaisdeUmsigparams): pass

# ================== body =========================

    @abstractmethod
    def visitconcretoBody(self, concretoBody): pass

# ================== exp =========================

    @abstractmethod
    def visitExpSoma(self, ExpSoma): pass

    @abstractmethod
    def visitExpSubtracao(self, ExpSubtracao): pass

    @abstractmethod
    def visitExpMultiplicacao(self, ExpMultiplicacao): pass

    @abstractmethod
    def visitExpDivisao(self, ExpDivisao): pass

    @abstractmethod
    def visitExpResto(self, ExpResto): pass

    @abstractmethod
    def visitExpDecremento(self, ExpDecremento): pass

    @abstractmethod
    def visitExpIncremento(self, ExpIncremento): pass

    @abstractmethod
    def visitExpIncrementoPrefixo(self, ExpIncrementoPrefixo): pass

    @abstractmethod
    def visitExpDecrementoPrefixo(self, ExpDecrementoPrefixo): pass

    @abstractmethod
    def visitExpPotencia(self, ExpPotencia): pass

    @abstractmethod
    def visitExpIgualdadeEstrita(self, ExpIgualdadeEstrita): pass

    @abstractmethod
    def visitExpDiferencaEstrita(self, ExpDiferencaEstrita): pass

    @abstractmethod
    def visitExpEbit(self, ExpEbit): pass

    @abstractmethod
    def visitExpXorbit(self, ExpXorbit): pass

    @abstractmethod
    def visitExpOUbit(self, ExpOUbit): pass

    @abstractmethod
    def visitExpigualdade(self, Expigualdade): pass

    @abstractmethod
    def visitExpdiferenca(self, Expdiferenca): pass

    @abstractmethod
    def visitExpmaior(self, Expmaior): pass

    @abstractmethod
    def visitExpmenor(self, Expmenor): pass

    @abstractmethod
    def visitExpmaiorigual(self, Expmaiorigual): pass

    @abstractmethod
    def visitExpmenorigual(self, Expmenorigual): pass

    @abstractmethod
    def visitExpElogico(self, ExpElogico): pass

    @abstractmethod
    def visitExpOUlogico(self, ExpOUlogico): pass

    @abstractmethod
    def visitExpNegacao(self, ExpNegacao): pass

    @abstractmethod
    def visitExpNegacaoBit(self, ExpNegacaoBit): pass

    @abstractmethod
    def visitExpParenteses(self, ExpParenteses): pass

    @abstractmethod
    def visitExpPositivo(self, ExpPositivo): pass

    @abstractmethod
    def visitExpNegativo(self, ExpNegativo): pass

    @abstractmethod
    def visitExpTernario(self, ExpTernario): pass

    @abstractmethod
    def visitExpMaisIgual(self, ExpMaisIgual): pass

    @abstractmethod
    def visitExpMenosIgual(self, ExpMenosIgual): pass

    @abstractmethod
    def visitExpMultiplicacaoIgual(self, ExpMultiplicacaoIgual): pass

    @abstractmethod
    def visitExpPotenciaIgual(self, ExpPotenciaIgual): pass

    @abstractmethod
    def visitExpDivisaoIgual(self, ExpDivisaoIgual): pass

    @abstractmethod
    def visitExpRestoIgual(self, ExpRestoIgual): pass

    @abstractmethod
    def visitExpDeslocamentoEsquerdaIgual(self, ExpDeslocamentoEsquerdaIgual): pass

    @abstractmethod
    def visitExpDeslocamentoDireitaIgual(self, ExpDeslocamentoDireitaIgual): pass

    @abstractmethod
    def visitExpDeslocamentoDireitaSemSinalIgual(self, ExpDeslocamentoDireitaSemSinalIgual): pass

    @abstractmethod
    def visitExpEbitIgual(self, ExpEbitIgual): pass

    @abstractmethod
    def visitExpXorbitIgual(self, ExpXorbitIgual): pass

    @abstractmethod
    def visitExpOUbitIgual(self, ExpOUbitIgual): pass

    @abstractmethod
    def visitExpNewSemParametro(self, ExpNewSemParametro): pass

    @abstractmethod
    def visitExpNewComParametro(self, ExpNewComParametro): pass

    @abstractmethod
    def visitExpAcessoAtributo(self, ExpAcessoAtributo): pass

    @abstractmethod
    def visitExpAcessoMetodo(self, ExpAcessoMetodo): pass

    @abstractmethod
    def visitExpThis(self, ExpThis): pass

    @abstractmethod
    def visitExpNum(self, ExpNum): pass

    @abstractmethod
    def visitExpId(self, ExpId): pass

    @abstractmethod
    def visitExpCall(self, ExpCall): pass

    @abstractmethod
    def visitExpAssign(self, ExpAssign): pass

    @abstractmethod
    def visitExpTrue(self, ExpTrue): pass

    @abstractmethod
    def visitExpFalse(self, ExpFalse): pass

    @abstractmethod
    def visitExpStringAD(self, ExpStringAD): pass

    @abstractmethod
    def visitExpStringA(self, ExpStringA): pass

# ================== vardecl =========================

    @abstractmethod
    def visitLetSemValorVardecl(self, LetSemValorVardecl): pass

    @abstractmethod
    def visitVarSemValorVardecl(self, VarSemValorVardecl): pass

    @abstractmethod
    def visitConstSemValorVardecl(self, ConstSemValorVardecl): pass

    @abstractmethod
    def visitLetComValorVardecl(self, LetComValorVardecl): pass

    @abstractmethod
    def visitVarComValorVardecl(self, VarComValorVardecl): pass

    @abstractmethod
    def visitConstComValorVardecl(self, ConstComValorVardecl): pass

# ================== stms =========================

    @abstractmethod
    def visitUmstms(self, Umstms): pass

    @abstractmethod
    def visitMaisdeUmstms(self, MaisdeUmstms): pass

# ================== stm =========================

    @abstractmethod
    def visitForStm(self, ForStm): pass

    @abstractmethod
    def visitAssignStm(self, AssignStm): pass

    @abstractmethod
    def visitVardeclStm(self, VardeclStm): pass

    @abstractmethod
    def visitExpStm(self, ExpStm): pass

    @abstractmethod
    def visitReturnStm(self, ReturnStm): pass

    @abstractmethod
    def visitWhileStm(self, WhileStm): pass

    @abstractmethod
    def visitIfStm(self, IfStm): pass

    @abstractmethod
    def visitIfElseStm(self, IfElseStm): pass

# ================== assign =========================

    @abstractmethod
    def visitAtribuicaoSimples(self, AtribuicaoSimples): pass

    @abstractmethod
    def visitAtribuicaoAtributo(self, AtribuicaoAtributo): pass

# ================== call =========================

    @abstractmethod
    def visitCallSemParametro(self, CallSemParametro): pass

    @abstractmethod
    def visitCallComParametro(self, CallComParametro): pass

    @abstractmethod
    def visitCallAtributoSemParametro(self, CallAtributoSemParametro): pass

    @abstractmethod
    def visitCallAtributoComParametro(self, CallAtributoComParametro): pass

# ================== params =========================

    @abstractmethod
    def visitUmparams(self, Umparams): pass

    @abstractmethod
    def visitMaisdeUmparams(self, MaisdeUmparams): pass