#  Linguagem JavaScript - Elementos Léxicos

Esta documentação descreve os elementos léxicos do subconjunto da linguagem JavaScript especificado. A seguir, destacamos seus elementos léxicos:

#### 1. Palavras reservadas

A linguagem apresenta as seguintes palavras reservadas:
**break**, **case**, **class**, **const**, **constructor**, **continue**, **debugger**, **default**, **delete**, **do**, **else**, **finally**, **for**, **function**, **if**, **import**, **in**, **new**, **return**, **switch**, **this**, **typeof**, **var**, **void**, **while**, **with**, **protected**, **static**, **private**, **public**, **let**, **boolean**, **byte**, **char**, **final**, **int**, **true**, **false**, **null**, **undefined**.

#### 2. Operadores

A linguagem apresenta uma ampla variedade de operadores suportados:
* **Aritméticos:** `+` (soma), `-` (subtração), `*` (multiplicação), `/` (divisão), `%` (resto), `**` (exponenciação), `++` (incremento), `--` (decremento).
* **Relacionais e Igualdade:** `<` (menor), `<=` (menor igual), `>` (maior), `>=` (maior igual), `==` (igualdade), `!=` (desigualdade), `===` (igual estrita), `!==` (desigual estrita).
* **Lógicos e Bit a Bit:** `&&` (and lógico), `||` (or lógico), `!` (não lógico), `&` (and bit a bit), `|` (or bit a bit), `^` (xor bit a bit), `~` (não bit a bit), `<<` , `>>`, `>>>`.
* **Atribuição:** `=`, `+=`, `-=`, `*=`, `**=`, `/=`, `%=`, `<<=`, `>>=`, `>>>=`, `&=`, `^=`, `|=`.
* **Outros:** `? :` (operador ternário), `.` (acesso a membro).

#### 3. Delimitadores

Os comandos e estruturas utilizam os seguintes delimitadores:
* **;** (Ponto e vírgula): para encerrar declarações de variáveis, atributos e comandos.
* **,** (Vírgula): para separar parâmetros de funções e argumentos.
* **( )** (Parênteses): para expressões, assinaturas de funções e blocos de controle.
* **{ }** (Chaves): para delimitar os blocos de código em métodos, funções e classes.
* **[ ]** (Colchetes): suportados nativamente pelos tokens para indexação ou arrays.
* **"** e **'** (Aspas): para envolver textos literais.

#### 4. Identificadores

Para os identificadores (`ID`), aplicam-se as regras comuns em linguagens de programação. Um identificador é aceito para nomear variáveis, funções, classes, métodos e parâmetros.

#### 5. Literais (Números e Strings)

A linguagem dá suporte aos seguintes dados básicos:
* **Números:** Podem ser inteiros (`INT_LITERAL`), de ponto flutuante (`FLOAT_LITERAL`), octais (`OCTAL`) e hexadecimais (`HEXADECIMAL`).
* **Strings:** Textos delimitados por aspas simples (`STRING_A`) ou duplas (`STRING_AD`).
* **Booleanos:** Valores lógicos `true` e `false`.

#### 6. Erros e Tratamento Léxico

Qualquer coisa que não se enquadre na gramática e não seja reconhecida como um token válido, é considerada como um erro léxico. Adicionalmente, o léxico ignora comentários no código (`COMENTARIO`).