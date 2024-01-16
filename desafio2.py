def calcular_nivel(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas
    nivel = ''

    if vitorias < 10:
        nivel = 'Ferro'
    elif 10 <= vitorias <= 20:
        nivel = 'Bronze'
    elif 20 < vitorias <= 50:
        nivel = 'Prata'
    elif 50 < vitorias <= 80:
        nivel = 'Ouro'
    elif 80 < vitorias <= 90:
        nivel = 'Diamante'
    elif 90 < vitorias <= 100:
        nivel = 'Lendário'
    else:
        nivel = 'Imortal'

    return f"O Herói tem um saldo de {saldo_vitorias} e está no nível de {nivel}"

# Exemplo de uso da função
resultado = calcular_nivel(60, 20)
print(resultado)
