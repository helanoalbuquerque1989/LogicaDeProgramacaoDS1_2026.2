# TODO: Implemente a expressão de validação
media_aluno = 7.5
frequencia_percentual = 80

# Crie a variável aprovado com a expressão lógica
aprovado = None # Substitua None pela expressão lógica
print("Status de aprovação:", aprovado)

media_aluno = float (input("media do aluno"))
frequencia_porcentual = int(input("frequencia do alune"))
media_final = media_aluno >= 6
frequencia_final = frequencia_porcentual >= 75
resultado = media_final and frequencia_final 
print("O aluno foi aprovado?", resultado)




