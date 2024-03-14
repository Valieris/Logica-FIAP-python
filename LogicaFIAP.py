#exercicio 1 

Total = 87426

total = 87426
segundos = (total % 60)
minutos = (total // 60)
horas = (minutos // 60)
horas_minutos = (minutos % 60)

print("total:", horas, "horas", horas_minutos, "minutos", segundos, 'segundos')

#exercicio 2

nota1 = 4
nota2 = 9
nota3 = 7

media = (nota1 + nota2 + nota3)/3
if media > 6:
    print('aprovado', media)

else:
    print('Reprovado', media)

#exercicio 3
    
Salario = float(input ("Me informe seu salario:"))
idade = int(input("me informe sua idade:"))

if Salario >= 1500 and idade >= 18:
    print ("Pode realizar emprestimo")
else:
    print ("Não pode realizar emprestimo")


    # Colocar 3 Aspas para executar cada exercicio separadamente!