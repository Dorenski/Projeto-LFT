from abc import abstractmethod
from abc import ABCMeta

#================== program =========================

class Program(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Umfuncdecl(Program):
    def __init__(self, funcdecl):
        self.funcdecl = funcdecl
    def accept(self, visitor): 
        return visitor.visitUmfuncdecl(self)

class MaisdeUmfuncdecl(Program):
    def __init__(self, funcDecl, program):
        self.funcDecl = funcDecl
        self.program = program
    def accept(self, visitor): 
        return visitor.visitMaisdeUmfuncdecl(self)
    
class Umvardecl(Program):
    def __init__(self, vardecl):
        self.vardecl = vardecl
    def accept(self, visitor): 
        return visitor.visitUmvardecl(self)

class MaisdeUmvardecl(Program):
    def __init__(self, vardecl, program):
        self.vardecl = vardecl
        self.program = program
    def accept(self, visitor): 
        return visitor.visitMaisdeUmvardecl(self)

class Umclassdecl(Program):
    def __init__(self, classdecl):
        self.classdecl = classdecl
    def accept(self, visitor): 
        return visitor.visitUmclassdecl(self)

class MaisdeUmclassdecl(Program):
    def __init__(self, classdecl, program):
        self.classdecl = classdecl
        self.program = program
    def accept(self, visitor): 
        return visitor.visitMaisdeUmclassdecl(self)
    
#================== classdecl =========================

class Classdecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class concretoClassdecl(Classdecl):
    def __init__(self, type, classbody):
        self.type = type
        self.classbody = classbody
    def accept(self, visitor): 
        return visitor.visitconcretoClassdecl(self)

#================== classbody =========================

class Classbody(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class concretoClassbody(Classbody):
    def __init__(self, classmembers):
        self.classmembers = classmembers
    def accept(self, visitor): 
        return visitor.visitconcretoClassbody(self)
    
#================== classmembers =========================

class Classmembers(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Umclassmember(Classmembers):
    def __init__(self, classmember):
        self.classmember = classmember
    def accept(self, visitor): 
        return visitor.visitUmclassmember(self)

class MaisdeUmclassmember(Classmembers):
    def __init__(self, classmember, classmembers):
        self.classmember = classmember
        self.classmembers = classmembers
    def accept(self, visitor): 
        return visitor.visitMaisdeUmclassmember(self)   
    
#================== classmember =========================

class Classmember(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class methodClassmember(Classmember):
    def __init__(self, methoddecl):
        self.methoddecl = methoddecl
    def accept(self, visitor): 
        return visitor.visitmethodClassmember(self)
    
class constructorClassmember(Classmember):
    def __init__(self, constructordecl):
        self.constructordecl = constructordecl
    def accept(self, visitor): 
        return visitor.visitconstructorClassmember(self)
    
class attrClassmember(Classmember):
    def __init__(self, attrdecl):
        self.attrdecl = attrdecl
    def accept(self, visitor): 
        return visitor.visitattrClassmember(self)
    
#================== constructordecl =========================

class Constructordecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ParametroConstrutordecl(Constructordecl):
    def __init__(self, sigparams, body):
        self.sigparams = sigparams
        self.body = body
    def accept(self, visitor): 
        return visitor.visitParametroConstrutordecl(self)

class SemParametroConstrutordecl(Constructordecl):
    def __init__(self, body):
        self.body = body
    def accept(self, visitor): 
        return visitor.visitSemParametroConstrutordecl(self)

#================== methoddecl =========================

class Methoddecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ParametroMethoddecl(Methoddecl):
    def __init__(self, type, sigparams, body):
        self.type = type
        self.sigparams = sigparams
        self.body = body
    def accept(self, visitor): 
        return visitor.visitParametroMethoddecl(self)
    
class SemParametroMethoddecl(Methoddecl):
    def __init__(self, type, body):
        self.type = type
        self.body = body
    def accept(self, visitor): 
        return visitor.visitSemParametroMethoddecl(self)
    
#================== attrdecl =========================

class Attrdecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SemValorAttrdecl(Attrdecl):
    def __init__(self, type):
        self.type = type
    def accept(self, visitor): 
        return visitor.visitSimplesAttrdecl(self)
    
class ComValorAttrdecl(Attrdecl):
    def __init__(self, type, exp):
        self.type = type
        self.exp = exp
    def accept(self, visitor): 
        return visitor.visitComValorAttrdecl(self)

#================== funcdecl =========================

class Funcdecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class concretoFuncdecl(Funcdecl):
    def __init__(self, signature, body):
        self.signature = signature
        self.body = body
    def accept(self, visitor): 
        return visitor.visitconcretoFuncdecl(self)

#================== signature =========================

class Signature(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ParametroSignature(Signature):
    def __init__(self, type, sigparams):
        self.type = type
        self.sigparams = sigparams
    def accept(self, visitor): 
        return visitor.visitParametroSignature(self)

class SemParametroSignature(Signature):
    def __init__(self, type):
        self.type = type
    def accept(self, visitor): 
        return visitor.visitSemParametroSignature(self)
    
#================== body =========================

class Body(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class concretoBody(Body):
    def __init__(self, stms):
        self.stms = stms
    def accept(self, visitor): 
        return visitor.visitconcretoBody(self)
    
#================== exp =========================

class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpSoma(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpSoma(self)
    
class ExpSubtracao(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpSubtracao(self)
    
class ExpMultiplicacao(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpMultiplicacao(self)

class ExpDivisao(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpDivisao(self)

class ExpResto(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpResto(self)
    
class ExpDecremento(Exp):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor): 
        return visitor.visitExpDecremento(self)
    
class ExpIncremento(Exp):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor): 
        return visitor.visitExpIncremento(self)

class ExpIncrementoPrefixo(Exp):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor): 
        return visitor.visitExpIncrementoPrefixo(self)

class ExpDecrementoPrefixo(Exp):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor): 
        return visitor.visitExpDecrementoPrefixo(self)
    
class ExpPotencia(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpPotencia(self)

class ExpIgualdadeEstrita(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpIgualdade(self)
    
class ExpDiferencaEstrita(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpDiferenca(self)
    
class ExpEbit(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpEbitabit(self)

class ExpXorbit(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpXorbit(self)

class ExpOUbit(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpOUbit(self)
    
class Expigualdade(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExigualdade(self)
    
class Expdiferenca(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpdiferenca(self)

class Expmaior(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpmaior(self)
    
class Expmenor(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpmenor(self)

class Expmaiorigual(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpmaiorigual(self)

class Expmenorigual(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpmenorigual(self)

class ExpElogico(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpElogico(self)

class ExpOUlogico(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpOUlogico(self)

class ExpNegacao(Exp):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor): 
        return visitor.visitExpNegacao(self)
    
class ExpNegacaoBit(Exp):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor): 
        return visitor.visitExpNegacaoBit(self)
    
class ExpParenteses(Exp):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor): 
        return visitor.visitExpParenteses(self)
    
class ExpPositivo(Exp):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor): 
        return visitor.visitExpPositivo(self)
    
class ExpNegativo(Exp):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor): 
        return visitor.visitExpNegativo(self)
    
class ExpTernario(Exp):
    def __init__(self, exp1, exp2, exp3):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
    def accept(self, visitor): 
        return visitor.visitExpTernario(self)
    
class ExpMaisIgual(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpMaisIgual(self)
    
class ExpMenosIgual(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpMenosIgual(self)

class ExpMultiplicacaoIgual(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpMultiplicacaoIgual(self)
    
class ExpPotenciaIgual(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpPotenciaIgual(self)
    
class ExpDivisaoIgual(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpDivisaoIgual(self)
    
class ExpRestoIgual(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpRestoIgual(self)
    
class ExpDeslocamentoEsquerdaIgual(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpDeslocamentoEsquerdaIgual(self)
    
class ExpDeslocamentoDireitaIgual(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpDeslocamentoDireitaIgual(self)
    
class ExpDeslocamentoDireitaSemSinalIgual(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpDeslocamentoDireitaSemSinalIgual(self)
    
class ExpEbitIgual(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpEbitIgual(self)
    
class ExpXorbitIgual(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpXorbitIgual(self)
    
class ExpOUbitIgual(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitExpOUbitIgual(self)

class ExpNewSemParametro(Exp):
    def __init__(self, type):
        self.type = type
    def accept(self, visitor): 
        return visitor.visitExpNewSemParametro(self)
    
class ExpNewComParametro(Exp):
    def __init__(self, type, params):
        self.type = type
        self.params = params
    def accept(self, visitor): 
        return visitor.visitExpNewComParametro(self)
    
class ExpAcessoAtributo(Exp):
    def __init__(self, exp, type):
        self.exp = exp
        self.type = type
    def accept(self, visitor): 
        return visitor.visitExpAcessoAtributo(self)

class ExpAcessoMetodo(Exp):
    def __init__(self, exp, type, params):
        self.exp = exp
        self.type = type
        self.call = params
    def accept(self, visitor): 
        return visitor.visitExpAcessoMetodo(self)

class ExpThis(Exp):
    def accept(self, visitor): 
        return visitor.visitExpThis(self)
    
class ExpNum(Exp):
    def __init__(self, num):
        self.num = num
    def accept(self, visitor): 
        return visitor.visitExpNum(self)
    
class ExpId(Exp):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor): 
        return visitor.visitExpId(self)
    
class ExpCall(Exp):
    def __init__(self, call):
        self.call = call
    def accept(self, visitor): 
        return visitor.visitExpCall(self)

class ExpAssign(Exp):
    def __init__(self, assign):
        self.assign = assign
    def accept(self, visitor): 
        return visitor.visitExpAssign(self)
    
class ExpTrue(Exp):
    def accept(self, visitor): 
        return visitor.visitExpTrue(self)
    
class ExpFalse(Exp):
    def accept(self, visitor): 
        return visitor.visitExpFalse(self)
    
class ExpStringAD(Exp):
    def accept(self, visitor): 
        return visitor.visitExpStringAD(self)

class ExpStringA(Exp):
    def accept(self, visitor): 
        return visitor.visitExpStringA(self)

#================== vardecl =========================

class Vardecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class LetSemValorVardecl(Vardecl):
    def __init__(self, type):
        self.type = type
    def accept(self, visitor): 
        return visitor.visitLetSemValorVardecl(self)

class VarSemValorVardecl(Vardecl):
    def __init__(self, type):
        self.type = type
    def accept(self, visitor): 
        return visitor.visitVarSemValorVardecl(self)
    
class ConstSemValorVardecl(Vardecl):
    def __init__(self, type):
        self.type = type
    def accept(self, visitor): 
        return visitor.visitConstSemValorVardecl(self)

class LetComValorVardecl(Vardecl):
    def __init__(self, type, exp):
        self.type = type
        self.exp = exp
    def accept(self, visitor): 
        return visitor.visitLetComValorVardecl(self)
    
class VarComValorVardecl(Vardecl):
    def __init__(self, type, exp):
        self.type = type
        self.exp = exp
    def accept(self, visitor): 
        return visitor.visitVarComValorVardecl(self)
    
class ConstComValorVardecl(Vardecl):
    def __init__(self, type, exp):
        self.type = type
        self.exp = exp
    def accept(self, visitor): 
        return visitor.visitConstComValorVardecl(self)
    
#================== stms =========================

class Stms(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass    

class Umstm(Stms):
    def __init__(self, stm):
        self.stm = stm
    def accept(self, visitor): 
        return visitor.visitUmstm(self)
    
class MaisdeUmstm(Stms):
    def __init__(self, stm, stms):
        self.stm = stm
        self.stms = stms
    def accept(self, visitor): 
        return visitor.visitMaisdeUmstm(self)
    
#================== stm =========================

class Stm(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ForStm(Stm):
    def __init__(self, exp1, exp2, exp3, body):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.body = body
    def accept(self, visitor): 
        return visitor.visitForStm(self)
    
class AssignStm(Stm):
    def __init__(self, assign):
        self.assign = assign
    def accept(self, visitor): 
        return visitor.visitAssignStm(self)
    
class VardeclStm(Stm):
    def __init__(self, vardecl):
        self.vardecl = vardecl
    def accept(self, visitor): 
        return visitor.visitVardeclStm(self)    
    
class ExpStm(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor): 
        return visitor.visitExpStm(self)
    
class ReturnStm(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor): 
        return visitor.visitReturnStm(self)

class WhileStm(Stm):
    def __init__(self, exp, body):
        self.exp = exp
        self.body = body
    def accept(self, visitor): 
        return visitor.visitWhileStm(self)
    
class IfStm(Stm):
    def __init__(self, exp, body):
        self.exp = exp
        self.body = body
    def accept(self, visitor): 
        return visitor.visitIfStm(self)
    
class IfElseStm(Stm):
    def __init__(self, exp, body1, body2):
        self.exp = exp
        self.body1 = body1
        self.body2 = body2
    def accept(self, visitor): 
        return visitor.visitIfElseStm(self)

#================== assign =========================

class Assign(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class AtribuicaoSimples(Assign):
    def __init__(self, type, exp):
        self.type = type
        self.exp = exp
    def accept(self, visitor): 
        return visitor.visitAtribuicaoSimples(self)
    
class AtribuicaoAtributo(Assign):
    def __init__(self, exp1, type, exp2):
        self.exp1 = exp1
        self.type = type
        self.exp2 = exp2
    def accept(self, visitor): 
        return visitor.visitAtribuicaoAtributo(self)
    
#================== call =========================

class Call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallSemParametro(Call):
    def __init__(self, type):
        self.type = type
    def accept(self, visitor): 
        return visitor.visitCallSemParametro(self)
    
class CallComParametro(Call):
    def __init__(self, type, params):
        self.type = type
        self.params = params
    def accept(self, visitor): 
        return visitor.visitCallComParametro(self)

class CallAtributoSemParametro(Call):
    def __init__(self, exp, type):
        self.exp = exp
        self.type = type
    def accept(self, visitor): 
        return visitor.visitCallAtributoSemParametro(self)
    
class CallAtributoComParametro(Call):
    def __init__(self, exp, type, params):
        self.exp = exp
        self.type = type
        self.params = params
    def accept(self, visitor): 
        return visitor.visitCallAtributoComParametro(self)
    
#================== params =========================

class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Umparam(Params):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor): 
        return visitor.visitUmparam(self)

class MaisdeUmparam(Params):
    def __init__(self, exp, params):
        self.exp = exp
        self.params = params
    def accept(self, visitor): 
        return visitor.visitMaisdeUmparam(self)