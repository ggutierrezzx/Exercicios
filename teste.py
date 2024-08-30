# NUMERO1

# INDICE = 13
# SOMA = 0
# K = 0

# while K < INDICE:
#     K += 1
#     SOMA += K

# print(SOMA)




# def numero_fibonacci(num):
    
#     a = 0
#     b = 1
    
    
#     while b < num:
#         temp = b  
#         b = a + b  
#         a = temp 
    
#     if num == b or num == 0:  
#         print(f"O numero {num} pertence a sequencia de Fibonacci.") 
#     else:
#         print(f"O numero {num} nao pertence a sequencia de Fibonacci.")

# # Teste com um número
# numero = 30
# numero_fibonacci(numero)


# import json

# def calcular_faturamento(faturamento_json):
    
#     with open(faturamento_json, 'r') as file:
#         dados = json.load(file)
    
    
#     valores = [dia['valor'] for dia in dados['faturamento_diario'] if dia['valor'] > 0]
    
 
#     menor_valor = min(valores)
#     maior_valor = max(valores)
    
    
#     media_mensal = sum(valores) / len(valores)
    
    
#     dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)
    
#     return {
#         "menor_valor": menor_valor,
#         "maior_valor": maior_valor,
#         "dias_acima_da_media": dias_acima_da_media
#     }


# resultado = calcular_faturamento('faturamento.json')

# print(f"Menor valor de faturamento: {resultado['menor_valor']}")
# print(f"Maior valor de faturamento: {resultado['maior_valor']}")
# print(f"Numero de dias acima da média: {resultado['dias_acima_da_media']}")


# estado_faturamento = {
#     "SP": 67836.43,
#     "RJ": 36678.66,
#     "MG": 29229.88,
#     "ES": 27165.48,
#     "Outros": 19849.53
# }


# faturamento_total = sum(estado_faturamento.values())


# percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in estado_faturamento.items()}

# print(percentuais)


# def inverter_string(texto):
  
#     texto_invertido = ""
    
 
#     for i in range(len(texto) - 1, -1, -1):
#         texto_invertido += texto[i]
    
#     return texto_invertido


# texto = "Giuseppe"
# resultado = inverter_string(texto)
# print(resultado)











    



