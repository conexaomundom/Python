# O usuario vai entrar com 3 notas
# Calcule a media dessas tres notas e exibe o resultado

# Primeira forma do código notas

# nota1 = float(input("Digite sua primeira nota: "))
# nota2 = float(input("Digite sua segunda nota: "))
# nota3 = float(input("Digite sua terceira nota: "))

# notas = []
# notas = notas + [nota1, nota2, nota3]

# print("Sua média é: ", notas/3, sep = "")

# Segunda forma do codigo notas



# Informações para começar o for
qnt_notas = 4
notas = []

for i in range(1, qnt_notas):
    notas.append(float(input("Digite sua nota: ")))

print("Aluno, sua media é: ", sum(notas)/len(notas), sep = "")
