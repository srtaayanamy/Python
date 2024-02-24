#inicio do curso em Python
print ('hello world')
print ('8+5')
print ('8'+'5')
print (8+5)
print ('olá' , 5)
# , traz a mesma função de + porem com diferenças

nome = ('anna')
idade = 40
peso = 67.9
print (nome, idade, peso)

# input = leia
nom = input ('qual seu nome? ')
id = input ('qual sua idade? ')
pes = input ('qual seu peso? ')
print (nom, id, pes)

#desafio 
pessoa = input ('qual seu nome? ')
print ('Boas vindas,', pessoa)

dia = input ('dia:')
mes = input ('mês:')
ano = input ('ano:')
print ('você nasceu no dia', dia,'do', mes, 'de', ano, '. Correto?')

#format()
dia = input ('dia:')
mes = input ('mês:')
ano = input ('ano:')
print ('você nasceu no dia {} do {} de {}. Correto?' .format(dia, mes, ano))
