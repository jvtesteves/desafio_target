# Função para verificar a existência da letra 'a' (maiúscula ou minúscula) e contar suas ocorrências

def verificar_letra_a_e_contar(string):
    # Convertendo a string para minúsculas para contar todas as ocorrências de 'a' ou 'A'
    contagem_a = string.lower().count('a')
    
    # Verificando se a letra 'a' existe e mostrando a quantidade de ocorrências
    if contagem_a > 0:
        print(f"A letra 'a' aparece {contagem_a} vezes na string informada.")
    else:
        print("A letra 'a' não aparece na string informada.")

# Exemplo de uso:
string_informada = "I only want to win hard"  # Exemplo de string, pode ser alterada
verificar_letra_a_e_contar(string_informada)
