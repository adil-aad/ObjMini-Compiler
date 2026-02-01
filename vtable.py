# vtable.py

class VTable:
    def __init__(self):
        self.methods = []  # list of "ClassName.methodName"

    def add_method(self, label):
        self.methods.append(label)

    def replace_method(self, index, label):
        self.methods[index] = label


def build_vtables(classes):
    vtables = {}

    def build_for_class(cname):
        if cname in vtables:
            return vtables[cname]

        c = classes[cname]

        # 1. Start with parent vtable (Inheritance)
        if c.parent:
            parent_vt = build_for_class(c.parent)
            vt = VTable()
            vt.methods = parent_vt.methods.copy()
        else:
            vt = VTable()

        # 2. Add / Override methods (Dynamic Dispatch)
        for m in c.methods:
            label = f"{cname}.{m}"
            overridden = False

            for i, entry in enumerate(vt.methods):
                # Check if the method name (after the dot) matches
                if entry.split(".")[1] == m:
                    vt.replace_method(i, label)
                    overridden = True
                    break

            if not overridden:
                vt.add_method(label)

        vtables[cname] = vt
        return vt

    for cname in classes:
        build_for_class(cname)

    return vtables


def print_vtables(vtables):
    print("\n--- Virtual Method Tables ---")
    for cname, vt in vtables.items():
        print(f"VTable for class {cname}")
        for i, m in enumerate(vt.methods):
            print(f"  [{i}] {m}")