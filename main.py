import requests, os
from bs4 import BeautifulSoup

# Menu do programa
def menu ():
    print ("Bem-vindo ao Negociador de Moedas 1.0")
    print (update + " da " + url)
    print ("Escolha pelo número da lista o país que deseja consultar a moeda.")
    input ("Tecle enter para iniciar o programa!")
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que formata o texto da URL
def formatacao (texto):
    caracteres = "[<td>]/ " 
    for caracteres in caracteres:
        texto = texto.replace(caracteres, "")
    return texto

# Função que cria o database com todos os dados necessários da URL
def database (sopa):
    for texto in sopa:
        nome = ["cidade", "moeda", "código", "numero"]
        sopa = formatacao(str(texto.find_all("td"))).split(",")
        dicionario = dict()
        universalCurrency =  "Nouniversalcurrency" in sopa
        if universalCurrency == False:
            for chave, valor in zip(nome, sopa):
                if chave == "cidade" or chave == "código":
                    dicionario [chave] = valor
        else:
            continue
        moedas.append (dicionario)

# Programa principal
moedas = []      

# Requisição a URL
url = "https://www.iban.com/currency-codes"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

# Capturando as informações necessárias da URL
update = str (soup.find("p").next_sibling).replace("\n", "")
tabela = soup.find_all("tr")
del tabela[0] # Deletei o primeiro item da lista porque o valor chegou vazio.

# Criando o database 
database(tabela)

menu()
while True:
    # Lista todas as moedas cadastradas
    for numero, lista in enumerate(moedas):
        print (f"#{numero} - {lista['cidade']}")
    try:
        resposta = int(input ("#: "))
        if (resposta <= len(moedas)):
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("Você escolheu o "+ moedas[resposta].get("cidade"))
            print ("O código da moeda é "+ moedas[resposta].get("código"))
            while True:
                resposta = input ("Deseja escolher outra moeda? s/n: ").lower()
                if resposta == "s":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                elif resposta == "n":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print ("Programa encerrado.")
                    input("Pressione ENTER para continuar...")
                    exit()
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Opção inválida.")
                    input("Pressione ENTER para continuar...")
                    os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida.")
            input("Pressione ENTER para continuar...")
            continue
    except ValueError:
        print("Opção inválida.")