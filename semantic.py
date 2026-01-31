class ClassInfo:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.fields = {}     # name → type
        self.methods = {}    # name → (returnType, paramTypes)
