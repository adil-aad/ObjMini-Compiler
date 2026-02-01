class CodeGenerator:

    def __init__(self, vtables, layouts):
        self.vtables = vtables
        self.layouts = layouts
        self.tempCount = 0

    def new_temp(self):
        self.tempCount += 1
        return f"t{self.tempCount}"


    def gen_new_object(self, className):
        layout = self.layouts[className]
        size = layout.size

        t = self.new_temp()
        print(f"{t} = alloc {size}")
        print(f"store {t}[0] = &VTable_{className}")

        print(f"call {className}_constructor({t})")
        return t


    def gen_method_call(self, objTemp, className, methodName):

        vt = self.vtables[className]

        index = None
        for i, m in enumerate(vt.methods):
            if m.split(".")[1] == methodName:
                index = i
                break

        t1 = self.new_temp()
        t2 = self.new_temp()

        print(f"{t1} = load {objTemp}[0]")
        print(f"{t2} = load {t1}[{index}]")
        print(f"call {t2}({objTemp})")


    def gen_field_load(self, objTemp, className, fieldName):
        offset = self.layouts[className].offsets[fieldName]
        t = self.new_temp()
        print(f"{t} = load {objTemp}[{offset}]")
        return t
