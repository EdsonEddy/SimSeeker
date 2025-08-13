import sys
from antlr4 import *
from gen.Python3Lexer import Python3Lexer
from gen.Python3Parser import Python3Parser

def main():
    
    code_example = """
def main():
    x = 5
    y = 10
    result = x + y
    print("The result is:", result)

if __name__ == "__main__":
    main()
"""

    # Create lexer and parser
    lexer = Python3Lexer(InputStream(code_example))
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)

    # Parse starting at the 'file_input' rule (root of Python grammar)
    tree = parser.file_input()

    # Print the parse tree (in LISP style)
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
