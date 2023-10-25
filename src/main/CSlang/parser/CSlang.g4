// ID: 1952606

grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: class_decl* class_prog? EOF;



/**** class ****/
class_prog: CLASS (ID INHERITANCE)? 'Program'  LP program_member_list RP;
program_member_list: (programMainDecl | attribute_decl | method_decl)* ;
programMainDecl: FUNC '@main' LB RB CL return_type main_block_stm;

class_decl: CLASS (ID INHERITANCE)? ID LP members* RP;
members: (attribute_decl | method_decl | programMainDecl);

/**** attribute_decl ****/
attribute_decl: mutability (ID | AT_ID) val_list_decl val_decl SM | mutability id_list CL attr_type SM;
val_list_decl: CM (ID | AT_ID) val_list_decl val_decl CM | CL attr_type ASSIGN ;

mutability: (CONST | VAR);
id_list: (AT_ID | ID) id_plist;
id_plist: CM (AT_ID | ID) id_plist | ;

//val_list: val_decl val_plist;
//val_plist: CM val_decl val_plist | ;
val_decl: (INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | exp);

/**** method_decl ****/
method_decl: (nor_method | con_method) block_stm;

nor_method: FUNC (AT_ID | ID) LB param_list RB CL return_type;
con_method: FUNC CONSTRUCTOR LB param_list RB ;

param_list: param param_plist | ;
param_plist: CM param param_plist | ;
param: ID params CL type_name;
params: CM ID params | ;

/**** return type ****/
return_type: (type_name | VOID | array_type);

/**** block statement ****/
block_stm: LP statement* RP;

main_block_stm: LP main_stm* RP;

/**** typename ****/
type_name: (INT | FLOAT | STRING | BOOL | ID);
array_type: LSB INTLIT RSB type_name;
attr_type: type_name | array_type ;

/****************************************************************************/
/*																	 		*/
/*								5.Expressions								*/
/* 																			*/
/****************************************************************************/
exp: exp1 (CONCATENATION) exp1 | exp1;
exp1: exp2 (LT | GT | LE | GE | EQUAL | NOT_EQUAL) exp2 | exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (ADD | SUB) exp4 | exp4;
exp4: exp4 (MUL | INT_DIV | DIV | MOD) exp5 | exp5;
exp5: NOT exp5 | exp6;
exp6: SUB exp6 | exp7;
exp7: exp7 index_operator | exp8;
exp8: exp8 DOT exp9 | exp9;
exp9: exp10 DOT exp10 | exp10;
exp10: NEW exp10 LB exp_list RB | operands;

operands: AT_ID LB exp_list RB | ID LB exp_list RB | AT_ID | ID | SELF | NULL | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | LB exp RB | array_lit;

exp_list: exp CM exp_list | exp;

index_operator: LSB exp RSB index_operator  | LSB exp RSB;

/******* MEMBER ACCESS *******/
instance_access: exp DOT ID ;
static_attr_access: (ID DOT)? AT_ID ;
method_access: exp DOT ID LB exp_list RB ;
static_method_access: (ID DOT)? AT_ID LB exp_list RB ;


/****************************************************************************/
/*																	 		*/
/*								5.Statements								*/
/* 																			*/
/****************************************************************************/
statement:    variableDeclaration
            | arrayDeclaration
            | assignmentStatement
            | arrayAssignmentStatement
            | returnStatement
            | continueStatement
            | breakStatement
            | ifStatement
            | invocationStatement
            | forStatement
            | block_stm;

main_stm:   variableDeclaration
            | arrayDeclaration
            | assignmentStatement
            | arrayAssignmentStatement
            | returnStatement
            | continueStatement
            | breakStatement
            | ifStatement
            | main_invocation_stm
            | forStatement
            | block_stm;

//variableDeclaration: mutability id_list CL type_name assign_list? SM;
//assign_list: ASSIGN (val_list | exp) ;
variableDeclaration: attribute_decl;

arrayDeclaration: VAR ID (CM ID)* CL type_name LSB INTLIT RSB SM;

assignmentStatement: exp ASSINGMENT exp SM;

arrayAssignmentStatement: ID LSB exp RSB ASSINGMENT exp SM;

