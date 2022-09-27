# def big_mac():                      # criando uma função , uma ou mais tarefas expecifica que podera ser chamada depois 
#     print("Sanduiche bic mac")

# print("Inicio")
# big_mac()
# print("Fim")


def fazer_big_mac(nome):
    print(f"sanduiche big mac {nome}")

# fazer_big_mac("Geraldo")
# fazer_big_mac("Luciana")
# fazer_big_mac("Camila")

def fazer_batata(tamanho):
    print(f"batata {tamanho}")

def preparar_refrigerante(tipo,tamanho):
    print(f"{tipo} {tamanho}")

# fazer_big_mac("Geraldo")
# fazer_batata("Grande")
# preparar_refrigerante("Coca", "Média")

def fazer_combo_big_mac(nome, tamanho_batata, tipo_refri, tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri, tamanho_refri)

# fazer_combo_big_mac("Roger", "Grande", "Coca", "Média")

def soma_num(num1,num2):
    return num1 + num2

resultado = soma_num(15,20)
# print(resultado)

def maior_num(list_num):
    list_num.sort()
    list_num.reverse()
    maior_num = list_num[0]
    return maior_num

resultado = maior_num([45,534,546,76,224,6,79,678,45,223,76,7,967,23,424,87])
print(resultado)
