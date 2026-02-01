from codegen import CodeGenerator

cg = CodeGenerator(vtables, layouts)

print("\n--- CODE GENERATION DEMO ---")

obj = cg.gen_new_object("B")
cg.gen_method_call(obj, "B", "getX")
