#----------LISTA 2 Q1 --------------

#1-Faça um Programa que peça dois números e imprima o maior deles.

print("Digite dois números e o programa irá lhe dizer qual deles é o maior \n")
 n1 = input("digite um número :\n")
 n2 = input("digite o outro número :\n")
 if( n1 > n2):
     print("o número maior é ", n1)
 else(n1 < n2):
     print( "o número maior é ", n2)
 if(n1 == n2):
     print("Os dois número são iguais")