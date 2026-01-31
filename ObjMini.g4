grammar ObjMini;

/* ============================
   Parser Rules
============================ */

program
    : classDecl* mainBlock EOF
    ;

mainBlock
    : 'main' block
    ;

classDecl
    : 'class' ID ('extends' ID)? '{' member* '}'
    ;

member
    : fieldDecl
    | methodDecl
    | constructorDecl
    ;

fieldDecl
    : accessModifier type ID ';'
    ;

methodDecl
    : accessModifier type ID '(' paramList? ')' block
    ;

constructorDecl
    : accessModifier ID '(' paramList? ')' block
    ;

paramList
    : param (',' param)*
    ;

param
    : type ID
    ;

block
    : '{' statement* '}'
    ;

statement
    : varDecl
    | assignment
    | expression ';'    // Combined method calls into expression
    | returnStmt
    | block
    ;

varDecl
    : type ID ';'
    ;

assignment
    : ID '=' expression ';'
    ;

returnStmt
    : 'return' expression? ';'
    ;

// THE FIXED EXPRESSION RULE
expression
    : 'new' ID '(' argList? ')'          # NewObject
    | 'this'                             # This
    | ID                                 # Identifier
    | INT                                # Integer
    | expression '.' ID '(' argList? ')' # MethodCall
    | '(' expression ')'                 # Parentheses
    ;

argList
    : expression (',' expression)*
    ;

type
    : 'int' | 'bool' | 'void' | ID ;

accessModifier
    : 'public' | 'private' ;

/* ============================
   Lexer Rules
============================ */

ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
INT     : [0-9]+ ;
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;