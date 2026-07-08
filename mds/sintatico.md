# Documentação Sintática da Linguagem JavaScript (Subset)

# 1. Elementos Sintáticos.

Um programa nesta linguagem é composto por uma ou mais declarações de funções, variáveis ou classes, conforme apresentado na seguinte regra[cite: 3]:
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


Onde as regras definem a estrutura completa para a criação de classes (contendo construtores, métodos e atributos) e funções. O elemento `sigparams` representa os argumentos formais recebidos. Por último, temos o `body` que delimita obrigatoriamente o bloco de comandos envolvidos por chaves[cite: 3].


## 1.1 Comandos da Linguagem JavaScript

Com relação aos comandos aceitos, a linguagem lida com estruturas de repetição (for, while), condicionais (if, else), controle de fluxo (return), declarações de variáveis e comandos de expressões, conforme apresentado nas seguintes regras[cite: 3]:

stm → FOR "(" exp ";" exp ";" exp ")" body
| assign ";"
| vardecl
| exp ";"
| RETURN exp ";"
| WHILE "(" exp ")" body
| IF "(" exp ")" body
| IF "(" exp ")" body ELSE body


O comando `for` inicia com a palavra reservada FOR, seguido por três expressões delimitadas por ponto e vírgula dentro de parênteses e um escopo de execução (`body`). Os comandos `while` e `if` seguem lógica similar, exigindo uma expressão de teste condicional entre parênteses acompanhada de seu respectivo bloco de comandos[cite: 3]. Quanto ao comando `return`, ele inicia com a palavra reservada RETURN seguida de uma expressão e finalizada com o delimitador `;`[cite: 3].


## 1.2 Expressões em JavaScript

A linguagem dá suporte a um conjunto abrangente de expressões aritméticas, lógicas, relacionais, atribuições, instanciações e acessos a membros, detalhados fielmente pela seguinte regra[cite: 3]:

exp → exp "+" exp | exp "-" exp | exp "" exp | exp "/" exp | exp "%" exp | exp "--" |
exp "++" | "++" exp | "--" exp |  exp "" exp | exp "=" exp | exp "!" exp | exp "&" exp |
exp "^" exp | "'" exp | exp "'" | exp "==" exp | exp "!=" exp |  exp ">" exp | exp "<" exp | exp ">=" exp |
exp "<=" exp | exp "&&" exp | exp "||" exp | "!" exp | "~" exp | "(" exp ")" | "+" exp | "-" exp | exp "?" exp ":" exp |
exp "+=" exp | exp "-=" exp | exp "=" exp | exp "=" exp | exp "/=" exp | exp "%=" exp |
exp "<<=" exp | exp ">>=" exp | exp ">>>=" exp | exp "&=" exp | exp "^=" exp |  "'" exp "|=" exp "'" |
NEW ID "(" ")" | NEW ID "(" params ")" | exp "." ID | exp "." call | THIS |
num | ID | call  | assign | TRUE | FALSE | STRING_AD | STRING_A



### 1.2.1 Chamadas de Função e Atribuição

A linguagem provê suporte para chamadas de funções e métodos (com ou sem a passagem de parâmetros), além de atribuições diretas de valores a identificadores ou propriedades de objetos, conforme as regras apresentadas a seguir[cite: 3]:

assign → ID "=" exp | exp "." ID "=" exp
call → ID "(" params ")" | ID "(" ")" | exp "." ID "(" params ")" | exp "." ID "(" ")"
params → exp "," params | exp



# 2. Exemplos de Código.

A seguir, alguns exemplos de código perfeitamente estruturados e válidos de acordo com a sintaxe da linguagem[cite: 3]:

```javascript
class Retangulo {
    largura;
    altura;
    
    constructor(l, a) {
        this.largura = l;
        this.altura = a;
    }
}
JavaScript
function calcular(valor, limite) {
    let i = 0;
    while (i < limite) {
        valor += 5;
        i++;
    }
    return valor;
}
JavaScript
function processar() {
    let flag = true;
    if (flag === true) {
        return 1;
    } else {
        return 0;
    }
}