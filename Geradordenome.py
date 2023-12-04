import random  # Importa a biblioteca random

nome = "" # Define os nome e sobrenome como uma string vazia
sobrenome = ""
listadenomes = ['Felipe','Gabi','Bárbara', 'Kelvin', 'Maicon',  'Marisa', 'Iris', 'Ingrid', 'Marcelo', 'Mayara']
listadesobrenomes = [ "Machado",'Bastos','Mendes','Alcântara', 'Alves', 'Ribeiro','Teixeira', 'Caldeira', 'Santos','Vasco']
for digito in range (1): # Declara que só irá utilizar um nome/sobrenome por vez
    nomealeatorio = random.choice(listadenomes)
    sobrenomealeatorio = random.choice(listadesobrenomes)
    nome += nomealeatorio
    sobrenome += sobrenomealeatorio
print(nome, sobrenome + "\nEste foi o nome gerado.")

