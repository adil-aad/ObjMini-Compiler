from antlr4 import *
from ObjMiniLexer import ObjMiniLexer
from ObjMiniParser import ObjMiniParser
from ObjMiniListener import ObjMiniListener
from ClassCollector import ClassCollector
from checker import *

def main():
    input_stream = FileStream("test.objmini")
    lexer = ObjMiniLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ObjMiniParser(tokens)

    tree = parser.program()

    walker = ParseTreeWalker()
    collector = ClassCollector()
    walker.walk(collector, tree)

    classes = collector.classes

    check_parent_exists(classes)
    detect_cycles(classes)
    check_overriding(classes)

    print("Semantic analysis finished")

if __name__ == "__main__":
    main()
