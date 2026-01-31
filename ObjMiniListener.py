# Generated from ObjMini.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ObjMiniParser import ObjMiniParser
else:
    from ObjMiniParser import ObjMiniParser

# This class defines a complete listener for a parse tree produced by ObjMiniParser.
class ObjMiniListener(ParseTreeListener):

    # Enter a parse tree produced by ObjMiniParser#program.
    def enterProgram(self, ctx:ObjMiniParser.ProgramContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#program.
    def exitProgram(self, ctx:ObjMiniParser.ProgramContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#mainBlock.
    def enterMainBlock(self, ctx:ObjMiniParser.MainBlockContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#mainBlock.
    def exitMainBlock(self, ctx:ObjMiniParser.MainBlockContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#classDecl.
    def enterClassDecl(self, ctx:ObjMiniParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#classDecl.
    def exitClassDecl(self, ctx:ObjMiniParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#member.
    def enterMember(self, ctx:ObjMiniParser.MemberContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#member.
    def exitMember(self, ctx:ObjMiniParser.MemberContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#fieldDecl.
    def enterFieldDecl(self, ctx:ObjMiniParser.FieldDeclContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#fieldDecl.
    def exitFieldDecl(self, ctx:ObjMiniParser.FieldDeclContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#methodDecl.
    def enterMethodDecl(self, ctx:ObjMiniParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#methodDecl.
    def exitMethodDecl(self, ctx:ObjMiniParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#constructorDecl.
    def enterConstructorDecl(self, ctx:ObjMiniParser.ConstructorDeclContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#constructorDecl.
    def exitConstructorDecl(self, ctx:ObjMiniParser.ConstructorDeclContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#paramList.
    def enterParamList(self, ctx:ObjMiniParser.ParamListContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#paramList.
    def exitParamList(self, ctx:ObjMiniParser.ParamListContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#param.
    def enterParam(self, ctx:ObjMiniParser.ParamContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#param.
    def exitParam(self, ctx:ObjMiniParser.ParamContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#block.
    def enterBlock(self, ctx:ObjMiniParser.BlockContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#block.
    def exitBlock(self, ctx:ObjMiniParser.BlockContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#statement.
    def enterStatement(self, ctx:ObjMiniParser.StatementContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#statement.
    def exitStatement(self, ctx:ObjMiniParser.StatementContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#varDecl.
    def enterVarDecl(self, ctx:ObjMiniParser.VarDeclContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#varDecl.
    def exitVarDecl(self, ctx:ObjMiniParser.VarDeclContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#assignment.
    def enterAssignment(self, ctx:ObjMiniParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#assignment.
    def exitAssignment(self, ctx:ObjMiniParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#returnStmt.
    def enterReturnStmt(self, ctx:ObjMiniParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#returnStmt.
    def exitReturnStmt(self, ctx:ObjMiniParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#Integer.
    def enterInteger(self, ctx:ObjMiniParser.IntegerContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#Integer.
    def exitInteger(self, ctx:ObjMiniParser.IntegerContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#Identifier.
    def enterIdentifier(self, ctx:ObjMiniParser.IdentifierContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#Identifier.
    def exitIdentifier(self, ctx:ObjMiniParser.IdentifierContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#NewObject.
    def enterNewObject(self, ctx:ObjMiniParser.NewObjectContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#NewObject.
    def exitNewObject(self, ctx:ObjMiniParser.NewObjectContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#This.
    def enterThis(self, ctx:ObjMiniParser.ThisContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#This.
    def exitThis(self, ctx:ObjMiniParser.ThisContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#MethodCall.
    def enterMethodCall(self, ctx:ObjMiniParser.MethodCallContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#MethodCall.
    def exitMethodCall(self, ctx:ObjMiniParser.MethodCallContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#Parentheses.
    def enterParentheses(self, ctx:ObjMiniParser.ParenthesesContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#Parentheses.
    def exitParentheses(self, ctx:ObjMiniParser.ParenthesesContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#argList.
    def enterArgList(self, ctx:ObjMiniParser.ArgListContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#argList.
    def exitArgList(self, ctx:ObjMiniParser.ArgListContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#type.
    def enterType(self, ctx:ObjMiniParser.TypeContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#type.
    def exitType(self, ctx:ObjMiniParser.TypeContext):
        pass


    # Enter a parse tree produced by ObjMiniParser#accessModifier.
    def enterAccessModifier(self, ctx:ObjMiniParser.AccessModifierContext):
        pass

    # Exit a parse tree produced by ObjMiniParser#accessModifier.
    def exitAccessModifier(self, ctx:ObjMiniParser.AccessModifierContext):
        pass



del ObjMiniParser