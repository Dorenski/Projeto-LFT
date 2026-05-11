# JavaScript — Elementos Léxicos

JavaScript é uma linguagem de programação de alto nível, interpretada e versátil, utilizada principalmente para criar interatividade e funcionalidades dinâmicas em páginas e aplicações web.

---

## 1. Palavras reservadas

Palavras reservadas do ECMAScript 2015:

| | | |
|---|---|---|
| [break](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/break) | [case](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/switch) | [catch](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/try...catch) |
| [class](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/class) | [const](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/const) | [continue](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/continue) |
| [debugger](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/debugger) | [default](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/switch) | [delete](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete) |
| [do](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/do...while) | [else](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/if...else) | [export](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/export) |

---

## 2. Operadores e expressões

| **Precedência** | **Tipo do Operador** | **Associatividade** | **Operadores** |
|---|---|---|---|
| 20 | Agrupamento | n/a | `( ... )` |
| 19 | Acesso a membro | esquerda para direita | `... . ...` |
| 18 | Chamada a função | esquerda para direita | `...( ... )` |
| 17 | Incremento pós-fixado | n/a | `...++` |
| 16 | Operadores unários | direita para esquerda | `!`, `~`, `+`, `-`, `typeof`, `void`, `delete` |
| 15 | Exponenciação | direita para esquerda | `**` |
| 14 | Multiplicação / divisão / resto | esquerda para direita | `*`, `/`, `%` |
| 13 | Adição / subtração | esquerda para direita | `+`, `-` |
| 12 | Deslocamento de bits | esquerda para direita | `<<`, `>>`, `>>>` |
| 11 | Relacionais | esquerda para direita | `<`, `<=`, `>`, `>=`, `in`, `instanceof` |
| 10 | Igualdade | esquerda para direita | `==`, `!=`, `===`, `!==` |
| 9 | E bit-a-bit | esquerda para direita | `&` |
| 8 | OU exclusivo bit-a-bit | esquerda para direita | `^` |
| 7 | OU bit-a-bit | esquerda para direita | `|` |
| 6 | E lógico | esquerda para direita | `&&` |
| 5 | OU lógico | esquerda para direita | `||` |
| 4 | Condicional | direita para esquerda | `? :` |
| 3 | Atribuição | direita para esquerda | `=`, `+=`, `-=`, `*=`, `/=` |
| 2 | yield | direita para esquerda | `yield`, `yield*` |
| 1 | Propagação | n/a | `...` |
| 0 | Vírgula / sequência | esquerda para direita | `,` |

---

## 3. Delimitadores

Os comandos em JavaScript utilizam `;` como delimitador de instruções. Os parâmetros de funções utilizam `,` como separador.

Além disso, JavaScript utiliza:

- `( )` para expressões e chamadas de funções;
- `[ ]` para vetores e acesso indexado;
- `{ }` para blocos de comandos e objetos.

---

## 4. Identificadores

Um identificador deve começar com:

- uma letra;
- underline (`_`);
- ou cifrão (`$`).

Os caracteres seguintes também podem incluir números (`0-9`).

Como JavaScript é *case-sensitive*, letras maiúsculas e minúsculas são diferenciadas.

### Exemplos

```javascript
let variavel1;
let variavel_01;
let _variavel;
```

---

## 5. Números

JavaScript dá suporte a:

- números inteiros;
- números de ponto flutuante;
- valores positivos e negativos.

---

## 6. Erros

JavaScript ignora espaços em branco, tabulações e quebras de linha durante a execução do código, exceto em situações específicas da sintaxe.

As quebras de linha também podem ser utilizadas para indicar a posição do código em mensagens de erro e processos de análise léxica e sintática.
