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
    def visitCallComParamtro(self, CallComParamtro): pass

    @abstractmethod
    def visitCallAtributoSemParametro(self, CallAtributoSemParametro): pass

    @abstractmethod
    def visitCallAtributoComParametro(self, CallAtributoComParametro): pass

# ================== params =========================

    @abstractmethod
    def visitUmparams(self, Umparams): pass

    @abstractmethod
    def visitMaisdeUmparams(self, MaisdeUmparams): pass