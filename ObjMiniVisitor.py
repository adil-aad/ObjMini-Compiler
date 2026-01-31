# Generated from ObjMini.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ObjMiniParser import ObjMiniParser
else:
    from ObjMiniParser import ObjMiniParser

# This class defines a complete generic visitor for a parse tree produced by ObjMiniParser.

class ObjMiniVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ObjMiniParser#program.
    def visitProgram(self, ctx:ObjMiniParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#mainBlock.
    def visitMainBlock(self, ctx:ObjMiniParser.MainBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#classDecl.
    def visitClassDecl(self, ctx:ObjMiniParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#member.
    def visitMember(self, ctx:ObjMiniParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#fieldDecl.
    def visitFieldDecl(self, ctx:ObjMiniParser.FieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#methodDecl.
    def visitMethodDecl(self, ctx:ObjMiniParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#constructorDecl.
    def visitConstructorDecl(self, ctx:ObjMiniParser.ConstructorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#paramList.
    def visitParamList(self, ctx:ObjMiniParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#param.
    def visitParam(self, ctx:ObjMiniParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#block.
    def visitBlock(self, ctx:ObjMiniParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#statement.
    def visitStatement(self, ctx:ObjMiniParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#varDecl.
    def visitVarDecl(self, ctx:ObjMiniParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#assignment.
    def visitAssignment(self, ctx:ObjMiniParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#returnStmt.
    def visitReturnStmt(self, ctx:ObjMiniParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#Integer.
    def visitInteger(self, ctx:ObjMiniParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#Identifier.
    def visitIdentifier(self, ctx:ObjMiniParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#NewObject.
    def visitNewObject(self, ctx:ObjMiniParser.NewObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#This.
    def visitThis(self, ctx:ObjMiniParser.ThisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#MethodCall.
    def visitMethodCall(self, ctx:ObjMiniParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#Parentheses.
    def visitParentheses(self, ctx:ObjMiniParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#argList.
    def visitArgList(self, ctx:ObjMiniParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#type.
    def visitType(self, ctx:ObjMiniParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ObjMiniParser#accessModifier.
    def visitAccessModifier(self, ctx:ObjMiniParser.AccessModifierContext):
        return self.visitChildren(ctx)



del ObjMiniParser