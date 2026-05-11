**JavaScript -- Elementos léxicos.**

JavaScript é uma linguagem de programação de alto nível, interpretada e versátil, utilizada principalmente para criar interatividade e funcionalidades dinâmicas em páginas e aplicações web.

**1. Palavras reservadas**

Palavras reservadas do ECMAScript 2015:

| [break](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/break)       | [case](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/switch)          | [catch](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/try...catch) |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [class](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/class)       | [const](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/const)          | [continue](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/continue) |
| [debugger](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/debugger) | [default](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/switch)       | [delete](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)      |
| [do](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/do...while)     | [else](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/if...else)       | [export](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/export)     |
| [extends](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/class)     | [finally](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/try...catch)  | [for](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/for)           |
| [function](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/function) | [if](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/if...else)         | [import](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/import)     |
| [in](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/in)              | [instanceof](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/instanceof) | [new](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/new)            |
| [return](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/return)     | [super](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/super)           | [switch](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/switch)     |
| [this](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/this)          | [throw](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/throw)          | [try](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/try...catch)   |
| [typeof](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/typeof)      | [var](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/var)              | [void](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/void)          |
| [while](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/while)       | with                                                                                                 | [yield](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/yield)        |
| await                                                                                             | protected                                                                                            | static                                                                                            |
| private                                                                                           | public                                                                                               | let                                                                                               |
| abstract                                                                                          | boolean                                                                                              | byte                                                                                              |
| char                                                                                              | double                                                                                               | final                                                                                             |
| float                                                                                             | int                                                                                                  | long                                                                                              |
| short                                                                                             | true                                                                                                 | false                                                                                             |
| null                                                                                              | undefined                                                                                            |                                                                                                   |

**2. Operadores e expressões**

