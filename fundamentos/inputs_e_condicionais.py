A = input("Insira um valor para A: ")
B = input("Insira um valor para B: ")

if A > B:
    aux = A
    A = B
    B = aux

print("O valor de A é: ", A)
print("O valor de B é: ", B)

# Na exibição do print, existe um espaço extra entre o texto e o valor da variável. Isso ocorre porque o valor da variável é concatenado com uma string que contém um espaço em branco. Para corrigir isso, basta remover o espaço em branco da string. O comportamento padrão de Python é de, ao inserir uma vírgula no valor de um print, um espaço em branco é inserido automaticamente. Para evitar isso, basta concatenar a string com o valor da variável sem a vírgula e utilizar o f"{}" para inserir o valor da variável na string.
