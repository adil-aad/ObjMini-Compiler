from antlr4 import *
from ObjMiniLexer import ObjMiniLexer
from ObjMiniParser import ObjMiniParser

def main():
    input_stream = FileStream("test.objmini")
    lexer = ObjMiniLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ObjMiniParser(tokens)

    tree = parser.program()
    print("Parsing successful!")
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()
