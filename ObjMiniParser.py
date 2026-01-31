# Generated from ObjMini.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,179,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,5,0,38,8,0,10,0,12,0,
        41,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,3,2,53,8,2,1,2,1,
        2,5,2,57,8,2,10,2,12,2,60,9,2,1,2,1,2,1,3,1,3,1,3,3,3,67,8,3,1,4,
        1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,79,8,5,1,5,1,5,1,5,1,6,1,
        6,1,6,1,6,3,6,88,8,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,96,8,7,10,7,12,
        7,99,9,7,1,8,1,8,1,8,1,9,1,9,5,9,106,8,9,10,9,12,9,109,9,9,1,9,1,
        9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,120,8,10,1,11,1,11,1,11,
        1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,3,13,133,8,13,1,13,1,13,
        1,14,1,14,1,14,1,14,1,14,3,14,142,8,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,3,14,152,8,14,1,14,1,14,1,14,1,14,1,14,3,14,159,8,
        14,1,14,5,14,162,8,14,10,14,12,14,165,9,14,1,15,1,15,1,15,5,15,170,
        8,15,10,15,12,15,173,9,15,1,16,1,16,1,17,1,17,1,17,0,1,28,18,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,2,2,0,15,17,20,20,
        1,0,18,19,182,0,39,1,0,0,0,2,45,1,0,0,0,4,48,1,0,0,0,6,66,1,0,0,
        0,8,68,1,0,0,0,10,73,1,0,0,0,12,83,1,0,0,0,14,92,1,0,0,0,16,100,
        1,0,0,0,18,103,1,0,0,0,20,119,1,0,0,0,22,121,1,0,0,0,24,125,1,0,
        0,0,26,130,1,0,0,0,28,151,1,0,0,0,30,166,1,0,0,0,32,174,1,0,0,0,
        34,176,1,0,0,0,36,38,3,4,2,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,
        0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,39,1,0,0,0,42,43,3,2,1,0,43,
        44,5,0,0,1,44,1,1,0,0,0,45,46,5,1,0,0,46,47,3,18,9,0,47,3,1,0,0,
        0,48,49,5,2,0,0,49,52,5,20,0,0,50,51,5,3,0,0,51,53,5,20,0,0,52,50,
        1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,58,5,4,0,0,55,57,3,6,3,0,
        56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,61,1,
        0,0,0,60,58,1,0,0,0,61,62,5,5,0,0,62,5,1,0,0,0,63,67,3,8,4,0,64,
        67,3,10,5,0,65,67,3,12,6,0,66,63,1,0,0,0,66,64,1,0,0,0,66,65,1,0,
        0,0,67,7,1,0,0,0,68,69,3,34,17,0,69,70,3,32,16,0,70,71,5,20,0,0,
        71,72,5,6,0,0,72,9,1,0,0,0,73,74,3,34,17,0,74,75,3,32,16,0,75,76,
        5,20,0,0,76,78,5,7,0,0,77,79,3,14,7,0,78,77,1,0,0,0,78,79,1,0,0,
        0,79,80,1,0,0,0,80,81,5,8,0,0,81,82,3,18,9,0,82,11,1,0,0,0,83,84,
        3,34,17,0,84,85,5,20,0,0,85,87,5,7,0,0,86,88,3,14,7,0,87,86,1,0,
        0,0,87,88,1,0,0,0,88,89,1,0,0,0,89,90,5,8,0,0,90,91,3,18,9,0,91,
        13,1,0,0,0,92,97,3,16,8,0,93,94,5,9,0,0,94,96,3,16,8,0,95,93,1,0,
        0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,15,1,0,0,0,99,97,
        1,0,0,0,100,101,3,32,16,0,101,102,5,20,0,0,102,17,1,0,0,0,103,107,
        5,4,0,0,104,106,3,20,10,0,105,104,1,0,0,0,106,109,1,0,0,0,107,105,
        1,0,0,0,107,108,1,0,0,0,108,110,1,0,0,0,109,107,1,0,0,0,110,111,
        5,5,0,0,111,19,1,0,0,0,112,120,3,22,11,0,113,120,3,24,12,0,114,115,
        3,28,14,0,115,116,5,6,0,0,116,120,1,0,0,0,117,120,3,26,13,0,118,
        120,3,18,9,0,119,112,1,0,0,0,119,113,1,0,0,0,119,114,1,0,0,0,119,
        117,1,0,0,0,119,118,1,0,0,0,120,21,1,0,0,0,121,122,3,32,16,0,122,
        123,5,20,0,0,123,124,5,6,0,0,124,23,1,0,0,0,125,126,5,20,0,0,126,
        127,5,10,0,0,127,128,3,28,14,0,128,129,5,6,0,0,129,25,1,0,0,0,130,
        132,5,11,0,0,131,133,3,28,14,0,132,131,1,0,0,0,132,133,1,0,0,0,133,
        134,1,0,0,0,134,135,5,6,0,0,135,27,1,0,0,0,136,137,6,14,-1,0,137,
        138,5,12,0,0,138,139,5,20,0,0,139,141,5,7,0,0,140,142,3,30,15,0,
        141,140,1,0,0,0,141,142,1,0,0,0,142,143,1,0,0,0,143,152,5,8,0,0,
        144,152,5,13,0,0,145,152,5,20,0,0,146,152,5,21,0,0,147,148,5,7,0,
        0,148,149,3,28,14,0,149,150,5,8,0,0,150,152,1,0,0,0,151,136,1,0,
        0,0,151,144,1,0,0,0,151,145,1,0,0,0,151,146,1,0,0,0,151,147,1,0,
        0,0,152,163,1,0,0,0,153,154,10,2,0,0,154,155,5,14,0,0,155,156,5,
        20,0,0,156,158,5,7,0,0,157,159,3,30,15,0,158,157,1,0,0,0,158,159,
        1,0,0,0,159,160,1,0,0,0,160,162,5,8,0,0,161,153,1,0,0,0,162,165,
        1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,29,1,0,0,0,165,163,1,
        0,0,0,166,171,3,28,14,0,167,168,5,9,0,0,168,170,3,28,14,0,169,167,
        1,0,0,0,170,173,1,0,0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,31,1,
        0,0,0,173,171,1,0,0,0,174,175,7,0,0,0,175,33,1,0,0,0,176,177,7,1,
        0,0,177,35,1,0,0,0,15,39,52,58,66,78,87,97,107,119,132,141,151,158,
        163,171
    ]

