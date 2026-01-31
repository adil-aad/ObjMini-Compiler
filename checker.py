def check_parent_exists(classes):
    for c in classes.values():
        if c.parent and c.parent not in classes:
            print(f"Error: Parent class {c.parent} not found for {c.name}")

def detect_cycles(classes):

    def visit(cname, visited, stack):
        visited.add(cname)
        stack.add(cname)

        parent = classes[cname].parent
        if parent:
            if parent not in visited:
                if visit(parent, visited, stack):
                    return True
            elif parent in stack:
                return True

        stack.remove(cname)
        return False

    visited = set()
    for cname in classes:
        if cname not in visited:
            if visit(cname, visited, set()):
                print("Error: Inheritance cycle detected")
                return

def check_overriding(classes):
    for c in classes.values():
        parent = classes.get(c.parent)
        if not parent:
            continue

        for m in c.methods:
            if m in parent.methods:
                if c.methods[m] != parent.methods[m]:
                    print(f"Error: Invalid override of {m} in {c.name}")
