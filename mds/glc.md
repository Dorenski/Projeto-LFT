# GLC da Linguagem JavaScript
Terminais são representados pelos elementos cuja grafia está em maiúsculo, bem como pelos símbolos literais.

program → funcdecl | funcdecl program | vardecl | vardecl program | classdecl | classdecl program

classdecl → CLASS ID classbody

classbody → "{" classmembers "}"

classmembers → classmember | classmember classmembers

classmember → methoddecl | constructordecl | attrdecl

constructordecl → CONSTRUCTOR "(" sigparams ")" body | CONSTRUCTOR "(" ")" body

methoddecl → ID "(" sigparams ")" body | ID "(" ")" body

attrdecl → ID ";" | ID "=" exp ";"

funcdecl → signature body

signature → FUNCTION ID "(" sigparams ")" | FUNCTION ID "(" ")"

sigparams → ID |  ID "," sigparams

body → "{" stms "}"

exp → exp "+" exp | exp "-" exp | exp "*" exp | exp "/" exp | exp "%" exp | exp "--" |
      exp "++" | "++" exp | "--" exp |  exp "**" exp | exp "===" exp | exp "!==" exp | exp "&" exp |
      exp "^" exp | "'" exp | exp "'" | exp "==" exp | exp "!=" exp |  exp ">" exp | exp "<" exp | exp ">=" exp |
      exp "<=" exp | exp "&&" exp | exp "||" exp | "!" exp | "~" exp | "(" exp ")" | "+" exp | "-" exp | exp "?" exp ":" exp |
      exp "+=" exp | exp "-=" exp | exp "*=" exp | exp "**=" exp | exp "/=" exp | exp "%=" exp |
      exp "<<=" exp | exp ">>=" exp | exp ">>>=" exp | exp "&=" exp | exp "^=" exp |  "'" exp "|=" exp "'" |
      NEW ID "(" ")" | NEW ID "(" params ")" | exp "." ID | exp "." call | THIS |
      num | ID | call  | assign | TRUE | FALSE | STRING_AD | STRING_A

vardecl → LET ID ";" | VAR ID ";" | CONST ID ";" | LET ID "=" exp ";" | CONST ID "=" exp ";" | VAR ID "=" exp ";"

stms → stm | stm stms

stm → FOR "(" exp ";" exp ";" exp ")" body | assign ";" | vardecl | exp ";" | RETURN exp ";" | WHILE "(" exp ")" body | IF "(" exp ")" body | IF "(" exp ")" body ELSE body

assign → ID "=" exp | exp "." ID "=" exp

call → ID "(" params ")" | ID "(" ")" | exp "." ID "(" params ")" | exp "." ID "(" ")"

params → exp "," params | exp