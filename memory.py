class ObjectLayout:
    def __init__(self):
        self.offsets = {}    # fieldName → offset
        self.size = 0


def build_layouts(classes):
    layouts = {}

    def build_for_class(cname):
        if cname in layouts:
            return layouts[cname]

        c = classes[cname]
        layout = ObjectLayout()

        offset = 1   # 0 reserved for vtable pointer

        # inherit parent fields
        if c.parent:
            parent_layout = build_for_class(c.parent)
            layout.offsets = parent_layout.offsets.copy()
            offset = parent_layout.size

        # add own fields
        for f in c.fields:
            layout.offsets[f] = offset
            offset += 1

        layout.size = offset
        layouts[cname] = layout
        return layout

    for cname in classes:
        build_for_class(cname)

    return layouts


def print_layouts(layouts):
    for cname, layout in layouts.items():
        print(f"\nLayout for class {cname}")
        for f, off in layout.offsets.items():
            print(f"  {f} → offset {off}")
        print(f"  Object size = {layout.size}")
