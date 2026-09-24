# exercicios-cursoemvideo-mundo-python-3

### Anotações das aulas

### 1\. Tuplas (Aula 16)

* **Conceito:** São variáveis compostas que permitem armazenar múltiplos valores em uma única estrutura[1].
* **Imutabilidade:** As tuplas são **imutáveis**; ou seja, uma vez criadas, seus elementos não podem ser alterados, adicionados ou removidos durante a execução do programa[4].
* **Sintaxe e Acesso:** São delimitadas por parênteses `()`[8] e seus elementos são acessados por índices numéricos a partir de `0`[9][10]. Também suportam fatiamento (*slicing*)[10].
* **Métodos e Iteração:** Podem ser percorridas por laços `for`[13] e contam com funções como `len()` (para verificar o tamanho)[14][16], `sorted()` (exibição em ordem)[17], `.count()` (conta ocorrências de um valor)[18] e `.index()` (localiza a posição de um item)[19].

---

### 2\. Listas - Partes 1 e 2 (Aulas 17 e 18)

* **Conceito e Mutabilidade:** São coleções compostas delimitadas por colchetes `[]`[20]. Ao contrário das tuplas, as listas são **mutáveis** e podem ter seus elementos modificados livremente[20].
* **Inclusão de Elementos:**
  * `.append(valor)`: adiciona um novo item ao final da lista[22][23].
  * `.insert(posição, valor)`: insere um item em uma posição específica, deslocando os demais[23].
* **Remoção de Elementos:**
  * `del lista[índice]` ou `.pop(índice)`: removem pelo índice[24][25]. Chamado sem parâmetro, o `.pop()` elimina o último elemento[25][26].
  * `.remove(valor)`: busca e elimina a primeira ocorrência do valor informado[25][27].
* **Cópia vs. Ligação:** Ao igualar duas listas (`B = A`), o Python cria uma **ligação** entre elas (modificar B altera A)[28][29]. Para gerar uma **cópia independente**, utiliza-se fatiamento `B = A[:]` ou o método `.copy()`[28].
* **Listas Compostas (Aninhadas):** Permitem inserir listas dentro de outras listas, viabilizando estruturas bidimensionais (como matrizes) acessadas por múltiplos índices (ex: `pessoas`)[33].

---

### 3\. Dicionários (Aula 19)

* **Conceito e Chaves Literais:** Estruturas de dados delimitadas por chaves `{}`[36][37]. Têm como diferencial o uso de **chaves/índices literais** (personalizados) em vez de apenas índices numéricos[36][38].
* **Estrutura:** Compostos por pares de **chaves** (*keys*), **valores** (*values*) e **itens** (*items*)[39] (ex: `dados = {'nome': 'Pedro', 'idade': 25}`)[37][42].
* **Manipulação:**
  * Para adicionar ou atualizar: `dados['sexo'] = 'M'` (não se utiliza `.append()`)[43].
  * Para remover: `del dados['idade']`[44].
* **Métodos Principais:** `.keys()` (retorna as chaves), `.values()` (retorna os valores) e `.items()` (retorna os pares chave-valor)[40][41].

---

### 4\. Funções - Partes 1 e 2 (Aulas 20 e 21)

* **Conceito e** **def** **:** Permitem criar **rotinas** personalizadas para reaproveitar trechos de código recorrentes, declaradas com a instrução `def`[45].
* **Parâmetros e Empacotamento:**
  * As funções podem receber argumentos dentro dos parênteses[48].
  * **Empacotamento (** **\*args** **):** O uso do asterisco `*` permite receber uma quantidade variável de parâmetros agrupados em uma tupla[49].
* **Parâmetros Opcionais:** Permitem definir valores padrão na declaração (ex: `def somar(a=0, b=0, c=0)`), tornando a passagem desses argumentos opcional[50][51].
* **Ajuda Interativa e Docstrings:**
  * A função `help()` exibe o manual interativo de funções e módulos[52].
  * É possível criar documentações para as próprias funções inserindo uma **Docstring** (texto entre aspas triplas `"""..."""`) na primeira linha após o `def`[53].
* **Escopo de Variáveis:**
  * **Escopo Local:** Variáveis criadas dentro de uma função só existem em seu bloco[56].
  * **Escopo Global:** Variáveis declaradas no programa principal[57][58]. A palavra-chave `global` permite modificar uma variável global dentro de um escopo local[59].
* **Retorno de Valores (** **return** **):** O comando `return` faz com que a função envie um resultado de volta para o ponto onde foi chamada, dando mais flexibilidade ao código[60].

---

### 5\. Módulos e Pacotes (Aula 22)

* **Modularização:** Consiste em dividir um programa grande em arquivos menores (`.py`), melhorando a organização, a legibilidade e a manutenção[63].
* **Módulos:** Arquivos `.py` contendo funções e definições que podem ser importados com `import nome_modulo` ou `from nome_modulo import funcao`[66].
* **Pacotes:** Quando o número de módulos aumenta, eles são agrupados em pastas chamadas **pacotes**, organizados por assuntos (ex: números, datas, cores)[70].
  * Cada pasta de pacote no Python contém um arquivo especial de inicialização chamado `__init__.py`[73].

---

### 6\. Tratamento de Erros e Exceções (Aula 23)

* **Diferença entre Erro Sintático e Exceções:**
  * **Erro Sintático:** Falha na escrita ou gramática da linguagem[74].
  * **Exceção:** Ocorre quando o código está escrito corretamente, mas falha durante a execução devido a uma situação imprevista (ex: `ValueError`, `ZeroDivisionError`, `IndexError`, `NameError`)[75].
* **Estrutura** **try / except / else / finally** **:**
  * `try`: Bloco onde o código propenso a erros é executado[81][82].
  * `except`: Bloco acionado caso ocorra uma falha/exceção específica ou genérica[81].
  * `else`: Bloco executado apenas se o `try` ocorrer sem nenhum erro[85][86].
  * `finally`: Bloco **sempre** executado ao término da estrutura, com ou sem erro (ideal para fechar conexões ou arquivos)[87].