returnStatement: RETURN exp? SM;

continueStatement: CONTINUE SM;

breakStatement: BREAK SM;

ifStatement: IF (LP statement RP)? exp block_stm elseStatement?;
elseStatement: ELSE block_stm ;

forStatement: FOR initStm conStm postStm block_stm;
initStm: ID ASSINGMENT exp SM;
conStm: ID (LT | GT | LE | GE) INTLIT SM;
postStm: ID ASSINGMENT exp;

invocationStatement: method_access SM | static_method_access SM | static_attr_access SM;
main_invocation_stm: method_access SM | static_method_access SM | static_attr_access SM | instance_access SM;

/****** COMMENTS *****/
LINE_CMT: '//' ~[\r\n]* -> skip;
BLOCK_CMT: '/*' .*? '*/' -> skip;

/***********************************************************/
IMPORT: 'import';
ENTRYPOINT: '@main';

/****** KEYWORDS *****/
CONST: 'const';
VAR: 'var';

INT: 'int';
FLOAT: 'float';
STRING: 'string';
BOOL: 'bool';
BREAK: 'break';
CLASS: 'class';
CONTINUE: 'continue';
ELSE: 'else';
INHERITANCE: '<-';
IF: 'if';
NEW: 'new';
FOR: 'for';
RETURN: 'return';
VOID: 'void';
NULL: 'null';
CONSTRUCTOR: 'constructor';
FUNC: 'func';
//TRUE: 'true';
//FALSE: 'false';
SELF: 'self';

/****** OPERATORS ****/
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
INT_DIV: '\\';
MOD: '%';
NOT_EQUAL: '!=';
EQUAL: '==';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
OR: '||';
AND: '&&';
NOT: '!';
CONCATENATION: '^';
ASSINGMENT: ':=';
ASSIGN: '=';

/****** SEPARATORS *****/
LSB: '[';
RSB: ']';
LP: '{';
RP: '}';
LB: '(';
RB: ')';
SM: ';';
CL: ':';
DOT: '.';
CM: ',';

/****** LITERALS *********/
BOOLLIT: 'true' | 'false';

//STRINGLIT: '"' STR_CHAR* '"' {self.text = self.text.strip('"')};
STRINGLIT: '"' (ESCAPE_SEQUENCE | ~["\r\n])* '"' {self.text = self.text.strip('"')};

FLOATLIT:
	DIGIT+ DOT
	| DIGIT+ DOT DIGIT+
	| DIGIT+ (DOT DIGIT+)? [eE] [+-]? DIGIT+
	| DIGIT+ DOT [eE] [+-]? DIGIT+;

//INTLIT: DIGIT+;
INTLIT: '0' | [1-9] [0-9]*;

array_lit: LSB element arraylit_list RSB ;
element: (INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | exp);
arraylit_list: CM element arraylit_list | ;

ID: [_a-zA-Z][_a-zA-Z0-9]*;
AT_ID: '@'[_a-zA-Z][_a-zA-Z0-9]*;

/**** FRAGMENT *****/
fragment DIGIT: [0-9];

NEWLINE: '\n'+ -> skip;

UNCLOSE_STRING:
	'"' STR_CHAR* ([\b\t\n\f\r'\\] | EOF) {
		error = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '\'', '\\']
		if error[-1] in possible:
			raise UncloseString(error[1:-1])
		else:
			raise UncloseString(error[1:])
	};

fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\';

WS: [ \t\r\f\b\n]+ -> skip; // skip spaces, tabs, form feed, newline

ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL {
        illegal_str = str(self.text)
        raise IllegalEscape(illegal_str[1:])
    };

//UNCLOSE_STRING: '"' (~['"\r\n] | ESC_ILLEGAL)* EOF '\n' -> type(UNCLOSE_STRING), setText("<unclosed string>");

/**** FRAGMENT *****/
// fragment STR_CHAR: ~[\r\n"\\] | ('\\' [bfrnt"\\]);

fragment STR_CHAR: ~[\b\f\r\n\t'"\\] | ESCAPE_SEQUENCE | '\\"';
fragment ESCAPE_SEQUENCE: '\\' [bfrnt'\\];

ERROR_CHAR: .{raise ErrorToken(self.text)};