class ObjMiniParser ( Parser ):

    grammarFileName = "ObjMini.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'class'", "'extends'", "'{'", 
                     "'}'", "';'", "'('", "')'", "','", "'='", "'return'", 
                     "'new'", "'this'", "'.'", "'int'", "'bool'", "'void'", 
                     "'public'", "'private'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_mainBlock = 1
    RULE_classDecl = 2
    RULE_member = 3
    RULE_fieldDecl = 4
    RULE_methodDecl = 5
    RULE_constructorDecl = 6
    RULE_paramList = 7
    RULE_param = 8
    RULE_block = 9
    RULE_statement = 10
    RULE_varDecl = 11
    RULE_assignment = 12
    RULE_returnStmt = 13
    RULE_expression = 14
    RULE_argList = 15
    RULE_type = 16
    RULE_accessModifier = 17

    ruleNames =  [ "program", "mainBlock", "classDecl", "member", "fieldDecl", 
                   "methodDecl", "constructorDecl", "paramList", "param", 
                   "block", "statement", "varDecl", "assignment", "returnStmt", 
                   "expression", "argList", "type", "accessModifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    ID=20
    INT=21
    WS=22
    COMMENT=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mainBlock(self):
            return self.getTypedRuleContext(ObjMiniParser.MainBlockContext,0)


        def EOF(self):
            return self.getToken(ObjMiniParser.EOF, 0)

        def classDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjMiniParser.ClassDeclContext)
            else:
                return self.getTypedRuleContext(ObjMiniParser.ClassDeclContext,i)


        def getRuleIndex(self):
            return ObjMiniParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ObjMiniParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 36
                self.classDecl()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.mainBlock()
            self.state = 43
            self.match(ObjMiniParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(ObjMiniParser.BlockContext,0)


        def getRuleIndex(self):
            return ObjMiniParser.RULE_mainBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainBlock" ):
                listener.enterMainBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainBlock" ):
                listener.exitMainBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainBlock" ):
                return visitor.visitMainBlock(self)
            else:
                return visitor.visitChildren(self)




    def mainBlock(self):

        localctx = ObjMiniParser.MainBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mainBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(ObjMiniParser.T__0)
            self.state = 46
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ObjMiniParser.ID)
            else:
                return self.getToken(ObjMiniParser.ID, i)

        def member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjMiniParser.MemberContext)
            else:
                return self.getTypedRuleContext(ObjMiniParser.MemberContext,i)


        def getRuleIndex(self):
            return ObjMiniParser.RULE_classDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDecl" ):
                listener.enterClassDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDecl" ):
                listener.exitClassDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecl" ):
                return visitor.visitClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def classDecl(self):

        localctx = ObjMiniParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(ObjMiniParser.T__1)
            self.state = 49
            self.match(ObjMiniParser.ID)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 50
                self.match(ObjMiniParser.T__2)
                self.state = 51
                self.match(ObjMiniParser.ID)


            self.state = 54
            self.match(ObjMiniParser.T__3)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 55
                self.member()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(ObjMiniParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldDecl(self):
            return self.getTypedRuleContext(ObjMiniParser.FieldDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(ObjMiniParser.MethodDeclContext,0)


        def constructorDecl(self):
            return self.getTypedRuleContext(ObjMiniParser.ConstructorDeclContext,0)


        def getRuleIndex(self):
            return ObjMiniParser.RULE_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember" ):
                listener.enterMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember" ):
                listener.exitMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = ObjMiniParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_member)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.fieldDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.methodDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.constructorDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def accessModifier(self):
            return self.getTypedRuleContext(ObjMiniParser.AccessModifierContext,0)


        def type_(self):
            return self.getTypedRuleContext(ObjMiniParser.TypeContext,0)


        def ID(self):
            return self.getToken(ObjMiniParser.ID, 0)

        def getRuleIndex(self):
            return ObjMiniParser.RULE_fieldDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldDecl" ):
                listener.enterFieldDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldDecl" ):
                listener.exitFieldDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDecl" ):
                return visitor.visitFieldDecl(self)
            else:
                return visitor.visitChildren(self)




    def fieldDecl(self):

        localctx = ObjMiniParser.FieldDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_fieldDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.accessModifier()
            self.state = 69
            self.type_()
            self.state = 70
            self.match(ObjMiniParser.ID)
            self.state = 71
            self.match(ObjMiniParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def accessModifier(self):
            return self.getTypedRuleContext(ObjMiniParser.AccessModifierContext,0)


        def type_(self):
            return self.getTypedRuleContext(ObjMiniParser.TypeContext,0)


        def ID(self):
            return self.getToken(ObjMiniParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(ObjMiniParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(ObjMiniParser.ParamListContext,0)


        def getRuleIndex(self):
            return ObjMiniParser.RULE_methodDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDecl" ):
                listener.enterMethodDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDecl" ):
                listener.exitMethodDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = ObjMiniParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.accessModifier()
            self.state = 74
            self.type_()
            self.state = 75
            self.match(ObjMiniParser.ID)
            self.state = 76
            self.match(ObjMiniParser.T__6)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1277952) != 0):
                self.state = 77
                self.paramList()


            self.state = 80
            self.match(ObjMiniParser.T__7)
            self.state = 81
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def accessModifier(self):
            return self.getTypedRuleContext(ObjMiniParser.AccessModifierContext,0)


        def ID(self):
            return self.getToken(ObjMiniParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(ObjMiniParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(ObjMiniParser.ParamListContext,0)


        def getRuleIndex(self):
            return ObjMiniParser.RULE_constructorDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorDecl" ):
                listener.enterConstructorDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorDecl" ):
                listener.exitConstructorDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructorDecl" ):
                return visitor.visitConstructorDecl(self)
            else:
                return visitor.visitChildren(self)




    def constructorDecl(self):

        localctx = ObjMiniParser.ConstructorDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_constructorDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.accessModifier()
            self.state = 84
            self.match(ObjMiniParser.ID)
            self.state = 85
            self.match(ObjMiniParser.T__6)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1277952) != 0):
                self.state = 86
                self.paramList()


            self.state = 89
            self.match(ObjMiniParser.T__7)
            self.state = 90
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjMiniParser.ParamContext)
            else:
                return self.getTypedRuleContext(ObjMiniParser.ParamContext,i)


        def getRuleIndex(self):
            return ObjMiniParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = ObjMiniParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.param()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 93
                self.match(ObjMiniParser.T__8)
                self.state = 94
                self.param()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(ObjMiniParser.TypeContext,0)


        def ID(self):
            return self.getToken(ObjMiniParser.ID, 0)

        def getRuleIndex(self):
            return ObjMiniParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ObjMiniParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.type_()
            self.state = 101
            self.match(ObjMiniParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjMiniParser.StatementContext)
            else:
                return self.getTypedRuleContext(ObjMiniParser.StatementContext,i)


        def getRuleIndex(self):
            return ObjMiniParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ObjMiniParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(ObjMiniParser.T__3)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3389584) != 0):
                self.state = 104
                self.statement()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self.match(ObjMiniParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(ObjMiniParser.VarDeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(ObjMiniParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(ObjMiniParser.ExpressionContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(ObjMiniParser.ReturnStmtContext,0)


        def block(self):
            return self.getTypedRuleContext(ObjMiniParser.BlockContext,0)


        def getRuleIndex(self):
            return ObjMiniParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ObjMiniParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_statement)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.expression(0)
                self.state = 115
                self.match(ObjMiniParser.T__5)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 117
                self.returnStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 118
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(ObjMiniParser.TypeContext,0)


        def ID(self):
            return self.getToken(ObjMiniParser.ID, 0)

        def getRuleIndex(self):
            return ObjMiniParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = ObjMiniParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.type_()
            self.state = 122
            self.match(ObjMiniParser.ID)
            self.state = 123
            self.match(ObjMiniParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ObjMiniParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(ObjMiniParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ObjMiniParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = ObjMiniParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(ObjMiniParser.ID)
            self.state = 126
            self.match(ObjMiniParser.T__9)
            self.state = 127
            self.expression(0)
            self.state = 128
            self.match(ObjMiniParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ObjMiniParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ObjMiniParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = ObjMiniParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(ObjMiniParser.T__10)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3158144) != 0):
                self.state = 131
                self.expression(0)


            self.state = 134
            self.match(ObjMiniParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ObjMiniParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IntegerContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ObjMiniParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ObjMiniParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ObjMiniParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ObjMiniParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class NewObjectContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ObjMiniParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ObjMiniParser.ID, 0)
        def argList(self):
            return self.getTypedRuleContext(ObjMiniParser.ArgListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewObject" ):
                listener.enterNewObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewObject" ):
                listener.exitNewObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewObject" ):
                return visitor.visitNewObject(self)
            else:
                return visitor.visitChildren(self)


    class ThisContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ObjMiniParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThis" ):
                listener.enterThis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThis" ):
                listener.exitThis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThis" ):
                return visitor.visitThis(self)
            else:
                return visitor.visitChildren(self)


    class MethodCallContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ObjMiniParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(ObjMiniParser.ExpressionContext,0)

        def ID(self):
            return self.getToken(ObjMiniParser.ID, 0)
        def argList(self):
            return self.getTypedRuleContext(ObjMiniParser.ArgListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodCall" ):
                listener.enterMethodCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodCall" ):
                listener.exitMethodCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesesContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ObjMiniParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(ObjMiniParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentheses" ):
                listener.enterParentheses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentheses" ):
                listener.exitParentheses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentheses" ):
                return visitor.visitParentheses(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ObjMiniParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                localctx = ObjMiniParser.NewObjectContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 137
                self.match(ObjMiniParser.T__11)
                self.state = 138
                self.match(ObjMiniParser.ID)
                self.state = 139
                self.match(ObjMiniParser.T__6)
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3158144) != 0):
                    self.state = 140
                    self.argList()


                self.state = 143
                self.match(ObjMiniParser.T__7)
                pass
            elif token in [13]:
                localctx = ObjMiniParser.ThisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 144
                self.match(ObjMiniParser.T__12)
                pass
            elif token in [20]:
                localctx = ObjMiniParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 145
                self.match(ObjMiniParser.ID)
                pass
            elif token in [21]:
                localctx = ObjMiniParser.IntegerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(ObjMiniParser.INT)
                pass
            elif token in [7]:
                localctx = ObjMiniParser.ParenthesesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 147
                self.match(ObjMiniParser.T__6)
                self.state = 148
                self.expression(0)
                self.state = 149
                self.match(ObjMiniParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 163
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ObjMiniParser.MethodCallContext(self, ObjMiniParser.ExpressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 153
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 154
                    self.match(ObjMiniParser.T__13)
                    self.state = 155
                    self.match(ObjMiniParser.ID)
                    self.state = 156
                    self.match(ObjMiniParser.T__6)
                    self.state = 158
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3158144) != 0):
                        self.state = 157
                        self.argList()


                    self.state = 160
                    self.match(ObjMiniParser.T__7) 
                self.state = 165
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ObjMiniParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ObjMiniParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ObjMiniParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = ObjMiniParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.expression(0)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 167
                self.match(ObjMiniParser.T__8)
                self.state = 168
                self.expression(0)
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ObjMiniParser.ID, 0)

        def getRuleIndex(self):
            return ObjMiniParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = ObjMiniParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1277952) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccessModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ObjMiniParser.RULE_accessModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessModifier" ):
                listener.enterAccessModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessModifier" ):
                listener.exitAccessModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccessModifier" ):
                return visitor.visitAccessModifier(self)
            else:
                return visitor.visitChildren(self)




    def accessModifier(self):

        localctx = ObjMiniParser.AccessModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_accessModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            _la = self._input.LA(1)
            if not(_la==18 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




