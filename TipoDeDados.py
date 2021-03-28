'''
Tipos de Dados
O Python permite trabalhar com diferentes tipos de dados: 
          
● Strings - são dados definidos entre aspas duplas (“) ou simples (‘) ,
representando texto, que normalmente é exibido por um programa ou
exportado por ele.
Ex: “Olá Python”

● Números Inteiros (Integer) - são números sem casas decimais, números
inteiros. São definidos simplesmente como um número inteiro comum.
Ex: 5, 31, 150

● Números decimais (float) - números com casas decimais, são definidos com o
número e as casas decimais após o ponto.
Ex: 5.67, 99.99

● Boolean - utilizado para representar os conceitos de Verdadeiro ou Falso.
Booleans só podem assumir estes dois valores, representados por “True” e
“False” (mas sem as aspas)
Ex: True, False

'''

string_1 = "Olá Python"
string_2 = 'Adeus Python'
print(string_1)
print(string_2)

string_texto = '''Olá. Esta é uma string texto no Python.
Aqui pode usar " ou '
Caracteres são escapados como se espera.
É a terceira forma de definir uma string, apesar de não ser tão usual....
\t testando o TAB para finalizar'''                             
print(string_texto)

string_3 = "Livro de Richard Bach"
string_4 = 'O titulo é "Fernão Capelo Gaivota"'
print(string_3)
print(string_4)

string_5 = "o magnifico Fernão disse \"Nós somos na verdade ideias da Grande Gaivota...\""
string_6 = 'Do autor\'Para o verdadeiro Fernão Capelo Gaivota que vive em nós"'
string_7 = 'Alexander O\'Neal "Criticize"'
print(string_5)
print(string_6)
print(string_7)


#Sequência Escapada   Significado

#\\                  Contrabarra
#\'                  Aspas simples
#\"                  Aspas duplas
#\a                  Caracter de controle ASCII Bell (BEL)
#\b                  Caracter ASCII Backspace (BS
#\f                  Caracter ASCII Formfeed (FF)
#\n                  Caracter ASCII Linefeed (LF) - este cria uma nova linha no output
#\r                  Caracter ASCII Carriage Return (CR)
#\t                  Caracter ASCII Tab Horizontal (TAB)
#\v                  Caracter ASCII Tab Vertical (VT)
#\ooo                Caracter ASCII com valor octal “ooo”
#\xhh                Caracter ASCII com valor hex de “hh” 





string12 = "Olá, o meu nome é João"
substring1 = "meu"
print(string12.find(substring1))
substring2 = "Sergio"
