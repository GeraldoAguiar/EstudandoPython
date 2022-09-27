familia = ["Geraldo" , "Luciana" , "Camila" , "Leticia" , "Nick"]

print(familia) # retorna um indice

print(familia[0]) # retorna o primeiro item do indice

print(familia[-1]) # retorna um indice de traz pra frente

print(familia[2:]) # retorna a partir do indice 2

print(familia[1:4]) # retorna a partir do indice 1 até o 4, excluindo o 4 

familia[2] = "Camila Diana" # alterando um valor dentro de uma lista
print(familia)

familia.extend(["Gracilene", "Alberto"]) # adicionando valor a uma lista ja existente
print(familia)

familia.append("Lucia") # adicioando um unico valor a lista
print(familia)

familia.insert(2,"Tati") # adicionando um valor no meio da lista
print(familia)

familia.pop() # removendo o ultimo item da lista
print(familia)

familia.remove("Nick") # removendo um item especifico de uma lista
print(familia)

#familia.clear() # limpando todos os dados da lista
#print(familia)

print(familia.index("Leticia")) # retornando o numero do indice pelo nome que esta na lista

print(familia.count("Leticia")) # conta quantos indices tem com o mesmo nome dentro da lista

idade_familia = [27,26,25,26,23]
 
idade_familia.sort() # ordena os numeros dentro de uma lista do menor para o maior
                     # caso a lista seja em string ele ordena em ordem alfabetica
print(idade_familia)

idade_familia.sort()    # para o reverse funcionar tenho que primeiro ondena-la 
idade_familia.reverse() # ordena os numeros dentro de uma lista do maior para o menor
                        # caso a lista seja em string ele ordena em ordem alfabetica ao contrario
print(idade_familia)

familia2 = familia.copy  # fazendo uma copia da lista totalmente independente
print(familia2)
familia.remove("Geraldo")
print(familia2)

coordenadas = (-49 , -36) # criando uma Tuple , é uma lista que não pode ser modificada
coordenadas.pop()
print(coordenadas)