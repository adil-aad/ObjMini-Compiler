from ObjMiniListener import ObjMiniListener
from ObjMiniParser import ObjMiniParser
from semantic import ClassInfo

class ClassCollector(ObjMiniListener):

    def __init__(self):
        self.classes = {}

    def enterClassDecl(self, ctx:ObjMiniParser.ClassDeclContext):
        name = ctx.ID(0).getText()

        parent = None
        if ctx.ID(1):
            parent = ctx.ID(1).getText()

        if name in self.classes:
            print(f"Error: Duplicate class {name}")
        else:
            self.classes[name] = ClassInfo(name, parent)



    def enterFieldDecl(self, ctx):
        className = ctx.parentCtx.parentCtx.ID(0).getText()
        fieldType = ctx.type().getText()
        fieldName = ctx.ID().getText()

        self.classes[className].fields[fieldName] = fieldType

    def enterMethodDecl(self, ctx):
        className = ctx.parentCtx.parentCtx.ID(0).getText()

        returnType = ctx.type().getText()
        name = ctx.ID().getText()

        params = []
        if ctx.paramList():
            for p in ctx.paramList().param():
                params.append(p.type().getText())

        self.classes[className].methods[name] = (returnType, params)
