import calendar




ano = int(input('Digite o ano:'))
mes = int(input('Mês:')) 
dia = int(input('Dia:'))
calen= 2023
mes1= 8 
dia1= 25

print(calendar.calendar(2023))

print(calendar.month(ano,mes))

dia_semana = calendar.weekday(ano,mes,dia)
if mes == mes1 and dia == dia1:
    print('Feliz aniversário')

if dia_semana == 0:
    print('Segunda')
elif dia_semana == 1:
    print('Terça-feira')
elif dia_semana == 2:
    print('Quarta-feira')
elif dia_semana == 3:
    print('Quinta-feira')
elif dia_semana == 4:
    print('Sexta-feira')
elif dia_semana == 5:
    print('Sabado')
else:
    print('Domingo')
