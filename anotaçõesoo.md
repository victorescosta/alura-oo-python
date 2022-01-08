Introdução a Orientação a objetos
==
Paradigma procedural x OO

Procedural - limitações do paradigma procedural
- Implementar novamente uma mesma regra, gerando mais um local caso a regra precise ser alterada
- "Cachorro que tem muitos donos acaba morrendo de fome"
- "Copie o código de validação que está no formulário ABCD" - para não arriscar inserir erros em códigos que já estão funcionando ou em produção

OO: Juntar as coisas com as características que a agrupam
- Dado e funcionalidade (comportamento) devem andar juntos, auxiliando a manutenção e legibilidade do código
- Encapsulamento de código

Momento atual do projeto [Capítulo1](https://github.com/alura-cursos/Curso-Python-3-Introdu-o-a-Orienta-o-a-objetos/archive/capitulo1.zip)

**Classes e Objetos**:
- Antes de criar um Objeto, eu tenho que definir uma classe (antes de fazer um bolo, tenho que definir a receita)
```
>>> from conta import Conta
>>> Conta()
<conta.Conta object at 0x7fa24ee46d00>
>>> conta = Conta() - referência para guardar a classe conta e disponibilizar o acesso
conta e Conta() possuem endereços na memória diferentes
```
- Uma classe é uma especificação de um tipo, definindo valores e comportamentos
- Um objeto é uma instância de uma classe onde podemos definir valores para seus atributos
- Para criar uma instância, **não** é obrigatório preencher os valores de todos os atributos
- Uma boa analogia é considerar a classe como a receita para a criação de algum prato, por exemplo, um delicioso bolo de cenoura ;-)

Classe: Conta. Atributos: Número, titular, saldo, limite.

Funções construtoras: 

`def __init__(self):` - constrói objeto, cria na memória para chamar a sua função

1- Cria nossa função construtora (def _._init_._(self))
2- Definir os atributos, características especificas dentro de uma classe
3- O self é a referência que sabe encontrar o objeto que está sendo construído na classe dentro da função init
4- Uma classe serve como uma planta, como um conceito para vários objetos

```python
class Conta:

def __init__(self, numero, titular, limite, saldo):

	print("Construindo objeto... {}".format(self))
	self.numero = numero
	self.titular = titular
	self.limite = saldo
	self.saldo = limite
```

Como podemos fazer no Python para economizar a escrita do código de criação de um objeto Conta? Supondo que apenas as contas com limites especiais precisariam passar tal argumento.
```python
class Conta:
	def __init__(self, numero, titular, saldo, limite = 1000.0)
	self.numero = numero
	self.titular = titular
	self.saldo = saldo
	self.limite = limite
``` 
E o código de nossos 3 objetos ficaria assim:
```python
conta1 = Conta(1, "Alberto", 99.0)
conta2 = Conta(3, "Mateus", 9999.0, 2000.0)
```
uml - representação diagramática de classes
Através da referência eu posso acessar os atributos
- Classes
- Objetos
- Função construtora
- Endereço e referência de objetos
- Atributos de classe
- Acesso aos atributos através do objeto

Momento atual do projeto [Capítulo2](https://github.com/alura-cursos/Curso-Python-3-Introdu-o-a-Orienta-o-a-objetos/archive/capitulo2.zip)

Função construtora init define quais objetos e atributos. Qual o comportamento do objeto? As **funções ** na OO se chamam **Métodos**. Os métodos se coloca na Classe a qual  pertence. As funcionalidades estão melhor encapsuladas dentro do método

`conta.extrato()` - acessa pra mim o objeto e chama a função extrato

```python
class Jogo:
	def __init__(self):
		self.contador = 0
		
	def incrementa(self):
		self.contador+=1
		
jogo = Jogo()
jogo.incrementa()
print(jogo.contador)
```

None e coletor de lixo
- Python possui garbage collector
- Para derreferenciar: 
`outraRef = None`

- Como criar e chamar métodos através do objeto
- Acesso aos atributos através do `self`
- Garbage Collector
- Tipo `None`

Momento atual do projeto [Capítulo3](https://github.com/alura-cursos/Curso-Python-3-Introdu-o-a-Orienta-o-a-objetos/archive/capitulo3.zip)

----
Encapsulamento
- Atributos privados: 

tornar o atributo privado (impedir de ser acessado diretamente (analogia de alguém mexer em sua bolsa), double underscore (encapsulando o acesso aos atributos)
self._._numero = numero

```python
class Conta:

def __init__(self, numero, titular, limite, saldo):
	print("Construindo objeto... {}".format(self))
	self.__numero = numero
	self.__titular = titular
	self.__limite = limite
	self.__saldo = saldo
```
`__` dá um nome diferente para o atributo da classe alterando em todos os lugares. o atributo recebe o nome da classe como prefixo

Exemplo encapsulamento no `contas.py`, demonstra uma boa refatoração do código:
```python
def transfere(self, valor, destino):
	self.saca(valor)
	destino.deposita(valor)
```
Ou seja, existe código que foi criado fora da classe e depois entra na classe, também existe o contrário. Como perceber isso? verificar se está utilizando os métodos daquela classe
1- Uma classe deveria ter uma única responsabilidade, ter apenas uma razão para existir, ela deve ser coesa. Não deve assumir responsabilidades que não são delas **Coesão**

Princípio **SOLID**
- Atributos privados
- Encapsulamento de código
- Encapsulamento da manipulação dos atributos nos métodos
- Coesão do código

----
Usando Propriedades
Se você quiser fazer algo com o seu objeto, você deve definir um método!
- Getters e Setters
Métodos que devolvem algo: Getters
Métodos que acessem algo: Setters
- Set nunca retorna nada!
- Apenas utiliza-los quando for realmente necessários

- Propriedades
Para funcionar sem parêntesis, é necessário colocar a `@property` - métodos que dão acesso, chama sem a necessidade do parênteses

se eu tô executando `conta.limite` eu estou executando o getter, se eu faço a atribuição `conta.limite = 2000` eu estou executando o setter

- Métodos de leitura dos atributos, os getters
- Métodos de modificação dos atributos, os setters
- Propriedades

Momento atual do projeto [Capítulo5](https://github.com/alura-cursos/Curso-Python-3-Introdu-o-a-Orienta-o-a-objetos/archive/capitulo5.zip)

---

Métodos privados
Assim como existem atributos privados, também existem métodos privados
`def __MetodoPrivado(self, valor):`

Métodos da classe
Métodos estáticos pode ter cheiro de linguagem procedural e pode fugir do paradigma de OO!
`@staticmethod` 

- Métodos privados
- Métodos da classe, os métodos estáticos

---

