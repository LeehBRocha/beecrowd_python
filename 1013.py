import math

valor = input().split(" ")

a,b,c = valor

maiorAB = (int(a) + int(b) + abs(int(a) - int(b)))/2
maior = (int(c) + int(maiorAB) +abs(int(maiorAB) - int(c)))/2

print('%d eh o maior' %maior)