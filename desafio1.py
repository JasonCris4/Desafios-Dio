import random

nome_heroi = input('Digite o nome do seu herói:')

xp = random.randint(1, 10000)  

if xp < 1000:
    nivel = "ferro"
elif 1001 <= xp <= 2000:
    nivel = "bronze"
elif 2001 <= xp <= 5000:
    nivel = "prata"
elif 5001 <= xp <= 6000:
    nivel = "ouro"
elif 6001 <= xp <= 7000:
    nivel = "platina"
elif 7001 <= xp <= 8000:
    nivel = "ascendente"
elif 8001 <= xp <= 9000:
    nivel = "imortal"
elif 9001 <= xp <= 10000:
    nivel = "radiante"
else:
    nivel = "nível além de radiante"  

mensagem_final = f"O herói de nome {nome_heroi} está no nível de {nivel}."
print(f"XP: {xp}")
print(mensagem_final)
