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
        MaisdeUmfuncdecl.funcdecl.accept(self)
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
        print(ParametroMethoddecl.type,"( ", end='', sep='')
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
        