| **Precedência** | **Tipo do Operador**                                                                                                                     | **Associatividade**   | **Operadores**     |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------------|
| 20              | [Agrupamento](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/Grouping)                                      | n/a                   | ( ... )            |
| 19              | [Acesso a Membro](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/Property_accessors#Dot_notation)           | esquerda para direita | ... . ...          |
|                 | [Acesso a Membro Computado](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/Property_accessors#Dot_notation) | esquerda para direita | ... \[ ... \]      |
|                 | [new](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/new) (com lista de argumentos)                         | n/a                   | new ... ( ... )    |
| 18              | [Chamada a Função](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Guide/Functions)                                              | esquerda para direita | ... ( *... *)      |
|                 | [new](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/new) (sem lista de argumentos)                         | direita para esquerda | new ...            |
| 17              | [Incremento Pós-fixado](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Increment)                           | n/a                   | ... ++             |
|                 | [Decremento Pós-fixado](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Decrement)                           | n/a                   | ... \--            |
| 16              | [NÃO lógico](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Logical_NOT)                                    | direita para esquerda | ! ...              |
|                 | [NÃO bit-a-bit](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Bitwise_NOT)                                 | direita para esquerda | \~ ...             |
|                 | [Positivo Unário](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Unary_plus)                                | direita para esquerda | \+ ...             |
|                 | [Negativo Unário](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Unary_negation)                            | direita para esquerda | \- ...             |
|                 | [Incremento Pré-fixado](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Increment)                           | direita para esquerda | ++ ...             |
|                 | [Decremento Pré-fixado](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Decrement)                           | direita para esquerda | \-- ...            |
|                 | [typeof](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/typeof)                                             | direita para esquerda | typeof ...         |
|                 | [void](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/void)                                                 | direita para esquerda | void ...           |
|                 | [delete](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)                                             | direita para esquerda | delete ...         |
| 15              | [Exponenciação](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Exponentiation)                              | direita para esquerda | ... \*\* ...       |
| 14              | [Multiplicação](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Multiplication)                              | esquerda para direita | ... \* ...         |
|                 | [Divisão](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Division)                                          | esquerda para direita | ... / ...          |
|                 | [Resto](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Remainder)                                           | esquerda para direita | ... % ...          |
| 13              | [Adição](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Addition)                                           | esquerda para direita | ... + ...          |
|                 | [Subtração](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Subtraction)                                     | esquerda para direita | ... - ...          |
| 12              | [Deslocamento de bits para esquerda](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators)                        | esquerda para direita | ... \<\< ...       |
|                 | [Deslocamento de bits para direita](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators)                         | esquerda para direita | ... \>\> ...       |
|                 | [Deslocamento de bits para direita, sem sinal](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators)              | esquerda para direita | ... \>\>\> ...     |
| 11              | [Menor Que](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Less_than_operator)                              | esquerda para direita | ... \< ...         |
|                 | [Menor ou Igual a](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Less_than__or_equal_operator)             | esquerda para direita | ... \<= ...        |
|                 | [Maior Que](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Greater_than_operator)                           | esquerda para direita | ... \> ...         |
|                 | [Maior ou Igual a](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Greater_than_or_equal_operator)           | esquerda para direita | ... \>= ...        |
|                 | [in](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/in)                                                     | esquerda para direita | ... in ...         |
|                 | [instanceof](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/instanceof)                                     | esquerda para direita | ... instanceof ... |
| 10              | [Igualdade](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Equality)                                        | esquerda para direita | ... == ...         |
|                 | [Desigualdade](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Inequality)                                   | esquerda para direita | ... != ...         |
|                 | [Igualdade Estrita](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Identity)                                | esquerda para direita | ... === ...        |
|                 | [Desigualdade Estrita](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Nonidentity)                          | esquerda para direita | ... !== ...        |
| 9               | [E bit-a-bit](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Bitwise_AND)                                   | esquerda para direita | ... & ...          |
| 8               | [OU exclusivo bit-a-bit](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Bitwise_XOR)                        | esquerda para direita | ... \^ ...         |
| 7               | [OU bit-a-bit](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Bitwise_OR)                                   | esquerda para direita | ... \| ...         |
| 6               | [E lógico](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Logical_AND)                                      | esquerda para direita | ... && ...         |
| 5               | [OU lógico](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators#Logical_OR)                                      | esquerda para direita | ... \|\| ...       |
| 4               | [Condicional](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/Conditional_operator)                          | direita para esquerda | ... ? ... : ...    |
| 3               | [Atribuição](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators)                                                | direita para esquerda | ... = ...          |
|                 |                                                                                                                                          |                       | ... += ...         |
|                 |                                                                                                                                          |                       | ... -= ...         |
|                 |                                                                                                                                          |                       | ... \*= ...        |
|                 |                                                                                                                                          |                       | ... /= ...         |
|                 |                                                                                                                                          |                       | ... %= ...         |
|                 |                                                                                                                                          |                       | ... \<\<= ...      |
|                 |                                                                                                                                          |                       | ... \>\>= ...      |
|                 |                                                                                                                                          |                       | ... \>\>\>= ...    |
|                 |                                                                                                                                          |                       | ... &= ...         |
|                 |                                                                                                                                          |                       | ... \^= ...        |
|                 |                                                                                                                                          |                       | ... \|= ...        |
| 2               | [yield](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/yield)                                               | direita para esquerda | yield ...          |
|                 | [yield\*](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/yield*)                                            |                       | yield\* ...        |
| 1               | [Propagação](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/Spread_syntax)                                  | n/a                   | \... ...           |
| 0               | [Vírgula / Sequência](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/Comma_operator)                        | esquerda para direita | ... , ...          |

**3. Delimitadores**

Os comandos em JavaScript utilizam ';' como delimitador de instruções. Os parâmetros de funções utilizam ',' como separador. Além disso, utiliza os delimitadores '( )' para expressões e chamadas de funções, '\[ \]' para vetores e '{ }' para blocos de comandos e objetos.

**4. Identificadores**

Um nome de variável em JavaScript, chamado de identificador, deve começar com uma letra, underline (\_), ou cifrão (\$); os caracteres seguintes podem também ser números (0-9). Devido JavaScript ser case-sensitive, letras incluem caracteres de \"A\" a \"Z\" (maiúsculos) e caracteres de \"a\" a \"z\" (minúsculos)

Ex:

let variavel1;  
let variavel_01;  
let \_variavel;

**5. Números**

JavaScript dá suporte a números inteiros e números de ponto flutuante. Além disso, permite o uso de sinais positivos e negativos.

**6. Erros**

Além disso, JavaScript ignora espaços em branco, tabulações e quebras de linha durante a execução do código, exceto em situações específicas da sintaxe. As quebras de linha também podem ser utilizadas para indicar a posição do código em mensagens de erro e processos de análise léxica e sintática.
