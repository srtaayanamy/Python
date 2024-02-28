#continuação do curso de python

n1 = int (input ('digite o primeiro numero:'))
n2 = int (input ('digite o segundo numero:'))
soma = n1 + n2 
print ('O resultado da soma é: {}' .format(soma))
print ('a soma vale: {}' .format(n1+n2))
#juntar a str na outra é concatenação
#int, float, bool, str

a = input ('digite algo: ')
print ('o tipo primitivo é: ', type(a))
print ('Só tem espaços? ', a.isspace())
print ('é numérico? ', a.isnumeric())

#há diversas funções de is"alguma coisa", basta testar usando mesma sintaxe
# + adição - subtração * multiplicação e / divisão ** potencia // divisão inteira % resto da divisão == igual
# ordem de precedência: - (); **; *,/,//,%; +,-
# pode usar por exemplo, {:.3f} dentro do .format pra aparecer so 3 casas decimais
# ,end=' ' pra não quebrar a linha entre prints e \n p quebrar

print ('=' * 20)
print (pow(4,3))
print ('oi' * 5)

nome = input ('Qual seu nome?')
print ('prazer em te conhecer, {:=^20}!'.format(nome))
#pode usar <,>,^