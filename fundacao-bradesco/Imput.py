nome = input("Digite o seu nome: ")
salario = float (input("Digite o seu salário: "))
situacao = input("Você esta trabalhando? ")
nomeFormatado = nome.capitalize()

print("\nSeu nome é: ",nomeFormatado)
print("Seu sálario é de: %.2f " % salario)
print("Você esta dentro do mercado de trabalho: ",situacao)