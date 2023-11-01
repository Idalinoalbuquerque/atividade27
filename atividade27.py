# Exercício Python 27: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. DICA: VEJA SOBRE FUNÇÃO REPLACE(), LOWER() E UMA FORMA DE INVERTER OS CARACTERES. 
frase = str(input("digite a frase: "))
frase = frase.upper().replace(" ","")
inv = frase.upper() [::-1]
inv = inv.replace(" ", "") 
if frase == inv:
    print(" é um palíndromo")
else:
    print("não é palíndromo")
