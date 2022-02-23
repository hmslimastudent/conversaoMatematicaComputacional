########################################################################
# Software criado por Henrique Matheus da Silva Lima                   #
# para treinar a conversão de números de um sistema de numeração       #
# para outro                                                           #
########################################################################

# Ambos os imports são para a função limparTerminal()
import os
import platform

# Como o próprio nome diz, essa função apenas limpa o terminal para não poluir a janela com textos passados
def limparTerminal():
	if (platform.system() == "Windows"): # Para funcionar, preciso chamar uma função específica do sistema operacional, eu uso Linux, mas a maioria das pessoas usam Windows
		clear = lambda: os.system("cls")
	else:
		clear = lambda: os.system("clear")
	clear()

# Essa função serve apenas para receber um valor que será processado por uma determinada função servida no parâmetro
def receberValor(funcao):
	valor = input("Informe o valor a ser convertido: ")
	funcao(valor)

def esperarInputparaContinuar():
	print("")
	x = input("Pressione ENTER para voltar à tela de menu")

# Função de conversão de decimal para binário
def converterDeDecimalParaBinario(entrada):
	
	if ('.' in entrada or ',' in entrada):
		entrada = entrada.replace(",", ".") # Caso o usuário tenha inserido um número fracionário com vírgula (por exemplo 2,5) em vez de ter usado ponto (2,5)
		numero = entrada.split(".")
		parteInteira = int(numero[0])
		parteFracionaria = float(int(numero[1])/10**(len(numero[1])))
	else:
		parteInteira = int(entrada)
		
	binarioParteInteira = ''
	binarioParteFracionaria = ''
	
	if (parteInteira == 0):
		binarioParteInteira = '0'
	else:
		while (parteInteira >= 1):
			binarioParteInteira += str(parteInteira % 2)
			parteInteira = int(parteInteira / 2)
	
	if ('.' in entrada or ',' in entrada):
		while (True):
			
			parteFracionaria = parteFracionaria * 2
			
			if (parteFracionaria == 1):
				binarioParteFracionaria += '1'
				break
			elif (parteFracionaria > 1):
				binarioParteFracionaria += '1'
				parteFracionaria -= 1
			else:
				binarioParteFracionaria += '0'
	
	if ('.' in entrada):
		print(f"> {binarioParteInteira[::-1]}.{binarioParteFracionaria}")
	else:
		print(f"> {binarioParteInteira[::-1]}")

	esperarInputparaContinuar()

# Função de conversão de decimal para binário
def converterDeBinarioParaDecimal(entrada):
	
	# Primeiro checa se o usuário inseriu realmente um número em formato binário
	if (entrada.lower().islower()): # Gambiarra pra ver se a entrada possui qualquer letra
		print("Atenção: o valor que você inseriu contém letras")
	elif ('2' in entrada or '3' in entrada or '4' in entrada or '5' in entrada or '6' in entrada or '7' in entrada or '8' in entrada): ## Não é um número binário válido
		print("Olha, você não inseriu um número binário, veja bem o que você inseriu")
	else:
		if ('.' in entrada or ',' in entrada):
			entrada = entrada.replace(",", ".") # Caso o usuário tenha inserido um número fracionário com vírgula (por exemplo 101,11) em vez de ter usado ponto (101.11)
			numero = entrada.split(".")
			binarioParteInteira = numero[0]
			binarioParteFracionaria = numero[1]
		else:
			binarioParteInteira = entrada
		
		soma = 0
		
		potencia = (len(binarioParteInteira) - 1)
		for el in binarioParteInteira:
			soma += int(el) * 2**potencia
			potencia -= 1
		
		potencia = -1
		if ('.' in entrada):
			for el in binarioParteFracionaria:
				soma += int(el) * 2**potencia
				potencia -= 1
		
		print(f"> {soma}")
	
	esperarInputparaContinuar()

# O programa propriamente dito
while (True):
	limparTerminal()
	print("Por favor, escolha o tipo de valor a ser convertido informando o número correspondente")
	print("(1) De numeral a binário")
	print("(2) De binário a decimal")
	print("(0) Finalizar programa")

	command = input("> ")
	
	if (command == "0"):
		break
	elif (command == "1"):
		receberValor(converterDeDecimalParaBinario)
	elif (command == "2"):
		receberValor(converterDeBinarioParaDecimal)
